#!/usr/bin/env python3

import requests
import os
import sys

username = sys.argv[1]
password = sys.argv[2]
repo = sys.argv[3]

# Set the URL for the Docker registry API
url = f"https://{username}:{password}@{repo}"

# Get the list of tags for the repository
response = requests.get(f"{url}/v2/_catalog")
if response.status_code != 200:
    print(f"Error: Unable to access repository {repo}")
    sys.exit(1)
tags = response.json().get("repositories", [])
if not tags:
    print(f"No repositories found in {repo}")
    sys.exit(1)

# Print the list of tags
print("Repositories:")
for big_tag in tags:
    response = requests.get(f"{url}/v2/{big_tag}/tags/list")
    if response.status_code != 200:
        print(f"Error: Unable to access tags for {big_tag}")
        continue
    tag_data = response.json()
    print(f"  {big_tag}:")
    for tag in tag_data.get("tags", []):
        print(f"    - {tag}")
