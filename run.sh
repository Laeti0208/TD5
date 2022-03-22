#!/bin/bash
#-> Setup venv
virtualenv .env
pip install -r requirements.txt

#-> Run python program
python3 main.py
