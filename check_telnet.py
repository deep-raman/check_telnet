import sys
import os
import argparse
import time
from datetime import date, timedelta, datetime

time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print "%s   Script START " % time

print "--------------------------------------------------------"
parser = argparse.ArgumentParser(description='Author : Raman Deep - Script telnet port check')
parser.add_argument('-host','--host', help='Hostname or IP Address to check',required=True)
parser.add_argument('-port','--port',help='Port number to check', required=True)

args = parser.parse_args()

#### Assign arguments to variables
host = args.host
port = args.port

flag = 0


telnet_command = "sleep 5 | telnet %s %s > /tmp/telnet.out" % (host,port)

telnet = os.system(telnet_command)

file = open('/tmp/telnet.out', 'r')

result = 0
for line in file :
  if "Escape character is" in line:
    result = 1

if result == 1 :
  flag = 0
  output = "OK : Host %s is reachable on port %s." % (host,port)	
else : 
  flag = 2
  output = "CRITICAL : Host %s is unreachable on port %s." % (host,port)

print output
print flag

sys.exit(flag)
