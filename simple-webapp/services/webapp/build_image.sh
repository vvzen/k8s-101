#!/usr/bin/env bash

set -e

image_tag=my-app-image

eval "$(minikube docker-env)"
docker build -t "$image_tag" .
