import xbmc, xbmcgui, xbmcaddon

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")
import common

FAVORITES = os.path.join(user_dataDir, 'favorites.txt')
if not (os.path.isfile(FAVORITES)):
    common.WriteList(FAV, 'Hello-World')
xbmcgui.Dialog().ok(title, 'Hello', 'World', 'Azael')



