/*
Create a terraform resource named mariadb_volume creating a docker volume with name=mariadb-volume
*/
resource "docker_volume" "mariadb_volume" {
  name = var.mariadb_volume_name
}