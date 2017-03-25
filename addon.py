import xbmc, xbmcgui, xbmcaddon, common

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')

FAVORITES = os.path.join(user_dataDir, 'favorites.txt')
if not (os.path.isfile(FAVORITES)):
    common.WriteList(FAV, 'Hello-World')


