from regex import F
import win32com.client
import glaciesClasses as gc
import ignisClasses as ic
import standingsClass as sc
import reader
import configparser
import time


startTime = time.time()
#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"config.txt"))
tier = config.get('config', 'Tier')
week = config.get('config', 'Week')

#########
# Setup #
#########
options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 6
options.Quality = 100

optionsTrans = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
optionsTrans.Format = 6
optionsTrans.Quality = 100
optionsTrans.transparency = False
optionsTrans.transparencyAmount = 100

jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\StandingsGlaciesBG.jpg")
jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\StandingsGlacies.jpg")
jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\StandingsIgnisBG.jpg")
jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\StandingsIgnis.jpg")
psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\jaymu\Desktop\RSC\psd_editor\RSC Standings.psd")
doc = psApp.Application.ActiveDocument

########################
# Header / Title Edits #
########################

## Edit Week Number ##
weekGroup = doc.activeLayer = (doc.layerSets["Title"])
weekLayer = weekGroup.ArtLayers["WeekNum"]
weekText = weekLayer.textItem
weekText.contents = 'WEEK ' + str(week)

## Edit Conference Banner ##
confGroup = doc.activeLayer = (doc.layerSets["Conference"])
glacisConfLayer = confGroup.ArtLayers["Banner_Glacies"]
ignisConfLayer = confGroup.ArtLayers["Banner_Ignis"]
glacisConfLayer.visible = False ## Hide both banners
ignisConfLayer.visible = False

confLayer = confGroup.ArtLayers["Banner_Glacies"]
confLayer.visible = True ## Unhide selected

## Edit Tier Banner ##
bannerGroup = doc.activeLayer = (doc.layerSets["Title"])
premierBannerGroup = (bannerGroup.layerSets["Premier"])
masterBannerGroup = (bannerGroup.layerSets["Master"])
eliteBannerGroup = (bannerGroup.layerSets["Elite"])
rivalBannerGroup = (bannerGroup.layerSets["Rival"])
challBannerGroup = (bannerGroup.layerSets["Challenger"])
prospBannerGroup = (bannerGroup.layerSets["Prospect"])

premierBannerGroup.visible = False ## Hide all banners
masterBannerGroup.visible = False
eliteBannerGroup.visible = False
rivalBannerGroup.visible = False
challBannerGroup.visible = False
prospBannerGroup.visible = False

tierBanner = (bannerGroup.layerSets[tier])
tierBanner.visible = True ## Unhide selected

                                    ###########
                                    # GLACIES #
                                    ###########

####################
# First Place Data #
####################

# Team 1 Group
firstGroup = doc.activeLayer = (doc.layerSets["Team 1"])

# Team 1 Text layers
teamLayer = firstGroup.ArtLayers["Team"] ## Team Name
playedLayer = firstGroup.ArtLayers["Played"] ## Games Played
winPercLayer = firstGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = firstGroup.ArtLayers["GF"] ## Goals For
gaLayer = firstGroup.ArtLayers["GA"] ## Goals Against
gdLayer = firstGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = firstGroup.ArtLayers["Wins"] ## Wins

# Team 1 Logo Group
logoGroup = (firstGroup.layerSets["Logo"])

## Team 1 Name Edit
teamName = gc.glaciesFirst.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)


## Team 1 Logo Edit
franch = gc.glaciesFirst.franchise ## Get franchise name of 1st team
franchAbbr = sc.franchises[franch] ## Get Franchise Abbreviation

teamLogo = (logoGroup.ArtLayers[franchAbbr]) ## Unhide req Logo
teamLogo.visible = True


## Team 1 Games Played Edit
gamesPlayed = gc.glaciesFirst.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 1 Win Perc Edit
winPerc = gc.glaciesFirst.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 1 Goals For Edit
goalsFor = gc.glaciesFirst.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 1 Goals Against Edit
goalsAgainst = gc.glaciesFirst.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 1 Goal Difference Edit
goalDiff = gc.glaciesFirst.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 1 Wins Edit
teamWins = gc.glaciesFirst.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

#####################
# Second Place Data #
#####################

# Team 2 Group
secondGroup = doc.activeLayer = (doc.layerSets["Team 2"])

# Team 2 Logo Group
logoGroup = (secondGroup.layerSets["Logo"])

# Team 2 Text layers
teamLayer = secondGroup.ArtLayers["Team"] ## Team Name
playedLayer = secondGroup.ArtLayers["Played"] ## Games Played
winPercLayer = secondGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = secondGroup.ArtLayers["GF"] ## Goals For
gaLayer = secondGroup.ArtLayers["GA"] ## Goals Against
gdLayer = secondGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = secondGroup.ArtLayers["Wins"] ## Wins

## Team 2 Name Edit
teamName = gc.glaciesSecond.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 2 Logo Edit
franch = gc.glaciesSecond.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 2 Games Played Edit
gamesPlayed = gc.glaciesSecond.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 2 Win Perc Edit
winPerc = gc.glaciesSecond.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 2 Goals For Edit
goalsFor = gc.glaciesSecond.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 2 Goals Against Edit
goalsAgainst = gc.glaciesSecond.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 2 Goal Difference Edit
goalDiff = gc.glaciesSecond.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 2 Wins Edit
teamWins = gc.glaciesSecond.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Third Place Data #
####################

# Team 3 Group
thirdGroup = doc.activeLayer = (doc.layerSets["Team 3"])

# Team 3 Logo Group
logoGroup = (thirdGroup.layerSets["Logo"])

# Team 3 Text layers
teamLayer = thirdGroup.ArtLayers["Team"] ## Team Name
playedLayer = thirdGroup.ArtLayers["Played"] ## Games Played
winPercLayer = thirdGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = thirdGroup.ArtLayers["GF"] ## Goals For
gaLayer = thirdGroup.ArtLayers["GA"] ## Goals Against
gdLayer = thirdGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = thirdGroup.ArtLayers["Wins"] ## Wins

## Team 3 Name Edit
teamName = gc.glaciesThird.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 3 Logo Edit
franch = gc.glaciesThird.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 3 Games Played Edit
gamesPlayed = gc.glaciesThird.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 3 Win Perc Edit
winPerc = gc.glaciesThird.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 3 Goals For Edit
goalsFor = gc.glaciesThird.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 3 Goals Against Edit
goalsAgainst = gc.glaciesThird.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 3 Goal Difference Edit
goalDiff = gc.glaciesThird.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 3 Wins Edit
teamWins = gc.glaciesThird.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Fourth Place Data #
####################

# Team 4 Group
fourthGroup = doc.activeLayer = (doc.layerSets["Team 4"])

# Team 4 Logo Group
logoGroup = (fourthGroup.layerSets["Logo"])

# Team 4 Text layers
teamLayer = fourthGroup.ArtLayers["Team"] ## Team Name
playedLayer = fourthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = fourthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = fourthGroup.ArtLayers["GF"] ## Goals For
gaLayer = fourthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = fourthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = fourthGroup.ArtLayers["Wins"] ## Wins

## Team 4 Name Edit
teamName = gc.glaciesFourth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 4 Logo Edit
franch = gc.glaciesFourth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 4 Games Played Edit
gamesPlayed = gc.glaciesFourth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 4 Win Perc Edit
winPerc = gc.glaciesFourth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 4 Goals For Edit
goalsFor = gc.glaciesFourth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 4 Goals Against Edit
goalsAgainst = gc.glaciesFourth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 4 Goal Difference Edit
goalDiff = gc.glaciesFourth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 4 Wins Edit
teamWins = gc.glaciesFourth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Fifth Place Data #
####################

# Team 5 Group
fifthGroup = doc.activeLayer = (doc.layerSets["Team 5"])

# Team 5 Logo Group
logoGroup = (fifthGroup.layerSets["Logo"])

# Team 5 Text layers
teamLayer = fifthGroup.ArtLayers["Team"] ## Team Name
playedLayer = fifthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = fifthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = fifthGroup.ArtLayers["GF"] ## Goals For
gaLayer = fifthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = fifthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = fifthGroup.ArtLayers["Wins"] ## Wins

## Team 5 Name Edit
teamName = gc.glaciesFifth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 5 Logo Edit
franch = gc.glaciesFifth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 5 Games Played Edit
gamesPlayed = gc.glaciesFifth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 5 Win Perc Edit
winPerc = gc.glaciesFifth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 5 Goals For Edit
goalsFor = gc.glaciesFifth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 5 Goals Against Edit
goalsAgainst = gc.glaciesFifth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 5 Goal Difference Edit
goalDiff = gc.glaciesFifth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 5 Wins Edits
teamWins = gc.glaciesFifth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Sixth Place Data #
####################

# Team 6 Group
sixthGroup = doc.activeLayer = (doc.layerSets["Team 6"])

# Team 6 Logo Group
logoGroup = (sixthGroup.layerSets["Logo"])

# Team 6 Text layers
teamLayer = sixthGroup.ArtLayers["Team"] ## Team Name
playedLayer = sixthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = sixthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = sixthGroup.ArtLayers["GF"] ## Goals For
gaLayer = sixthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = sixthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = sixthGroup.ArtLayers["Wins"] ## Wins

## Team 6 Name Edit
teamName = gc.glaciesSixth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 6 Logo Edit
franch = gc.glaciesSixth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 6 Games Played Edit
gamesPlayed = gc.glaciesSixth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 6 Win Perc Edit
winPerc = gc.glaciesSixth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 6 Goals For Edit
goalsFor = gc.glaciesSixth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 6 Goals Against Edit
goalsAgainst = gc.glaciesSixth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 6 Goal Difference Edit
goalDiff = gc.glaciesSixth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 6 Wins Edit
teamWins = gc.glaciesSixth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

######################
# Seventh Place Data #
######################

# Team 7 Group
seventhGroup = doc.activeLayer = (doc.layerSets["Team 7"])

# Team 7 Logo Group
logoGroup = (seventhGroup.layerSets["Logo"])

# Team 7 Text layers
teamLayer = seventhGroup.ArtLayers["Team"] ## Team Name
playedLayer = seventhGroup.ArtLayers["Played"] ## Games Played
winPercLayer = seventhGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = seventhGroup.ArtLayers["GF"] ## Goals For
gaLayer = seventhGroup.ArtLayers["GA"] ## Goals Against
gdLayer = seventhGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = seventhGroup.ArtLayers["Wins"] ## Wins

## Team 7 Name Edit
teamName = gc.glaciesSeventh.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 7 Logo Edit
franch = gc.glaciesSeventh.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 7 Games Played Edit
gamesPlayed = gc.glaciesSeventh.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 7 Win Perc Edit
winPerc = gc.glaciesSeventh.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 7 Goals For Edit
goalsFor = gc.glaciesSeventh.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 7 Goals Against Edit
goalsAgainst = gc.glaciesSeventh.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 7 Goal Difference Edit
goalDiff = gc.glaciesSeventh.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 7 Wins Edit
teamWins = gc.glaciesSeventh.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

#####################
# Eighth Place Data #
#####################

# Team 8 Group
eighthGroup = doc.activeLayer = (doc.layerSets["Team 8"])

# Team 8 Logo Group
logoGroup = (eighthGroup.layerSets["Logo"])

# Team 8 Text layers
teamLayer = eighthGroup.ArtLayers["Team"] ## Team Name
playedLayer = eighthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = eighthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = eighthGroup.ArtLayers["GF"] ## Goals For
gaLayer = eighthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = eighthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = eighthGroup.ArtLayers["Wins"] ## Wins

## Team 8 Name Edit
teamName = gc.glaciesEighth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 8 Logo Edit
franch = gc.glaciesEighth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 8 Games Played Edit
gamesPlayed = gc.glaciesEighth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 8 Win Perc Edit
winPerc = gc.glaciesEighth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 8 Goals For Edit
goalsFor = gc.glaciesEighth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 8 Goals Against Edit
goalsAgainst = gc.glaciesEighth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 8 Goal Difference Edit
goalDiff = gc.glaciesEighth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 8 Wins Edits
teamWins = gc.glaciesEighth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Ninth Place Data #
####################

# Team 9 Group
ninthGroup = doc.activeLayer = (doc.layerSets["Team 9"])

# Team 9 Logo Group
logoGroup = (ninthGroup.layerSets["Logo"])

# Team 9 Text layers
teamLayer = ninthGroup.ArtLayers["Team"] ## Team Name
playedLayer = ninthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = ninthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = ninthGroup.ArtLayers["GF"] ## Goals For
gaLayer = ninthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = ninthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = ninthGroup.ArtLayers["Wins"] ## Wins

## Team 9 Name Edit
teamName = gc.glaciesNinth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 9 Logo Edit
franch = gc.glaciesNinth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 9 Games Played Edit
gamesPlayed = gc.glaciesNinth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 9 Win Perc Edit
winPerc = gc.glaciesNinth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 9 Goals For Edit
goalsFor = gc.glaciesNinth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 9 Goals Against Edit
goalsAgainst = gc.glaciesNinth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 9 Goal Difference Edit
goalDiff = gc.glaciesNinth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 9 Wins Edits
teamWins = gc.glaciesNinth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Tenth Place Data #
####################

# Team 10 Group
tenthGroup = doc.activeLayer = (doc.layerSets["Team 10"])

# Team 10 Logo Group
logoGroup = (tenthGroup.layerSets["Logo"])

# Team 10 Text layers
teamLayer = tenthGroup.ArtLayers["Team"] ## Team Name
playedLayer = tenthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = tenthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = tenthGroup.ArtLayers["GF"] ## Goals For
gaLayer = tenthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = tenthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = tenthGroup.ArtLayers["Wins"] ## Wins

## Team 10 Name Edit
teamName = gc.glaciesTenth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 10 Logo Edit
franch = gc.glaciesTenth.franchise
franchAbbr = sc.franchises[franch]

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True


## Team 10 Games Played Edit
gamesPlayed = gc.glaciesTenth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 10 Win Perc Edit
winPerc = gc.glaciesTenth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 10 Goals For Edit
goalsFor = gc.glaciesTenth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 10 Goals Against Edit
goalsAgainst = gc.glaciesTenth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 10 Goal Difference Edit
goalDiff = gc.glaciesTenth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 10 Wins Edits
teamWins = gc.glaciesTenth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

backgroundGroup = doc.activeLayer = (doc.layerSets["Background"])
background = (backgroundGroup.layerSets["Background"])
doc.Export(ExportIn=jpgFileGlacies, ExportAs=2, Options=optionsTrans)
background.visible = True
doc.Export(ExportIn=jpgFileGlaciesBG, ExportAs=2, Options=options)
background.visible = False


                                    #########
                                    # IGNIS #
                                    #########


## Edit Conference Banner ##
confGroup = doc.activeLayer = (doc.layerSets["Conference"])
glacisConfLayer = confGroup.ArtLayers["Banner_Glacies"]
ignisConfLayer = confGroup.ArtLayers["Banner_Ignis"]
glacisConfLayer.visible = False ## Hide both banners
ignisConfLayer.visible = False

confLayer = confGroup.ArtLayers["Banner_Ignis"]
confLayer.visible = True ## Unhide selected

# Team 1 Group
firstGroup = doc.activeLayer = (doc.layerSets["Team 1"])

# Team 1 Text layers
teamLayer = firstGroup.ArtLayers["Team"] ## Team Name
playedLayer = firstGroup.ArtLayers["Played"] ## Games Played
winPercLayer = firstGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = firstGroup.ArtLayers["GF"] ## Goals For
gaLayer = firstGroup.ArtLayers["GA"] ## Goals Against
gdLayer = firstGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = firstGroup.ArtLayers["Wins"] ## Wins

# Team 1 Logo Group
logoGroup = (firstGroup.layerSets["Logo"])

## Team 1 Name Edit
teamName = ic.ignisFirst.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)


## Team 1 Logo Edit
franch = ic.ignisFirst.franchise ## Get franchise name of 1st team
franchAbbr = sc.franchises[franch] ## Get Franchise Abbreviation

for item in sc.franchises.values(): ## Hide all Logos
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr]) ## Unhide req Logo
teamLogo.visible = True


## Team 1 Games Played Edit
gamesPlayed = ic.ignisFirst.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 1 Win Perc Edit
winPerc = ic.ignisFirst.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 1 Goals For Edit
goalsFor = ic.ignisFirst.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 1 Goals Against Edit
goalsAgainst = ic.ignisFirst.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 1 Goal Difference Edit
goalDiff = ic.ignisFirst.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 1 Wins Edits
teamWins = ic.ignisFirst.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

#####################
# Second Place Data #
#####################

# Team 2 Group
secondGroup = doc.activeLayer = (doc.layerSets["Team 2"])

# Team 2 Logo Group
logoGroup = (secondGroup.layerSets["Logo"])

# Team 2 Text layers
teamLayer = secondGroup.ArtLayers["Team"] ## Team Name
playedLayer = secondGroup.ArtLayers["Played"] ## Games Played
winPercLayer = secondGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = secondGroup.ArtLayers["GF"] ## Goals For
gaLayer = secondGroup.ArtLayers["GA"] ## Goals Against
gdLayer = secondGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = secondGroup.ArtLayers["Wins"] ## Wins

## Team 2 Name Edit
teamName = ic.ignisSecond.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 2 Logo Edit
franch = ic.ignisSecond.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 2 Games Played Edit
gamesPlayed = ic.ignisSecond.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 2 Win Perc Edit
winPerc = ic.ignisSecond.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 2 Goals For Edit
goalsFor = ic.ignisSecond.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 2 Goals Against Edit
goalsAgainst = ic.ignisSecond.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 2 Goal Difference Edit
goalDiff = ic.ignisSecond.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 2 Wins Edits
teamWins = ic.ignisSecond.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Third Place Data #
####################

# Team 3 Group
thirdGroup = doc.activeLayer = (doc.layerSets["Team 3"])

# Team 3 Logo Group
logoGroup = (thirdGroup.layerSets["Logo"])

# Team 3 Text layers
teamLayer = thirdGroup.ArtLayers["Team"] ## Team Name
playedLayer = thirdGroup.ArtLayers["Played"] ## Games Played
winPercLayer = thirdGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = thirdGroup.ArtLayers["GF"] ## Goals For
gaLayer = thirdGroup.ArtLayers["GA"] ## Goals Against
gdLayer = thirdGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = thirdGroup.ArtLayers["Wins"] ## Wins

## Team 3 Name Edit
teamName = ic.ignisThird.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 3 Logo Edit
franch = ic.ignisThird.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 3 Games Played Edit
gamesPlayed = ic.ignisThird.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 3 Win Perc Edit
winPerc = ic.ignisThird.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 3 Goals For Edit
goalsFor = ic.ignisThird.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 3 Goals Against Edit
goalsAgainst = ic.ignisThird.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 3 Goal Difference Edit
goalDiff = ic.ignisThird.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 3 Wins Edits
teamWins = ic.ignisThird.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Fourth Place Data #
####################

# Team 4 Group
fourthGroup = doc.activeLayer = (doc.layerSets["Team 4"])

# Team 4 Logo Group
logoGroup = (fourthGroup.layerSets["Logo"])

# Team 4 Text layers
teamLayer = fourthGroup.ArtLayers["Team"] ## Team Name
playedLayer = fourthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = fourthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = fourthGroup.ArtLayers["GF"] ## Goals For
gaLayer = fourthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = fourthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = fourthGroup.ArtLayers["Wins"] ## Wins

## Team 4 Name Edit
teamName = ic.ignisFourth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 4 Logo Edit
franch = ic.ignisFourth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 4 Games Played Edit
gamesPlayed = ic.ignisFourth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 4 Win Perc Edit
winPerc = ic.ignisFourth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 4 Goals For Edit
goalsFor = ic.ignisFourth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 4 Goals Against Edit
goalsAgainst = ic.ignisFourth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 4 Goal Difference Edit
goalDiff = ic.ignisFourth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 4 Wins Edits
teamWins = ic.ignisFourth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Fifth Place Data #
####################

# Team 5 Group
fifthGroup = doc.activeLayer = (doc.layerSets["Team 5"])

# Team 5 Logo Group
logoGroup = (fifthGroup.layerSets["Logo"])

# Team 5 Text layers
teamLayer = fifthGroup.ArtLayers["Team"] ## Team Name
playedLayer = fifthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = fifthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = fifthGroup.ArtLayers["GF"] ## Goals For
gaLayer = fifthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = fifthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = fifthGroup.ArtLayers["Wins"] ## Wins

## Team 5 Name Edit
teamName = ic.ignisFifth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 5 Logo Edit
franch = ic.ignisFifth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 5 Games Played Edit
gamesPlayed = ic.ignisFifth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 5 Win Perc Edit
winPerc = ic.ignisFifth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 5 Goals For Edit
goalsFor = ic.ignisFifth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 5 Goals Against Edit
goalsAgainst = ic.ignisFifth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 5 Goal Difference Edit
goalDiff = ic.ignisFifth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 5 Wins Edits
teamWins = ic.ignisFifth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Sixth Place Data #
####################

# Team 6 Group
sixthGroup = doc.activeLayer = (doc.layerSets["Team 6"])

# Team 6 Logo Group
logoGroup = (sixthGroup.layerSets["Logo"])

# Team 6 Text layers
teamLayer = sixthGroup.ArtLayers["Team"] ## Team Name
playedLayer = sixthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = sixthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = sixthGroup.ArtLayers["GF"] ## Goals For
gaLayer = sixthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = sixthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = sixthGroup.ArtLayers["Wins"] ## Wins

## Team 6 Name Edit
teamName = ic.ignisSixth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 6 Logo Edit
franch = ic.ignisSixth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 6 Games Played Edit
gamesPlayed = ic.ignisSixth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 6 Win Perc Edit
winPerc = ic.ignisSixth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 6 Goals For Edit
goalsFor = ic.ignisSixth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 6 Goals Against Edit
goalsAgainst = ic.ignisSixth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 6 Goal Difference Edit
goalDiff = ic.ignisSixth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 6 Wins Edits
teamWins = ic.ignisSixth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

######################
# Seventh Place Data #
######################

# Team 7 Group
seventhGroup = doc.activeLayer = (doc.layerSets["Team 7"])

# Team 7 Logo Group
logoGroup = (seventhGroup.layerSets["Logo"])

# Team 7 Text layers
teamLayer = seventhGroup.ArtLayers["Team"] ## Team Name
playedLayer = seventhGroup.ArtLayers["Played"] ## Games Played
winPercLayer = seventhGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = seventhGroup.ArtLayers["GF"] ## Goals For
gaLayer = seventhGroup.ArtLayers["GA"] ## Goals Against
gdLayer = seventhGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = seventhGroup.ArtLayers["Wins"] ## Wins

## Team 7 Name Edit
teamName = ic.ignisSeventh.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 7 Logo Edit
franch = ic.ignisSeventh.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 7 Games Played Edit
gamesPlayed = ic.ignisSeventh.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 7 Win Perc Edit
winPerc = ic.ignisSeventh.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 7 Goals For Edit
goalsFor = ic.ignisSeventh.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 7 Goals Against Edit
goalsAgainst = ic.ignisSeventh.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 7 Goal Difference Edit
goalDiff = ic.ignisSeventh.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 7 Wins Edits
teamWins = ic.ignisSeventh.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

#####################
# Eighth Place Data #
#####################

# Team 8 Group
eighthGroup = doc.activeLayer = (doc.layerSets["Team 8"])

# Team 8 Logo Group
logoGroup = (eighthGroup.layerSets["Logo"])

# Team 8 Text layers
teamLayer = eighthGroup.ArtLayers["Team"] ## Team Name
playedLayer = eighthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = eighthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = eighthGroup.ArtLayers["GF"] ## Goals For
gaLayer = eighthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = eighthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = eighthGroup.ArtLayers["Wins"] ## Wins

## Team 8 Name Edit
teamName = ic.ignisEighth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 8 Logo Edit
franch = ic.ignisEighth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 8 Games Played Edit
gamesPlayed = ic.ignisEighth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 8 Win Perc Edit
winPerc = ic.ignisEighth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 8 Goals For Edit
goalsFor = ic.ignisEighth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 8 Goals Against Edit
goalsAgainst = ic.ignisEighth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 8 Goal Difference Edit
goalDiff = ic.ignisEighth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 8 Wins Edits
teamWins = ic.ignisEighth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Ninth Place Data #
####################

# Team 9 Group
ninthGroup = doc.activeLayer = (doc.layerSets["Team 9"])

# Team 9 Logo Group
logoGroup = (ninthGroup.layerSets["Logo"])

# Team 9 Text layers
teamLayer = ninthGroup.ArtLayers["Team"] ## Team Name
playedLayer = ninthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = ninthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = ninthGroup.ArtLayers["GF"] ## Goals For
gaLayer = ninthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = ninthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = ninthGroup.ArtLayers["Wins"] ## Wins

## Team 9 Name Edit
teamName = ic.ignisNinth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 9 Logo Edit
franch = ic.ignisNinth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True

## Team 9 Games Played Edit
gamesPlayed = ic.ignisNinth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 9 Win Perc Edit
winPerc = ic.ignisNinth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 9 Goals For Edit
goalsFor = ic.ignisNinth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 9 Goals Against Edit
goalsAgainst = ic.ignisNinth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 9 Goal Difference Edit
goalDiff = ic.ignisNinth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 9 Wins Edits
teamWins = ic.ignisNinth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)

####################
# Tenth Place Data #
####################

# Team 10 Group
tenthGroup = doc.activeLayer = (doc.layerSets["Team 10"])

# Team 10 Logo Group
logoGroup = (tenthGroup.layerSets["Logo"])

# Team 10 Text layers
teamLayer = tenthGroup.ArtLayers["Team"] ## Team Name
playedLayer = tenthGroup.ArtLayers["Played"] ## Games Played
winPercLayer = tenthGroup.ArtLayers["WinPerc"] ## Win Percentage
gfLayer = tenthGroup.ArtLayers["GF"] ## Goals For
gaLayer = tenthGroup.ArtLayers["GA"] ## Goals Against
gdLayer = tenthGroup.ArtLayers["GD"] ## Goal Difference
winsLayer = tenthGroup.ArtLayers["Wins"] ## Wins

## Team 10 Name Edit
teamName = ic.ignisTenth.team
teamText = teamLayer.TextItem
teamText.contents = str(teamName)

## Team 10 Logo Edit
franch = ic.ignisTenth.franchise
franchAbbr = sc.franchises[franch]

for item in sc.franchises.values():
    teamLogo = (logoGroup.ArtLayers[item])
    teamLogo.visible = False

teamLogo = (logoGroup.ArtLayers[franchAbbr])
teamLogo.visible = True


## Team 10 Games Played Edit
gamesPlayed = ic.ignisTenth.gp
gpText = playedLayer.TextItem
gpText.contents = str(gamesPlayed)

## Team 10 Win Perc Edit
winPerc = ic.ignisTenth.winPerc
winPercText = winPercLayer.TextItem
winPercText.contents = str(winPerc)

## Team 10 Goals For Edit
goalsFor = ic.ignisTenth.gs
gfText = gfLayer.TextItem
gfText.contents = str(goalsFor)

## Team 10 Goals Against Edit
goalsAgainst = ic.ignisTenth.gc
gaText = gaLayer.TextItem
gaText.contents = str(goalsAgainst)

## Team 10 Goal Difference Edit
goalDiff = ic.ignisTenth.gd
gdText = gdLayer.TextItem
gdText.contents = str(goalDiff)

## Team 10 Wins Edits
teamWins = ic.ignisTenth.gw
winsText = winsLayer.TextItem
winsText.contents = str(teamWins)


backgroundGroup = doc.activeLayer = (doc.layerSets["Background"])
background = (backgroundGroup.layerSets["Background"])
doc.Export(ExportIn=jpgFileIgnis, ExportAs=2, Options=optionsTrans)
background.visible = True
doc.Export(ExportIn=jpgFileIgnisBG, ExportAs=2, Options=options)

endTime = time.time()
print(endTime - startTime)