# Cybersecurity 1 Course Labs

This repo contains the labs for the Cybersecurity 1 Ethical Hacking course.

## Lab Content

The labs are diveded into different categories. Each lab configuration is present under their own directory.

|Lab|Path|
|:--:|:--:|
|Web Hacking|`web`|
|Burp Suite|`burp-suite`|
|Network Security|`netsec`|
|Vulnerability Research|`vuln-research`|
|Metasploit|`metasploit`|
|Privelage Esacalation (Linux)|`privelage-escalation`|

## Setup

The labs are setup using packer which creates an OVA image that can be imported into hypervisors. The configuration scripts are present under `packer/linux`. Please refer to {packer readnme here} for setup details

## Flag Generation

The labs utilized a flag generator application to create dynamic flags for students that are then injected into the labs. For usage guide and configurations, refer to [Flag Generation](flag_generator/app/README.md).
