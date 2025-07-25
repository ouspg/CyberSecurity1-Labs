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
    less \
    python3

# Clean up apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure the programs
RUN mkdir /var/run/sshd

# Create users and groups
RUN groupadd -g 1004 usergroup1 && \
    groupadd -g 1005 usergroup2

RUN useradd -m -s /bin/bash developer && \
    echo "developer:password" | chpasswd && \
    chmod 771 /home/developer

RUN useradd -m -s /bin/bash devops && \
    echo "devops:password" | chpasswd && \
    usermod -aG usergroup1 devops && \
    chmod 771 /home/devops

RUN useradd -m -s /bin/bash automation && \
    echo "automation:password" | chpasswd && \
    usermod -aG usergroup1 automation && \
    usermod -aG usergroup2 automation && \
    chmod 771 /home/automation

RUN useradd -m -s /bin/bash infra_admin && \
    echo "infra_admin:password" | chpasswd && \
    usermod -aG usergroup2 infra_admin && \
    chmod 771 /home/infra_admin

# Configuring Level 1 - SUID
RUN chmod u+s /usr/bin/base64

# Configuring Level 2 - PATH
COPY --from=builder /src/vuln_bin /home/user3/vuln_bin
RUN chown root:usergroup1 /home/user3/vuln_bin && \
    chmod 4750 /home/user3/vuln_bin
RUN ln -s /home/user3/vuln_bin /home/user2/vuln_bin

# Configuring Level 3 - Cron Job
# TODO: cron script should only be writable by owner and group.
COPY ./scripts/cron.sh /home/user3/backup.sh
RUN chown user4:usergroup2 /home/user3/backup.sh && \
    chmod 760 /home/user3/backup.sh
COPY ./configs/crontab /etc/crontab
RUN chmod 640 /etc/crontab

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