
###########################################################
#                                                         #
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html) #
#                                                         #
# info: you must host message.xml and add its address to  #
# message_xml_url below, you can write your news in the   #
# xml and it will show when called by this                #
#                                                         #
##################Author:Les][smor#########################

import os           
import urlparse     
import xbmc         
import xbmcaddon   
import xbmcgui      
import xbmcplugin   
import koding
from koding import Download 
from koding import route, Run 
addon_id = xbmcaddon.Addon().getAddonInfo('id')
ownAddon = xbmcaddon.Addon(id=addon_id)

message_xml_url = "http://kodihelp.net/other/message.xml"

@route(mode="dialog_example")
def Dialog_Example():
    
    koding_test = message_xml_url
    mytext = koding.Text_File(path=koding_test, mode='r')
    
    main_text = mytext
    my_buttons = ['Close', 'Watch Tutorial']
    my_choice = koding.Custom_Dialog(main_content=main_text,pos='center',size='900x600',buttons=my_buttons,transparency=90,highlight_color='gold',header='UPDATES AND INSTRUCTIONS')
    if my_choice ==0: 
        ownAddon.setSetting('firstrun',value="false")
    elif my_choice ==1:
        xbmc.Player().play('http://c4nv4s.co.uk/canvas/files/tut.mp4')