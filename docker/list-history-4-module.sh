#!/bin/bash

file=$1
project=$2
module=$3

gcloud auth activate-service-account --key-file=$file
gcloud config set project $project

gcloud container images list-tags asia.gcr.io/$project/$module
