import csv
import ignisClasses
import glaciesClasses
import standingsClass as sc

with open('psd_test.csv', newline='') as csvfile:
    standings = csv.reader(csvfile)
    
    
    for row in standings:
        for i in row:
            new = [i.upper() for i in row]
        print(new)
        sc.standings.franchOrder.append(new[2])
        sc.standings.teamOrder.append(new[3])
        sc.standings.gpOrder.append(new[4])
        sc.standings.gwOrder.append(new[5])
        sc.standings.glOrder.append(new[6])
        sc.standings.gsOrder.append(new[7])
        sc.standings.gcOrder.append(new[8])
        sc.standings.gdOrder.append(new[9])
        sc.standings.winPercOrder.append(new[10])
        sc.standings.ffWinOrder.append(new[11])
        sc.standings.ffLossOrder.append(new[12])
        sc.standings.recordOrder.append(new[13])



###################
# IGNIS Standings #
###################

# First place class
ignisClasses.ignisFirst.franchise = sc.standings.franchOrder[0]
ignisClasses.ignisFirst.team = sc.standings.teamOrder[0]
ignisClasses.ignisFirst.gp = sc.standings.gpOrder[0]
ignisClasses.ignisFirst.gw = sc.standings.gwOrder[0]
ignisClasses.ignisFirst.gl = sc.standings.glOrder[0]
ignisClasses.ignisFirst.gs = sc.standings.gsOrder[0]
ignisClasses.ignisFirst.gc = sc.standings.gcOrder[0]
ignisClasses.ignisFirst.gd = sc.standings.gdOrder[0]
ignisClasses.ignisFirst.winPerc = sc.standings.winPercOrder[0]
ignisClasses.ignisFirst.ffWin = sc.standings.ffWinOrder[0]
ignisClasses.ignisFirst.ffLoss = sc.standings.ffLossOrder[0]
ignisClasses.ignisFirst.record = sc.standings.recordOrder[0]

# Second place class
ignisClasses.ignisSecond.franchise = sc.standings.franchOrder[1]
ignisClasses.ignisSecond.team = sc.standings.teamOrder[1]
ignisClasses.ignisSecond.gp = sc.standings.gpOrder[1]
ignisClasses.ignisSecond.gw = sc.standings.gwOrder[1]
ignisClasses.ignisSecond.gl = sc.standings.glOrder[1]
ignisClasses.ignisSecond.gs = sc.standings.gsOrder[1]
ignisClasses.ignisSecond.gc = sc.standings.gcOrder[1]
ignisClasses.ignisSecond.gd = sc.standings.gdOrder[1]
ignisClasses.ignisSecond.winPerc = sc.standings.winPercOrder[1]
ignisClasses.ignisSecond.ffWin = sc.standings.ffWinOrder[1]
ignisClasses.ignisSecond.ffLoss = sc.standings.ffLossOrder[1]
ignisClasses.ignisSecond.record = sc.standings.recordOrder[1]

# Third place class
ignisClasses.ignisThird.franchise = sc.standings.franchOrder[2]
ignisClasses.ignisThird.team = sc.standings.teamOrder[2]
ignisClasses.ignisThird.gp = sc.standings.gpOrder[2]
ignisClasses.ignisThird.gw = sc.standings.gwOrder[2]
ignisClasses.ignisThird.gl = sc.standings.glOrder[2]
ignisClasses.ignisThird.gs = sc.standings.gsOrder[2]
ignisClasses.ignisThird.gc = sc.standings.gcOrder[2]
ignisClasses.ignisThird.gd = sc.standings.gdOrder[2]
ignisClasses.ignisThird.winPerc = sc.standings.winPercOrder[2]
ignisClasses.ignisThird.ffWin = sc.standings.ffWinOrder[2]
ignisClasses.ignisThird.ffLoss = sc.standings.ffLossOrder[2]
ignisClasses.ignisThird.record = sc.standings.recordOrder[2]

# Fourth place class
ignisClasses.ignisFourth.franchise = sc.standings.franchOrder[3]
ignisClasses.ignisFourth.team = sc.standings.teamOrder[3]
ignisClasses.ignisFourth.gp = sc.standings.gpOrder[3]
ignisClasses.ignisFourth.gw = sc.standings.gwOrder[3]
ignisClasses.ignisFourth.gl = sc.standings.glOrder[3]
ignisClasses.ignisFourth.gs = sc.standings.gsOrder[3]
ignisClasses.ignisFourth.gc = sc.standings.gcOrder[3]
ignisClasses.ignisFourth.gd = sc.standings.gdOrder[3]
ignisClasses.ignisFourth.winPerc = sc.standings.winPercOrder[3]
ignisClasses.ignisFourth.ffWin = sc.standings.ffWinOrder[3]
ignisClasses.ignisFourth.ffLoss = sc.standings.ffLossOrder[3]
ignisClasses.ignisFourth.record = sc.standings.recordOrder[3]

# Fifth place class
ignisClasses.ignisFifth.franchise = sc.standings.franchOrder[4]
ignisClasses.ignisFifth.team = sc.standings.teamOrder[4]
ignisClasses.ignisFifth.gp = sc.standings.gpOrder[4]
ignisClasses.ignisFifth.gw = sc.standings.gwOrder[4]
ignisClasses.ignisFifth.gl = sc.standings.glOrder[4]
ignisClasses.ignisFifth.gs = sc.standings.gsOrder[4]
ignisClasses.ignisFifth.gc = sc.standings.gcOrder[4]
ignisClasses.ignisFifth.gd = sc.standings.gdOrder[4]
ignisClasses.ignisFifth.winPerc = sc.standings.winPercOrder[4]
ignisClasses.ignisFifth.ffWin = sc.standings.ffWinOrder[4]
ignisClasses.ignisFifth.ffLoss = sc.standings.ffLossOrder[4]
ignisClasses.ignisFifth.record = sc.standings.recordOrder[4]

# Sixth place class
ignisClasses.ignisSixth.franchise = sc.standings.franchOrder[5]
ignisClasses.ignisSixth.team = sc.standings.teamOrder[5]
ignisClasses.ignisSixth.gp = sc.standings.gpOrder[5]
ignisClasses.ignisSixth.gw = sc.standings.gwOrder[5]
ignisClasses.ignisSixth.gl = sc.standings.glOrder[5]
ignisClasses.ignisSixth.gs = sc.standings.gsOrder[5]
ignisClasses.ignisSixth.gc = sc.standings.gcOrder[5]
ignisClasses.ignisSixth.gd = sc.standings.gdOrder[5]
ignisClasses.ignisSixth.winPerc = sc.standings.winPercOrder[5]
ignisClasses.ignisSixth.ffWin = sc.standings.ffWinOrder[5]
ignisClasses.ignisSixth.ffLoss = sc.standings.ffLossOrder[5]
ignisClasses.ignisSixth.record = sc.standings.recordOrder[5]

# Seventh place class
ignisClasses.ignisSeventh.franchise = sc.standings.franchOrder[6]
ignisClasses.ignisSeventh.team = sc.standings.teamOrder[6]
ignisClasses.ignisSeventh.gp = sc.standings.gpOrder[6]
ignisClasses.ignisSeventh.gw = sc.standings.gwOrder[6]
ignisClasses.ignisSeventh.gl = sc.standings.glOrder[6]
ignisClasses.ignisSeventh.gs = sc.standings.gsOrder[6]
ignisClasses.ignisSeventh.gc = sc.standings.gcOrder[6]
ignisClasses.ignisSeventh.gd = sc.standings.gdOrder[6]
ignisClasses.ignisSeventh.winPerc = sc.standings.winPercOrder[6]
ignisClasses.ignisSeventh.ffWin = sc.standings.ffWinOrder[6]
ignisClasses.ignisSeventh.ffLoss = sc.standings.ffLossOrder[6]
ignisClasses.ignisSeventh.record = sc.standings.recordOrder[6]

# Eighth place class
ignisClasses.ignisEighth.franchise = sc.standings.franchOrder[7]
ignisClasses.ignisEighth.team = sc.standings.teamOrder[7]
ignisClasses.ignisEighth.gp = sc.standings.gpOrder[7]
ignisClasses.ignisEighth.gw = sc.standings.gwOrder[7]
ignisClasses.ignisEighth.gl = sc.standings.glOrder[7]
ignisClasses.ignisEighth.gs = sc.standings.gsOrder[7]
ignisClasses.ignisEighth.gc = sc.standings.gcOrder[7]
ignisClasses.ignisEighth.gd = sc.standings.gdOrder[7]
ignisClasses.ignisEighth.winPerc = sc.standings.winPercOrder[7]
ignisClasses.ignisEighth.ffWin = sc.standings.ffWinOrder[7]
ignisClasses.ignisEighth.ffLoss = sc.standings.ffLossOrder[7]
ignisClasses.ignisEighth.record = sc.standings.recordOrder[7]

# Ninth place class
ignisClasses.ignisNinth.franchise = sc.standings.franchOrder[8]
ignisClasses.ignisNinth.team = sc.standings.teamOrder[8]
ignisClasses.ignisNinth.gp = sc.standings.gpOrder[8]
ignisClasses.ignisNinth.gw = sc.standings.gwOrder[8]
ignisClasses.ignisNinth.gl = sc.standings.glOrder[8]
ignisClasses.ignisNinth.gs = sc.standings.gsOrder[8]
ignisClasses.ignisNinth.gc = sc.standings.gcOrder[8]
ignisClasses.ignisNinth.gd = sc.standings.gdOrder[8]
ignisClasses.ignisNinth.winPerc = sc.standings.winPercOrder[8]
ignisClasses.ignisNinth.ffWin = sc.standings.ffWinOrder[8]
ignisClasses.ignisNinth.ffLoss = sc.standings.ffLossOrder[8]
ignisClasses.ignisNinth.record = sc.standings.recordOrder[8]

# Tenth place class
ignisClasses.ignisTenth.franchise = sc.standings.franchOrder[9]
ignisClasses.ignisTenth.team = sc.standings.teamOrder[9]
ignisClasses.ignisTenth.gp = sc.standings.gpOrder[9]
ignisClasses.ignisTenth.gw = sc.standings.gwOrder[9]
ignisClasses.ignisTenth.gl = sc.standings.glOrder[9]
ignisClasses.ignisTenth.gs = sc.standings.gsOrder[9]
ignisClasses.ignisTenth.gc = sc.standings.gcOrder[9]
ignisClasses.ignisTenth.gd = sc.standings.gdOrder[9]
ignisClasses.ignisTenth.winPerc = sc.standings.winPercOrder[9]
ignisClasses.ignisTenth.ffWin = sc.standings.ffWinOrder[9]
ignisClasses.ignisTenth.ffLoss = sc.standings.ffLossOrder[9]
ignisClasses.ignisTenth.record = sc.standings.recordOrder[9]

###################
# IGNIS Standings #
###################

# First place class
glaciesClasses.glaciesFirst.franchise = sc.standings.franchOrder[10]
glaciesClasses.glaciesFirst.team = sc.standings.teamOrder[10]
glaciesClasses.glaciesFirst.gp = sc.standings.gpOrder[10]
glaciesClasses.glaciesFirst.gw = sc.standings.gwOrder[10]
glaciesClasses.glaciesFirst.gl = sc.standings.glOrder[10]
glaciesClasses.glaciesFirst.gs = sc.standings.gsOrder[10]
glaciesClasses.glaciesFirst.gc = sc.standings.gcOrder[10]
glaciesClasses.glaciesFirst.gd = sc.standings.gdOrder[10]
glaciesClasses.glaciesFirst.winPerc = sc.standings.winPercOrder[10]
glaciesClasses.glaciesFirst.ffWin = sc.standings.ffWinOrder[10]
glaciesClasses.glaciesFirst.ffLoss = sc.standings.ffLossOrder[10]
glaciesClasses.glaciesFirst.record = sc.standings.recordOrder[10]

# Second place class
glaciesClasses.glaciesSecond.franchise = sc.standings.franchOrder[11]
glaciesClasses.glaciesSecond.team = sc.standings.teamOrder[11]
glaciesClasses.glaciesSecond.gp = sc.standings.gpOrder[11]
glaciesClasses.glaciesSecond.gw = sc.standings.gwOrder[11]
glaciesClasses.glaciesSecond.gl = sc.standings.glOrder[11]
glaciesClasses.glaciesSecond.gs = sc.standings.gsOrder[11]
glaciesClasses.glaciesSecond.gc = sc.standings.gcOrder[11]
glaciesClasses.glaciesSecond.gd = sc.standings.gdOrder[11]
glaciesClasses.glaciesSecond.winPerc = sc.standings.winPercOrder[11]
glaciesClasses.glaciesSecond.ffWin = sc.standings.ffWinOrder[11]
glaciesClasses.glaciesSecond.ffLoss = sc.standings.ffLossOrder[11]
glaciesClasses.glaciesSecond.record = sc.standings.recordOrder[11]

# Third place class
glaciesClasses.glaciesThird.franchise = sc.standings.franchOrder[12]
glaciesClasses.glaciesThird.team = sc.standings.teamOrder[12]
glaciesClasses.glaciesThird.gp = sc.standings.gpOrder[12]
glaciesClasses.glaciesThird.gw = sc.standings.gwOrder[12]
glaciesClasses.glaciesThird.gl = sc.standings.glOrder[12]
glaciesClasses.glaciesThird.gs = sc.standings.gsOrder[12]
glaciesClasses.glaciesThird.gc = sc.standings.gcOrder[12]
glaciesClasses.glaciesThird.gd = sc.standings.gdOrder[12]
glaciesClasses.glaciesThird.winPerc = sc.standings.winPercOrder[12]
glaciesClasses.glaciesThird.ffWin = sc.standings.ffWinOrder[12]
glaciesClasses.glaciesThird.ffLoss = sc.standings.ffLossOrder[12]
glaciesClasses.glaciesThird.record = sc.standings.recordOrder[12]

# Fourth place class
glaciesClasses.glaciesFourth.franchise = sc.standings.franchOrder[13]
glaciesClasses.glaciesFourth.team = sc.standings.teamOrder[13]
glaciesClasses.glaciesFourth.gp = sc.standings.gpOrder[13]
glaciesClasses.glaciesFourth.gw = sc.standings.gwOrder[13]
glaciesClasses.glaciesFourth.gl = sc.standings.glOrder[13]
glaciesClasses.glaciesFourth.gs = sc.standings.gsOrder[13]
glaciesClasses.glaciesFourth.gc = sc.standings.gcOrder[13]
glaciesClasses.glaciesFourth.gd = sc.standings.gdOrder[13]
glaciesClasses.glaciesFourth.winPerc = sc.standings.winPercOrder[13]
glaciesClasses.glaciesFourth.ffWin = sc.standings.ffWinOrder[13]
glaciesClasses.glaciesFourth.ffLoss = sc.standings.ffLossOrder[13]
glaciesClasses.glaciesFourth.record = sc.standings.recordOrder[13]

# Fifth place class
glaciesClasses.glaciesFifth.franchise = sc.standings.franchOrder[14]
glaciesClasses.glaciesFifth.team = sc.standings.teamOrder[14]
glaciesClasses.glaciesFifth.gp = sc.standings.gpOrder[14]
glaciesClasses.glaciesFifth.gw = sc.standings.gwOrder[14]
glaciesClasses.glaciesFifth.gl = sc.standings.glOrder[14]
glaciesClasses.glaciesFifth.gs = sc.standings.gsOrder[14]
glaciesClasses.glaciesFifth.gc = sc.standings.gcOrder[14]
glaciesClasses.glaciesFifth.gd = sc.standings.gdOrder[14]
glaciesClasses.glaciesFifth.winPerc = sc.standings.winPercOrder[14]
glaciesClasses.glaciesFifth.ffWin = sc.standings.ffWinOrder[14]
glaciesClasses.glaciesFifth.ffLoss = sc.standings.ffLossOrder[14]
glaciesClasses.glaciesFifth.record = sc.standings.recordOrder[14]

# Sixth place class
glaciesClasses.glaciesSixth.franchise = sc.standings.franchOrder[15]
glaciesClasses.glaciesSixth.team = sc.standings.teamOrder[15]
glaciesClasses.glaciesSixth.gp = sc.standings.gpOrder[15]
glaciesClasses.glaciesSixth.gw = sc.standings.gwOrder[15]
glaciesClasses.glaciesSixth.gl = sc.standings.glOrder[15]
glaciesClasses.glaciesSixth.gs = sc.standings.gsOrder[15]
glaciesClasses.glaciesSixth.gc = sc.standings.gcOrder[15]
glaciesClasses.glaciesSixth.gd = sc.standings.gdOrder[15]
glaciesClasses.glaciesSixth.winPerc = sc.standings.winPercOrder[15]
glaciesClasses.glaciesSixth.ffWin = sc.standings.ffWinOrder[15]
glaciesClasses.glaciesSixth.ffLoss = sc.standings.ffLossOrder[15]
glaciesClasses.glaciesSixth.record = sc.standings.recordOrder[15]

# Seventh place class
glaciesClasses.glaciesSeventh.franchise = sc.standings.franchOrder[16]
glaciesClasses.glaciesSeventh.team = sc.standings.teamOrder[16]
glaciesClasses.glaciesSeventh.gp = sc.standings.gpOrder[16]
glaciesClasses.glaciesSeventh.gw = sc.standings.gwOrder[16]
glaciesClasses.glaciesSeventh.gl = sc.standings.glOrder[16]
glaciesClasses.glaciesSeventh.gs = sc.standings.gsOrder[16]
glaciesClasses.glaciesSeventh.gc = sc.standings.gcOrder[16]
glaciesClasses.glaciesSeventh.gd = sc.standings.gdOrder[16]
glaciesClasses.glaciesSeventh.winPerc = sc.standings.winPercOrder[16]
glaciesClasses.glaciesSeventh.ffWin = sc.standings.ffWinOrder[16]
glaciesClasses.glaciesSeventh.ffLoss = sc.standings.ffLossOrder[16]
glaciesClasses.glaciesSeventh.record = sc.standings.recordOrder[16]

# Eighth place class
glaciesClasses.glaciesEighth.franchise = sc.standings.franchOrder[17]
glaciesClasses.glaciesEighth.team = sc.standings.teamOrder[17]
glaciesClasses.glaciesEighth.gp = sc.standings.gpOrder[17]
glaciesClasses.glaciesEighth.gw = sc.standings.gwOrder[17]
glaciesClasses.glaciesEighth.gl = sc.standings.glOrder[17]
glaciesClasses.glaciesEighth.gs = sc.standings.gsOrder[17]
glaciesClasses.glaciesEighth.gc = sc.standings.gcOrder[17]
glaciesClasses.glaciesEighth.gd = sc.standings.gdOrder[17]
glaciesClasses.glaciesEighth.winPerc = sc.standings.winPercOrder[17]
glaciesClasses.glaciesEighth.ffWin = sc.standings.ffWinOrder[17]
glaciesClasses.glaciesEighth.ffLoss = sc.standings.ffLossOrder[17]
glaciesClasses.glaciesEighth.record = sc.standings.recordOrder[17]

# Ninth place class
glaciesClasses.glaciesNinth.franchise = sc.standings.franchOrder[18]
glaciesClasses.glaciesNinth.team = sc.standings.teamOrder[18]
glaciesClasses.glaciesNinth.gp = sc.standings.gpOrder[18]
glaciesClasses.glaciesNinth.gw = sc.standings.gwOrder[18]
glaciesClasses.glaciesNinth.gl = sc.standings.glOrder[18]
glaciesClasses.glaciesNinth.gs = sc.standings.gsOrder[18]
glaciesClasses.glaciesNinth.gc = sc.standings.gcOrder[18]
glaciesClasses.glaciesNinth.gd = sc.standings.gdOrder[18]
glaciesClasses.glaciesNinth.winPerc = sc.standings.winPercOrder[18]
glaciesClasses.glaciesNinth.ffWin = sc.standings.ffWinOrder[18]
glaciesClasses.glaciesNinth.ffLoss = sc.standings.ffLossOrder[18]
glaciesClasses.glaciesNinth.record = sc.standings.recordOrder[18]

# Tenth place class
glaciesClasses.glaciesTenth.franchise = sc.standings.franchOrder[19]
glaciesClasses.glaciesTenth.team = sc.standings.teamOrder[19]
glaciesClasses.glaciesTenth.gp = sc.standings.gpOrder[19]
glaciesClasses.glaciesTenth.gw = sc.standings.gwOrder[19]
glaciesClasses.glaciesTenth.gl = sc.standings.glOrder[19]
glaciesClasses.glaciesTenth.gs = sc.standings.gsOrder[19]
glaciesClasses.glaciesTenth.gc = sc.standings.gcOrder[19]
glaciesClasses.glaciesTenth.gd = sc.standings.gdOrder[19]
glaciesClasses.glaciesTenth.winPerc = sc.standings.winPercOrder[19]
glaciesClasses.glaciesTenth.ffWin = sc.standings.ffWinOrder[19]
glaciesClasses.glaciesTenth.ffLoss = sc.standings.ffLossOrder[19]
glaciesClasses.glaciesTenth.record = sc.standings.recordOrder[19]