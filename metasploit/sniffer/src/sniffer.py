"""
Packet Sniffer for Meterpreter HTTP Detection
This script listens for HTTP requests on a specific port and checks for a User-Agent header
that matches a predefined regex. If a match is found, it writes a flag to a file
and exits the program.
"""

import sys

from scapy.all import *

# Configurations
USER_AGENT_REGEX = rb"Mozilla/5.0.*Gecko/20100101|Mozilla/5.0.*like Gecko"
INTERFACE = "eth0"
FLAG = "FLAG{meterpreter_http_detected}"


def packet_callback(packet: "scapy.packet.Packet") -> None:
    """
    ## Description:
    Callback function for processing captured packets.

    ## Parameters:
    packet (scapy.packet.Packet): The captured packet.

    ## Returns:
    None
    """
    with open("/var/opt/flag2.txt", "w") as f:
        f.write(FLAG)
    sys.exit(0)


def packet_filter(packet: "scapy.packet.Packet") -> bool:
    """
    ## Description:
    Filter function to check if the packet is an HTTP request with the specified User-Agent.

    ## Parameters:
    packet (scapy.packet.Packet): The captured packet.

    ## Returns:
    bool: True if the packet matches the criteria, False otherwise.
    """

    if packet.haslayer(TCP) and packet.haslayer(Raw):
        tcp_layer = packet[TCP]
        raw_data = packet[Raw].load

        # Check if its the required HTTP request
        if b"User-Agent" in raw_data:
            match = re.search(USER_AGENT_REGEX, raw_data)
            return match is not None


def main():
    """
    ## Description:
    Main function to start the packet sniffer.
    """

    sniff(lfilter=packet_filter, prn=packet_callback, iface=INTERFACE)
