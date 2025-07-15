# This script sniffs for network packets

import sys
from scapy.all import *

# Configurations

TARGET_PORT = 4444
TARGET_USER_AGENT = b"Mozilla/5.0 (iPad; CPU OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1"
INTERFACE = "eth0"
FLAG = "FLAG{meterpreter_http_detected}"

def packet_callback(packet):
    pass

def packet_filter(packet):
    pass

def main():
    pass

if __name__ == "__main__":
    pass
