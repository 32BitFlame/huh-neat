import winsound
import random
import sys
from time import sleep
import os
os.system("title " + str(random.randint(0,10000)))
sys.argv[0] = str(random.randint(0,10000))
sleep(random.randint(5,30))
winsound.PlaySound('m.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
sleep(30)
