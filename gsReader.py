import gspread
import standingsClass as sc


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