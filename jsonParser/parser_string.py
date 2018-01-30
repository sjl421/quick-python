import json



def buildDateRange(param):
    if not param:
        return 'Nothing'
    startTmp=''
    if 'startDate' in param.keys():
        startTmp = str(param['startDate']['year'])
        if 'month' in param['startDate'].keys():
            startTmp+='-' + str(param['startDate']['month'])

    endTmp='now'
    if 'endDate' in param.keys():
        endTmp = str(param['endDate']['year'])
        if 'month' in param['endDate'].keys():
            startTmp+='-' + str(param['startDate']['month'])

    return startTmp + '~' + endTmp


def parserString(line):
    if not line:
        return
    str = line.split("\t")
    targetStr = str[9]
    targetJson = json.loads(targetStr)
    profile = targetJson['responses']['21']['body']['profile']

    print('------------------------------social---------------------------------------')
    print('summary--->' + profile['summary'])
    print('industryName--->' + profile['industryName'])
    print('firstName--->' + profile['firstName'])
    print('lastName--->' + profile['lastName'])
    print('locationName--->' + profile['locationName'])
    print('headline--->' + profile['headline'])

    print('------------------------------work---------------------------------------')

    positionView = targetJson['responses']['21']['body']['positionView']
    works = positionView['elements']
    for work in works:
        print('companyName--->' + work['companyName'])
        print('title--->' + work['title'])
        print('locationName--->' + work['locationName'])
        print(buildDateRange(work['timePeriod']))
        if 'description' in work.keys():
            print('description--->' + work['description'])
        print()

    print('------------------------------education---------------------------------------')

    educationView = targetJson['responses']['21']['body']['educationView']
    educations = educationView['elements']
    for education in educations:
        print('schoolName--->' + education['schoolName'])
        print('fieldOfStudy--->' + education['fieldOfStudy'])
        print('degreeName--->' + education['degreeName'])
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

file = open('linkedin_first_row.txt')
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        parserString(line)

file.close()
