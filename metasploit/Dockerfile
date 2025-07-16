FROM python:3.5.10-slim-stretch
COPY <<EOF /etc/apt/sources.list
deb [trusted=yes] http://archive.debian.org/debian stretch main contrib non-free
deb [trusted=yes] http://archive.debian.org/debian-security stretch/updates main contrib non-free
EOF
RUN apt update && apt install binutils -y
WORKDIR /src
ADD sniffer ./
RUN pip3 install scapy pyinstaller
RUN pyinstaller cli.py

FROM vulhub/libssh:0.8.1
COPY --from=0 /src/dist /var/opt/mon/
COPY entrypoint.sh /usr/src/build/examples
RUN chmod +x /usr/src/build/examples/entrypoint.sh
CMD ["/usr/src/build/examples/entrypoint.sh"]
