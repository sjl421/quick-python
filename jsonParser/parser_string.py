## coding: utf-8

import json
import pymysql

linkedInData = {}


def buildDateRange(param):
    if not param:
        return 'Nothing'
    startTmp = ''
    if 'startDate' in param.keys():
        startTmp = str(param['startDate']['year'])
        if 'month' in param['startDate'].keys():
            startTmp += '-' + str(param['startDate']['month'])

    endTmp = 'now'
    if 'endDate' in param.keys():
        endTmp = str(param['endDate']['year'])
        if 'month' in param['endDate'].keys():
            startTmp += '-' + str(param['startDate']['month'])

    return startTmp + '~' + endTmp


def parserString(line):
    if not line:
        return
    str = line.split("\t")
    targetStr = str[9]
    targetJson = json.loads(targetStr)
    profile = targetJson['responses']['21']['body']['profile']

    print('------------------------------social---------------------------------------')
    linkedInData['summary'] = profile.get('summary','')
    linkedInData['industryName'] = profile.get('industryName','')
    linkedInData['firstName'] = profile.get('firstName','')
    linkedInData['lastName'] = profile.get('lastName','')
    linkedInData['locationName'] = profile.get('locationName','')
    linkedInData['headline'] = profile.get('headline','')

    print('------------------------------work---------------------------------------')

    worksData = []
    positionView = targetJson['responses']['21']['body']['positionView']
    works = positionView['elements']
    for work in works:
        workData = {}
        workData['companyName'] = work.get('companyName','')
        workData['title'] = work.get('title','')
        workData['locationName'] = work.get('locationName','')
        workData['timePeriod'] = buildDateRange(work.get('timePeriod',''))
        worksData.append(workData)

    linkedInData['worksData'] = worksData
    print('------------------------------education---------------------------------------')

    educationView = targetJson['responses']['21']['body']['educationView']
    educations = educationView['elements']
    for education in educations:
        print('schoolName--->' + education.get('schoolName',''))
        print('fieldOfStudy--->' + education.get('fieldOfStudy',''))
        print('degreeName--->' + education.get('degreeName',''))
        print(buildDateRange(education['timePeriod']))
        print()

    print('------------------------------skill---------------------------------------')

    skillView = targetJson['responses']['21']['body']['skillView']
    skills = skillView['elements']
    for skill in skills:
        print(skill['name'])

    print('------------------------------otherskill---------------------------------------')
    otherSkillStr = str[11]
    otherSkillJson = json.loads(otherSkillStr)
    otherSkills = otherSkillJson['responses']['0']['body']['elements']
    for otherSkill in otherSkills:
        print(otherSkill['skill']['name'])

    print("==========")
    print(linkedInData)
    save(linkedInData)

def save(data):
    conn = pymysql.connect(
        host='120.55.168.18',
        port=8840,
        user='',
        passwd='',
        db='testcase',
        charset='utf8')
    cur = conn.cursor()

    insert_sql = ('''INSERT INTO linkedin_bought(firstName,lastName,headline,summary,industryName,locationName,workExperience,education,skill) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
    print(linkedInData['firstName'])
    insert_data = (
        linkedInData['firstName'], linkedInData['lastName'], linkedInData['headline'], linkedInData['summary'],
        linkedInData['industryName'], linkedInData['locationName'], json.dumps(linkedInData['worksData']),
        '', '')
    try:
        cur.execute(insert_sql, insert_data)
        conn.commit()
        print
    except Exception as e:
        print("数据插入错误 [d%]") % e
    print('数据并插入mysql数据库完成')

file = open('linkedin_first_row.txt')
while 1:
    lines = file.readlines(1)
    if not lines:
        break
    for line in lines:
        parserString(line)

file.close()
