import time
import pynput.keyboard as k
import keyboard
import threading
import gui
class spam(threading.Thread):
    def __init__(self,startvar):
        super().__init__()
        self.startvar=startvar
        self.maxlinelen=250
        self.end=2000
        self.spammingtoggle=False
        self.destroy=False
    def run(self):
        print('running')
        while True:
            if self.spammingtoggle==True:
                if self.startvar<=self.end:
                    i=0
                    while True:
                        keyboard.press_and_release('ctrl+v')
                        if (i<=self.startvar)==False:
                            break
                        if i<self.maxlinelen:
                            i+=1
                        time.sleep(0.01)
                    keyboard.press_and_release('enter')
                    self.startvar+=1
                    time.sleep(0.01)
                else:
                    break
            if self.destroy==True:
                break
    def spammingstart(self):
        self.spammingtoggle=True
        print('spamming started')
    def spammingstop(self):
        self.spammingtoggle=False
        print('spamming stopped')
spam_thread=spam(0)
spam_thread.start()
gui_thread=gui.GUI()
gui_thread.start()
def on_press(key):
    if key==k.KeyCode(char='s'):
        if spam_thread.spammingtoggle==False:
            spam_thread.spammingstart()
            gui_thread.colourselectionno=1
        else:
            spam_thread.spammingstop()
            gui_thread.colourselectionno=0
        gui_thread.changecol()
    if key==k.KeyCode(char='e'):
        spam_thread.destroy=True
        gui_thread.exit()
        listener.stop()
with k.Listener(on_press=on_press) as listener:
    gui_thread.create()
    listener.join()
