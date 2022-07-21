import gspread
import configparser
import fixturesClass as fc

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

#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"config.txt"))
configWeek = config.get('config', 'Week')


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
    fc.prem.dateOrder.append(str(row[5][0:5])) # Date
    fc.prem.timeOrder.append(str(row[6])) # Time

for row in masterFixtures:
    fc.master.teamOrder.append(str(row[0]).upper())
    fc.master.teamOrder.append(str(row[4]).upper())
    fc.master.dateOrder.append(str(row[5][0:5]))
    fc.master.timeOrder.append(str(row[6]))

for row in eliteFixtures:
    fc.elite.teamOrder.append(str(row[0]).upper())
    fc.elite.teamOrder.append(str(row[4]).upper())
    fc.elite.dateOrder.append(str(row[5][0:5]))
    fc.elite.timeOrder.append(str(row[6]))

for row in rivalFixtures:
    fc.rival.teamOrder.append(str(row[0]).upper())
    fc.rival.teamOrder.append(str(row[4]).upper())
    fc.rival.dateOrder.append(str(row[5][0:5]))
    fc.rival.timeOrder.append(str(row[6]))

for row in challFixtures:
    fc.chall.teamOrder.append(str(row[0]).upper())
    fc.chall.teamOrder.append(str(row[4]).upper())
    fc.chall.dateOrder.append(str(row[5][0:5]))
    fc.chall.timeOrder.append(str(row[6]))

for row in prospFixtures:
    fc.prosp.teamOrder.append(str(row[0]).upper())
    fc.prosp.teamOrder.append(str(row[4]).upper())
    fc.prosp.dateOrder.append(str(row[5][0:5]))
    fc.prosp.timeOrder.append(str(row[6]))


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


## Take lineups from GSheet
    ## Check for Week number. Start row = offset + ((weeknum-1) * Teams in tier)




## Teams to dictionary
## Split for Week number
## Set ranges on WeekNum
## Split lists for conferences
## Edit PSD text for teams and schedule
## Unhide logos