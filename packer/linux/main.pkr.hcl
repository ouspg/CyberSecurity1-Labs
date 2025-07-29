packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware-iso" "ubuntusrv22" {
    "iso_url" = "${var.iso_url}"
    "iso_checksum" = "${var.iso_checksum}"
    # "iso_checksum_type" = "${var.iso_checksum_type}"
}

build {
    sources = ["source.vmware-iso.ubuntusrv22"]
    provisioner "shell" {
        inline = [
            "whoami"
        ]
    }
}