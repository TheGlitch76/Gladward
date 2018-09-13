#!/bin/bash
# This project is licensed under the MIT license. Please see the LICENSE file at the root of this project for more information.
# This script is designed to be run by a systemd service at boot. It auto-updates the project, installs dependencies from PIP,
# and runs the bot.

# There are no install instructions at the moment, but it should be easy enough to figure out.
git pull
pip3 install -r requirements.txt
python3 ./bot.py
