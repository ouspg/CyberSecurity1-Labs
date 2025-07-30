packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source  = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware-iso" "ubuntusrv22" {

  # ISO configurations
  iso_url      = "${var.iso_url}"
  iso_checksum = "${var.iso_checksum}"

  # Hardware configurations

  # Run Confgurations
  headless = "${var.headless}"
  # Shutdown configurations
  shutdown_command = "${var.shutdown_command}"

  # Boot Configurations
  boot_command = "${var.boot_command}"
  boot_wait    = "${var.boot_wait}"

  # Communucator configurations
  communicator = "ssh"
  ssh_username = "${var.ssh_username}"
  ssh_password = "${var.ssh_password}"
}

build {
  sources = ["source.vmware-iso.ubuntusrv22"]

  provisioner "shell" {
    inline = [
      "whoami"
    ]
  }
}