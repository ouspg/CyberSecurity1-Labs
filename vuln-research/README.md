# Vulnerability Research

This is the Vulnerability Research module for the course labs.

This lab extends a vulnerable MySQL service from [vulhub](https://github.com/vulhub/vulhub/tree/master/mysql/CVE-2012-2122).

## Configuration

Two configuration files are provided:

`init.sql`: Initialization script to create a fake database for students

`my.cnf`: Server confgirutation file.

You can update the root user password in `init.sql`. Besides that it is suggested not to update the rest of the init script or the config file as it may break other components of the lab during setup or when students are exploiting the services.
