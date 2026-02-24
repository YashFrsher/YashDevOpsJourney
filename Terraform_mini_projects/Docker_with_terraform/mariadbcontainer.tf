/*
Define a terraform resource mariadb for creating docker container with following specification:
Container Name: db
Image Used: mariadb:challenge
Hostname: db
Attach the container to network my_network
Publish a container's port(s) to the host:
Hostport: 0.0.0.0:3306
containerPort: 3306
Labels: challenge: second
Define environment variables inside mariadb resource:
MYSQL_ROOT_PASSWORD=1234
MYSQL_DATABASE=simple-website
Attach volume mariadb-volume to /var/lib/mysql directory within db container.
*/


resource "docker_container" "mariadb" {
    name = var.mariadb_container_name
    image = docker_image.mariadb-image.name
    hostname = var.mariadb_hostname
    networks_advanced {
        name = docker_network.private_network.name
    }
    ports {
        internal = 3306
        external = 3306
        ip = "0.0.0.0"
    }
    labels {
        label = "challenge"
        value = var.common_labels
    }
    env = [
        "MYSQL_ROOT_PASSWORD=${var.mysql_root_password}",
        "MYSQL_DATABASE=${var.mysql_database_name}"
    ]
    volumes {
        container_path = var.mariadb_containerpath
        volume_name = docker_volume.mariadb_volume.name
    }
}