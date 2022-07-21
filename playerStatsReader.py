import gspread
import win32com.client
import configparser



#########
# Setup #
#########
psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\jaymu\Desktop\RSC\psd_editor\fixGraphics\RSC10_PlayerStats.psd")
doc = psApp.Application.ActiveDocument 

options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit


sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
teamStats = sh.worksheet("Team Select")




team1Data = teamStats.get("A4:I7")
if len(team1Data[3]) == 1:
    team1Data = teamStats.get("A4:I6")
    team1Flag = True

team2Data = teamStats.get("A8:I11")
if len(team2Data[3]) == 1:
    team1Data = teamStats.get("A8:I10")
    team2Flag = True

print(team1Data)
team1Names = []
team1Players = []
team1Played = []
team1Goals = []
team1Assists = []
team1Saves = []
team1ShotPerc = []
team1WinPerc = []
team1GoalPart = []

team2Names = []
team2Players = []
team2Played = []
team2Goals = []
team2Assists = []
team2Saves = []
team2ShotPerc = []
team2WinPerc = []
team2GoalPart = []



for row in team1Data:
    team1Names.append(row[0])
    team1Players.append(row[1])
    team1Played.append(row[2])
    team1Goals.append(row[3])
    team1Assists.append(row[4])
    team1Saves.append(row[5])
    team1ShotPerc.append(row[6])
    team1WinPerc.append(row[7])
    team1GoalPart.append(row[8])
print(team1Names[0])

for row in team2Data:
    team2Names.append(row[0])
    team2Players.append(row[1])
    team2Played.append(row[2])
    team2Goals.append(row[3])
    team2Assists.append(row[4])
    team2Saves.append(row[5])
    team2ShotPerc.append(row[6])
    team2WinPerc.append(row[7])
    team2GoalPart.append(row[8])

                                                                    #####################
                                                                    # Left Team / Team1 #
                                                                    #####################


upperGroup = doc.activeLayer = (doc.layerSets["4 Players"])
leftGroup = upperGroup.layerSets["TS_Blue"]
player1 = leftGroup.layerSets["Player 1"]
player2 = leftGroup.layerSets["Player 2"]
player3 = leftGroup.layerSets["Player 3"]
player4 = leftGroup.layerSets["Player 4"]
################
# Player Names #
################

# Player 1
player1Name = player1.artLayers["Name"] 
player1NameText = player1Name.textItem
player1NameText.contents = team1Players[0]
# Player 2
player2Name = player2.artLayers["Name"]
player2NameText = player2Name.textItem
player2NameText.contents = team1Players[1]
# Player 3
player3Name = player3.artLayers["Name"]
player3NameText = player3Name.textItem
player3NameText.contents = team1Players[2]
# Player 4
player4Name = player4.artLayers["Name"]
if team1Flag != True:
    player4NameText = player4Name.textItem
    player4NameText.contents = team1Players[3]
else:
    player4Name.visible = False
################
# Games Played #
################
# Player 1
player1Games = player1.ArtLayers["Games"]
player1GamesText = player1Games.textItem
player1GamesText.contents = team1Played[0]
# Player 2
player2Games = player2.ArtLayers["Games"]
player2GamesText = player2Games.textItem
player2GamesText.contents = team1Played[1]
# Player 3
player3Games = player3.ArtLayers["Games"]
player3GamesText = player3Games.textItem
player3GamesText.contents = team1Played[2]
# Player 4
player4Games = player4.ArtLayers["Games"]
if team1Flag != True:
    player4GamesText = player4Games.textItem
    player4GamesText.contents = team1Played[3]
else:
    player4Games.visible = False

################
# Goals Scored #
################
# Player 1
player1Goals = player1.ArtLayers["Goals"]
player1GoalsText = player1Goals.textItem
player1GoalsText.contents = team1Goals[0]
# Player 2
player2Goals = player2.ArtLayers["Goals"]
player2GoalsText = player2Goals.textItem
player2GoalsText.contents = team1Goals[1]
# Player 3
player3Games = player3.ArtLayers["Goals"]
player3GamesText = player3Games.textItem
player3GamesText.contents = team1Goals[2]
# Player 4
player4Goals = player4.ArtLayers["Goals"]
if team1Flag != True:
    player4GoalsText = player4Goals.textItem
    player4GoalsText.contents = team1Goals[3]
else:
    player4Goals.visible = False

############
# Assists #
############
# Player 1
player1Assists = player1.ArtLayers["Assists"]
player1AssistsText = player1Assists.textItem
player1AssistsText.contents = team1Assists[0]
# Player 2
player2Assists = player2.ArtLayers["Assists"]
player2AssistsText = player2Assists.textItem
player2AssistsText.contents = team1Assists[1]
# Player 3
player3Assists = player3.ArtLayers["Assists"]
player3AssistsText = player3Assists.textItem
player3AssistsText.contents = team1Assists[2]
# Player 4
player4Assists = player4.ArtLayers["Assists"]
if team1Flag != True:
    player4AssistsText = player4Assists.textItem
    player4AssistsText.contents = team1Assists[3]
else:
    player4Assists.visible = False



#########
# Saves #
#########
# Player 1
player1Saves = player1.ArtLayers["Saves"]
player1SavesText = player1Saves.textItem
player1SavesText.contents = team1Saves[0]
# Player 2
player2Saves = player2.ArtLayers["Saves"]
player2SavesText = player2Saves.textItem
player2SavesText.contents = team1Saves[1]
# Player 3
player3Saves = player3.ArtLayers["Saves"]
player3SavesText = player3Saves.textItem
player3SavesText.contents = team1Saves[2]
# Player 4
player4Saves = player4.ArtLayers["Saves"]
if team1Flag != True:
    player4SavesText = player4Saves.textItem
    player4SavesText.contents = team1Saves[3]
else:
    player4Saves.visible = False

#############
# Shot Perc #
#############
# Player 1
player1ShotPerc = player1.ArtLayers["ShotPerc"]
player1ShotPercText = player1ShotPerc.textItem
player1ShotPercText.contents = team1ShotPerc[0]
# Player 2
player2ShotPerc = player2.ArtLayers["ShotPerc"]
player2ShotPercText = player2ShotPerc.textItem
player2ShotPercText.contents = team1ShotPerc[1]
# Player 3
player3ShotPerc = player3.ArtLayers["ShotPerc"]
player3ShotPercText = player3ShotPerc.textItem
player3ShotPercText.contents = team1ShotPerc[2]
# Player 4
player4ShotPerc = player4.ArtLayers["ShotPerc"]
if team1Flag != True:
    player4ShotPercText = player4ShotPerc.textItem
    player4ShotPercText.contents = team1ShotPerc[3]
else: 
    player4ShotPerc.visible = False

#############
# Win Perc #
#############
# Player 1
player1WinPerc = player1.ArtLayers["WinPerc"]
player1WinPercText = player1WinPerc.textItem
player1WinPercText.contents = team1WinPerc[0]
# Player 2
player2WinPerc = player2.ArtLayers["WinPerc"]
player2WinPercText = player2WinPerc.textItem
player2WinPercText.contents = team1WinPerc[1]
# Player 3
player3WinPerc = player3.ArtLayers["WinPerc"]
player3WinPercText = player3WinPerc.textItem
player3WinPercText.contents = team1WinPerc[2]
# Player 4
player4WinPerc = player4.ArtLayers["WinPerc"]
if team1Flag != True:
    player4WinPercText = player4WinPerc.textItem
    player4WinPercText.contents = team1WinPerc[3]
else:
    player4WinPerc.visible = False


#############
# Goal Part #
#############
# Player 1
player1GoalPart = player1.ArtLayers["GoalPart"]
player1GoalPartText = player1WinPerc.textItem
player1GoalPartText.contents = team1WinPerc[0]
# Player 2
player2GoalPart = player2.ArtLayers["GoalPart"]
player2GoalPartText = player2WinPerc.textItem
player2GoalPartText.contents = team1WinPerc[1]
# Player 3
player3GoalPart = player3.ArtLayers["GoalPart"]
player3GoalPartText = player3GoalPart.textItem
player3GoalPartText.contents = team1GoalPart[2]
# Player 4
player4GoalPart = player4.ArtLayers["GoalPart"]
if team1Flag != True:
    player4GoalPartText = player4GoalPart.textItem
    player4GoalPartText.contents = team1GoalPart[3]
else:
    player4GoalPart.visible = False



                                                                    ######################
                                                                    # Right Team / Team2 #
                                                                    ######################

rightGroup = upperGroup.layerSets["TS_Red"]
player1 = rightGroup.layerSets["Player 1"]
player2 = rightGroup.layerSets["Player 2"]
player3 = rightGroup.layerSets["Player 3"]
player4 = rightGroup.layerSets["Player 4"]
################
# Player Names #
################

# Player 1
player1Name = player1.artLayers["Name"] 
player1NameText = player1Name.textItem
player1NameText.contents = team2Players[0]
# Player 2
player2Name = player2.artLayers["Name"]
player2NameText = player2Name.textItem
player2NameText.contents = team2Players[1]
# Player 3
player3Name = player3.artLayers["Name"]
player3NameText = player3Name.textItem
player3NameText.contents = team2Players[2]
# Player 4
player4Name = player4.artLayers["Name"]
if team1Flag != True:
    player4NameText = player4Name.textItem
    player4NameText.contents = team2Players[3]
else:
    player4Name.visible = False
################
# Games Played #
################
# Player 1
player1Games = player1.ArtLayers["Games"]
player1GamesText = player1Games.textItem
player1GamesText.contents = team2Played[0]
# Player 2
player2Games = player2.ArtLayers["Games"]
player2GamesText = player2Games.textItem
player2GamesText.contents = team2Played[1]
# Player 3
player3Games = player3.ArtLayers["Games"]
player3GamesText = player3Games.textItem
player3GamesText.contents = team2Played[2]
# Player 4
player4Games = player4.ArtLayers["Games"]
if team1Flag != True:
    player4GamesText = player4Games.textItem
    player4GamesText.contents = team2Played[3]
else:
    player4Games.visible = False

################
# Goals Scored #
################
# Player 1
player1Goals = player1.ArtLayers["Goals"]
player1GoalsText = player1Goals.textItem
player1GoalsText.contents = team2Goals[0]
# Player 2
player2Goals = player2.ArtLayers["Goals"]
player2GoalsText = player2Goals.textItem
player2GoalsText.contents = team2Goals[1]
# Player 3
player3Games = player3.ArtLayers["Goals"]
player3GamesText = player3Games.textItem
player3GamesText.contents = team2Goals[2]
# Player 4
player4Goals = player4.ArtLayers["Goals"]
if team1Flag != True:
    player4GoalsText = player4Goals.textItem
    player4GoalsText.contents = team2Goals[3]
else:
    player4Goals.visible = False

############
# Assists #
############
# Player 1
player1Assists = player1.ArtLayers["Assists"]
player1AssistsText = player1Assists.textItem
player1AssistsText.contents = team2Assists[0]
# Player 2
player2Assists = player2.ArtLayers["Assists"]
player2AssistsText = player2Assists.textItem
player2AssistsText.contents = team2Assists[1]
# Player 3
player3Assists = player3.ArtLayers["Assists"]
player3AssistsText = player3Assists.textItem
player3AssistsText.contents = team2Assists[2]
# Player 4
player4Assists = player4.ArtLayers["Assists"]
if team1Flag != True:
    player4AssistsText = player4Assists.textItem
    player4AssistsText.contents = team2Assists[3]
else:
    player4Assists.visible = False



#########
# Saves #
#########
# Player 1
player1Saves = player1.ArtLayers["Saves"]
player1SavesText = player1Saves.textItem
player1SavesText.contents = team2Saves[0]
# Player 2
player2Saves = player2.ArtLayers["Saves"]
player2SavesText = player2Saves.textItem
player2SavesText.contents = team2Saves[1]
# Player 3
player3Saves = player3.ArtLayers["Saves"]
player3SavesText = player3Saves.textItem
player3SavesText.contents = team2Saves[2]
# Player 4
player4Saves = player4.ArtLayers["Saves"]
if team1Flag != True:
    player4SavesText = player4Saves.textItem
    player4SavesText.contents = team2Saves[3]
else:
    player4Saves.visible = False

#############
# Shot Perc #
#############
# Player 1
player1ShotPerc = player1.ArtLayers["ShotPerc"]
player1ShotPercText = player1ShotPerc.textItem
player1ShotPercText.contents = team2ShotPerc[0]
# Player 2
player2ShotPerc = player2.ArtLayers["ShotPerc"]
player2ShotPercText = player2ShotPerc.textItem
player2ShotPercText.contents = team2ShotPerc[1]
# Player 3
player3ShotPerc = player3.ArtLayers["ShotPerc"]
player3ShotPercText = player3ShotPerc.textItem
player3ShotPercText.contents = team2ShotPerc[2]
# Player 4
player4ShotPerc = player4.ArtLayers["ShotPerc"]
if team1Flag != True:
    player4ShotPercText = player4ShotPerc.textItem
    player4ShotPercText.contents = team2ShotPerc[3]
else: 
    player4ShotPerc.visible = False

#############
# Win Perc #
#############
# Player 1
player1WinPerc = player1.ArtLayers["WinPerc"]
player1WinPercText = player1WinPerc.textItem
player1WinPercText.contents = team2WinPerc[0]
# Player 2
player2WinPerc = player2.ArtLayers["WinPerc"]
player2WinPercText = player2WinPerc.textItem
player2WinPercText.contents = team2WinPerc[1]
# Player 3
player3WinPerc = player3.ArtLayers["WinPerc"]
player3WinPercText = player3WinPerc.textItem
player3WinPercText.contents = team2WinPerc[2]
# Player 4
player4WinPerc = player4.ArtLayers["WinPerc"]
if team1Flag != True:
    player4WinPercText = player4WinPerc.textItem
    player4WinPercText.contents = team2WinPerc[3]
else:
    player4WinPerc.visible = False


#############
# Goal Part #
#############
# Player 1
player1GoalPart = player1.ArtLayers["GoalPart"]
player1GoalPartText = player1WinPerc.textItem
player1GoalPartText.contents = team2WinPerc[0]
# Player 2
player2GoalPart = player2.ArtLayers["GoalPart"]
player2GoalPartText = player2WinPerc.textItem
player2GoalPartText.contents = team2WinPerc[1]
# Player 3
player3GoalPart = player3.ArtLayers["GoalPart"]
player3GoalPartText = player3GoalPart.textItem
player3GoalPartText.contents = team2GoalPart[2]
# Player 4
player4GoalPart = player4.ArtLayers["GoalPart"]
if team1Flag != True:
    player4GoalPartText = player4GoalPart.textItem
    player4GoalPartText.contents = team2GoalPart[3]
else:
    player4GoalPart.visible = False