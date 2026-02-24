/*
Define a terraform resource phpmyadmin for docker container with following configurations:
Container Name: db_dashboard
Image Used: phpmyadmin/phpmyadmin
Hostname: phpmyadmin
Attach the container to network my_network
Publish a container's port(s) to the host:
Hostport: 0.0.0.0:8081
containerPort: 80
Labels: challenge: second
Establish link based connectivity between db and db_dashboard containers (Deprecated)
Explicitly specify a dependency on mariadb terraform resource
*/


resource "docker_container" "phpmyadmin" {
    name = var.dashboard_container_name
    image = var.dashboard_image_name
    hostname = var.dashboard_hostname
    networks_advanced {
        name = docker_network.private_network.name
    }
    depends_on = [ docker_container.mariadb ]
    links = [
        docker_container.mariadb.name
    ]
    ports {
        internal = 80
        external = 8081
        ip = "0.0.0.0"
    }
    labels {
        label = "challenge"
        value = var.common_labels
    }
}