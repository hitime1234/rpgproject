def move(id_,type_):
    if id_ == " ":
        return ["punch","A weak attack, does 15 damage extra","uppercut","a powerful attack for unarmed enemies, yet still weaker then a sword. Does 25 extra but costs 10 mana"]
    
        
def manacost(id_,movet):
    if id_ == " ":
        if movet == 1:
            return 0
        elif movet == 2:
            return 10

def attackadd(id_,movet):
    if id_ == " " and movet ==  1:
        return 15
    if id_ == " " and movet ==  2:
        return 25


def posicheck(id_):
    if id_ == " ":
        return 0
    if id_ == "greggerson":
        return 0
    if id_ == "Snake":
        return 5
    if id_ == "Bear":
        return 7
    if id_ == "Rat":
        return 0
    if id_ == "Monkey":
        return 0
    if id_ == "Centaur":
        return 0
    
def bleedcheck(id_):
    if id_ == " ":
        return 0
    if id_ == "greggerson":
        return 200
    if id_ == "Bear":
        return 7
    if id_ == "Rat":
        return 0
    if id_ == "Snake":
        return 0
    if id_ == "Monkey":
        return 0
    if id_ == "Centaur":
        return 0

def firecheck(id_):
    if id_ == " ":
        return 0
    if id_ == "greggerson":
        return 2
    if id_ == "Bear":
        return 0
    if id_ == "Snake":
        return 0
    if id_ == "Monkey":
        return 0
    if id_ == "Centuar":
        return 0
    if id_ == "Rat":
        return 0
    
def icecheck(id_):
    if id_ == " ":
        return 0
    if id_ == "greggerson":
        return 2
    if id_ == "Bear":
        return 0
    if id_ == "Snake":
        return 0
    if id_ == "Rat":
        return 0
    if id_ == "Monkey":
        return 0
    if id_ == "Centaur":
        return 0

def magiccheck(id_):
    if id_ == " ":
        return ["none","none","none","none"]

def magicdamage(id_,move):
    if id_ == " " and move == "magicdamage1":
        return "error"
    if id_ == " " and move == "magicdamage1":
        return "error"

def magiccost(id_,move):
    if id_ == " " and move == "magiccost1":
        return "error"
    if id_ == " " and move == "magiccost2":
        return "error"


        
def lookup(id_,type_):
    if type_ == "moves":
        arraymove = move(id_,type_)
        return arraymove
    if type_ == "cost1":
        movet =  1
        send = manacost(id_,movet)
        return send
    if type_ == "cost2":
        movet =  2
        send = manacost(id_,movet)
        return send
    if type_ == "attackadd1":
        movet =  1
        send = attackadd(id_,movet)
        return send
    if type_ == "attackadd2":
        movet =  2
        send = attackadd(id_,movet)
        return send
    if type_ == "posicheck":
        send = int(posicheck(id_))
        return send
    if type_ == "bleedcheck":
        send = int(bleedcheck(id_))
        return send
    if type_ == "firecheck":
        send = int(firecheck(id_))
        return send
    if type_ == "icecheck":
        send = int(icecheck(id_))
        return send
    if type_ == "magicmoves":
        send = magiccheck(id_)
        return send
    if type_ ==  "magiccost1" or type_ == "magiccost2":
        send = magiccost(id_,type_)
        return send
    if type_ == "magicdamage1" or type_ == "magicdamage2":
        send = magiccost(id_, type_)
        return send



    else:
        return "error"
    
    
        
    
            
