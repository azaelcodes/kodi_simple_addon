import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")

# Data Directory
list_item = xbmcgui.ListItem(label=user_dataDir)
xbmcplugin.addDirectoryItem(_handle, url, list_item, false)
xbmcplugin.endOfDirectory(_handle)