#!/usr/bin/env python


# Use adb to list all packages on the device

import os
import sys

def getPackages():
    packages = []
    cmd = "adb shell pm list packages -3"
    lines = os.popen(cmd).readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("package:"):
            packages.append(line[8:])
    return packages

def getPackagePath(package):
    cmd = f"adb shell pm path {package}"
    lines = os.popen(cmd).readlines()
    for line in lines:
        if line.startswith("package:"):
            return line[8:]
    return None


if __name__ == "__main__":
    packages = getPackages()
    print("Select a package to pull:")
    for i, package in enumerate(packages):
        print(f"{i+1}. {package}")
    try:
        choice = int(input("Enter the number of the package to pull: "))
        if choice < 1 or choice > len(packages):
            raise ValueError("Invalid choice")
    except ValueError as e:
        print("Invalid choice")
        sys.exit(1)
    package = packages[choice-1]
    print(f"Pulling {package}")
    path = getPackagePath(package)
    if path is None:
        print(f"Could not get path for {package}")
        sys.exit(1)
    path = path.strip()
    print(f"Path: {path}")
    cmd = f"adb pull {path} {package}.apk"
    print(f"Running: {cmd}")
    os.system(cmd)

