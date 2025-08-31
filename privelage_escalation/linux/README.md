# Linux Privelage Escalation

This is the lab for the Linux Privelage Escalation module.

## Challenge Setup

The labs challenges are setup on different levels. Each level has seperate configurations that are required

{include lab architecture here}

The lab invovles 2 systems that need to be exploited.

## User Creation

For the challenges, following users are created.

|User|System|Groups|
|:--:|:--:|:--:|
|`dev_arni`|`system1`||
|`devops_venla`|`system1, system2`|`usergroup1`|
|`jenkins_agent`|`system2`|`usergroup1, usergroup2`|
|`admin_anna`|`system2`|`usergroup2`|

### Leve 1 - SUID

User `dev_aarni` and `devops_venla` are created and given SUID access to `base64` binary in `Dockerfile-system1`.

### Level 2 - PATH

A `tns_runner` binary is placed by compiling `scripts/vulnerable.c` in `Dockerfile-system2`. The binary is run with user `jenkins_agent` privelages and placed in user `devops_venla` home directory and given execute permissions.

The binary simply tries to run another binary `thm` with user `jenkins_agent` privelages.

### Level 3 - Cron

`admin_anna` user sets up a cron job that runs a script placed under user `jenkins_agent` home directory and this user is given read write permissions on the cron script.

During image build, the crontab is copied from `configs/crontab` which is configured to run the script `scripts/cron.sh` which is just a dummy script.

### Level 4 - SUDO

The `admin_anna` user is given sudo access on certain binaries.

During image build the `sudoers` file is copied from `configs/sudoers`.
