#!/bin/bash

file2=$1
project2=$2
module=$3
version=$4
cluster=$5
zone=$6
namespace=$7

gcloud auth activate-service-account --key-file=$file2
gcloud config set project $project2
docker login -u _json_key -p "$(cat $file2)" https://asia.gcr.io

docker push asia.gcr.io/$project2/$module:$version
gcloud container clusters get-credentials $cluster --zone $zone --project $project2
kubectl set image deployment $module $module-sha256=asia.gcr.io/$project2/$module:$version --namespace=$namespace
