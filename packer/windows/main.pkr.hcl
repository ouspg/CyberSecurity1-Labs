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
  communicator   = "winrm"
  winrm_username = "${var.winrm_username}"
  winrm_password = "${var.winrm_password}"
  winrm_timeout  = "3h"

  # Boot configurations
  boot_command = "${var.boot_command}"
  boot_wait    = "${var.boot_wait}"

  # Shutdown configurations
  shutdown_command = "shutdown /s /t 10 /f /d p:4:1 /c \"Packer Shutdown\""

}

build {
  sources = ["source.vmware-iso.winsrv"]

  provisioner "powershell" {
    inline = [
      "Write-Host 'Hello from inside the Windows Server VM!'"
    ]
  }
}