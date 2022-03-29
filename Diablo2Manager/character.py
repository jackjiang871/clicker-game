import math

class Character:

    ## character static variables ##
    charName = "wind"
    charClass = "paladin"

    ## character numeric variables ##
    charLevel = 1
    charCurExp = 0 
    charStr = 25
    charDex = 20
    charVit = 25
    charEng = 15

    '''
    more leveling details at:
    http://classic.battle.net/diablo2exp/basics/levels.shtml
    Hit Points: 55
    Mana: 15
    Life +2
    Mana +1.5
    1 Vitality point gives 3 Life
    1 Vitality point gives 1 Stamina
    1 Energy point gives 1.5 Mana
    Frames	15	14	13	12	11	10	9
    FCR +%	0	9	18	30	48	75	125
    '''

    ## character calculated variables ##
    charLevelExp = (charLevel-1)^2*100 + (charLevel)*500 
    charHP = charLevel*2 + charVit*3
    charMP = math.floor(charLevel*1.5 + charEng*1.5)

    ## character combat variables ##
    charMainSkill = "melee"
    charOffSkill = "melee"
    
    ## character list variables ##
    charSkills1 = []
    charSkills2 = []
    charSkills3 = []
    charInv = []
    charCharms = []
    charEquip = []

    '''
    item stats: name, statsName, statsNum, skillName, SkillNum
    '''

