import win32com.client
import standingsClass as sc
import gsReader as reader
import configparser
import time

premCount = len(sc.PremStandings.franchOrder)
masterCount = len(sc.MasterStandings.franchOrder)
eliteCount = len(sc.EliteStandings.franchOrder)
rivalCount = len(sc.RivalStandings.franchOrder)
challCount = len(sc.ChallStandings.franchOrder)
prospCount = len(sc.ProspStandings.franchOrder)

totalCount = premCount+masterCount+eliteCount+rivalCount+challCount+prospCount

startTime = time.time()
#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"config.txt"))
week = config.get('config', 'Week')

#########
# Setup #
#########
options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit

pngOpts = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
pngOpts.Format = 13   # PNG Format
pngOpts.PNG8 = False  # Sets it to PNG-24 bit
pngOpts.quality = 100

def editStandings():
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
    


    loopCount = 0 ## 0: Prem Start | 17: Master Start  

    while loopCount <= totalCount:
        if loopCount <= premCount:
            tier = 'Premier'
            tierClass = sc.PremStandings
            jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\PremStandingsGlaciesBG.png")
            jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\PremStandingsGlacies.png")
            jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\PremStandingsIgnisBG.png")
            jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\PremStandingsIgnis.png")
        if loopCount > premCount and loopCount <= premCount+masterCount:
            tier = 'Master'
            tierClass = sc.MasterStandings
            jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\MasterStandingsGlaciesBG.png")
            jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\MasterStandingsGlacies.png")
            jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\MasterStandingsIgnisBG.png")
            jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\MasterStandingsIgnis.png")
        if loopCount > premCount+masterCount and loopCount <= premCount+masterCount+eliteCount:
            tier = 'Elite'
            tierClass = sc.EliteStandings
                     
        if loopCount > premCount+masterCount+eliteCount and loopCount <= premCount+masterCount+eliteCount+rivalCount:
            tier = 'Rival'
            tierClass = sc.RivalStandings 
            jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\RivalStandingsGlaciesBG.png")
            jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\RivalStandingsGlacies.png")
            jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\RivalStandingsIgnisBG.png")
            jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\RivalStandingsIgnis.png")
   
        if loopCount > premCount+masterCount+eliteCount+rivalCount and loopCount <= premCount+masterCount+eliteCount+rivalCount+challCount:
            tier = 'Challenger'
            tierClass = sc.ChallStandings
            jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editorOutputs\\ChallStandingsGlaciesBG.png")
            jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ChallStandingsGlacies.png")
            jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ChallStandingsIgnisBG.png")
            jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ChallStandingsIgnis.png")   
        if loopCount > premCount+masterCount+eliteCount+rivalCount+challCount and loopCount <= premCount+masterCount+eliteCount+rivalCount+challCount+prospCount:
            tier = 'Prospect'
            tierClass = sc.ProspStandings  
            jpgFileGlaciesBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ProspStandingsGlaciesBG.png")
            jpgFileGlacies = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ProspStandingsGlacies.png")
            jpgFileIgnisBG = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ProspStandingsIgnisBG.png")
            jpgFileIgnis = (r"C:\Users\jaymu\Desktop\RSC\psd_editor\Outputs\ProspStandingsIgnis.png")  

        
        ## Edit Conference Banner ##
        confGroup = doc.activeLayer = (doc.layerSets["Conference"])
        glacisConfLayer = confGroup.ArtLayers["Banner_Glacies"]
        ignisConfLayer = confGroup.ArtLayers["Banner_Ignis"]
        glacisConfLayer.visible = False ## Hide both banners
        ignisConfLayer.visible = False

        confLayer = confGroup.ArtLayers["Banner_Ignis"]
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
        teamName = tierClass.teamOrder[0]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)


        ## Team 1 Logo Edit
        franch = tierClass.franchOrder[0] ## Get franchise name of 1st team
        franchAbbr = sc.franchises[franch] ## Get Franchise Abbreviation

        teamLogo = (logoGroup.ArtLayers[franchAbbr]) ## Unhide req Logo
        teamLogo.visible = True


        ## Team 1 Games Played Edit
        gamesPlayed = tierClass.gpOrder[0]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 1 Win Perc Edit
        winPerc = tierClass.winPercOrder[0]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 1 Goals For Edit
        goalsFor = tierClass.gsOrder[0]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 1 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[0]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 1 Goal Difference Edit
        goalDiff = tierClass.gdOrder[0]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 1 Wins Edit
        teamWins = tierClass.gwOrder[0]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[1]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 2 Logo Edit
        franch = tierClass.franchOrder[1]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 2 Games Played Edit
        gamesPlayed = tierClass.gpOrder[1]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 2 Win Perc Edit
        winPerc = tierClass.winPercOrder[1]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 2 Goals For Edit
        goalsFor = tierClass.gsOrder[1]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 2 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[1]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 2 Goal Difference Edit
        goalDiff = tierClass.gdOrder[1]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 2 Wins Edit
        teamWins = tierClass.gwOrder[1]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1

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
        teamName = tierClass.teamOrder[2]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 3 Logo Edit
        franch = tierClass.franchOrder[2]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 3 Games Played Edit
        gamesPlayed = tierClass.gpOrder[2]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 3 Win Perc Edit
        winPerc = tierClass.winPercOrder[2]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 3 Goals For Edit
        goalsFor = tierClass.gsOrder[2]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 3 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[2]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 3 Goal Difference Edit
        goalDiff = tierClass.gdOrder[2]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 3 Wins Edit
        teamWins = tierClass.gwOrder[2]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[3]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 4 Logo Edit
        franch = tierClass.franchOrder[3]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 4 Games Played Edit
        gamesPlayed = tierClass.gpOrder[3]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 4 Win Perc Edit
        winPerc = tierClass.winPercOrder[3]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 4 Goals For Edit
        goalsFor = tierClass.gsOrder[3]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 4 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[3]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 4 Goal Difference Edit
        goalDiff = tierClass.gdOrder[3]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 4 Wins Edit
        teamWins = tierClass.gwOrder[3]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[4]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 5 Logo Edit
        franch = tierClass.franchOrder[4]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 5 Games Played Edit
        gamesPlayed = tierClass.gpOrder[4]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 5 Win Perc Edit
        winPerc = tierClass.winPercOrder[4]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 5 Goals For Edit
        goalsFor = tierClass.gsOrder[4]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 5 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[4]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 5 Goal Difference Edit
        goalDiff = tierClass.gdOrder[4]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 5 Wins Edits
        teamWins = tierClass.gwOrder[4]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[5]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 6 Logo Edit
        franch = tierClass.franchOrder[5]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 6 Games Played Edit
        gamesPlayed = tierClass.gpOrder[5]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 6 Win Perc Edit
        winPerc = tierClass.winPercOrder[5]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 6 Goals For Edit
        goalsFor = tierClass.gsOrder[5]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 6 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[5]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 6 Goal Difference Edit
        goalDiff = tierClass.gdOrder[5]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 6 Wins Edit
        teamWins = tierClass.gwOrder[5]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[6]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 7 Logo Edit
        franch = tierClass.franchOrder[6]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 7 Games Played Edit
        gamesPlayed = tierClass.gpOrder[6]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 7 Win Perc Edit
        winPerc = tierClass.winPercOrder[6]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 7 Goals For Edit
        goalsFor = tierClass.gsOrder[6]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 7 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[6]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 7 Goal Difference Edit
        goalDiff = tierClass.gdOrder[6]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 7 Wins Edit
        teamWins = tierClass.gwOrder[6]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[7]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 8 Logo Edit
        franch = tierClass.franchOrder[7]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 8 Games Played Edit
        gamesPlayed = tierClass.gpOrder[7]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 8 Win Perc Edit
        winPerc = tierClass.winPercOrder[7]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 8 Goals For Edit
        goalsFor = tierClass.gsOrder[7]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 8 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[7]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 8 Goal Difference Edit
        goalDiff = tierClass.gdOrder[7]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 8 Wins Edits
        teamWins = tierClass.gwOrder[7]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[8]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 9 Logo Edit
        franch = tierClass.franchOrder[8]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 9 Games Played Edit
        gamesPlayed = tierClass.gpOrder[8]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 9 Win Perc Edit
        winPerc = tierClass.winPercOrder[8]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 9 Goals For Edit
        goalsFor = tierClass.gsOrder[8]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 9 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[8]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 9 Goal Difference Edit
        goalDiff = tierClass.gdOrder[8]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 9 Wins Edits
        teamWins = tierClass.gwOrder[8]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[9]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 10 Logo Edit
        franch = tierClass.franchOrder[9]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True


        ## Team 10 Games Played Edit
        gamesPlayed = tierClass.gpOrder[9]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 10 Win Perc Edit
        winPerc = tierClass.winPercOrder[9]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 10 Goals For Edit
        goalsFor = tierClass.gsOrder[9]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 10 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[9]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 10 Goal Difference Edit
        goalDiff = tierClass.gdOrder[9]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 10 Wins Edits
        teamWins = tierClass.gwOrder[9]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1


        backgroundGroup = doc.activeLayer = (doc.layerSets["Background"])
        background = (backgroundGroup.layerSets["Background"])
        doc.Export(ExportIn=jpgFileGlacies, ExportAs=2, Options=pngOpts)
        time.sleep(3)
        background.visible = True
        time.sleep(3)
        doc.Export(ExportIn=jpgFileGlaciesBG, ExportAs=2, Options=options)
        doc.Close(2)


                                            #########
                                            # IGNIS #
                                            #########

        psApp.Open(r"C:\Users\jaymu\Desktop\RSC\psd_editor\RSC Standings.psd")
        doc = psApp.Application.ActiveDocument  

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
        teamName = tierClass.teamOrder[10]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)


        ## Team 1 Logo Edit
        franch = tierClass.franchOrder[10] ## Get franchise name of 1st team
        franchAbbr = sc.franchises[franch] ## Get Franchise Abbreviation

        teamLogo = (logoGroup.ArtLayers[franchAbbr]) ## Unhide req Logo
        teamLogo.visible = True


        ## Team 1 Games Played Edit
        gamesPlayed = tierClass.gpOrder[10]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 1 Win Perc Edit
        winPerc = tierClass.winPercOrder[10]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 1 Goals For Edit
        goalsFor = tierClass.gsOrder[10]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 1 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[10]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 1 Goal Difference Edit
        goalDiff = tierClass.gdOrder[10]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 1 Wins Edit
        teamWins = tierClass.gwOrder[10]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[11]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 2 Logo Edit
        franch = tierClass.franchOrder[11]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 2 Games Played Edit
        gamesPlayed = tierClass.gpOrder[11]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 2 Win Perc Edit
        winPerc = tierClass.winPercOrder[11]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 2 Goals For Edit
        goalsFor = tierClass.gsOrder[11]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 2 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[11]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 2 Goal Difference Edit
        goalDiff = tierClass.gdOrder[11]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 2 Wins Edit
        teamWins = tierClass.gwOrder[11]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[12]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 3 Logo Edit
        franch = tierClass.franchOrder[12]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 3 Games Played Edit
        gamesPlayed = tierClass.gpOrder[12]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 3 Win Perc Edit
        winPerc = tierClass.winPercOrder[12]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 3 Goals For Edit
        goalsFor = tierClass.gsOrder[12]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 3 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[12]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 3 Goal Difference Edit
        goalDiff = tierClass.gdOrder[12]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 3 Wins Edit
        teamWins = tierClass.gwOrder[12]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[13]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 4 Logo Edit
        franch = tierClass.franchOrder[13]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 4 Games Played Edit
        gamesPlayed = tierClass.gpOrder[13]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 4 Win Perc Edit
        winPerc = tierClass.winPercOrder[13]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 4 Goals For Edit
        goalsFor = tierClass.gsOrder[13]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 4 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[13]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 4 Goal Difference Edit
        goalDiff = tierClass.gdOrder[13]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 4 Wins Edit
        teamWins = tierClass.gwOrder[13]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[14]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 5 Logo Edit
        franch = tierClass.franchOrder[14]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 5 Games Played Edit
        gamesPlayed = tierClass.gpOrder[14]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 5 Win Perc Edit
        winPerc = tierClass.winPercOrder[14]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 5 Goals For Edit
        goalsFor = tierClass.gsOrder[14]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 5 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[14]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 5 Goal Difference Edit
        goalDiff = tierClass.gdOrder[14]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 5 Wins Edits
        teamWins = tierClass.gwOrder[14]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[15]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 6 Logo Edit
        franch = tierClass.franchOrder[15]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 6 Games Played Edit
        gamesPlayed = tierClass.gpOrder[15]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 6 Win Perc Edit
        winPerc = tierClass.winPercOrder[15]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 6 Goals For Edit
        goalsFor = tierClass.gsOrder[15]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 6 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[15]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 6 Goal Difference Edit
        goalDiff = tierClass.gdOrder[15]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 6 Wins Edit
        teamWins = tierClass.gwOrder[15]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[16]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 7 Logo Edit
        franch = tierClass.franchOrder[16]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 7 Games Played Edit
        gamesPlayed = tierClass.gpOrder[16]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 7 Win Perc Edit
        winPerc = tierClass.winPercOrder[16]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 7 Goals For Edit
        goalsFor = tierClass.gsOrder[16]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 7 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[16]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 7 Goal Difference Edit
        goalDiff = tierClass.gdOrder[16]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 7 Wins Edit
        teamWins = tierClass.gwOrder[16]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[17]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 8 Logo Edit
        franch = tierClass.franchOrder[17]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 8 Games Played Edit
        gamesPlayed = tierClass.gpOrder[17]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 8 Win Perc Edit
        winPerc = tierClass.winPercOrder[17]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 8 Goals For Edit
        goalsFor = tierClass.gsOrder[17]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 8 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[17]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 8 Goal Difference Edit
        goalDiff = tierClass.gdOrder[17]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 8 Wins Edits
        teamWins = tierClass.gwOrder[17]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[18]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 9 Logo Edit
        franch = tierClass.franchOrder[18]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True

        ## Team 9 Games Played Edit
        gamesPlayed = tierClass.gpOrder[18]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 9 Win Perc Edit
        winPerc = tierClass.winPercOrder[18]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 9 Goals For Edit
        goalsFor = tierClass.gsOrder[18]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 9 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[18]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 9 Goal Difference Edit
        goalDiff = tierClass.gdOrder[18]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 9 Wins Edits
        teamWins = tierClass.gwOrder[18]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1
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
        teamName = tierClass.teamOrder[19]
        teamText = teamLayer.TextItem
        teamText.contents = str(teamName)

        ## Team 10 Logo Edit
        franch = tierClass.franchOrder[19]
        franchAbbr = sc.franchises[franch]

        teamLogo = (logoGroup.ArtLayers[franchAbbr])
        teamLogo.visible = True


        ## Team 10 Games Played Edit
        gamesPlayed = tierClass.gpOrder[19]
        gpText = playedLayer.TextItem
        gpText.contents = str(gamesPlayed)

        ## Team 10 Win Perc Edit
        winPerc = tierClass.winPercOrder[19]
        winPercText = winPercLayer.TextItem
        winPercText.contents = str(winPerc)

        ## Team 10 Goals For Edit
        goalsFor = tierClass.gsOrder[19]
        gfText = gfLayer.TextItem
        gfText.contents = str(goalsFor)

        ## Team 10 Goals Against Edit
        goalsAgainst = tierClass.gcOrder[19]
        gaText = gaLayer.TextItem
        gaText.contents = str(goalsAgainst)

        ## Team 10 Goal Difference Edit
        goalDiff = tierClass.gdOrder[19]
        gdText = gdLayer.TextItem
        gdText.contents = str(goalDiff)

        ## Team 10 Wins Edits
        teamWins = tierClass.gwOrder[19]
        winsText = winsLayer.TextItem
        winsText.contents = str(teamWins)
        loopCount += 1

        backgroundGroup = doc.activeLayer = (doc.layerSets["Background"])
        background = (backgroundGroup.layerSets["Background"])
        doc.Export(ExportIn=jpgFileGlacies, ExportAs=2, Options=pngOpts)
        time.sleep(3)
        background.visible = True
        time.sleep(3)
        doc.Export(ExportIn=jpgFileGlaciesBG, ExportAs=2, Options=options)
        doc.Close(2)

editStandings()

endTime = time.time()
print(endTime - startTime)