FROM gcc:11 AS builder
WORKDIR /src
COPY ./scripts/vulnerable.c ./
RUN gcc vulnerable.c -o vuln_bin -w

FROM ubuntu:focal

# install programs
RUN apt-get update && apt-get install -y \
    vim \
    nano \
    openssh-server \
    sudo \
    cron \
    less

# Clean up apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure the programs
RUN mkdir /var/run/sshd

# Create users and groups
RUN groupadd -g 1004 usergroup1 && \
    groupadd -g 1005 usergroup2

RUN useradd -m -s /bin/bash user1 && \
    echo "user1:password" | chpasswd && \
    chmod 771 /home/user1

RUN useradd -m -s /bin/bash user2 && \
    echo "user2:password" | chpasswd && \
    usermod -aG usergroup1 user2 && \
    chmod 771 /home/user2

RUN useradd -m -s /bin/bash user3 && \
    echo "user3:password" | chpasswd && \
    usermod -aG usergroup1 user3 && \
    usermod -aG usergroup2 user3 && \
    chmod 771 /home/user3

RUN useradd -m -s /bin/bash user4 && \
    echo "user4:password" | chpasswd && \
    usermod -aG usergroup2 user4 && \
    chmod 771 /home/user4

# Configuring Level 1 - SUID
RUN chmod u+s /usr/bin/base64

# Configuring Level 2 - PATH
COPY --from=builder /src/vuln_bin /home/user3/vuln_bin
RUN chown root:root /home/user3/vuln_bin && \
    chmod 4755 /home/user3/vuln_bin
RUN ln -s /home/user3/vuln_bin /home/user2/vuln_bin

# Configuring Level 3 - Cron Job
# TODO: cron script should only be writable by owner and group.
COPY ./scripts/cron.sh /home/user3/backup.sh
RUN  chown user4:usergroup2 /home/user3/backup.sh && \
    chmod 760 /home/user3/backup.sh
COPY ./configs/crontab /etc/crontab

# Configuring Level 4 - SUDO
COPY ./configs/sudoers /etc/sudoers
RUN chmod 440 /etc/sudoers

# Setup dummy flags
RUN echo "Flag1" > /home/user2/flag1.txt && \
    chown user2:user2 /home/user2/flag1.txt && \
    chmod 640 /home/user2/flag1.txt
RUN echo "Flag2" > /home/user3/flag2.txt && \
    chown user3:user3 /home/user3/flag2.txt && \
    chmod 640 /home/user3/flag2.txt
RUN echo "Flag3" > /home/user4/flag3.txt && \
    chown user4:user4 /home/user4/flag3.txt && \
    chmod 640 /home/user4/flag3.txt
RUN echo "Flag4" > /root/flag4.txt

# Copying entrypoint script
COPY ./scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 770 /usr/local/bin/entrypoint.sh


CMD ["/usr/local/bin/entrypoint.sh"]