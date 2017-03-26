import xbmc, xbmcgui, xbmcaddon
import os, io, json

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user_dataDir = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")

def write_list(fileName, list, indent=True):
    try:
        with io.open(fileName, 'w', encoding='utf-8') as handle:
            if indent:
                handle.write(unicode(json.dumps(list, indent=2, ensure_ascii=False)))
            else:
                handle.write(unicode(json.dumps(list, ensure_ascii=False)))
        success = True
    except Exception as ex:
        xbmc.log("{0}".format(ex), 3)
        success = False

    return success


FAVORITES = os.path.join(user_dataDir, 'favorites.txt')
if not (os.path.isfile(FAVORITES)):
    write_list(FAVORITES, 'Hello-World')
xbmcgui.Dialog().ok(title, 'Hello', 'World', 'Azael')



