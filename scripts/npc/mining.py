# Cole - Ardentmill
status = -1
ans = 0

def init():
    # If does not have mining
    sm.sendNext("Now what can I do for ya?\r\n#L0#Hear an explanation about #bMining#k#l\r\n#L1#Learn #bMining#k#l")

def action(answer, response):
    global status
    status += 1
    sm.chat("answer is " + str(answer) + ", response is " + str(response))
    if status == 0:
        if response == 0:
            sm.sendSayOkay("If you're looking to get yourself some minerals, all you need is the Mining skill. Refine the "
                        "minerals you collect in one of them molds #p9031006# sells, then use them to craft all sorts "
                        "of useful items.")
            sm.dispose()
        else:
            sm.sendAskYesNo("Do you really want to learn #bMining#k? It'll cost you some money... #b5,000 Mesos#k, "
                            "to be exact.")
    if status == 1 and answer == 1:
        sm.sendSayOkay("I sadly cannot give you mining yet :(")
        sm.dispose()
    else:
        sm.dispose()