FROM ubuntu:focal

# install programs
RUN apt-get update && apt-get install -y \
    vim \
    openssh-server \
    sudo

# Create users
RUN useradd -m -s /bin/bash user1 && \
    echo "user1:password" | chpasswd

# Configure users
COPY sudoers /etc/sudoers

# Configure the programs
RUN mkdir /var/run/sshd

# Setup flags
RUN echo "Flag3" > /root/flag3.txt


CMD ["/usr/sbin/sshd", "-D"]