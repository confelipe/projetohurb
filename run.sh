#/bin/bash
sudo kubectl config use-context minikube
sudo kubectl apply -f app-mysql.yaml
sudo kubectl apply -f app-mysql-service.yaml
sudo kubectl apply -f app.yaml
sudo kubectl apply -f app-service.yaml