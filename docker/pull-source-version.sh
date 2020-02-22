#!/bin/bash

file=$1
project1=$2
module=$3
version=$4
project2=$5

gcloud auth activate-service-account --key-file=$file
gcloud config set project $project1
docker login -u _json_key -p "$(cat $file)" https://asia.gcr.io

docker pull asia.gcr.io/$project1/$module:$version
docker tag asia.gcr.io/$project1/$module:$version asia.gcr.io/$project2/$module:$version
docker tag asia.gcr.io/$project1/$module:$version asia.gcr.io/$project2/$module:latest
