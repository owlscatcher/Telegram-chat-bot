import random
import operator
import os

def get_random_character():
    char_name_dict = {'STR': ['Воин', './resources/warrior/'],
                      'DEX': ['Разбойник', './resources/rogue/'],
                      'INT': ['Маг', './resources/wizard/'],
                      'CON': ['Варвар', './resources/barbarian/'],
                      'WIS': ['Клирик', './resources/cleric/'],
                      'CHA': ['Бард', './resources/bard/'],
                      'STRDEX': ['Рыцарь', './resources/knight/'],
                      'STRINT': ['Магус', './resources/magus/'],
                      'STRCON': ['Берсерк', './resources/berserk/'],
                      'STRCHA': ['Паладин', './resources/paladin/'],
                      'DEXINT': ['Мистический лучник', './resources/arcanarcher/'],
                      'DEXWIS': ['Монах', './resources/monk/'],
                      'INTWIS': ['Детектив', './resources/investigator/'],
                      'INTCHA': ['Чародей', './resources/sorcer/'],
                      'CONWIS': ['Друид', './resources/druid/'],
                      'WISCHA': ['Оракул', './resources/oracul/']}

    STR = random.randint(1, 10)
    DEX = random.randint(1, 10)
    CON = random.randint(1, 10)
    INT = random.randint(1, 10)
    WIS = random.randint(1, 10)
    CHA = random.randint(1, 10)

    ability_dict = {'STR': STR, 'DEX': DEX,
                    'CON': CON, 'INT': INT, 'WIS': WIS, 'CHA': CHA}
    ability_cortege_sorted = sorted(
        ability_dict.items(), key=operator.itemgetter(1))

    if(ability_cortege_sorted[4][1] == ability_cortege_sorted[5][1]):
        char_name = (
            ability_cortege_sorted[4][0] + ability_cortege_sorted[5][0])
    else:
        char_name = ability_cortege_sorted[5][0]

    temp_result = char_name_dict.get(char_name)

    if(temp_result == None):
        char_name = char_name[:3]
        temp_result = char_name_dict.get(char_name)

    displayed_name = temp_result[0]
    pic_path = temp_result[1]

    files = os.listdir(pic_path)
    images = list(
        filter(
            lambda x: x.endswith('.jpg') | x.endswith('.jpeg') | x.endswith('.png') | x.endswith('.webp'), 
            files)
        )

    pic_path += images[random.randint(0, (len(images) - 1))]

    text_char = ('`STR: ' + str(STR) + '    DEX: ' + str(DEX) +
                '\nCON: ' + str(CON) + '    INT: ' + str(INT) +
                '\nWIS: ' + str(WIS) + '    CHA: ' + str(CHA) +
                '\n\nТвой класс: ' + displayed_name + '!`')
    summary_dict = {'pic': pic_path, 'text': text_char}

    return summary_dict
