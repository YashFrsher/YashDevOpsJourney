/*
Define a terraform resource php-httpd for creating docker container with following specification:
Container Name: webserver
Hostname: php-httpd
Image used: php-httpd:challenge
Attach the container to network my_network
Publish a container's port(s) to the host:
Hostport: 0.0.0.0:80
containerPort: 80
Labels: challenge: second
Create a volume with host_path /root/code/terraform-challenges/challenge2/lamp_stack/website_content/ and container_path /var/www/html within webserver container.
*/


resource "docker_container" "php-httpd" {
    name = var.php_container_name
    hostname = var.php_hostname
    image = docker_image.php-httpd-image.name
    networks_advanced {
        name = docker_network.private_network.name
    }
    ports {
        internal = 80
        external = 80
        ip = "0.0.0.0"
    }
    labels {
        label = "challenge"
        value = var.common_labels
    }
    volumes {
        host_path = var.php_container_hostpath
        container_path = var.php_container_containerpath
    }
}

