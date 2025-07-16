#!/bin/bash

/var/opt/mon/cli/cli &

/usr/src/build/examples/ssh_server_fork \
    --hostkey=/etc/ssh/ssh_host_rsa_key \
    --ecdsakey=/etc/ssh/ssh_host_ecdsa_key \
    --dsakey=/etc/ssh/ssh_host_dsa_key \
    --rsakey=/etc/ssh/ssh_host_rsa_key \
    -p 22 0.0.0.0


