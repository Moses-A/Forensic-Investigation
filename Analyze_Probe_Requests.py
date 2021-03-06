#!/usr/bin/python
# Written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"

from scapy.all import *
import optparse

probeReqs = []
count = 0

def SniffLocation(p):
global count
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
	if netName not in probeReqs:
	    probeReqs.append(netName)
	    count = count + 1
	    print '\t ', count, ' Detection of WiFi Location: ' + netName


def main():
    parser = optparse.OptionParser("Usages From Program: -I <Interface>")
    parser.add_option('-I', dest='interface', type='string', help='Specify Interface Type', default='mon0')
    (options, args) = parser.parse_args()
    interface = options.interface
    if options.interface == None:
        print parser.usage
	exit(0)
    if not os.geteuid() == 0:
	sys.exit('\t Please Run As Root!!')		# Checks to see if the user is root, THIS CODE NEEDS UID 0     
    os.system('sudo airmon-ng start wlan0')		# Interacts with terminal to put the wireless NIC in monitor mode.
    print " \t The Sniffing Has Begun... Please Wait... \n\n"
    sniff(iface=interface, prn=SniffLocation)


if __name__ == '__main__':
    main()
