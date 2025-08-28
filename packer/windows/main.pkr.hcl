packer {
  required_plugins {
    vmware = {
      version = "~> 1"
      source  = "github.com/hashicorp/vmware"
    }
  }
}

source "vmware-iso" "winsrv" {

}

build {
    sources = ["source.vmware-iso.winsrv"]
}