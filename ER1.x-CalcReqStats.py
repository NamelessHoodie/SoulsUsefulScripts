import sys

statList =      [
"Level",        #0 
"Vigor",        #1
"Mind",         #2
"Endurance",    #3
"Strength",     #4
"Dexterity",    #5
"Intelligence", #6
"Faith",        #7
"Arcane"        #8
                ]

startingClassesDict = {
    "Vagabond": [9, 15, 10, 11, 14, 13, 9, 9, 7],
    "Warrior": [8, 11, 12, 11, 10, 16, 10, 8, 9],
    "Hero": [7, 14, 9, 12, 16, 9, 7, 8, 11],
    "Bandit": [5, 10, 11, 10, 9, 13, 9, 8, 14],
    "Astrologer": [6, 9, 15, 9, 8, 12, 16, 7, 9],
    "Prophet": [7, 10, 14, 8, 11, 10, 7, 16, 10],
    "Samurai": [9, 12, 11, 13, 12, 15, 9, 8, 8],
    "Prisoner": [9, 11, 12, 11, 11, 14, 14, 6, 9],
    "Confessor": [10, 10, 13, 10, 12, 12, 9, 14, 9],
    "Wretch": [1, 10, 10, 10, 10, 10, 10, 10, 10]
}

def Main():
    if len(sys.argv) > 5:
        PrintFormattedClassesRequirement()
    else:
        ShowUsage()

def ShowUsage():
    tempStr = "python calcstats.py "

    for i in GetWeaponStatRange():
        tempStr += f"<{statList[i]} Req> "
    statList.pop()

    print("Usage:")
    print(tempStr)

def PrintFormattedClassesRequirement():
    strs = GetFormattedStrListClassesRequirements()
    PrintStringList(strs)

def PrintStringList(strList):
    for str in strList:
        print(str)

def GetWepRequirementsFormmattedStr(statLst):
    tempStr = "Weapon Requirements: "
    for i in GetWeaponStatRange():
        tempStr += f"{statList[i]}={statLst[i]}, "
    tempStr = tempStr.removesuffix(", ")
    return tempStr

def GetFormattedStrListClassesRequirements():
    statRequirementList = GetStatGoalListFromArgs()
    classesPrintOutList = []
    classesPrintOutList.append(GetWepRequirementsFormmattedStr(statRequirementList))
    for (name, classStatList) in startingClassesDict.items():
        classPrintOutList = []
        statDiff = GetStatDiff(classStatList, statRequirementList)
        classTotalLevel = classStatList[0]
        classLevelsRequired = 0
        for i in range(0, len(statDiff)):
            currentStat = statDiff[i]
            classTotalLevel += currentStat
            classLevelsRequired += currentStat
            padStatStr = (" " * (12 - len(statList[i])))
            classPrintOutList.append(f"{padStatStr}{statList[i]}: {classStatList[i]} + {currentStat} = {str(classStatList[i] + currentStat)}")
        
        #classNamePadStr = (" " * (12 - len(name)))
        classPrintOutList.insert(0, f"{name}: RL={classStatList[0]}+{classLevelsRequired}={classTotalLevel}")
        classPrintOutList.append("")
        classesPrintOutList += classPrintOutList
    
    return classesPrintOutList

def GetStatDiff(base, goal):
    diffList = []
    for x in range(0, len(base)):
        diffList.append(0)
    #print(base)
    #print(goal)
    for i in range(0, len(base)):
        #print(i)
        #print(base)
        #print(goal)
        if base[i] >= goal[i]:
            diffList[i] = 0 
        else:
            diffList[i] = goal[i] - base[i]
    
    return diffList

def GetWeaponStatRange():
    return range(4, 9)

def GetStatGoalListFromArgs():
    statGoalList = [
    0, #0-Level        
    0, #1-Vigor        
    0, #2-Mind         
    0, #3-Endurance    
    0, #4-Strength     
    0, #5-Dexterity    
    0, #6-Intelligence 
    0, #7-Faith       
    0  #8-Arcane       
                    ]
    
    for i in GetWeaponStatRange():
        statGoalList[i] = GetWepStatGoalFromArg(i)

    #print(statGoalList)
    return statGoalList
        
def GetWepStatGoalFromArg(index):
    # if index == 0:
    #     return sys.argv[1]
    if index >= 4:
        return int(sys.argv[index - 3])

Main()

