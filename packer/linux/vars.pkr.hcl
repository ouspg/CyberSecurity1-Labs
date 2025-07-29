variable "iso_url" {
    description = "The URL of the ISO image to use for the build."
    type = string
    default = "https://example.com/path/to/linux.iso"
}

variable "iso_checksum" {
    description = "The checksum of the ISO image."
    type = string
    default = "d6dab0c3a657988501b4bd76f1297c053df710e06e0c3aece60dead24f270b4d"
}