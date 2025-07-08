FROM vulhub/mysql:5.5.23

ADD init.sql /tmp/init.sql

RUN service mysql start && mysql -u root -p123456 < /tmp/init.sql
