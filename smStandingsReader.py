import gspread
import configparser
import fixturesClass as fc
import win32com.client
import os


#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"SMStandingsConfig.txt"))
configWeek = config.get('config', 'Week')
configTier = config.get('config', 'Tier')
configConf = config.get('config', 'Conference')
configDirectory = config.get('config', 'Path')


###############
# Class Setup #
###############
class standings:
    teamOrder = []
    winsOrder = []
    abbrOrder = []


############
# GS Setup #
############
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
wks = sh.worksheet("TableOutput")

# PNG Options
pngFile = (os.path.join(configDirectory, 'Outputs/SMStandings.png'))
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
premIdx = str("B2:F{}".format(premCount))
masterIdx = str("B{}:F{}".format(premCount + 1, premCount + masterCount))
eliteIdx = str("B{}:F{}".format(premCount + masterCount + 1, premCount +
                                masterCount + eliteCount))
rivalIdx = str("B{}:F{}".format(premCount + masterCount + eliteCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount))
challIdx = str("B{}:F{}".format(premCount + masterCount + eliteCount + rivalCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount +
                                challCount))
prospIdx = str("B{}:F{}".format(premCount + masterCount + eliteCount + rivalCount + 
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
if configTier == 'Premier':
    tierData = premData
    tierClass = fc.teamsPrem
    teamsConf = (premCount - offset)//2
if configTier == 'Master':
    tierData = masterData
    tierClass = fc.teamsMaster
    teamsConf = masterCount//2
if configTier == 'Elite':
    tierData = eliteData
    tierClass = fc.teamsElite
    teamsConf = eliteCount//2
if configTier == 'Rival':
    tierData = rivalData
    tierClass = fc.teamsRival
    teamsConf = rivalCount//2
if configTier == 'Challenger':
    tierData = challData
    tierClass = fc.teamsChall//2
    teamsConf = challCount//2
if configTier == 'Prospect':
    tierData = prospData
    tierClass = fc.teamsProsp
    teamsConf = prospCount//2


for row in tierData:
    if configConf == "Glacies":
        if row[0] == "Glacies":
            standings.teamOrder.append(str(row[2]).upper())
            standings.winsOrder.append(str(row[4]).upper())
    if configConf == "Ignis":
        if row[0] == "Ignis":
            standings.teamOrder.append(str(row[2]).upper())
            standings.winsOrder.append(str(row[4]).upper())

for team in standings.teamOrder:
    standings.abbrOrder.append(tierClass[team])

            




def editTable(teamsConf):
    psApp = win32com.client.Dispatch("Photoshop.Application")
    psApp.Open(os.path.join(configDirectory, 'SMStandings.psd'))
    doc = psApp.Application.ActiveDocument 
    titlegroup = doc.activeLayer = (doc.layerSets["Title Banner"])
    weekNum = titlegroup.ArtLayers["WeekNum"]
    weeknumText = weekNum.textItem
    weeknumText.contents = "WEEK {} | {}".format(str(configWeek), str(configConf).upper())
    bannerGroup = titlegroup.layerSets[configTier]
    bannerGroup.visible = True

    loopCount = 0
    while loopCount < teamsConf:
        # Edit Team Names
        teamGroup =  doc.activeLayer = (doc.layerSets["Team {}".format(loopCount+1)])
        teamName = teamGroup.ArtLayers["TeamName"]
        teamNameText = teamName.textItem
        teamNameText.contents = standings.teamOrder[loopCount]
        # Edit Team Wins
        teamWins = teamGroup.ArtLayers["Wins"]
        teamWinsText = teamWins.textItem
        teamWinsText.contents = standings.winsOrder[loopCount]
        # Edit Team Logos
        teamLogoGroup = teamGroup.LayerSets["Logo"]
        teamLogo = teamLogoGroup.ArtLayers[standings.abbrOrder[loopCount]]
        teamLogo.visible = True
        loopCount += 1

    if configTier == 'Premier':
        extraTeamGroup =  doc.activeLayer = (doc.layerSets["Team 9"])
        extraTeamGroup.visible = False
        extraTeamGroup2 =  doc.activeLayer = (doc.layerSets["Team 10"])
        extraTeamGroup2.visible = False
    doc.Export(ExportIn=pngFile, ExportAs=2, Options=options)
    doc.Close(2)
    
    


    

editTable(teamsConf)