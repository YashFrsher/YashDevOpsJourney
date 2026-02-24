/*
Create a terraform resource named php-httpd-image for building docker image with following specifications:
Image name: php-httpd:challenge
Build context: lamp_stack/php_httpd
Labels: challenge: second
*/

resource "docker_image" "php-httpd-image" {
  name = var.php_image_name
  build {
    context = "lamp_stack/php_httpd"
    labels {
      label = "challenge"
      value = var.common_labels
  }
}
}