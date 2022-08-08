import win32com.client
import gspread
import configparser
import fixturesClass as fc
import os
import time

startTime = time.time()
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
fixturesSheet = sh.worksheet("FixturesOutput")
tableSheet = sh.worksheet("TableOutput")



premFixtures = []
masterFixtures = []
eliteFixtures = []
rivalFixtures = []
challFixtures = []
prospFixtures = []

#########
# Setup #
#########
options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit

#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"fixturesConfig.txt"))
configWeek = config.get('config', 'Week')
configPath = config.get('config', 'Path')


########################
# Count Nmber of Teams #
########################
teamCounts = tableSheet.get("A2:A")

offset = 1
premTeams = 0
masterTeams = 0
eliteTeams = 0
rivalTeams = 0
challTeams = 0
prospTeams = 0

for i in teamCounts:
    if i[0] == 'Premier':
        premTeams += 1
    elif i[0] == 'Master':
        masterTeams += 1
    elif i[0] == 'Elite':
        eliteTeams += 1
    elif i[0] == 'Rival':
        rivalTeams += 1
    elif i[0] == 'Challenger':
        challTeams += 1
    elif i[0] == 'Prospect':
        prospTeams += 1


#########################
# Count Number of Games #
#########################
gameCounts = fixturesSheet.get("A2:A")

premGames = 0
masterGames = 0
eliteGames = 0
rivalGames = 0
challGames = 0
prospGames = 0

for i in gameCounts:
    if i[0] == 'Premier':
        premGames += 1
    elif i[0] == 'Master':
        masterGames += 1
    elif i[0] == 'Elite':
        eliteGames += 1
    elif i[0] == 'Rival':
        rivalGames += 1
    elif i[0] == 'Challenger':
        challGames += 1
    elif i[0] == 'Prospect':
        prospGames += 1

##########################
# Sheet Indexes 20/07/22 #
##########################
premGamesOffset = premGames + 1
premIdx = str("A2:K{}".format(premGamesOffset))
masterIdx = str("A{}:K{}".format(premGamesOffset + 1, premGamesOffset + masterGames))
eliteIdx = str("A{}:K{}".format(premGamesOffset + masterGames + 1, premGamesOffset +
                                masterGames + eliteGames))
rivalIdx = str("A{}:K{}".format(premGamesOffset + masterGames + eliteGames + 1,
                                premGamesOffset + masterGames + eliteGames +  rivalGames))
challIdx = str("A{}:K{}".format(premGamesOffset + masterGames + eliteGames + rivalGames + 1,
                                premGamesOffset + masterGames + eliteGames +  rivalGames +
                                challGames))
prospIdx = str("A{}:K{}".format(premGamesOffset + masterGames + eliteGames + rivalGames + 
                                challGames + 1,
                                premGamesOffset + masterGames + eliteGames +  rivalGames +
                                challGames + prospGames))   




##########################
# Split Fixtures by Tier #
##########################

# Premier
premData = fixturesSheet.get(premIdx)
for row in premData:
    if row[2] == configWeek:
        premFixtures.append(row[3:])
# Master
masterData = fixturesSheet.get(masterIdx)
for row in masterData:
    if row[2] == configWeek:
        masterFixtures.append(row[3:])  
# Elite
eliteData = fixturesSheet.get(eliteIdx)
for row in eliteData:
    if row[2] == configWeek:
        eliteFixtures.append(row[3:])
# Rival
rivalData = fixturesSheet.get(rivalIdx)
for row in rivalData:
    if row[2] == configWeek:
        rivalFixtures.append(row[3:])
# Challenger
challData = fixturesSheet.get(challIdx)
for row in challData:
    if row[2] == configWeek:
        challFixtures.append(row[3:])
# Prospect
prospData = fixturesSheet.get(prospIdx)
for row in prospData:
    if row[2] == configWeek:
        prospFixtures.append(row[3:])


###########################
# Store fixtures to class #
###########################

for row in premFixtures:
    fc.prem.teamOrder.append(str(row[0]).upper()) # Team 1
    fc.prem.teamOrder.append(str(row[4]).upper()) # Team 2
    if len(row) == 7:
        fc.prem.dateOrder.append(str(row[5][0:5])) # Date (If Scheduled)
    else:
        fc.prem.dateOrder.append(str("TBC"))

for row in masterFixtures:
    fc.master.teamOrder.append(str(row[0]).upper())
    fc.master.teamOrder.append(str(row[4]).upper())
    fc.master.dateOrder.append(str(row[5][0:5]))
    if len(row) == 7:
        fc.master.dateOrder.append(str(row[5][0:5]))
    else:
        fc.master.dateOrder.append(str("TBC"))

for row in eliteFixtures:
    fc.elite.teamOrder.append(str(row[0]).upper())
    fc.elite.teamOrder.append(str(row[4]).upper())
    fc.elite.dateOrder.append(str(row[5][0:5]))
    if len(row) == 7:
        fc.elite.dateOrder.append(str(row[5][0:5]))
    else:
        fc.elite.dateOrder.append(str("TBC"))

for row in rivalFixtures:
    fc.rival.teamOrder.append(str(row[0]).upper())
    fc.rival.teamOrder.append(str(row[4]).upper())
    fc.rival.dateOrder.append(str(row[5][0:5]))
    if len(row) == 7:
        fc.rival.dateOrder.append(str(row[5][0:5]))
    else:
        fc.rival.dateOrder.append(str("TBC"))

for row in challFixtures:
    fc.chall.teamOrder.append(str(row[0]).upper())
    fc.chall.teamOrder.append(str(row[4]).upper())
    fc.chall.dateOrder.append(str(row[5][0:5]))
    if len(row) == 7:
        fc.chall.dateOrder.append(str(row[5][0:5]))
    else:
        fc.chall.dateOrder.append(str("TBC"))

for row in prospFixtures:
    fc.prosp.teamOrder.append(str(row[0]).upper())
    fc.prosp.teamOrder.append(str(row[4]).upper())
    if len(row) == 7:
        fc.prosp.dateOrder.append(str(row[5][0:5]))
    else:
        fc.prosp.dateOrder.append(str("TBC"))


## Add logo order to classes
for team in fc.prem.teamOrder: # Premier
    franchAbbr = fc.teamsPrem[team]
    fc.prem.logoOrder.append(franchAbbr)

for team in fc.master.teamOrder: # Master
    franchAbbr = fc.teamsMaster[team]
    fc.master.logoOrder.append(franchAbbr)

for team in fc.elite.teamOrder: # Elite
    franchAbbr = fc.teamsElite[team]
    fc.elite.logoOrder.append(franchAbbr)

for team in fc.rival.teamOrder: # Rival
    franchAbbr = fc.teamsRival[team]
    fc.rival.logoOrder.append(franchAbbr)

for team in fc.chall.teamOrder: # Challenger
    franchAbbr = fc.teamsChall[team]
    fc.chall.logoOrder.append(franchAbbr)

for team in fc.prosp.teamOrder: # Prospect
    franchAbbr = fc.teamsProsp[team]
    fc.prosp.logoOrder.append(franchAbbr)



premCount = len(fc.teamsPrem)
masterCount = len(fc.teamsMaster)
elitCount = len(fc.teamsElite)
rivalCount = len(fc.teamsRival)
challCount = len(fc.teamsChall)
prospCount = len(fc.teamsProsp)
totalGames = premCount+(masterCount*2)+(elitCount*2)+(rivalCount*2)+(challCount*2)+(prospCount*2)
loopCount = 0

 

def checkTier(count):
    psApp = win32com.client.Dispatch("Photoshop.Application")
    psApp.Open(os.path.join(configPath, "RSC10_Weekly_Results.psd"))
    doc = psApp.Application.ActiveDocument    
    print("Checking Tier...")
    if count < 6:
        if count == 0:
            tier = 'Premier'
            tierClass = fc.prem
            teamClass = fc.teamsPrem
            topGroup = doc.activeLayer = (doc.layerSets["Premier"])
            pngFixt = (os.path.join(configPath, "Outputs\PremFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\PremFixturesTrans.png"))
        else:
            topGroup = doc.activeLayer = (doc.layerSets["Conference Tiers"])
        if count == 1:
            tier = 'Master'
            tierClass = fc.master
            teamClass = fc.teamsMaster
            pngFixt = (os.path.join(configPath, "Outputs\MasterFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\MasterFixturesTrans.png"))
        if count == 2:
            tier = "Elite"
            tierClass = fc.elite
            teamClass = fc.teamsElite
            pngFixt = (os.path.join(configPath, "Outputs\EliteFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\EliteFixturesTrans.png"))
        if count == 3:
            tier = 'Rival'
            tierClass = fc.rival
            teamClass = fc.teamsRival
            pngFixt = (os.path.join(configPath, "Outputs\RivalFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\RivalFixturesTrans.png"))
        if count == 4:
            tier = 'Challenger'
            tierClass = fc.chall
            teamClass = fc.teamsChall
            pngFixt = (os.path.join(configPath, "Outputs\ChallengerFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\ChallengerFixturesTrans.png"))
        if count == 5:
            tier = 'Prospect'
            tierClass = fc.prosp
            teamClass = fc.teamsProsp
            pngFixt = (os.path.join(configPath, "Outputs\ProspectFixtures.png"))
            pngFixtTrans = (os.path.join(configPath, "Outputs\ProspectFixturesTrans.png"))
        ## Edit Week Number ##
        topGroup.visible = True
        weekGroup = topGroup.layerSets["WeekNumGroup"]
        weekLayer = weekGroup.ArtLayers["WeekNum"]
        weekText = weekLayer.textItem
        weekText.contents = 'WEEK ' + str(configWeek)
        editFixtures(topGroup, teamClass, tierClass, tier, pngFixt, pngFixtTrans)
    else:
        print("Finished")
        endTime = time.time()
        print("Exectution time: " + str((endTime-startTime)))
        input("Press Enter to close.")


def editFixtures(topGroup,teamClass,tierClass, tier, pngFixt, pngFixtTrans):   
    currLoopCount = 0
    maxLoops = len(teamClass)//2
    gameCount = 0
    flag = True
    print("Tier: " + tier)
    print("----------------")
    if tier == "Premier":
        maxLoops = len(teamClass)//2
    else:
        maxLoops = len(teamClass)

    while currLoopCount < maxLoops:
        if currLoopCount < maxLoops//2:
            confGroup = topGroup.layerSets["Glacies"]
            print("Glacies")
        if currLoopCount >= maxLoops//2 and currLoopCount < maxLoops:
            confGroup = topGroup.layerSets["Ignis"]
            print("Ignis")
            if flag == True:
                gameCount = 0
                flag = False
        gameCount += 1
        print("Game: " + str(gameCount))
        ############
        # Row Data #
        ############
        currRow = confGroup.layerSets["Game{}".format(gameCount)]
        # Tier Banner

        # Left Team
        leftTeam = currRow.ArtLayers["LeftTeam"] # Team Name
        leftTeamText = leftTeam.TextItem
        logoGroupLeft = currRow.layerSets["Left Logo"] # Logo Group
        # Right Team
        rightTeam = currRow.ArtLayers["RightTeam"] # Team Name
        rightTeamText = rightTeam.TextItem
        logoGroupRight = currRow.layerSets["Right Logo"] # Logo Group
        # Date
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 
        # Left Logo Select
        leftTeamName = str(tierClass.teamOrder[0])
        leftAbbr = teamClass[leftTeamName]
        print(leftAbbr)
        teamLogoLeft = (logoGroupLeft.ArtLayers[leftAbbr])
        # Right Logo Select
        rightTeamName = str(tierClass.teamOrder[1])
        rightAbbr = teamClass[rightTeamName]
        print(rightAbbr)
        teamLogoRight = (logoGroupRight.ArtLayers[rightAbbr])

        leftTeamText.contents = str(tierClass.teamOrder[0])
        rightTeamText.contents = str(tierClass.teamOrder[1])
        matchDateText.contents = str(tierClass.dateOrder[0])
        teamLogoLeft.visible = True
        teamLogoRight.visible = True
        
        currLoopCount += 1
        tierClass.teamOrder.pop(0)
        tierClass.teamOrder.pop(0)
        tierClass.dateOrder.pop(0)
        print("------")
 
        

    # End of loop, save PNG and close document
    if tier != 'Premier':
        tilesGroup = topGroup.layerSets["Tiles"]
        tierBannerGroup = tilesGroup.layerSets["Tier"]
        tierBanner = tierBannerGroup.artLayers[tier]
        tierBanner.visible = True
    psApp = win32com.client.Dispatch("Photoshop.Application")
    doc = psApp.Application.ActiveDocument 
    doc.Export(ExportIn = pngFixt, ExportAs=2, Options=options)
    bg = doc.artLayers["Background"]
    bg.visible = False
    doc.Export(ExportIn = pngFixtTrans, ExportAs=2, Options=options)
    doc.Close(2)
    print("PNGs saved.")
    print(tier + " Tier Complete")
    print("Reloading PSD. This may take some time.")
    print("----------------------------------------")
    if tier == 'Premier':
        count = 1
    if tier == 'Master':
        count = 2
    if tier == 'Elite':
        count = 3
    if tier == 'Rival':
        count = 4
    if tier == 'Challenger':
        count = 5
    if tier == 'Prospect':
        count = 6
    checkTier(count)
print("Editing upcoming fixtures for week {} games".format(configWeek))
print("Loading Photoshop and/or PSD. This may take some time.")
print("--------------------------------------------------------")
checkTier(loopCount)