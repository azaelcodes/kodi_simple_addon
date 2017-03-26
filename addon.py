import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")

# Data Directory
xbmcgui.Dialog().ok(addon, 'Title 1', user_dataDir, 'Last one')