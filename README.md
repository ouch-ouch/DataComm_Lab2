- Problem Statement - Deploy a simple application to K8 that returns the current time when visited using the path "/time"
Steps used to test the image on minikube

# Step 1: Build the Docker Image
docker build -t time-app:tag .

# Step 2: Start Minikube
minikube start

# Step 3: Set Minikube's Docker Environment
eval $(minikube docker-env)

# Step 4: Rebuild the Docker Image for Minikube
docker build -t sushant4nyu/time-app:tag .

# Step 5: Create the Deployment in Kubernetes
kubectl create deployment time-app --image=sushant4nyu/time-app:tag

# Step 6: Expose the Deployment as a Service
kubectl expose deployment time-app --type=NodePort --port=8080

# Step 7: Verify that the Pods are Running
kubectl get pods

# Step 8: Get the Minikube IP
minikube ip

# Step 9: Access the Application in the Browser
# Open this URL in your browser:
http://<MINIKUBE_IP>:8080/time

# Step 10: If the Service is Not Accessible, Expose as LoadBalancer
kubectl expose deployment time-app --type=LoadBalancer --port=8080

# Step 11: Start Minikube Tunnel for LoadBalancer to Work
minikube tunnel

# Step 12: Verify from Inside Minikube
kubectl exec -it $(kubectl get pod -l app=time-app -o jsonpath="{.items[0].metadata.name}") -- curl http://localhost:8080/time

# Step 13: Final Browser Check
# Open this URL in your browser:
http://<MINIKUBE_IP>:8080/time
