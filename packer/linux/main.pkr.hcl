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
  cpus      = 2
  memory    = 2048
  disk_size = 30720
  network   = "nat"

  # Run Confgurations
  headless = "${var.headless}"

  # Shutdown configurations
  shutdown_command = "echo '${var.ssh_password}' | sudo -S -E shutdown -P now"

  # Boot Configurations
  boot_command = "${var.boot_command}"
  boot_wait    = "${var.boot_wait}"

  # Communucator configurations
  communicator = "ssh"
  ssh_username = "${var.ssh_username}"
  ssh_password = "${var.ssh_password}"
  ssh_timeout  = "30m"

  # HTTP directory configuration
  http_directory = "http"

  # Export configurations
  format = "ova"
}

build {
  sources = ["source.vmware-iso.ubuntusrv22"]

  provisioner "file" {
    source = "../../vuln-research/"
    destination = "/labs/vuln_research"
  }
  provisioner "file" {
    source = "../../metasploit/"
    destination = "/labs/metasploit"
  }
  provisioner "file" {
    source = "../../privelege_escalation/linux/"
    destination = "/labs/priv_esc"
  }
}