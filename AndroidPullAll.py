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
    for pkg in packages:
        print(pkg)
        path = getPackagePath(pkg)
        if path is None:
            print(f"Could not get path for {pkg}")
            continue
        path = path.strip()
        print(f"Path: {path}")
        cmd = f"adb pull {path} {pkg}.apk"
        print(f"Running: {cmd}")
        os.system(cmd)

