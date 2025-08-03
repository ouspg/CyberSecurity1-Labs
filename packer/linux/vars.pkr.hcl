variable "iso_url" {
  description = "The URL of the ISO image to use for the build."
  type        = string
  default     = "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso"
}

variable "iso_checksum" {
  description = "The checksum of the ISO image."
  type        = string
  default     = "d6dab0c3a657988501b4bd76f1297c053df710e06e0c3aece60dead24f270b4d"
}

variable "ssh_username" {
  description = "The SSH username for the VM."
  type        = string
  default     = "ubuntu"
}

variable "ssh_password" {
  description = "The SSH password for the VM."
  type        = string
  default     = env("SSH_PASSWORD")
}

variable "shutdown_command" {
  description = "The command to shut down the VM."
  type        = string
  default     = "shutdown -P now"
}

variable "headless" {
  description = "When this value is set to true, the machine will start without a console."
  type        = bool
  default     = false
}

variable "boot_command" {
  description = "The command to boot the VM."
  type        = list(string)
  default     = ["e<wait><down><down><down><end> autoinstall 'ds=nocloud;s=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'<F10>"]
}

variable "boot_wait" {
  description = "The time to wait for the VM to boot."
  type        = string
  default     = "10s"
}