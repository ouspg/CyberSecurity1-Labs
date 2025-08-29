packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source  = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware-iso" "winsrv" {
  # ISO configurations
  iso_url      = "${var.iso_url}"
  iso_checksum = "${var.iso_checksum}"

  # Hardware configurations
  cpus      = "${var.cpu_num}"
  memory    = "${var.mem_size}"
  disk_size = "${var.disk_size}"

# Communucator configurations
  communicator = "winrm"
  winrm_username = "${var.winrm_username}"
  winrm_password = "${var.winrm_password}"
  winrm_timeout  = "3h"

}

build {
  sources = ["source.vmware-iso.winsrv"]
}