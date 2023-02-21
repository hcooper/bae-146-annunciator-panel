import logging, logging.handlers
from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
from time import sleep
from queue import Queue
import os

def setupLogging(logFileName):
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    fileHandler = logging.handlers.RotatingFileHandler(logFileName, maxBytes=500000, backupCount=7)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

# MAIN
# setupLogging("SimConnectMobiFlight.log")
q = Queue(maxsize=100)
sm = SimConnectMobiFlight()
vr = MobiFlightVariableRequests(sm, q)
vr.clear_sim_variables()

VARS = {
    "(L:L_ANNUNS_WhiteBars_il)",
    "(L:L_ANNUNS_Splr_Y_il)",
    "(L:L_ANNUNS_Splr_G_il)",
    "(L:L_ANNUNS_AirBrk_il)",
    "(L:L_ANNUNS_YD_amber_il)",
    "(L:L_ANNUNS_AP_il)",
    "(L:L_ANNUNS_Pitch_il)",
    "(L:L_ANNUNS_Roll_green_il)",
    "(L:L_ANNUNS_GSL_white_il)",
    "(L:L_ANNUNS_GSL_green_il)",
    "(L:L_ANNUNS_ALT_white_il)",
    "(L:L_ANNUNS_ALT_green_il)",
    "(L:L_ANNUNS_LOC_white_il)",
    "(L:L_ANNUNS_LOC_green_il)",
    "(L:L_ANNUNS_Vor_white_il)",
    "(L:L_ANNUNS_Vor_green_il)",
    "(L:L_ANNUNS_Rnav_green_il)",
    "(L:L_ANNUNS_BckLoc_white_il)",
    "(L:L_ANNUNS_BckLoc_green_il)",
    "(L:L_ANNUNS_Hdg_green_il)",
    "(L:L_ANNUNS_Mach_il)",
    "(L:L_ANNUNS_IAS_il)",
    "(L:L_ANNUNS_Outer_il)",
    "(L:L_ANNUNS_Lnav_green_il)",
}

status={}

def print_status():
    os.system('cls')
    for k,v in status.items():
        if v:
            print(k,v)

for var in VARS:
    vr.get(var)
    status[var] = False

while True:
    while not q.empty():
        event = q.get()
        status[event.name] = event.float_value
        print_status()

    sleep(.1)