#!/bin/bash

echo "Updating and installing Docker"
sudo yum update -y
sudo yum upgrade -y
sudo yum remove docker \
  docker-client \
  docker-client-latest \
  docker-common \
  docker-latest \
  docker-latest-logrotate \
  docker-logrotate \
  docker-engine
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
sudo yum-config-manager -y \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce docker-ce-cli containerd.io

echo "Starting and enabling Docker"
sudo systemctl start docker
sudo systemctl enable docker
