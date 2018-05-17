# flock inventory
# v0.0 14-05-18 master@owlh.net

import flockdefs
import json
import flocklogger 
import flockmonitor

flogger = flocklogger.flocklogger


def loadinventory():
    with open(flockdefs.inventory) as json_data:
        owlhs = json.load(json_data)
    return owlhs

def printinventory(owlhs):
    for owlh in owlhs: 
        print owlh["name"]

def run():
    owls = loadinventory()
    for owl in owls: 
        flogger("checks for owl name -> %s, owl ip -> %s" % (owl["name"], owl["ip"]))
        alive, ssh = flockmonitor.check_owl_alive(owl)
        if alive:
            running, status_ok = get_status_sniffer(owl,ssh)
            if running:
                if not status_ok:
                    flockmonitor.stop_sniffer(owl,ssh)
            elif status_ok:
                flockmonitor.run_sniffer(owl,ssh)
            flockmonitor.get_file_list(owl, ssh)
        ssh.close()


