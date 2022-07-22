import gspread
import configparser
import fixturesClass as fc
#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"SMStandingsConfig.txt"))
configTier = config.get('config', 'Tier')
configConf = config.get('config', 'Conference')

###############
# Class Setup #
###############
class standings:
    teamOrder = []
    winsOrder = []
    abbrOrder = []


#########
# Setup #
#########
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
wks = sh.worksheet("TableOutput")


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
premIdx = str("C2:F{}".format(premCount))
masterIdx = str("C{}:F{}".format(premCount + 1, premCount + masterCount))
eliteIdx = str("C{}:F{}".format(premCount + masterCount + 1, premCount +
                                masterCount + eliteCount))
rivalIdx = str("C{}:F{}".format(premCount + masterCount + eliteCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount))
challIdx = str("C{}:F{}".format(premCount + masterCount + eliteCount + rivalCount + 1,
                                premCount + masterCount + eliteCount +  rivalCount +
                                challCount))
prospIdx = str("C{}:F{}".format(premCount + masterCount + eliteCount + rivalCount + 
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
if configTier == 'Master':
    tierData = masterData
    tierClass = fc.teamsMaster
if configTier == 'Elite':
    tierData = eliteData
    tierClass = fc.teamsElite
if configTier == 'Rival':
    tierData = rivalData
    tierClass = fc.teamsRival
if configTier == 'Challenger':
    tierData = challData
    tierClass = fc.teamsChall
if configTier == 'Prospect':
    tierData = prospData
    tierClass = fc.teamsProsp


for row in tierData:
    standings.teamOrder.append(str(row[1]).upper())
    standings.winsOrder.append(str(row[3]).upper())
for team in standings.teamOrder:
    standings.abbrOrder.append(tierClass[team])

print(standings.abbrOrder)
