import xbmc, xbmcgui, xbmcaddon

addon = xbmcaddon.Addon('plugin.video.abctest')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
link = 'http://topiptv.net:5890/live/atoz/atoz/3320.ts'

li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={ "Title": title })
li.setProperty('isPlayable', 'true')
xbmc.Player().play(item=link, listitem=li)