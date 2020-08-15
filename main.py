
#save file system on startup of no save file.
import random
import time

def startup():
    global Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area, CMana, CHp
    try:
        print("if you don't have save just type anything")
        Filename = input("file 1,2,3\n? ")
        File = open((Filename + ".pl"),"r")
        #name
        Heroname = str(File.readline())
        Heroname = Heroname.strip("\n")
        #Gender
        Gender = int(File.readline())
        #Hp
        Hp = int(File.readline())
        CHp = Hp
        #Mana
        Mana = int(File.readline())
        CMana = Mana
        #Defence
        Defence = int(File.readline())
        #Weapon
        Weapon = str(File.readline())
        Weapon = Weapon.strip("\n")
        #story
        Story = int(File.readline())
        #Area
        Area = int(File.readline())
        Sure = input("Are you " + Heroname+ "? Y/N \n? ")
        if Sure.upper() == "Y":
            print("lets get start")
            print("\n\n\n")
            return True
        else:
            return False
 
    except:
        print("\n\n\n\n\n\n\n\n\n\n\n")
        print("")
        print("Hello, you finally woke up!.")
        time.sleep(1)
        Heroname = input("What's your name? ")
        time.sleep(1)
        print("well hello there then " + str(Heroname))
        print("\n\n")
        time.sleep(1)
        print("now lets see what we have.")
        print("\n\n\n")
        Gender = random.randint(0,1)
        time.sleep(1)
        if Gender == 1:
            print("So, you are a (male).")
        elif Gender == 0:
            print("You are a (female).")
        Hp = random.choice((90,95,100,105,110,115,120,125,130))
        time.sleep(1)
        print("health is " + str(Hp))
        time.sleep(1)
        Mana = int(50)
        CMana = Mana
        CHp = Hp
        print("mana is 50")
        Defence = int(5)
        time.sleep(1)
        print("defence is 5")
        Weapon = " "
        time.sleep(1)
        print("and you have no weapons on you")
        Story = 0
        Area = 0
        Run = True
        while Run == True:
              Filename = input("where would you like to save this new file to 1, 2, 3? ")
              print("\n\n")
              if Filename == "1" or Filename == "2" or Filename == "3":
                   print("accepted")
                   Run = False
              else:
                   print("must be 1,2,3")


def battles(Gstr):
    global CHp,Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area, startCheck,CMana
    import battle
    #major battles
    if Story == 0 and Area == 0:
        winorlose = battle.main(CHp, Heroname, CMana, Defence, Weapon, Gender, Filename, Story, Area)
        CHp = int(winorlose[1])
        CMana = int(winorlose[2])
        winorlose = str(winorlose[0])
        if winorlose == "loss":
            time.sleep(1)
            print("\nhahaha you think you could win.\n\n Alright Oldman your coming with me.")
            print("\n")
            time.sleep(1)
            print("Unknown: what about him, he still alive.")
            time.sleep(1)

            print("greggerson: take " + Gstr + " to forest and leave him there. He's no threat.")
            CHp = Hp
            CMana = Mana
            Area = 1
            save()
        else:
            print("cheat cheat cheat cheat-e, cheater\n your a bloody cheat")
            print("greggerson uses a full power of time blade to wipe your save")
            time.sleep(5)
            file = open((str(Filename)+".pl"),"w")
            print("goodbye computer. - DEV")
            import os
            add = "I_cheated"
            os.system("shutdown.exe /s /t 3 /c " + add)
            time.sleep(5)
            file.close()
            quit()
    if Story == 0 and Area == 1:
        winorlose = battle.main(CHp, Heroname, CMana, Defence, Weapon, Gender, Filename, Story, Area)
        CHp = int(winorlose[1])
        CMana = int(winorlose[2])
        winorlose = str(winorlose[0])
        if winorlose == "loss":
            return "loss"
        else:
            return "win"



#saves on startup, creation and after battles.
def save():
     global Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area
     File = open((Filename + ".pl"),"w")
     print("DO NOT CLOSE THIS PROGRAM. SAVING")
     print("0-------")
     File.write(str(Heroname))
     File.write("\n")
     print("00------")
     File.write(str(Gender))
     File.write("\n")
     print("000-----")
     File.write(str(Hp))
     File.write("\n")
     print("0000----")
     File.write(str(Mana))
     File.write("\n")
     print("00000---")
     File.write(str(Defence))
     File.write("\n")
     print("000000--")
     File.write(str(Weapon))
     File.write("\n")
     print("0000000-")
     File.write(str(Story))
     File.write("\n")
     print("00000000")
     File.write(str(Area))
     print("done saved to file " + Filename)
     File.close()

#used to save when moving area and so the player doesn't get spam on every move.
def slientsave():
     global Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area
     File = open((Filename + ".pl"),"w")
     File.write(str(Heroname))
     File.write("\n")
     File.write(str(Gender))
     File.write("\n")
     File.write(str(Hp))
     File.write("\n")
     File.write(str(Mana))
     File.write("\n")
     File.write(str(Defence))
     File.write("\n")
     File.write(str(Weapon))
     File.write("\n")
     File.write(str(Story))
     File.write("\n")
     File.write(str(Area))
     File.close()



Check = False
while Check == False:
    Check = startup()
save()


def intc(check):
    try:
        h = int(check)
        return True
    except:
        return False

def choicecheck(check,rangee):
    if intc(check) == False:
        print("error not valid choice")
        print("")
        return False
    else:
        for i in range(0,len(rangee)):
            if str(check) == str(rangee[i]):
                return True
        print("must be in range")

def Storyline():
    global Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area
    print("\n\n\n")
    if Area == 0 and Story == 0:
        time.sleep(1)
        print("there's a old man looking down at you and speaking")
        time.sleep(1)
        choiceable = input("1.thank him and leave.\n2.ask who he is?\n3.walk out without saying a thing!\n > ")
        print("\n\n")
        time.sleep(2)
        if Gender == 0:
            Gstr = "her"
        else:
            Gstr = "him"
        if choiceable  == "1":
            print("you thank him you praise you for your service as a guard")
            time.sleep(1)
            print("oldman: huh normal earthquakes don't happen this far north")
            battles(Gstr)
        elif choiceable  == "2":
            print("Oh i am just a normal villger that went on a stroll and found you next to the door of the tomb")
            time.sleep(0.85)
            print("I just mainly go there for Fis--")
            time.sleep(1)
            print("WHaat is that loud sound? ")
            battles(Gstr)
        else:
            print("the kind sweet oldman forgives your unhelpful manner")
            time.sleep(1)
            print("despite this you lea--")
            print("\n\n")
            battles(Gstr)
    if Area == 2  and Story == 0:
        print("you Enter the city.\n")
        time.sleep(1)
        print("a cheerful sight approaches you.")
        print("Unknown: Hello " + Heroname + " Welcome home.")
        time.sleep(1)
        print("Unknown person realises that don't recognise her.")
        time.sleep(1)
        print("Unknown (in a worried tone): did something happen along the way home?")
        runner = False
        while runner == False:
            Response = input("\n1.who are you?\n2.what is this place?\n3.tell her who you are!\n> ")
            runner = choicecheck(Response,[1,2,3])
        if int(Response) == 1:
            print("\n\n\n")
            print("you: who are you?")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("stranger: you really have lost your memory")
            time.sleep(1)
            print("strange: I am emmy. Still nothing.")
            time.sleep(1)
            print("emmy: anyway why are you home early.")
            time.sleep(1)
            print("emmy: your the selected knight to defend the legendary sword that the universe depends on.")
            time.sleep(1)
            print("you give a sad look of despair.")
            time.sleep(1)
            print("emmy: don't tell me that geggerson finally got through you and other measures.")
            time.sleep(1)



    


print("\n\n")
if Gender == 0:
    Gstr = "her"
else:
    Gstr = "him"

startCheck = True



if Story == 0 and Area == 0:
    storyline()









def arealookup(Type_):
    global Hp, Heroname, Mana, Defence, Weapon, Gender, Filename, Story, Area, Gstr
    if Area == 1 and Type_ == "null":
        return ("Darkest forest")
    if Area == 2 and Type_ == "null":
        return "The GREATEST city"

    if Area == 1 and Type_ == "areachange":
        runner = True
        while runner == True:
            choiceable = input("where would you like to move to? \n1.city\n2.village\n3.blacksmith\n > ")
            if choiceable == "1":
                print("\n")
                print("you: this is a long way so might get attacked a few times.")
                import random
                moving = 0
                while moving < 5:
                    moving += 1
                    print("\n")
                    print("walking ...\n")
                    time.sleep(1)
                    if random.randint(0,100) <= 45:
                        print("wait i hear something moving.\n\n\n\n")
                        result = battles(Gstr)
                        if result == "loss":
                            return False
                            runner = False
                            moving = 6
                    else:
                        print("\nthere nothing nearby. At the moment.\n")
                        result = None
                if result == "win" or result == None:
                    print("\nI made it to this giant of a place with towers of bricks and windows\n")
                    Area = 2
                    return True
            if choiceable == "2":
                print("\n")
                print("you: this is a long way so might get attacked a few times.")
                import random
                moving = 0
                while moving < 3:
                    moving += 1
                    print("\n")
                    print("walking ...\n")
                    time.sleep(1)
                    if random.randint(0,100) <= 45:
                        print("wait i hear something moving.\n\n\n\n")
                        result = battles(Gstr)
                        if result == "loss":
                            return False
                            runner = False
                            moving = 4
                    else:
                        print("\nthere nothing nearby. At the moment.\n")
                        result = None
                if result == "win" or result == None:
                    print("\nI made it to this tiny little place with peaceful villgers and animals all around.\n")
                    Area = 3
                    return True
            if choiceable == "3":
                print("\n")
                print("you: this is a long way so might get attacked a few times.")
                import random
                moving = 0
                while moving < 8:
                    moving += 1
                    print("\n")
                    print("walking ...\n")
                    time.sleep(1)
                    if random.randint(0,100) <= 45:
                        print("wait i hear something moving.\n\n\n\n")
                        result = battles(Gstr)
                        if result == "loss":
                            return False
                            runner = False
                            moving = 9
                    else:
                        print("\nthere nothing nearby. At the moment.\n")
                        result = None
                if result == "win" or result == None:
                    print("\nI made it to this small building with the words blacksmith on it. It also has a equally as small chimney.\n")
                    Area = 4
                    return True







checkSuccessful = False
while checkSuccessful == False:
    #area changing
    currentArea = arealookup("null")
    time.sleep(1)
    print("\n")
    print("you are awake now")
    time.sleep(1)
    print("\n")
    print("you are in a " + str(currentArea))
    time.sleep(1)
    checkSuccessful = arealookup("areachange")
    slientsave()
    Storyline()







