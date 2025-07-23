FROM ubuntu:focal

# install programs
RUN apt-get update && apt-get install -y \
    vim \
    openssh-server \
    sudo \
    cron 

# Create users
RUN useradd -m -s /bin/bash user1 && \
    echo "user1:password" | chpasswd

RUN useradd -m -s /bin/bash user2 && \
    echo "user2:password" | chpasswd

RUN useradd -m -s /bin/bash user3 && \
    echo "user3:password" | chpasswd

COPY script.sh /home/user2/script.sh
RUN touch /home/user2/cron.log && \
    chown user3:user3 /home/user2/cron.log && \
    chmod 644 /home/user2/cron.log
RUN  chown user3:user3 /home/user2/script.sh && \
    chmod 766 /home/user2/script.sh && \
    echo "* * * * * user3 /home/user2/script.sh" >> /etc/crontab
# Configure users
COPY sudoers /etc/sudoers
RUN chmod 440 /etc/sudoers

# Configure the programs
RUN mkdir /var/run/sshd
RUN chmod u+s /usr/bin/base64

# Setup flags
RUN echo "Flag2" > /home/user3/flag2.txt && \
    chown user3:user3 /home/user3/flag2.txt && \
    chmod 640 /home/user3/flag2.txt
RUN echo "Flag3" > /root/flag3.txt


COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 744 /usr/local/bin/entrypoint.sh


CMD ["/usr/local/bin/entrypoint.sh"]