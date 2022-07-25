import win32com.client
import weeklyFixturesReader as wfr
import fixturesClass as fc
import configparser
import os
#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"fixturesConfig.txt"))
week = config.get('config', 'Week')
configPath = config.get('config', 'Path')

#########
# Setup #
#########
options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit

def editFixtures():
    psApp = win32com.client.Dispatch("Photoshop.Application")
    
    psApp.Open(os.path.join(configPath, "RSC10_Weekly_Results.psd"))
    doc = psApp.Application.ActiveDocument 
    
    loopCount = 18
    premTeams = len(fc.teamsPrem)
    masterTeams = len(fc.teamsMaster)
    eliteTeams = len(fc.teamsElite)
    rivalTeams = len(fc.teamsRival)
    challTeams = len(fc.teamsChall)
    prospTeams = len(fc.teamsProsp)
    totalTeams = premTeams+masterTeams+eliteTeams+rivalTeams+challTeams+prospTeams

    while loopCount <= totalTeams:
        if loopCount <= premTeams:
            premFlag = True
            tier = 'Premier'
            tierClass = fc.prem
            teamClass = fc.teamsPrem
            topGroup = doc.activeLayer = (doc.layerSets["Premier"])
            pngFixt = (configPath.join("Outputs\PremFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\PremFixturesTRANS.png"))
        else:
            topGroup = doc.activeLayer = (doc.layerSets["Conference Tiers"])
        if loopCount > premTeams and loopCount <= premTeams+masterTeams:
            tier = 'Master'
            tierClass = fc.master
            teamClass = fc.teamsMaster
            pngFixt = (configPath.join("Outputs\MasterFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\MasterFixturesTRANS.png"))
        if loopCount > premTeams+masterTeams and loopCount <= premTeams+masterTeams+eliteTeams:
            tier = 'Elite'
            tierClass = fc.elite
            teamClass = fc.teamsElite
            pngFixt = (configPath.join("Outputs\EliteFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\EliteFixturesTRANS.png"))
        if loopCount > premTeams+masterTeams+eliteTeams and loopCount <= premTeams+masterTeams+eliteTeams+rivalTeams:
            tier = 'Rival'
            tierClass = fc.rival
            teamClass = fc.teamsRival
            pngFixt = (configPath.join("Outputs\RivalFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\RivalFixturesTRANS.png"))
        if loopCount > premTeams+masterTeams+eliteTeams+rivalTeams and loopCount <= premTeams+masterTeams+eliteTeams+rivalTeams+challTeams:
            tier = 'Challenger'
            tierClass = fc.chall
            teamClass = fc.teamsChall
            pngFixt = (configPath.join("Outputs\ChallengerFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\ChallengerFixturesTRANS.png"))
        if loopCount > premTeams+masterTeams+eliteTeams+rivalTeams+challTeams and loopCount <= premTeams+masterTeams+eliteTeams+rivalTeams+challTeams+prospTeams:
            tier = 'Prospect'
            tierClass = fc.prosp
            teamClass = fc.teamsProsp
            pngFixt = (configPath.join("Outputs\ProspectFixtures.png"))
            pngFixtTrans = (configPath.join("Outputs\ProspectFixturesTRANS.png"))
        


        ########################
        # Header / Title Edits #
        ########################

        ## Edit Week Number ##
        topGroup.visible = True
        weekGroup = topGroup.layerSets["WeekNumGroup"]
        weekLayer = weekGroup.ArtLayers["WeekNum"]
        weekText = weekLayer.textItem
        weekText.contents = 'WEEK ' + str(week)

                                            #########
                                            # Ignis #
                                            #########

        # Ignis Group
        ignisGroup = topGroup.layerSets["Ignis"]


        ###################
        # First Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game1"] # Assign row's layer
        #Layer's left team
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        # Layer's right team
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        # Layer's date
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 
        # Layer's left logo
        logoGroupLeft = currRow.layerSets["Left Logo"]
        logoGroupRight = currRow.layerSets["Right Logo"]

        leftTeamName = str(tierClass.teamOrder[0])
        leftAbbr = teamClass[leftTeamName]
        teamLogoLeft = (logoGroupLeft.ArtLayers[leftAbbr])
        teamLogoLeft.visible = True
        rightTeamName = str(tierClass.teamOrder[1])
        rightAbbr = teamClass[rightTeamName]
        teamLogoRight = (logoGroupRight.ArtLayers[rightAbbr])
        teamLogoRight.visible = True

        leftTeamText.contents = str(tierClass.teamOrder[0])
        rightTeamText.contents = str(tierClass.teamOrder[1])
        matchDateText.contents = str(tierClass.dateOrder[0])


        ###################
        # Second Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game2"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[2])
        rightTeamText.contents = str(tierClass.teamOrder[3])
        matchDateText.contents = str(tierClass.dateOrder[1])

        ###################
        # Third Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game3"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[4])
        rightTeamText.contents = str(tierClass.teamOrder[5])
        matchDateText.contents = str(tierClass.dateOrder[2])

        ###################
        # Fourth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game4"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[6])
        rightTeamText.contents = str(tierClass.teamOrder[7])
        matchDateText.contents = str(tierClass.dateOrder[3])

        ###################
        # Fifth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game5"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[8])
        rightTeamText.contents = str(tierClass.teamOrder[9])
        matchDateText.contents = str(tierClass.dateOrder[4])

        ###################
        # Sixth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game6"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[10])
        rightTeamText.contents = str(tierClass.teamOrder[11])
        matchDateText.contents = str(tierClass.dateOrder[5])

        ###################
        # Seventh Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game7"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[12])
        rightTeamText.contents = str(tierClass.teamOrder[13])
        matchDateText.contents = str(tierClass.dateOrder[6])

        ###################
        # Eigth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game8"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[14])
        rightTeamText.contents = str(tierClass.teamOrder[15])
        matchDateText.contents = str(tierClass.dateOrder[7])

        ###################
        # Ninth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game9"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[16])
        rightTeamText.contents = str(tierClass.teamOrder[17])
        matchDateText.contents = str(tierClass.dateOrder[8])

        ###################
        # Tenth Row Data #
        ###################
        currRow = ignisGroup.layerSets["Game10"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[18])
        rightTeamText.contents = str(tierClass.teamOrder[19])
        matchDateText.contents = str(tierClass.dateOrder[9])



                                            ###########
                                            # Glacies #
                                            ###########

        # Glacies Group
        glaciesGroup = topGroup.layerSets["Glacies"]


        ###################
        # First Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game1"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[0])
        rightTeamText.contents = str(tierClass.teamOrder[1])
        matchDateText.contents = str(tierClass.dateOrder[0])


        ###################
        # Second Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game2"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[2])
        rightTeamText.contents = str(tierClass.teamOrder[3])
        matchDateText.contents = str(tierClass.dateOrder[1])

        ###################
        # Third Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game3"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[4])
        rightTeamText.contents = str(tierClass.teamOrder[5])
        matchDateText.contents = str(tierClass.dateOrder[2])

        ###################
        # Fourth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game4"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[6])
        rightTeamText.contents = str(tierClass.teamOrder[7])
        matchDateText.contents = str(tierClass.dateOrder[3])

        ###################
        # Fifth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game5"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[8])
        rightTeamText.contents = str(tierClass.teamOrder[9])
        matchDateText.contents = str(tierClass.dateOrder[4])

        ###################
        # Sixth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game6"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[10])
        rightTeamText.contents = str(tierClass.teamOrder[11])
        matchDateText.contents = str(tierClass.dateOrder[5])

        ###################
        # Seventh Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game7"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[12])
        rightTeamText.contents = str(tierClass.teamOrder[13])
        matchDateText.contents = str(tierClass.dateOrder[6])

        ###################
        # Eigth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game8"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[14])
        rightTeamText.contents = str(tierClass.teamOrder[15])
        matchDateText.contents = str(tierClass.dateOrder[7])

        ###################
        # Ninth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game9"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[16])
        rightTeamText.contents = str(tierClass.teamOrder[17])
        matchDateText.contents = str(tierClass.dateOrder[8])

        ###################
        # Tenth Row Data #
        ###################
        currRow = glaciesGroup.layerSets["Game10"]
        leftTeam = currRow.ArtLayers["LeftTeam"]
        leftTeamText = leftTeam.TextItem
        rightTeam = currRow.ArtLayers["RightTeam"]
        rightTeamText = rightTeam.TextItem
        matchDate = currRow.ArtLayers["Date"]
        matchDateText = matchDate.TextItem 

        leftTeamText.contents = str(tierClass.teamOrder[18])
        rightTeamText.contents = str(tierClass.teamOrder[19])
        matchDateText.contents = str(tierClass.dateOrder[9])

    background = doc.activeLayer = (doc.layerSets["Background"])
    doc.Export(ExportIn=pngFixt, ExportAs=2, Options=options)
    background.visible = False
    doc.Export(ExportIn=pngFixtTrans, ExportAs=2, Options=options)
    doc.Close(2)

    editFixtures()