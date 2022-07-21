from asyncore import loop
import configparser
import win32com.client
import fixturesClass as fc
import time
import os

#################
# Config Reader #
#################
config = configparser.ConfigParser()
config.read_file(open(r"deskConfig.txt"))
numGames = config.get('config', 'Games')

castersList = config.get('config', 'Casters')
castersList = castersList.split(',')

streamer = config.get('config', 'Streamer')

teams = config.get('config', 'Teams')
teams = teams.split(',')

tiers = config.get('config', 'Tiers')
tiers = tiers.split(',')

confs = config.get('config', 'Conferences')
confs = confs.split(',')

#########
# Setup #
#########

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
options.Format = 13
options.quality = 100
options.PNG8 = False  # Sets it to PNG-24 bit


psApp = win32com.client.Dispatch("Photoshop.Application")





def editDesk(numGames):
    loopCount = 0
    while loopCount < numGames:
        psApp.Open(os.path.join(__location__, 'fixGraphics/RSC10_CasterScreen.psd'))
        doc = psApp.Application.ActiveDocument     
        ## Class Setter
        if tiers[0] == "Premier":
            premFlag = True
            teamsClass = fc.teamsPrem
        elif tiers[0] == "Master":
            teamsClass = fc.teamsMaster
        elif tiers[0] == "Elite":
            teamsClass = fc.teamsElite
        elif tiers[0] == "Rival":
            teamsClass = fc.teamsRival
        elif tiers[0] == "Challenger":
            teamsClass = fc.teamsChall
        elif tiers[0] == "Prospect":
            teamsClass = fc.teamsProsp
        else:
            teamsClass = None
   

        titleGroup = doc.activeLayer = (doc.layerSets["Title"]) ## Group for Tier and Conf banners
        ## Tier Banners
        tierBannerGroup = titleGroup.layerSets["Tier"] 
        tierBanner = tierBannerGroup.layerSets[tiers[0]] 
        tierBanner.visible = True

        ## Conf Banners
        if tiers[0] != "Premier":
            confBannerGroup = titleGroup.layerSets["Conference / Stage"]
            confBanner = confBannerGroup.ArtLayers[confs[0]]
            confBanner.visible = True
        
        ## Casters
        casterLeftGroup = doc.activeLayer = (doc.layerSets["CasterLeft"]) ## Group for Left Casters
        casterLeftName = casterLeftGroup.ArtLayers["Caster"]
        casterLeftText = casterLeftName.textItem
        casterLeftText.contents = castersList[0]
        casterLeftHandle = casterLeftGroup.ArtLayers["Handle"]


        casterRightGroup = doc.activeLayer = (doc.layerSets["CasterRight"]) ## Group for Right Casters
        casterRightName = casterRightGroup.ArtLayers["Caster"]
        casterRightText = casterRightName.textItem
        casterRightText.contents = castersList[1]
        casterRightHandle = casterRightGroup.ArtLayers["Handle"]
 



        ## Streamer
        streamerBannerGroup = doc.activeLayer = (doc.layerSets["StreamerBanner"])
        streamerName = streamerBannerGroup.ArtLayers["Streamer"]
        streamerNameText = streamerName.textItem
        streamerNameText.contents = streamer
        ## Teams
        matchInfoGroup = doc.activeLayer = (doc.layerSets["Match"]) ## Parent group for match info
        leftTeamName = matchInfoGroup.ArtLayers["TeamNameLeft"] ## Left Team Name
        leftTeamNameText = leftTeamName.textItem
        leftTeamNameText.contents = teams[0]

        rightTeamName = matchInfoGroup.ArtLayers["TeamNameRight"] ## Right Team Name
        rightTeamNameText = rightTeamName.textItem
        rightTeamNameText.contents = teams[1]

        leftTeamLogoGroup = matchInfoGroup.layerSets["LeftTeamLogo"] ## Left Team Logo
        leftLogoAbbr = teamsClass[str(teams[0]).upper()]
        leftLogo = leftTeamLogoGroup.ArtLayers[leftLogoAbbr]
        leftLogo.visible = True


        RightTeamLogoGroup = matchInfoGroup.layerSets["RightTeamLogo"] ## Right Team Logo
        RightLogoAbbr = teamsClass[str(teams[1]).upper()]
        RightLogo = RightTeamLogoGroup.ArtLayers[RightLogoAbbr]
        RightLogo.visible = True

        ## Pop used from lists
        tiers.pop(0)
        confs.pop(0)
        castersList.pop(0)
        castersList.pop(0)
        teams.pop(0)
        teams.pop(0)
        if loopCount == 0:
            pngCasterDesk = (os.path.join(__location__, 'Outputs/CasterDesk.png'))
        if loopCount == 1:
            pngCasterDesk = (os.path.join(__location__, 'Outputs/CasterDesk2.png'))  
        if loopCount == 2:
            pngCasterDesk = (os.path.join(__location__, 'Outputs/CasterDesk3.png'))     
        doc.Export(ExportIn=pngCasterDesk, ExportAs=2, Options=options)
        doc.Close(2)
        print("Caster Screen " + str(loopCount+1) + " Saved")

        loopCount +=1

    print(str(numGames) + " Caster Sreens Edited")


editDesk(int(numGames))