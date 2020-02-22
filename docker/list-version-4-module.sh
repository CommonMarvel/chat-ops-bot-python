#!/bin/bash

file=$1
project=$2
module=$3
cluster=$4
zone=$5
namespace=$6

gcloud auth activate-service-account --key-file=$file
gcloud config set project $project

gcloud container clusters get-credentials $cluster --zone $zone --project $project

kubectl describe deployment $module --namespace=$namespace