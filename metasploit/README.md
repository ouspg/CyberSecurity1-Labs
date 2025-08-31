# Metasploit

This is the lab for the metasploit module. This lab utilizes a vulnerable libssh service from [vulhub](https://github.com/vulhub/vulhub/tree/master/libssh/CVE-2018-10933)

## Sniffer

The lab container image also includes a packet sniffer application as an added challenge layer.

The packet sniffer listens for HTTP trafic to detect a meterpreter rever http session and reveals a flag. This application is built when building the docker image for this lab.
