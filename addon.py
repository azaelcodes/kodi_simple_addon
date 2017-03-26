import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")

# List example
addonHandle = int(sys.argv[1])
li = xbmcgui.ListItem(user_dataDir, iconImage='none.png')
xbmcplugin.addDirectory(handle=addonHandle, 'url:url//', listitem=li)

xbmcplugin.endOfDirectory(addonHandle)