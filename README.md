Steps used to test the image on minikube

  docker build -t time-app:tag .
  docker images
  docker save --output time-app.tar .
  docker save --output time-app.tar time-app:latest
  docker save --output time-app.tar time-app:tag
  docker load --input time-app.tar
  eval $(minikube docker-env)
  docker load --input my-image.tar
  docker load --input time-app.tar
  minikube logs
  minikubessh
  minikube ssh
  curl http://localhost:8080
  curl http://localhost:8080/time
  kubectl exec -it time-app-pod -- /bin/bash
  kubectl get services
  docker system prune
