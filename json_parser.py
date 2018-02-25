import os
import json
import sys
import glob
import logging
import time
from logging.handlers import TimedRotatingFileHandler

prefix = sys.argv[1]
dir = "/srv/runme/" + prefix
PATH = dir + "/proc.txt"

if glob.glob(PATH+"*") != []:
    for f in glob.glob(PATH+"*"):
        os.remove(f)

logging_level = logging.DEBUG
formatter = logging.Formatter()
handler = logging.handlers.TimedRotatingFileHandler(PATH, when="M", interval=2, backupCount=10)
handler.setFormatter(formatter)
logger = logging.getLogger("Rotating Log")
logger.addHandler(handler)
logger.setLevel(logging_level)

name_age = []
files = [filename for filename in glob.glob(dir + "/*") if 'Raw.txt' in filename]
for filename in files:
    with open(filename, 'r') as f:
        try:
            file = f.readlines()
        except:
            print('Bad input!!')

    for line in file:
        try:
            j_line = json.loads(line)
            name = j_line['name']
            age = j_line['prop']['age']
            if (age > 0):
                logger.debug(name + "\t" + str(age))
        except:
            pass
