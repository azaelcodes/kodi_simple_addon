import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")

# Data Directory
list_item = xbmcgui.ListItem(label=user_dataDir)