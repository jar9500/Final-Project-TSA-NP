#!/bin/bash

cd Netmiko
python3 backupconf.py
git add ../Backup\ Configuration
git commit -m "Menambahkan File Backup Baru"
git log
git status
