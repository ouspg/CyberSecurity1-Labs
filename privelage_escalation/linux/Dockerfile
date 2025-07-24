FROM gcc:11 AS builder
WORKDIR /src
COPY vulnerable.c ./
RUN gcc vulnerable.c -o vuln_bin -w

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

RUN useradd -m -s /bin/bash user4 && \
    echo "user4:password" | chpasswd

COPY script.sh /home/user3/script.sh
RUN touch /home/user3/cron.log && \
    chown user4:user4 /home/user3/cron.log && \
    chmod 644 /home/user3/cron.log
RUN  chown user4:user4 /home/user3/script.sh && \
    chmod 766 /home/user3/script.sh && \
    echo "* * * * * user4 /home/user3/script.sh" >> /etc/crontab

# Configure users
COPY sudoers /etc/sudoers
RUN chmod 440 /etc/sudoers

# Configure the programs
RUN mkdir /var/run/sshd
RUN chmod u+s /usr/bin/base64
COPY --from=builder /src/vuln_bin /home/user3/vuln_bin
RUN chown root:root /home/user3/vuln_bin && \
    chmod 4755 /home/user3/vuln_bin
RUN ln -s /home/user3/vuln_bin /home/user2/vuln_bin

# Setup flags
RUN echo "Flag2" > /home/user3/flag2.txt && \
    chown user3:user3 /home/user3/flag2.txt && \
    chmod 640 /home/user3/flag2.txt
RUN echo "Flag3" > /home/user4/flag3.txt && \
    chown user4:user4 /home/user4/flag3.txt && \
    chmod 640 /home/user4/flag3.txt
RUN echo "Flag4" > /root/flag4.txt


COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 744 /usr/local/bin/entrypoint.sh


CMD ["/usr/local/bin/entrypoint.sh"]