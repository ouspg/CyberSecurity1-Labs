packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware-iso" "linuxlab" {

}

build {
    sources = ["source.vmware-iso.linuxlab"]
    provisioner "shell" {
        inline = [
            "whoami"
        ]
    }
}