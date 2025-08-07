package kubernetes.admission

deny[msg] {
  input.request.kind.kind == "Pod"
  container := input.request.object.spec.containers[_]
  container.securityContext.runAsUser == 0
  msg := "Running as root is not allowed"
}
