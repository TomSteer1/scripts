#!/bin/bash

echo "Starting aws cli"

read -p "Enter AWS Access Key ID: " access
read -p "Enter AWS Secret: " secret
read -p "Enter Region: " region

echo "Starting with:"
echo "Access Key: $access"
echo "Secret: $secret"

if [[ -n $region ]]; then
    echo "Region $region"
    aws configure set region "$region"
fi

aws configure set aws_access_key_id "$access"
aws configure set aws_secret_access_key "$secret"

aws sts get-caller-identity
exec /bin/bash
