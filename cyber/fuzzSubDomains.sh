#!/bin/bash

# wfuzz -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.linkvortex.htb" -u http://linkvortex.htb 

# Usage
# ./fuzzSubDomains.sh <baseDomain> <extra parameters>
# --hh <length> : Filter out responses that do not have a length of <length> characters
# --hc <code> : Filter out responses that do not have a status code of <code>
# --hl <lines> : Filter out responses that do not have <lines> lines
# --hw <words> : Filter out responses that do not have <words> words

# Example
# Searches for subdomains of linkvortex.htb that do not return a length of 200 characters
# ./fuzzSubDomains.sh linkvortex.htb --hh 200 


# Check if the user has provided a base domain
if [ -z "$1" ]; then
		echo "Usage: ./fuzzSubDomains.sh <baseDomain> <extra parameters>"
		exit 1
else
	subDomain=$1
fi

# Check if the user has provided any number of extra parameters past the base domain
shift 1
extraParams=$@

echo "wfuzz -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H \"Host: FUZZ.$subDomain\" -u http://$subDomain $extraParams"
# Run the wfuzz command
wfuzz -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.$subDomain" -u http://$subDomain $extraParams
