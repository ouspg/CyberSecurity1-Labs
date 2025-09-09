# Packer Templates

This directory contains Packer templates and supporting files for building Linux and Windows virtual machine images used in lab environments.

---

## Directory Structure

```bash
packer/
├── linux/
│   ├── main.pkr.hcl           # Main Packer template for Linux
│   ├── vars.pkr.hcl           # Variable definitions for Linux builds
│   ├── README.md              # Linux image build instructions
│   ├── configs/
│   │   ├── firstboot.service  # Systemd service for first boot tasks.
│   ├── http/
│   │   ├── meta-data          # Cloud-init meta-data
│   │   └── user-data          # Cloud-init user-data
|   ├── output-ubuntusrv22/
|   │   └── packer-ubuntusrv22.ova  # Output Ubuntu Server OVA image
|   ├── packer_cache/          # Packer cache (ISOs, etc.)
|   │   ├── *.iso
|   │   ├── *.iso.lock
|   │   └── port/              # Port files used during builds
│   └── scripts/
│       ├── firstboot.sh       # Script executed on first boot
│       └── setup.sh           # Setup script for provisioning

```

---

## Dependencies

1. **Packer:**
    Packer is used for building and proviosing the VM's. Can be installed from HashiCorp website
2. **VMWare Workstation:**
    The packer template also utlizes the `vmware` plugin to build and provision the virtual machines, so you also need to have vmware workstation installed aswell.
3. **OVF Tools:** The ovftools is used by packer to export the VM in ova format   for easy distribution. The tools can be installed from [here](https://developer.broadcom.com/tools/open-virtualization-format-ovf-tool/latest). You may need to add this to PATH, once installed.

---

## Usage

### Linux Image Build

> You may need to first configure the individual labs before running `packer build .`. Please refer to the documentation of the individual labs.

1. **Change Working Directory:**
    Change you working direcrtory:

    ```bash
    cd CyberSecruity1/packer/linux
    ```

1. **Configure Variables:**  
   Edit `linux/vars.pkr.hcl` to set build-specific variables (e.g., SSH username, passwords, etc.).
    Set the `ssh_password` used by packer reference in `vars.pkr.hcl`. The password needs to be set as an environment variable. Please also see [SSH Password](#ssh-password)

    ```bash
    export SSH_PASSWORD=<some_ssh_password>
    ```

1. **Configure Secret Key:**
    Set the secret key in `scripts/firstboot.sh`. See [Secret Key](#secret-key)

1. **Build the Image:**  
   Run the following commands from the `packer/linux/` directory:

   ```sh
   packer init .
   packer build .
   ```

   After proviosiong is done, it will export the image as `packer-{source_name}.ova` under `output-<source_name>.ova` and also create a `.vmx` that can be used to configure the vm in vmware workstation. This image can be distrubuted to the students which they can import into their own systems.

1. **Customization:**  
   - Cloud-init files are in `http/`.
   - Custom scripts and systemd services are in `scripts/` and `configs/`.

---

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

The `scripts/firstboot.sh` script exports a secret key which is used by the flag generator and OWASP Juice Shop during VM setup to create dynamic flags. You need to provide this key before building the VM with packer. Also refer to [Flag Generation](../../flag_generator/app/README.md) to learn more.

---

## Notes

- **Cloud-init:**  
  The Linux build uses cloud-init for initial configuration under `http/user-data` and `http/meta-data`.

- **Scripts:**  
  Place any provisioning or setup scripts in the appropriate `scripts/` directory.

- **Cache:**  
  The `packer_cache/` directory is used by Packer to store downloaded ISOs and other resources. You can safely delete this directory to reclaim space, but Packer will re-download resources as needed.
