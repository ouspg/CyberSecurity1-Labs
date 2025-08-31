# VM Generation

This repo utilizes packer to build a virtual machine image of the labs which is then exported as OVA which can be imported into hypervisors.

1. [Layout](#directory-layout)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Configurations](#configurations)

## Directory Layout

The packer configurations and scripts are explained as below:

|File|Description|
|:--:|:--:|
|`main.pkr.hcl`|This is the main packer file that includes all the steps for building and proviosing the VM|
|`vars.pkr.hcl`|This file includes stores variables that are referenced in `main.pkr.hcl`|
|`http/user-data`|User data file used for unattened and automated installation for linux|
|`scripts/setup.sh`|Proviosnary script that installs required dependencies, creates directories etc.|
|`scripts/firstboot.sh`|Script that is run during the first boot of the VM by the students. This generates the dynamic flags and starts the lab services|
|`configs/firstboot.service`|Service configuration file for `firstboot.sh` script|

## Dependencies

You need to have packer installed on the system. Packer can be installed from the HashiCorp website.
The packer script also utlizes the `vmware` plugin to build and provision the virtual machines, so you also need to have vmware workstation installed aswell.

## Setup

> You will need to first configure the individual labs before running `packer build .`. Please refer to the documentation of the individual labs.

To create the lab, first go the the packer directory:

```bash
cd CyberSecruity1/packer/linux
```

Install the required packer plugins:

```bash
packer init .
```

Set the `ssh_password` used by packer reference in `vars.pkr.hcl`. The password needs to be set as an environment variable. Please also see [SSH Password](#ssh-password)

```bash
export SSH_PASSWORD=<some_ssh_password>
```

Set the secret key in `scripts/firstboot.sh`. See [Secret Key](#secret-key)

Finally build and provion the image. After proviosiong is done, it will export the image as `packer-{source_name}.ova` under `output-<source_name>.ova` This image can be distrubuted to the students which they can import into their own systems.

```bash
packer build .
```

## Configurations

### SSH Password

Before running the packer build, you need to specify the password for the user account that packer will use to communicate with the vm during proviosing. By default, a `ubuntu` account is created during the autoinstall, specified under `http/user-data`, and the same account is used by packer via ssh, specified in `vars.pkr.hcl`.

If you wish to update the account name and password, update the `username` field in `http/user-data` and also the `ssh_username` variable in `vars.pkr.hcl`.

To provide the updated password to packer, you need to provide it as an environment variable:

```bash
export SSH_PASSWORD=<your_ssh_password>
```

To update the password in `user-data`, you need to provide the hashed password. The hash can be created as:

```bash
mkpasswd --method=SHA-512 --rounds=4096 "<my_password>"
```

### Secret Key

The `scripts/firstboot.sh` script exports a secret key which is used by the flag generator and OWASP Juice Shop during VM setup to create dynamic flags. You need to provide this key before building the VM with packer. Also refer to [Flag Generation](flag_generator/app/README.md) to learn more.
