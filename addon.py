import sys
import xml.etree.ElementTree as ET
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

addon = xbmcaddon.Addon('plugin.video.azaelcodesfavs')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
favorites = xbmc.translatePath('special://userdata/favourites.xml')
tree = ET.parse(favorites)
root = tree.getroot()

for favorite in root.findall('favorite'):
    list_item = xbmcgui.ListItem(label=favorite.get('name'))
    xbmcplugin.addDirectoryItem(_handle, _url, list_item, False)
xbmcplugin.endOfDirectory(_handle)