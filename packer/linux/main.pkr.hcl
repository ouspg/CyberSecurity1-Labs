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

  # copy all the necessary files and scripts to the machine
  # some files are moved to /tmp because packer doesnt have permision to copy
  # files in restricted directories. These files will be later moved to their correct
  # locations during proviosing with `setup.sh`
  # https://developer.hashicorp.com/packer/docs/provisioners/file
  provisioner "file" {
    source      = "./configs/firstboot.service"
    destination = "/tmp/firstboot.service"
  }
  provisioner "file" {
    source      = "./scripts/firstboot.sh"
    destination = "/tmp/firstboot.sh"
  }

  # copying the file generator application
  provisioner "file" {
    source      = "../../flag_generator/"
    destination = "/tmp"
  }

  # copying the modified juice shop image
  provisioner "file" {
    source      = "../../web/juice-shop.tar"
    destination = "/tmp/juice_shop.tar"
  }

  # proviosing with the setup script
  provisioner "shell" {
    execute_command = "echo '${var.ssh_password}' | sudo -S env {{ .Vars }} {{ .Path }}"
    scripts = [
      "./scripts/setup.sh"
    ]
  }

  # copying all lab content to the VM
  provisioner "file" {
    source      = "../../vuln-research/"
    destination = "/labs/vuln_research"
  }
  provisioner "file" {
    source      = "../../metasploit/"
    destination = "/labs/metasploit"
  }
  provisioner "file" {
    source      = "../../privelage_escalation/linux/"
    destination = "/labs/priv_esc"
  }
  provisioner "file" {
    source      = "../../web/"
    destination = "/labs/web"
  }
}