#!/usr/bin/env python3

import requests
import os
import sys

username = sys.argv[1]
password = sys.argv[2]
repo = sys.argv[3]
real = bool(sys.argv[4]) if len(sys.argv) > 4 else False

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

options = []
# Print the list of tags
print("Repositories:")
for big_tag in tags:
    response = requests.get(f"{url}/v2/{big_tag}/tags/list")
    if response.status_code != 200:
        print(f"Error: Unable to access tags for {big_tag}")
        continue
    tag_data = response.json()
    for tag in tag_data.get("tags", []):
        options.append(f"{big_tag}:{tag}")


# Print the list of tags with numbers
print("Available tags:")
for i, tag in enumerate(options):
    print(f"{i + 1}: {tag}")

# Prompt the user to select a tag to delete
while True:
    try:
        print("To select multiple tags, separate the numbers with commas or a dash.")
        choice = input("Enter the number of the tag(s) to delete (0 to exit): ")
        if choice == "0":
            print("Exiting...")
            sys.exit(0)
        # Parse the input
        choices = []
        if "," in choice:        
            choices = choice.split(",")
            choices = [int(c.strip()) for c in choices]
        elif "-" in choice:
            start, end = choice.split("-")
            start, end = int(start), int(end)
            choices = list(range(start, end + 1))
        else:
            choices = [int(choice)]
        # Validate the input
        for c in choices:
            if c < 1 or c > len(options):
                print(f"Invalid choice: {c}. Please select a valid number.")
                break
        # Delete the selected tags
        for c in choices:
            tag = options[c - 1]
            print(f"Deleting {tag}...")
            tag_name = tag.split(":")[0]
            tag_version = tag.split(":")[1]
            digest_response = requests.get(f"{url}/v2/{tag_name}/manifests/{tag_version}", headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"})
            if digest_response.status_code != 200:
                print(f"Error: Unable to access manifest for {tag}")
                continue
            digest = digest_response.headers.get("Docker-Content-Digest")
            if not digest:
                print(f"Error: Unable to get digest for {tag}")
                continue
            if real:
                delete_response = requests.delete(f"{url}/v2/{tag_name}/manifests/{digest}")
                if delete_response.status_code == 202:
                    print(f"Successfully deleted {tag}")
                else:
                    print(f"Error: Unable to delete {tag}. Status code: {delete_response.status_code}")
            else:
                print(f"Simulated deletion of {tag} with digest {digest}")


    except ValueError:
        print("Invalid input. Please enter a number.")
