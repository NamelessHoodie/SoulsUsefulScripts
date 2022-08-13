from math import ceil, floor
import sys

separatorLenght = 80

#Tuple = Name, Duration, FlatDmg, %Dmg
statusEffects = []

def Main():
    RegisterDefaultStatuses()

    argsLen = GetArgsCount()
    maxHp = 0
    statusIndex = 0
    if argsLen > 1:
        statusIndex = GetArgInt(1)
    if argsLen > 0:
        maxHp = GetArgInt(0)
    else:
        ShowUsage()
        return

    DoLogicThenPrint(maxHp, statusIndex) 
    return
    
def RegisterDefaultStatuses():
    RegisterStatus("Poison - Standard", 90, 7, 0.07)
    RegisterStatus("Deadly Poison - Fetid Pot", 30, 12, 0.14)
    RegisterStatus("Deadly Poison - Venomous Fang/Serpent Arrow", 30, 14, 0.14)
    RegisterStatus("Perfumer's Poison", 30, 21, 0.21)
    RegisterStatus("Scarlet Rot - Weapon", 90, 15, 0.18)
    RegisterStatus("Scarlet Rot - Incantation", 90, 13, 0.33)

def RegisterStatus(name, duration, dmgFlat, percentDmg):
    statusEffects.append((name, duration, dmgFlat, percentDmg))
    return

def DoLogicThenPrint(maxHp, index):
    print(f"Target HP = {maxHp}")
    PrintSeparator()
    if index == 0:
        PrintAllStatusIndex(maxHp)
    else:
        PrintCalcIndex(maxHp, index)

    return

def PrintAllStatusIndex(maxHp):
    for i in range(0, len(statusEffects)):
        PrintCalcIndex(maxHp, i)

    return

def PrintCalcIndex(targetHp, index):
    name, duration, dmgFlat, dmgPercentage = statusEffects[index]
    #print(f"name={name}, duration={duration}, dmgFlat={dmgFlat}, dmgPercentage={dmgPercentage}")
    PrintCalc(targetHp, name, duration, dmgFlat, dmgPercentage)
    return

def PrintCalc(targetHp, name, duration, dmgFlat, dmgPercentage):
    #print(f"targetHp={targetHp}, name={name}, duration={duration}, dmgFlat={dmgFlat}, dmgPercentage={dmgPercentage}")
    dps = CalcDPS(targetHp, dmgFlat, dmgPercentage)
    totalDmg = CalcTotalDamage(dps, duration)
    procsToDth = targetHp / totalDmg
    timeToDth = floor(duration * procsToDth)
    procsToDthCeil = ceil(procsToDth)
    procsToDthFloor = floor(procsToDth)
    procsToDthFloorRemainder = procsToDth - procsToDthFloor
    procsToDthFloorDmgReq = totalDmg * procsToDthFloorRemainder
    procsToDthFloorDmgReqCeil = ceil(procsToDthFloorDmgReq)
    procsToKillFloorTxt = f"{procsToDthFloor}, Extra Damage Required = {procsToDthFloorDmgReqCeil} " if procsToDthFloor >= 1 else "N/A"
    
    print(f"{name}: Duration = {duration}, Dmg = {dmgFlat}, Dmg% = {dmgPercentage}")
    print(f"Proc Damage = {totalDmg}, Dps = {dps}")
    print(f"Procs to kill = {procsToDth}, Seconds to Kill = {timeToDth}")
    print(f"Procs to kill Floor = {procsToKillFloorTxt}")
    print(f"Procs to kill Ceil = {procsToDthCeil}")
    PrintSeparator()
    return

def CalcTotalDamage(dps, timeSeconds):
    totalDmg = dps * timeSeconds
    return floor(totalDmg)

def CalcDPS(maxHp, dmgFlat, dmgPercentage):
    return CalcPercentage(maxHp, dmgPercentage) + dmgFlat

def CalcPercentage(value, percentage):
    return (value / 100) * percentage

def ShowUsage():
    print("Usage:")
    print("CalcStatusDmg.py <TotalHp> <opt:statusIndex>")
    print("Status Indexes:")
    print(f"0 = All")
    i = 1
    for nameStr, dmgTicks, dmgPercentage, dmgFlat in statusEffects:
        print(f"{i} = {nameStr}")
        i += 1
    return

def PrintSeparator():
    print(GetStr("-", separatorLenght))
    return

def GetStr(char, charCount):
    return char * charCount

def GetArgsCount():
    return len(sys.argv) - 1

def GetArgStr(index):
    return sys.argv[1 + index]

def GetArgInt(index):
    return int(GetArgStr(index))

Main()




