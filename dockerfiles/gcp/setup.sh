#!/bin/bash

# Read /mnt for any .json files and ask the user if they want to use them
CONFIG_FILES=("/mnt"/*.json)
if [ -e "${CONFIG_FILES[0]}" ]; then
    echo "Found the following configuration files in /mnt:"
    select config_file in "${CONFIG_FILES[@]}" "None"; do
        if [ "$config_file" == "None" ]; then
            echo "No configuration file selected. Proceeding without one."
            CONFIG_FILE=""
            break
        elif [ -n "$config_file" ]; then
            echo "Using configuration file: $config_file"
            CONFIG_FILE="$config_file"
            break
        else
            echo "Invalid selection. Please try again."
        fi
    done
else
    echo "No configuration files found in /mnt. Proceeding without one."
    CONFIG_FILE=""
fi

# If a configuration file was selected, set it as an environment variable
if [ -n "$CONFIG_FILE" ]; then
    export CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE="$CONFIG_FILE"
    echo "CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE environment variable set to $CONFIG_FILE"
fi

# Spawn bash shell for user interaction
exec /bin/bash