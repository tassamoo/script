#! /usr/bin/env python3
import os

pem_key = str(input("write pem key: "))
connect = str(input("type username@external_IP: "))

os.system ("chmod 600 " + pem_key)
os.system ("ssh -i " + pem_key + " " + connect)