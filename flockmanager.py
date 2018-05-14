import os.path
import signal

import flockkiller
import flockdefs
import flocklogger 


flogger = flocklogger.flocklogger
killer = flockkiller.flockKiller()

def killme():
    return killer.killme

def registerflock():
    flogger (str(os.getpid()))
    file(flockdefs.pidfile, 'w').write(str(os.getpid()))

def amirunning():
    if os.path.isfile(flockdefs.pidfile):
        flogger ("I'm running, we don't need two of us, exiting...")
        flogger ("If you think I'm not running, please check proc and " + flockdefs.pidfile)
        return True
    registerflock()
    return False

def byebye():
    flogger ("Time to go home. See you soon")
    os.unlink(flockdefs.pidfile)