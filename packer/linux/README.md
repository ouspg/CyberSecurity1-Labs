# VM Generation

This repo utilizes packer to build a virtual machine image of the labs which is then exported as OVA which can be imported into hypervisors.

1. [Layout](#layout)
2. [Dependencies](#dependencies)
3. [Setup](#setup)

## Layout

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

To create the lab, first go the the packer directory:

```bash
cd CyberSecruity1/packer/linux
```

Install the required packer plugins:

```bash
packer init .
```

Finally build and provion the image. After proviosiong is done, it will export the image as `packer-{source_name}.ova` This image can be distrubuted to the students which they can import into their own systems.

```bash
packer build .
```



