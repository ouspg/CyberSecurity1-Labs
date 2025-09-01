#!/bin/bash
# This script sets up the lab environment for the Linux Packer build.
# It installs necessary packages and performs initial configurations.

# Installing Docker Engine
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update

apt-get install docker-ce -y docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# installing python
apt-get install -y python3 python3-pip python3-venv
# Setup directories for labs
mkdir -p /labs/vuln_research /labs/metasploit /labs/priv_esc /labs/web /labs/burp_suite

chown -R ubuntu:ubuntu /labs

# setup firstboot service
mv /tmp/firstboot.service /etc/systemd/system/firstboot.service
mv /tmp/firstboot.sh /usr/local/bin/firstboot.sh
chmod +x /usr/local/bin/firstboot.sh
systemctl enable firstboot.service

# setup flag generator
mv /tmp/app/ /usr/lib/python3.12/app
python3 -m venv /opt/venv
source /opt/venv/bin/activate
pip3 install -r /usr/lib/python3.12/app/requirements.txt

# load custom juice shop image
docker image load --input /tmp/juice_shop.tar