resource "docker_network" "private_network" {
  name = var.network_name
  attachable = true
  labels {
    label = "challenge"
    value = var.common_labels
  }
}