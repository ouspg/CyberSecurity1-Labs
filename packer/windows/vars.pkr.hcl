variable "iso_url" {
  description = "The URL of the ISO image to use for the build."
  type        = string
  default     = "https://software-download.microsoft.com/download/sg/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso"
}

variable "iso_checksum" {
  description = "The checksum of the ISO image."
  type        = string
  default     = "4f1457c4fe14ce48c9b2324924f33ca4f0470475e6da851b39ccbf98f44e7852"
}

variable "cpu_num" {
  description = "The number of cpus."
  type        = number
  default     = 2
}

variable "disk_size" {
  description = "The hard disk size."
  type        = number
  default     = 102400
}

variable "mem_size" {
  description = "The RAM size."
  type        = number
  default     = 4096
}

variable "winrm_username" {
  type    = string
  default = "winrm"
}

variable "winrm_password" {
  type    = string
  default = env("WINRM_PASSWORD")
}

variable "boot_command" {
  description = "The command to boot the VM."
  type        = list(string)
  default     = ["<spacebar>"]
}

variable "boot_wait" {
  description = "The time to wait for the VM to boot."
  type        = string
  default     = "20s"
}