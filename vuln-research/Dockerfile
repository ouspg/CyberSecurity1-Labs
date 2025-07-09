FROM vulhub/mysql:5.5.23

ADD my.cnf /etc/mysql/my.cnf

ADD init.sql /tmp/init.sql

RUN service mysql start && mysql -u root -p123456 < /tmp/init.sql
