from flask import Flask
import logging
import time
import sys 
import os
import shutil
from logging.handlers import TimedRotatingFileHandler


app = Flask(__name__)

#/srv/runme/prefix/Raw.txt




def create_timed_rotating_log(PATH, json_txt):
    """
    
    """
 
    logger.info(json_txt)



@app.route("/<json_txt>")
def store_json(json_txt):
    """

    """
    json_txt = json_txt.replace('\n', '')
    
    create_timed_rotating_log(PATH, json_txt)

    return "Thanks for visiting!"
    
# initialization
prefix = sys.argv[1]
PATH = "/srv/runme/" + prefix + "/Raw.txt"

print PATH

if(os.path.exists("/srv/runme/" + prefix)):
    shutil.rmtree("/srv/runme/" + prefix)
os.mkdir("/srv/runme/" + prefix)

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
     
handler = TimedRotatingFileHandler(PATH,
                                    when="m",
                                    interval=2,
                                    backupCount=5)
logger.addHandler(handler)

app.run(host='0.0.0.0', port=8080)
