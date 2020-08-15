def enemylookup(Story, Area, type_, name):
    import enemydata
    if type_ == "name":
      return enemydata.name(Story, Area)
    if type_ == "defence":
      return enemydata.defence(name,Story)
    if type_ == "Hp":
      return enemydata.Hp(name,Story)
    if type_ == "move1" or type_ == "move2" or type_ == "move3" or type_ == "move4":
      return enemydata.move(name,Story,type_)
    if type_ == "dialogue1" or type_ == "dialogue2" or type_ == "dialogue3" or type_ == "dialogue4" or type_ == "dialogue5":
      return enemydata.dialogue(name,Story,type_)

def weaponlookup(id_,type_):
    import weaponindex
    return weaponindex.lookup(id_,type_)

def main(Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area):
    import time
    import random
    print("\n\n")
    pextra = 0
    eextra = 0
    enemyName = str(enemylookup(Story, Area,"name", "null"))
    time.sleep(1)
    print(enemyName + ": " + str(enemylookup(Story,Area,"dialogue1",enemyName)))
    time.sleep(1)
    run = True
    while run == True:
        print("\n\n")
        print (("Oh no! ") + enemyName + (" is attacking! What will you do?"))
        takevalue = input ("1.Attack\n2.Defend\n3.Magic\n > ")
        magicarray = weaponlookup(Weapon, "magicmoves")
        if takevalue  == "1":
            moveselect = True
            while moveselect == True:
                temp = weaponlookup(Weapon,"moves")
                print("\n" + "your mana is: " + str(Mana))
                print("\n\n")
                print("1." +  str(temp[0]) + " - " + str(temp[1]))
                print("\n\n")
                print("2." +  str(temp[2]) + " - " + str(temp[3]))
                move = input("\n\n > ")

                costlookup = "cost" + str(move)
                negativemana  = str(weaponlookup(Weapon,costlookup))
                if negativemana == "error":
                    print("\n")
                    print("you think to your self, there nothing called that.")
                    print("try 1 or 2 only")
                else:
                    negativemana = int(negativemana)
                    moveselect = False

            if int(Mana)-  negativemana < 0:
                time.sleep(1)
                print("you can't attack with this move without enough mana")
                time.sleep(1)
            else:
                Mana = int(Mana) - negativemana
                buff = int(weaponlookup(Weapon,("attackadd" + move)))
                pextra = weaponlookup(Weapon,"posicheck") + weaponlookup(Weapon,"bleedcheck") +  weaponlookup(Weapon,"firecheck") + weaponlookup(Weapon,"icecheck")
                Cdamage = (int(buff * float(random.randint(65,120) /100)) + pextra)
                edefence = enemylookup(Story,Area,"defence",enemyName)
                try:
                    eHp = eHp
                except:
                    eHp = enemylookup(Story,Area,"Hp",enemyName)
                
                if (edefence *1.40) <= 1000:
                    eHp = eHp - int((1-((edefence*1.40)/1000)) * Cdamage)
                else:
                    eHp = eHp - int((1 - ((edefence) / 1000)) * Cdamage)
                time.sleep(1)
                print("\nyou used " + str(temp[int(move)]))
                time.sleep(1)
                print("\n")
                print("it did " + str(int((1-(edefence/1000)) * Cdamage)) +  " damage to the enemy's health")
                print(enemyName + " Hp is " + str(eHp))
                print("your mana is now " + str(Mana))
                print("\n\n")
                time.sleep(1)


                if eHp <= 0:
                    print("\n\n")
                    talk5 = enemylookup(Story, Area, "dialogue5", enemyName)
                    return ["win", str(Hp), str(Mana)]

                else:
                    print("it's " + enemyName + " turn")
                    talk2  = enemylookup(Story,Area,"dialogue2",enemyName)
                    time.sleep(2)
                    print(str(talk2))
                    enemymovechoice = "move" + str(random.randint(1,4))
                    enemymovearray = enemylookup(Story,Area,enemymovechoice,enemyName)
                    fextra = weaponlookup(enemyName, "posicheck") + weaponlookup(enemyName, "bleedcheck") + weaponlookup(enemyName,"firecheck") + weaponlookup(enemyName, "icecheck")
                    Edamage = int(int(enemymovearray[1]) *  float(random.randint(65,120)/100) +  fextra)
                    Hp = Hp - int((1-(Defence/1000)) * Edamage)
                    if enemymovearray[1] < 1:
                        eHp = eHp * (1+  enemymovearray[1])
                    time.sleep(1)
                    print("\n")
                    print(enemyName + " used " +  str(enemymovearray[0]))
                    print(enemyName + " did " +  str(Edamage) + " damage to you")
                    print("your Hp is now " + str(Hp))
                    time.sleep(1)
                    print("\n...\n")
                    if Hp <= 0:
                        run = False
                        talk5 = enemylookup(Story, Area, "dialogue5", enemyName)
                        print(str(talk5))
                        print("\n\n")
                        return ["loss",str(Hp),str(Mana)]
                    else:
                        run = True

        if takevalue == 3 and magicarray[0] != "none":
            magicselect = True
            while magicselect == True:
                print("\n" + "your mana is: " + str(Mana))
                print("\n\n")
                print("1." +  str(magicarray[0]) + " - " + str(magicarray[1]))
                print("\n\n")
                print("2." +  str(magicarray[2]) + " - " + str(magicarray[3]))
                move = input("\n\n > ")

                mcostlookup = "magiccost" + str(move)
                negativemana  = str(weaponlookup(Weapon,mcostlookup))
                if negativemana == "error":
                    print("\n")
                    print("you think to your self, there nothing called that.")
                    print("try 1 or 2 only")
                else:
                    negativemana = int(negativemana)
                    magicselect = False

            if int(Mana)- negativemana < 0:
                time.sleep(1)
                print("you can't cast a spell without enough mana")
                time.sleep(1)
            else:
                Mana = int(Mana) - negativemana
                buff = int(weaponlookup(Weapon,("magicdamage" + move)))
                movestore = Weapon
                Weapon = magicarray[int(move)]
                pextra = weaponlookup(Weapon,"posicheck") + weaponlookup(Weapon,"bleedcheck") +  weaponlookup(Weapon,"firecheck") + weaponlookup(Weapon,"icecheck")
                Weapon = movestore
                Cdamage = (int(buff * float(random.randint(90,110) /100)) + pextra)
                edefence = enemylookup(Story,Area,"defence",enemyName)
                try:
                    eHp = eHp
                except:
                    eHp = enemylookup(Story, Area, "Hp", enemyName)

                eHp = eHp - int((1-(edefence/1000)) * Cdamage)
                time.sleep(1)
                print("\nyou used " + str(temp[int(move)]))
                time.sleep(1)
                print("\n")
                print("it did " + str(int((1-(edefence/1000)) * Cdamage)) +  " damage to the enemy's health")
                print(enemyName + " Hp is " + str(eHp))
                print("your mana is now " + str(Mana))
                print("\n\n")
                time.sleep(1)


                if eHp <= 0:
                    print("\n\n")
                    talk5 = enemylookup(Story, Area, "dialogue5", enemyName)
                    return ["win",str(Hp),str(Mana)]
                else:
                    print("it's " + enemyName + " turn")
                    talk2  = enemylookup(Story,Area,"dialogue3",enemyName)
                    time.sleep(2)
                    print(str(talk2))
                    enemymovechoice = "move" + str(random.randint(1,4))
                    enemymovearray = enemylookup(Story,Area,enemymovechoice,enemyName)
                    fextra = weaponlookup(enemyName, "posicheck") + weaponlookup(enemyName, "bleedcheck") + weaponlookup(enemyName,"firecheck") + weaponlookup(enemyName, "icecheck")
                    Edamage = int(int(enemymovearray[1]) *  float(random.randint(65,120)/100) +  fextra)
                    Hp = Hp - int((1-(Defence/1000)) * Edamage)
                    if enemymovearray[1] < 1:
                        eHp = eHp * (1+  enemymovearray[1])
                    time.sleep(1)
                    print("\n")
                    print(enemyName + " used " +  str(enemymovearray[0]))
                    print(enemyName + " did " +  str(Edamage) + " damage to you")
                    print("your Hp is now " + str(Hp))
                    time.sleep(1)
                    print("\n...\n")
                    if Hp <= 0:
                        run = False
                        talk5 = enemylookup(Story, Area, "dialogue5", enemyName)
                        print(str(talk5))
                        print("\n\n")
                        return ["loss",str(Hp),str(Mana)]
                    else:
                        run = True









        elif magicarray[0] == "none" and takevalue == "3":
            print("\n\nyou don't have a weapon that can cast magic spells.")




        if takevalue == "2":
            if Weapon == " ":
                blocker = "fist"
            else:
                blocker = Weapon
            print("\n\n")
            print("you try and brace for impact with your " +  blocker)
            time.sleep(1)
            print("\n\n")
            print("it's " + enemyName + "  turn")
            talk2 = enemylookup(Story, Area, "dialogue4", enemyName)
            time.sleep(2)
            print(str(talk2))
            enemymovechoice = "move" + str(random.randint(1, 4))
            enemymovearray = enemylookup(Story, Area, enemymovechoice, enemyName)
            fextra = weaponlookup(enemyName, "posicheck") + weaponlookup(enemyName, "bleedcheck") + weaponlookup(enemyName, "firecheck") + weaponlookup(enemyName, "icecheck")
            Edamage = int(int(enemymovearray[1]) * float(random.randint(65, 120) / 100) + fextra)
            Hp = Hp - int((1 - (Defence / 1000)) * Edamage)
            eHp = enemylookup(Story, Area, "Hp", enemyName)
            if enemymovearray[1] < 1:
                eHp = eHp * (1 + enemymovearray[1])
            time.sleep(1)
            print("\n")
            print(enemyName + " used " + str(enemymovearray[0]))
            print(enemyName + " did " + str(Edamage) + " damage to you")
            print("your Hp is now " + str(Hp))
            time.sleep(1)
            print("\n...\n")
            if Hp <= 0:
                run = False
                talk5 = enemylookup(Story, Area, "dialogue5", enemyName)
                print(str(talk5))
                print("\n\n")
                return ["loss",str(Hp),str(Mana)]
            else:
                run = True







                
                
                
                
        
        
    
    
    

