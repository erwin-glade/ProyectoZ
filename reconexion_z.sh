#!/bin/sh  
while true; do  
    if ! ping -c 1 api.deepseek.com >/dev/null; then  
        nohup python3 iag_z_service.py > iag_z.log 2>&1 &  
    fi  
    sleep 10  
done  
