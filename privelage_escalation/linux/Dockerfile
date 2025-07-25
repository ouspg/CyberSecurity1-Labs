FROM gcc:11 AS builder
WORKDIR /src
COPY ./scripts/vulnerable.c ./
RUN gcc vulnerable.c -o tns_runner -w

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


# Creating realistic directories
RUN mkdir -p /opt/scripts \
    /var/backups \
    /srv/jenkins \
    /opt/legacy_tools \
    /mnt/shared/reports \
    /home/shared_configs

RUN echo "#!/bin/bash\n# nightly security scan" > /opt/scripts/security_scan.sh && \
    echo "#!/bin/bash\necho 'rotating logs...'" > /opt/scripts/log_rotate.sh && \
    chmod 740 /opt/scripts/security_scan.sh /opt/scripts/log_rotate.sh

# Clean up apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure the programs
RUN mkdir /var/run/sshd

# Create users and groups
RUN groupadd -g 1004 usergroup1 && \
    groupadd -g 1005 usergroup2

RUN useradd -m -s /bin/bash dev_aarni && \
    echo "dev_aarni:password" | chpasswd && \
    chmod 771 /home/dev_aarni

RUN useradd -m -s /bin/bash devops_venla && \
    echo "devops_venla:password" | chpasswd && \
    usermod -aG usergroup1 devops_venla && \
    chmod 771 /home/devops_venla

RUN useradd -m -s /bin/bash jenkins_agent && \
    echo "jenkins_agent:password" | chpasswd && \
    usermod -aG usergroup1 jenkins_agent && \
    usermod -aG usergroup2 jenkins_agent && \
    chmod 771 /home/jenkins_agent

RUN useradd -m -s /bin/bash admin_anna && \
    echo "admin_anna:password" | chpasswd && \
    usermod -aG usergroup2 admin_anna && \
    chmod 771 /home/admin_anna

# Configuring Level 1 - SUID
RUN chmod u+s /usr/bin/base64

# Configuring Level 2 - PATH
COPY --from=builder /src/tns_runner /home/jenkins_agent/tns_runner
RUN chown root:usergroup1 /home/jenkins_agent/tns_runner && \
    chmod 4750 /home/jenkins_agent/tns_runner
RUN ln -s /home/jenkins_agent/tns_runner /home/devops_venla/tns_runner

# Configuring Level 3 - Cron Job
COPY ./scripts/cron.sh /home/jenkins_agent/build.sh
RUN chown admin_anna:usergroup2 /home/jenkins_agent/build.sh && \
    chmod 760 /home/jenkins_agent/build.sh
RUN echo "Pipeline build failed." > /home/jenkins_agent/build_log.txt && \
    chown jenkins_agent:usergroup2 /home/jenkins_agent/build_log.txt && \
    chmod 640 /home/jenkins_agent/build_log.txt
COPY ./configs/crontab /etc/crontab
RUN chmod 644 /etc/crontab

# Configuring Level 4 - SUDO
COPY ./configs/sudoers /etc/sudoers
RUN chmod 440 /etc/sudoers

# Setup dummy flags
RUN echo "Flag1" > /home/devops_venla/flag1.txt && \
    chown devops_venla:devops_venla /home/devops_venla/flag1.txt && \
    chmod 640 /home/devops_venla/flag1.txt
RUN echo "Flag2" > /home/jenkins_agent/flag2.txt && \
    chown jenkins_agent:jenkins_agent /home/jenkins_agent/flag2.txt && \
    chmod 640 /home/jenkins_agent/flag2.txt
RUN echo "Flag3" > /home/admin_anna/flag3.txt && \
    chown admin_anna:admin_anna /home/admin_anna/flag3.txt && \
    chmod 640 /home/admin_anna/flag3.txt
RUN echo "Flag4" > /root/flag4.txt

# Copying entrypoint script
COPY ./scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 770 /usr/local/bin/entrypoint.sh


CMD ["/usr/local/bin/entrypoint.sh"]