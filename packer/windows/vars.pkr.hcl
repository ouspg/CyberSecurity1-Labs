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