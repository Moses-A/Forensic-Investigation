#!/usr/bin/env python2
# written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"

from _winreg import *

def BinaryToMac(val):				# Converts the binary information from the Windows Registry to readable MAC Addresses.
    addr = '';
    for ch in val:
        addr += '%02x '% ord(ch)	# Uses a binary to MAC conversion method, replaces spaces with ":" and returns the finished address
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr			

def PrintNetworks():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged" # The root location of the MAC Addresses
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print '\n\t[Scanning] Wifi Networks Previously Joined\n'
    for i in range(50):					
        try:
            guid = EnumKey(key, i)
        	netKey = OpenKey(key, str(guid))
        	(n, addr, t) = EnumValue(netKey, 5)     # Grabs the MAC Address of each connection
        	(n, name, t) = EnumValue(netKey, 4)     # Grabs the name of each connection
        	(n, dns, t)  = EnumValue(netKey, 3)     # Grabs the DNS server used of each connection
        	MACAddr = BinaryToMac(addr)				# After grabbing the info, sends it to the BinaryToMac function where the conversion occurs
        	netName = str(name)
            DNServer = str(dns)
    	    print '\n\t[Success] ' + netName + ' ' + MACAddr + '\n\t DNS Server : ' + DNServer 
    	    CloseKey(netKey)
        except:
            break

def main():
    PrintNetworks()
	
if __name__ == "__main__":
    main()
	
