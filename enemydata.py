def name(Story, Area):
    import random
    if Story == 0 and Area == 0:
       return "greggerson"
    if Story == 0 and Area == 1:
        radn = random.randint(1,5)
        if radn == 1:
            return "Rat"
        elif radn == 2:
            return "Monkey"
        elif radn ==  3:
            return "Snake"
        elif radn == 4:
            return "Centaur"
        elif radn  == 5:
            return "Bear"

def defence(name,Story):
    if Story == 0 and name == "greggerson":
        return 900
    if Story == 0 and name == "Rat":
        return 5
    if Story == 0 and name == "Monkey":
        return 5
    if Story == 0 and name == "Snake":
        return 5
    if Story == 0 and name == "Bear":
        return 5
    if Story == 0 and name == "Centaur":
        return 10



def Hp(name,Story):
    if Story == 0 and name == "greggerson":
        return 5000
    if Story == 0 and name == "Rat":
        return 20
    if Story == 0 and name == "Monkey":
        return 35
    if Story == 0 and name == "Snake":
        return 25
    if Story == 0 and name == "Bear":
        return 50
    if Story == 0 and name == "Centaur":
        return 85

def move(name,Story,type_):
    if Story == 0 and name == "greggerson":
       if type_ == "move1":
          return ["sword slash",1200]
       if type_ == "move2":
          return ["the sharp twisting of reality",9999999]
       if type_ == "move3":
          return ["sword blockaid",0.35]
       if type_ == "move4":
          return ["time corrupt",2000]

    if Story == 0 and name == "Rat":
       if type_ == "move1":
          return ["Bite",5]
       if type_ == "move2":
          return ["scratch",5]
       if type_ == "move3":
          return ["death stare",0.03]
       if type_ == "move4":
          return ["tail strike",6]

    if Story == 0 and name == "Monkey":
       if type_ == "move1":
          return ["punch",7]
       if type_ == "move2":
          return ["Mega punch",9]
       if type_ == "move3":
          return ["slap",8]
       if type_ == "move4":
          return ["steal",7]

    if Story == 0 and name == "Bear":
       if type_ == "move1":
          return ["punch",7]
       if type_ == "move2":
          return ["scratch",9]
       if type_ == "move3":
          return ["slap",8]
       if type_ == "move4":
          return ["bite",10]
    if Story == 0 and name == "Snake":
       if type_ == "move1":
          return ["constrict",5]
       if type_ == "move2":
          return ["bite",6]
       if type_ == "move3":
          return ["tailwhip",4]
       if type_ == "move4":
          return ["dry skin",0.10]

    if Story == 0 and name == "Centuar":
        if type_ == "move1":
            return ["Recharge", 0]
        if type_ == "move2":
            return ["Recharge", 0]
        if type_ == "move3":
            return ["full speed", 20]
        if type_ == "move4":
            return ["backbuck", 21]


def dialogue(name,Story,type_):
    if Story == 0 and name == "greggerson":
        if type_ == "dialogue1":
            return  "ahahah you think oldman. You can't stop the power of the legendary sword.\nOldman: no but this person can\n"
        if type_ == "dialogue2":
            return  "\nso your brave enough to take me on. \nAlright it time show you the powerful legendary sword."
        if type_ == "dialogue3":
            return "\nhow do you know magic, You don't even have a weapon to cast it with"
        if type_ == "dialogue4":
            return "\nhahahhahaha coward. \n you can't hide behind nothing.\n"
        if type_ == "dialogue5":
            return  "\n now that's expected outcome"

    if Story == 0 and name == "Snake":
        if type_ == "dialogue1":
            return "SSSssss.. -you don't know snake language. But it looks like it trying to fight.\n"
        if type_ == "dialogue2":
            return "\nSSSSSSSSSSSSsss. - The snake appears to be very angry."
        if type_ == "dialogue3":
            return "\nSSSSSSSsssssss - you assume that snake has never seen such wizard powers before.\n"
        if type_ == "dialogue4":
            return "\nSsSssSssS. \n -Even a weak snake looks to be laughing. \n"
        if type_ == "dialogue5":
            return "\n SSSSSSSSssssssssSs - Snake looking as if it's had just be opened up to possibilities.\n"

    if Story == 0 and name == "Centaur":
        if type_ == "dialogue1":
            return "ahahah you think oldman. You can't stop the power of the legendary sword.\nOldman: no but this person can\n"
        if type_ == "dialogue2":
            return "\nso your brave enough to take me on. \nAlright it time show you the powerful legendary sword."
        if type_ == "dialogue3":
            return "\nhow do you know magic, You don't even have a weapon to cast it with"
        if type_ == "dialogue4":
            return "\nhahahhahaha coward. \n you can't hide behind nothing.\n"
        if type_ == "dialogue5":
            return "\n now that's expected outcome"

    if Story == 0 and name == "Rat":
        if type_ == "dialogue1":
            return "ahahah you think oldman. You can't stop the power of the legendary sword.\nOldman: no but this person can\n"
        if type_ == "dialogue2":
            return "\nso your brave enough to take me on. \nAlright it time show you the powerful legendary sword."
        if type_ == "dialogue3":
            return "\nhow do you know magic, You don't even have a weapon to cast it with"
        if type_ == "dialogue4":
            return "\nhahahhahaha coward. \n you can't hide behind nothing.\n"
        if type_ == "dialogue5":
            return "\n now that's expected outcome"

    if Story == 0 and name == "Bear":
        if type_ == "dialogue1":
            return "ahahah you think oldman. You can't stop the power of the legendary sword.\nOldman: no but this person can\n"
        if type_ == "dialogue2":
            return "\nso your brave enough to take me on. \nAlright it time show you the powerful legendary sword."
        if type_ == "dialogue3":
            return "\nhow do you know magic, You don't even have a weapon to cast it with"
        if type_ == "dialogue4":
            return "\nhahahhahaha coward. \n you can't hide behind nothing.\n"
        if type_ == "dialogue5":
            return "\n now that's expected outcome"

    if Story == 0 and name == "Monkey":
        if type_ == "dialogue1":
            return "ahahah you think oldman. You can't stop the power of the legendary sword.\nOldman: no but this person can\n"
        if type_ == "dialogue2":
            return "\nso your brave enough to take me on. \nAlright it time show you the powerful legendary sword."
        if type_ == "dialogue3":
            return "\nhow do you know magic, You don't even have a weapon to cast it with"
        if type_ == "dialogue4":
            return "\nhahahhahaha coward. \n you can't hide behind nothing.\n"
        if type_ == "dialogue5":
            return "\n now that's expected outcome"







