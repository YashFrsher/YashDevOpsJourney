/*All Variables used*/
variable "php_image_name" {
  type = string
  description = "Name of the php application name"
}
variable "mariadb_image_name" {
  type = string
  description = "Name of the mariadb database."
}
variable "network_name" {
  type = string
  description = "Name of the custom network."
}
variable "php_container_name" {
  type = string
  description = "Container name of php application."
}
variable "common_labels" {
  type = string
  description = "labels used in all the resources."
}
variable "php_hostname" {
  type = string
  description = "Hostname of php application."
}
variable "php_container_hostpath" {
  type = string
  description = "hostpath where container path will be binded."
}
variable "php_container_containerpath" {
  type = string
  description = "container path which will be binded with hostpath."
}
variable "dashboard_container_name" {
  type = string
  description = "Name of the php dashboard."
}
variable "dashboard_hostname" {
  type = string
  description = "dashboard container hostname"
}
variable "dashboard_image_name" {
  type = string
  description = "image name of dashboard container"
}
variable "mariadb_container_name" {
  type = string
  description = "Container name of mariadb"
}
variable "mariadb_hostname" {
  type = string
  description = "hostname of mariadb"
}
variable "mariadb_containerpath" {
  type = string
  description = "container path for volume attached"
}
variable "mysql_root_password" {
  type = string
  description = "Password to connect to mariadb"
  sensitive = true
}
variable "mysql_database_name" {
  type = string
  description = "Database name"
}
variable "mariadb_volume_name" {
  type = string
  description = "Name of the shared volume of mariadb"
}