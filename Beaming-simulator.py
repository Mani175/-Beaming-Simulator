# coded by Mani.#0001
import random
import time
import requests
import os
import json
beamem_orna = [True,False]
os.system("color 2")
robux = 0
have_image_logger = False
have_one_click = False
money = 0
dualhook = 0
beamed_them = ["ohhh ok lemme go there\n(beamed them and their pin was 1548 XD)","soo it looks sus but lemme go in that link\n(they clicked  and you took their robux + adopt me pets)","why not, i'll do that, wait...\n(beamed them after 1 minutes took their robux plus mm2 knifes)","i got scammed before by this, but i trust you, let me join \n(bro got scammed 2 times , but still had some robux)","finally someone dmed me, ofc i will join you, just wait \n(you took their robux + ingame items)"]
notbeamed_them = ["its scam link \n(blocked u)","NIGGGERRRR I WONT CLICK THAT SHIT \n(simply reported you and blocked)","shit... get a life i wont click your shit \n(blocked u)","lol im a beamer too.... dont try to beam me \n(just not responded after that)","nigga tryna beam me \n(blocked you)","no \n(blocked and banned from the server you used to dm them)","goofy ahh nigga get a life \n(blocked u)"]
print("\nI DO NOT CONDONE BEAMING AND COMPROMISING ROBLOX ACCOUNTS ON THIS GAME, JUST MADE THIS FOR FUN\n")
time.sleep(2)
os.system("cls")
username = input("hmmm, lets pick up a cool name for your alt beaming account\nAccount Name >> ")
method = input("What method you're gonna use ? \n[1] Fake profile phishing\n[2] Fake private server\n[3] HAR Method\nMethod Number (ex. 1) >> ")
os.system("cls")
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
        os.system("cls")
        print("\n!beam - you use this command to beam someone\n!robux - shows how much u beamed\n!method - change your method\n!robux2money - convert yo robux to money\n!money - shows your balance in $$$\n!buymethod - lets you buy better methods to get beams easier\n!dualhook - sends dualhooked link generators to random beamers. you can check the results with typing !hits\n!hits - use this to check how much accounts you gained through dualhooking")
    elif command_user == "!dualhook":
        print("Sent dualhooked generator to other beamers.\n")
        dualhook += 1
        time.sleep(3)
        os.system("cls")
    elif command_user == "!hits":
        accs = dualhook * random.randrange(1,4)
        totalrbxmade = accs * random.randrange(1,1230)
        print(f"You gained {str(accs)} Accounts & {str(totalrbxmade)} Robux by sending your dualhooked generator to other beamers.")
        robux += totalrbxmade
    elif command_user == "!beam":
        os.system("cls")
        victim_req = requests.get("https://api.namefake.com/").text
        victim_json = json.loads(victim_req)
        victim_name = victim_json["name"]
        print("Now, the link below is your fake link. type the message before it to make victim click your link\n <message> "+link)
        user_message = input("Your message >> ")+" "+ link
        time.sleep(2)
        os.system("cls")
        print(username+" >> "+user_message)
        time.sleep(random.randrange(1,4))
        gonna_beam = random.choice(beamem_orna)
        if gonna_beam == True:
            print(victim_name+" >> "+random.choice(beamed_them))
            profit = random.randrange(2,12344)
            time.sleep(3.5)

            print("\nYou beamed "+str(profit)+" out of "+victim_name)
            robux += profit
            print("Your Robux Balance : "+str(robux))
        else:
            print(victim_name + ">> " + random.choice(notbeamed_them))
            time.sleep(3.5)
            os.system("cls")
            print("POV : victim didn't believe your link.")
    elif command_user == "!robux":
        print("Robux Balance : "+str(robux))
    elif command_user == "!method":
        newmethod = input("Which Method you want to use?\n[0] HAR Method\n[1] Fake profile phishing\n[2] Fake private server\n[3] Image Logger (Paid)\n[4] 1 Click Beaming Link (Paid)\nMethod Number (ex. 1) >> ")
        if newmethod == "1":
            print("Your method is now fake profile phishing.")
            method = "Fake profile phishing"
            link = "https://wwx-roblox.com/users/623486385/profile"
        elif newmethod == "0":
            print("Your method is now HAR Method")
            method = "HAR Method"
            link = "https://www.youtube.com/watch?v=I8C0ph40jrQ"
        elif newmethod == "2":
            print("Your method is now Fake private server")
            method = "Fake private server"
            link = "https://wwx-roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=1540374766387680189638314"
        elif newmethod == "3":
            if have_image_logger == True:
                print("Your method is now image logger")
                method = "Image logger"
                link = "https://cdn.discordapp.com/attachments/983813009694662666/989512486703235122/dog.png"
            else:
                print("You gotta buy that method with the command !buymethod")
        elif newmethod == "4":
            if have_one_click == True:
                print("Your method is now one click beaming link")
                link = "veryreallink.xyz"
                method = "1 Click Beaming Link"
            else:
                print("You gotta buy that method with the command !buymethod")

        else:
            print("method is dead (not valid)")
    elif command_user == "!robux2money":
        os.system("cls")
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
        print("Which Method you're gonna buy?\n[1] Image logger 200$\n[2] 1 Click beaming link 100$")
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

        else:
            print("method not found (invalid method, use numbers)")
