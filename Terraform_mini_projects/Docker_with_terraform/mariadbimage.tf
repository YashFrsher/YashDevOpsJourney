/*
Create a terraform resource named mariadb-image for building docker image with following specifications:
Image name: mariadb:challenge
Build context: lamp_stack/custom_db
Labels: challenge: second
*/

resource "docker_image" "mariadb-image" {
  name = var.mariadb_image_name
  build {
    context = "lamp_stack/custom_db"
    labels {
      label = "challenge" 
      value = var.common_labels
    }
  }
}