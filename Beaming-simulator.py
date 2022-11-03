import random
import time
import requests
import os
import json
beamem_orna = [True,False,False,True,False,True]
dualhook_orna = [True,False,False,True,False,True]
if os.name == "nt":
    os.system("color 2")
else:
    print("Looks like You're A Termux / Linux User.\nWe Could not change the terminal color to green.")
    time.sleep(2)
robux = 0
have_image_logger = False
have_one_click = False
have_stub = False
money = 0
dualhook = 0
def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

beamed_them = ["ohhh ok lemme go there\n(beamed them and their pin was 1548 XD)","soo it looks sus but lemme go in that link\n(they clicked  and you took their robux + adopt me pets)","why not, i'll do that, wait...\n(beamed them after 1 minutes took their robux plus mm2 knifes)","i got scammed before by this, but i trust you, let me go there.... \n(bro got scammed 2 times , but still had some robux)","finally someone dmed me, ofc, just wait \n(you took their robux + ingame items)","OH Ok, after that wanna be my friend \n(POV: He's 9 years old and he had lots of robux and you took them)"]
notbeamed_them = ["its scam link \n(blocked u)","NIGGGERRRR I WONT CLICK THAT SHIT \n(simply reported you and blocked)","shit... get a life i wont click your shit \n(blocked u)","lol im a beamer too.... dont try to beam me \n(just not responded after that)","bro tryna beam me \n(blocked you)","no \n(blocked and banned from the server you used to dm them)","goofy ahh get a life \n(blocked u)"]
print("\nI DO NOT CONDONE BEAMING AND COMPROMISING ROBLOX ACCOUNTS ON THIS GAME, JUST MADE THIS FOR FUN\n")
time.sleep(2)

cls()
username = input("hmmm, lets pick up a cool name for your alt beaming account\nAccount Name >> ")
method = input("What method you're gonna use ? \n[1] Fake profile phishing\n[2] Fake private server\n[3] HAR Method\nMethod Number (ex. 1) >> ")
cls()

if method == "1":
    print("Your method is now Fake profile phishing.")
    method = "Fake profile Phishing"
    link = "https://wwx-roblox.com/users/623486385/profile"
elif method == "2":
    print("Your method is now Fake private server phishing.")
    method = "Fake private server phishing"
    link = "https://wwx-roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=1540374766387680189638314"
elif method == "3":
    print("Your method is now HAR Method.")
    method = "HAR Method"
    link = "https://www.youtube.com/watch?v=I8C0ph40jrQ"
else:
    print("method is invalid")
    time.sleep(2)
    exit()
print("Type !help and press enter to learn the game.")
while True:
    command_user = input(">>").lower()
    if command_user == "!help":
        cls()
        print("\n!beam - you use this command to beam someone\n!robux - shows how much u beamed\n!method - change your method\n!robux2money - convert yo robux to money\n!money - shows your balance in $$$\n!buymethod - lets you buy better methods to get beams easier\n!dualhook - sends dualhooked link generators to random beamers. you can check the results with typing !hits\n!hits - use this to check how much accounts you gained through dualhooking")
    elif command_user == "!dualhook":
        print("Sent dualhooked generator to other beamers.\n")
        dualhook += 1
        time.sleep(1.5)
        cls()

    elif command_user == "!hits":
        if dualhook == 0:
            print("You never sent any dualhooks to anyone.")
        else:
            nigga = random.choice(dualhook_orna)
            if nigga == True:
                accs = dualhook * random.randrange(1, 4)
                totalrbxmade = random.randrange(1,250*dualhook)
                print(
                    f"You gained {str(accs)} Accounts & {str(totalrbxmade)} Robux by sending your dualhooked generator to other beamers.")
                time.sleep(2)
                robux += totalrbxmade
            else:
                print("You haven't gotten any hits")
    elif command_user == "!beam":
        cls()
        victim_req = requests.get("https://api.namefake.com/").text
        victim_json = json.loads(victim_req)
        victim_name = victim_json["name"]
        print("Now, the link below is your fake link. type the message before it to make victim click your link\n <message> "+link)
        user_message = input("Your message >> ")+" "+ link
        time.sleep(2)
        cls()
        print(username+" >> "+user_message)
        time.sleep(random.randrange(1,4))
        gonna_beam = random.choice(beamem_orna)
        if gonna_beam == True:
            print(victim_name+" >> "+random.choice(beamed_them))
            profit = random.randrange(2,12344)
            password = requests.get("https://www.passwordrandom.com/query?command=password").text
            summary = random.randrange(0,99999)
            rap = random.randrange(1,1000)
            value = random.randrange(1,1000)
            time.sleep(1)

            print("\nVictim Name : "+victim_name)
            print("Robux Balance : "+str(profit))
            print("Password : "+password)
            print("Summary : "+str(summary))
            print(f"\nYou beamed {profit} Robux out of "+victim_name)
            robux += profit
            print("Your Robux Balance : "+str(robux))
        else:
            print(victim_name + ">> " + random.choice(notbeamed_them))
            time.sleep(3.5)
            cls()
            print("POV : victim didn't believe your link.")
    elif command_user == "!robux":
        print("Robux Balance : "+str(robux))
    elif command_user == "!method":
        newmethod = input("Which Method you want to use?\n[0] HAR Method\n[1] Fake profile phishing\n[2] Fake private server\n[3] Image Logger (Paid)\n[4] 1 Click Beaming Link (Paid)\n[5] Malware/Stub Builder (Paid)\nMethod Number (ex. 1) >> ")
        if newmethod == "1":
            print("Your method is now fake profile phishing.")
            method = "Fake profile phishing"
            link = "https://wwx-roblox.com/users/623486385/profile"
            time.sleep(2)
        elif newmethod == "0":
            print("Your method is now HAR Method")
            method = "HAR Method"
            link = "https://www.youtube.com/watch?v=I8C0ph40jrQ"
            time.sleep(2)
        elif newmethod == "2":
            print("Your method is now Fake private server")
            method = "Fake private server"
            link = "https://wwx-roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=1540374766387680189638314"
            time.sleep(2)
        elif newmethod == "3":
            if have_image_logger == True:
                print("Your method is now image logger")
                method = "Image logger"
                link = "https://cdn.discordapp.com/attachments/983813009694662666/989512486703235122/dog.png"
                time.sleep(2)
            else:
                print("You gotta buy that method with the command !buymethod")
        elif newmethod == "4":
            if have_one_click == True:
                print("Your method is now one click beaming link")
                link = "veryreallink.xyz"
                method = "1 Click Beaming Link"
                time.sleep(2)
            else:
                print("You gotta buy that method with the command !buymethod")
        elif newmethod == "5":
            if have_stub == True:
                link = "https://upload.io/not-malware.exe"
                print("Your method is now Malware application. (Stub)")
                time.sleep(2)
                cls()
        else:
            print("method is dead (not valid)")
    elif command_user == "!robux2money":

        cls()
        print("Robux Balance : "+str(robux))
        print("1 Robux = $0.0125 ")
        rbx2money = input("How much robux you want to convert to money? >> ")
        if int(rbx2money) > robux:
            print("You cant convert "+rbx2money+" robux to money because you dont have enough robux.")
        else:
            print("Converting "+rbx2money+" Robux to Money....")
            robux -= int(rbx2money)
            money += int(rbx2money) * 0.0125

            print("Money Balance : "+str(money))
            print("Robux Balance : "+str(robux))
    elif command_user == "!money":
        print("Money Balance : "+str(money))
    elif command_user == "!buymethod":
        print("Which Method you're gonna buy?\n[1] Image logger 200$\n[2] 1 Click beaming link 100$\n[3] Malware Builder (.EXE) 50$")
        chmethod = input(">> ")
        if chmethod == "1":
            if money > 200 or money == 200:
                money -= 200
                have_image_logger = True
                print("now you have 1 Click image logger !\ntype !method and equip the method")

            else:
                print("An error occured while trying to buy. (You dont have enough money to buy)")
        elif chmethod == "2":

            if money > 100 or money == 100:
                money -= 100
                have_one_click = True
                print("now you have 1 Click logger link !\ntype !method and equip the method")

            else:
                print("An error occured while trying to buy. (You dont have enough money to buy)")
        elif chmethod == "3":
            if money > 50 or money == 50:
                money -= 50
                have_stub = True
                print("now you have Paid stub builder ! (Malware Builder)\ntype !method and equip the method")

        else:
            print("method not found (invalid method, use numbers)")
