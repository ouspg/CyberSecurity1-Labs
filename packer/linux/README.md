# VM Generation

This repo utilizes packer to build a virtual machine image of the labs which is then exported as OVA which can be imported into hypervisors.

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
