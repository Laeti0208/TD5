#!/bin/bash
#-> Setup venv
virtualenv .env
pip3 install -r requirements.txt

#-> Run python program
python3 ./Exo2_3/main.py
