#!/bin/bash

echo "account,password" >/docker/param.csv
echo "$1,$2" >>/docker/param.csv
