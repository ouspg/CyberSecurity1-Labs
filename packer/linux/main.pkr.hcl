packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware" "linuxlab" {

}

build {
    sources = ["source.vmware.linuxlab"]
    provisioner "shell" {
        inline = [
            "whoami"
        ]
    }
}