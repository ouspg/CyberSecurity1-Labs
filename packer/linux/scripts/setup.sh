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

# Setup directories for labs
mkdir -p /labs/vuln_research /labs/metasploit /labs/priv_esc

sudo chown -R ubuntu:ubuntu /labs