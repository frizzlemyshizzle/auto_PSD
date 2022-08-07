import win32com.client
import gspread
import os
import time
import gspread
import standingsClass as sc
import configparser


startTime = time.time()
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
wks = sh.worksheet("TableOutput")

#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"config.txt"))
configPath = config.get('config', 'Path')
configWeek = config.get('config', 'Week')


#############
# PNG Setup #
#############
options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit


offset = 1
premCount = 0
masterCount = 0
eliteCount = 0
rivalCount = 0
challCount = 0
prospCount = 0

tierCount = wks.get("A2:A")

for i in tierCount:
    if i[0] == 'Premier':
        premCount += 1
    elif i[0] == 'Master':
        masterCount += 1
    elif i[0] == 'Elite':
        eliteCount += 1
    elif i[0] == 'Rival':
        rivalCount += 1
    elif i[0] == 'Challenger':
        challCount += 1
    elif i[0] == 'Prospect':
        prospCount += 1

premCount += offset

##########################
# Sheet Indexes 19/07/22 #
##########################
premIdx = str("A2:K{}".format(premCount))
masterIdx = str("A{}:K{}".format(premCount + 1, premCount + masterCount))
eliteIdx = str("A{}:K{}".format(premCount + masterCount + 1, premCount +
                                masterCount + eliteCount))
rivalIdx = str("A{}:K{}".format(premCount + masterCount + eliteCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount))
challIdx = str("A{}:K{}".format(premCount + masterCount + eliteCount + rivalCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount +
                                challCount))
prospIdx = str("A{}:K{}".format(premCount + masterCount + eliteCount + rivalCount + 
                                challCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount +
                                challCount + prospCount))     

#####################
# Sheet Data Tables #
#####################
premData = wks.get(premIdx)
masterData = wks.get(masterIdx)
eliteData = wks.get(eliteIdx)
rivalData = wks.get(rivalIdx)
challData = wks.get(challIdx)
prospData = wks.get(prospIdx)

####################
# Data to Classes #
####################

# Premier Data
for row in premData:
    sc.PremStandings.franchOrder.append(str(row[2]).upper())
    sc.PremStandings.teamOrder.append(str(row[3]).upper())
    sc.PremStandings.gpOrder.append(str(row[4]))
    sc.PremStandings.gwOrder.append(str(row[5]))
    sc.PremStandings.glOrder.append(str(row[6]))
    sc.PremStandings.gsOrder.append(str(row[7]))
    sc.PremStandings.gcOrder.append(str(row[8]))
    sc.PremStandings.gdOrder.append(str(row[9]))
    sc.PremStandings.winPercOrder.append(str(row[10]))


# Master Data
for row in masterData:
    sc.MasterStandings.franchOrder.append(str(row[2]).upper())
    sc.MasterStandings.teamOrder.append(str(row[3]).upper())
    sc.MasterStandings.gpOrder.append(str(row[4]))
    sc.MasterStandings.gwOrder.append(str(row[5]))
    sc.MasterStandings.glOrder.append(str(row[6]))
    sc.MasterStandings.gsOrder.append(str(row[7]))
    sc.MasterStandings.gcOrder.append(str(row[8]))
    sc.MasterStandings.gdOrder.append(str(row[9]))
    sc.MasterStandings.winPercOrder.append(str(row[10]))

# Elite Data
for row in eliteData:
    sc.EliteStandings.franchOrder.append(str(row[2]).upper())
    sc.EliteStandings.teamOrder.append(str(row[3]).upper())
    sc.EliteStandings.gpOrder.append(str(row[4]))
    sc.EliteStandings.gwOrder.append(str(row[5]))
    sc.EliteStandings.glOrder.append(str(row[6]))
    sc.EliteStandings.gsOrder.append(str(row[7]))
    sc.EliteStandings.gcOrder.append(str(row[8]))
    sc.EliteStandings.gdOrder.append(str(row[9]))
    sc.EliteStandings.winPercOrder.append(str(row[10]))


# Rival Data
for row in rivalData:
    sc.RivalStandings.franchOrder.append(str(row[2]).upper())
    sc.RivalStandings.teamOrder.append(str(row[3]).upper())
    sc.RivalStandings.gpOrder.append(str(row[4]))
    sc.RivalStandings.gwOrder.append(str(row[5]))
    sc.RivalStandings.glOrder.append(str(row[6]))
    sc.RivalStandings.gsOrder.append(str(row[7]))
    sc.RivalStandings.gcOrder.append(str(row[8]))
    sc.RivalStandings.gdOrder.append(str(row[9]))
    sc.RivalStandings.winPercOrder.append(str(row[10]))


# Challenger Data
for row in challData:
    sc.ChallStandings.franchOrder.append(str(row[2]).upper())
    sc.ChallStandings.teamOrder.append(str(row[3]).upper())
    sc.ChallStandings.gpOrder.append(str(row[4]))
    sc.ChallStandings.gwOrder.append(str(row[5]))
    sc.ChallStandings.glOrder.append(str(row[6]))
    sc.ChallStandings.gsOrder.append(str(row[7]))
    sc.ChallStandings.gcOrder.append(str(row[8]))
    sc.ChallStandings.gdOrder.append(str(row[9]))
    sc.ChallStandings.winPercOrder.append(str(row[10]))

# Prospect Data
for row in prospData:
    sc.ProspStandings.franchOrder.append(str(row[2]).upper())
    sc.ProspStandings.teamOrder.append(str(row[3]).upper())
    sc.ProspStandings.gpOrder.append(str(row[4]))
    sc.ProspStandings.gwOrder.append(str(row[5]))
    sc.ProspStandings.glOrder.append(str(row[6]))
    sc.ProspStandings.gsOrder.append(str(row[7]))
    sc.ProspStandings.gcOrder.append(str(row[8]))
    sc.ProspStandings.gdOrder.append(str(row[9]))
    sc.ProspStandings.winPercOrder.append(str(row[10]))



tierCcount = 0

def checkTier(tierCount):
    psApp = win32com.client.Dispatch("Photoshop.Application")
    psApp.Open(os.path.join(configPath, "RSC_Standings.psd"))
    doc = psApp.Application.ActiveDocument 
    titleGroup = doc.activeLayer = (doc.layerSets["Title"])
    print("Checking Tier...")
    if tierCount < 6:
        titleGroup = doc.activeLayer = (doc.layerSets["Title"])
        if tierCount == 0:
            tier = 'Premier'
            tierClass = sc.PremStandings
            tierGroup = titleGroup.layerSets["Premier"]
        if tierCount == 1:
            tier = 'Master'
            tierClass = sc.MasterStandings
            tierGroup = titleGroup.layerSets["Master"]
        if tierCount == 2:
            tier = 'Elite'
            tierClass = sc.EliteStandings
            tierGroup = titleGroup.layerSets["Elite"]        
        if tierCount == 3:
            tier = 'Rival'
            tierClass = sc.RivalStandings
            tierGroup = titleGroup.layerSets["Rival"]
        if tierCount == 4:
            tier = 'Challenger'
            tierClass = sc.ChallStandings
            tierGroup = titleGroup.layerSets["Challenger"]
        if tierCount == 5:
            tier = 'Prospect'
            tierClass = sc.ProspStandings
            tierGroup = titleGroup.layerSets["Prospect"]

        tierGroup.visible = True
        weekNum = titleGroup.artLayers["WeekNum"]
        weekNumText = weekNum.TextItem
        weekNumText.contents = "WEEK " + str(configWeek)
        tierCount += 1
        editStandings(tier, tierClass, tierCount, tierGroup)
        
    else:
        print("------------------")
        print("All tiers complete")
        print("Finished")
        endTime = time.time()
        print("Execution time: " + str(endTime-startTime))

def editStandings(tier, tierClass, tierCount, tierGroup):
    psApp = win32com.client.Dispatch("Photoshop.Application")
    psApp.Open(os.path.join(configPath, "RSC_Standings.psd"))
    doc = psApp.Application.ActiveDocument 
    currLoop = 0
    maxLoops = len(tierClass.franchOrder)
    gameCount = 0
    print("Tier: " + tier)
    if tier == "Premier":
        premFlag = True
    else:
        premFlag = False
    confFlag = True
    while currLoop < maxLoops:
        psApp.Open(os.path.join(configPath, "RSC_Standings.psd"))
        doc = psApp.Application.ActiveDocument 
        confGroup = doc.layerSets["Conference"]
        if currLoop < maxLoops//2:
            conf = "Ignis"
            confBanner = confGroup.artLayers["Ignis"]
            confBanner.visible = True
        if currLoop >= maxLoops//2 and currLoop < maxLoops:
            conf = "Glacies"
            confBanner = confGroup.artLayers["Glacies"]
            if confFlag == True:
                gameCount = 0
                confGroup.artLayers["Ignis"].visible = False
                confFlag = False
        confBanner.visible = True
        titleGroup = doc.activeLayer = (doc.layerSets["Title"])
        tierGroup = titleGroup.layerSets[tier]
        tierGroup.visible = True

        teamGroup = doc.layerSets["Team {}".format(gameCount + 1)]

        teamNameLayer = teamGroup.ArtLayers["Team"] ## Team Name
        playedLayer = teamGroup.ArtLayers["Played"] ## Games Played
        winPercLayer = teamGroup.ArtLayers["WinPerc"] ## Win Percentage
        gfLayer = teamGroup.ArtLayers["GF"] ## Goals For
        gaLayer = teamGroup.ArtLayers["GA"] ## Goals Against
        gdLayer = teamGroup.ArtLayers["GD"] ## Goal Difference
        winsLayer = teamGroup.ArtLayers["Wins"] ## Wins
        logoGroup = (teamGroup.layerSets["Logo"]) ## Logo Group

        teamName = tierClass.teamOrder[0]
        teamText = teamNameLayer.TextItem
        teamText.contents = str(teamName)

        franch = tierClass.franchOrder[0] ## Get franchise name of 1st team
        franchAbbr = sc.franchises[franch] ## Get Franchise Abbreviation
        teamLogo = (logoGroup.ArtLayers[franchAbbr]) ## Find Franch logo
        

        ## Games Played Edit
        gamesPlayed = tierClass.gpOrder[0]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)
        ## Win Perc Edit
        winPerc = tierClass.winPercOrder[0]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)
        ## Goals For Edit
        goalsFor = tierClass.gsOrder[0]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)
        ## Goals Against Edit
        goalsAgainst = tierClass.gcOrder[0]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)
        ## Goal Difference Edit
        goalDiff = tierClass.gdOrder[0] 
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)
        ## Wins Edit
        teamWins = tierClass.gwOrder[0]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        ## Unhide Logo
        teamLogo.visible = True
        print("Team {} done.".format(gameCount + 1))
        print("---------------")
        currLoop += 1
        gameCount += 1
        if premFlag == True:
            teamGroup9 = doc.layerSets["Team 9"]
            teamGroup9.visible = False
            teamGroup10 = doc.layerSets["Team 10"]
            teamGroup10.visible = False
        if currLoop == maxLoops//2:
            pngImage = (os.path.join(configPath, "Outputs/Standings-W{}-{}-{}.png".format(configWeek, tier, conf)))
            print("Saving PNG for {}, {}".format(tier, conf))
            print("-----------------------------")
            doc.Export(ExportIn=pngImage, ExportAs=2, Options=options)
            doc.Close(2)
        if currLoop == maxLoops:
            pngImage = (os.path.join(configPath, "Outputs/Standings-W{}-{}-{}.png".format(configWeek, tier, conf)))
            print("Saving PNG for {}, {}".format(tier, conf))
            print("-----------------------------")
            doc.Export(ExportIn=pngImage, ExportAs=2, Options=options)

        tierClass.teamOrder.pop(0)
        tierClass.franchOrder.pop(0)
        tierClass.gpOrder.pop(0)
        tierClass.winPercOrder.pop(0)
        tierClass.gsOrder.pop(0)
        tierClass.gcOrder.pop(0)
        tierClass.gdOrder.pop(0)
        tierClass.gwOrder.pop(0)
    doc.Close(2)

    checkTier(tierCount)

checkTier(tierCcount)