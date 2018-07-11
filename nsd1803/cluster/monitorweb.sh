#!/bin/bash

VIP=201.1.1.4:80
RIP1=192.168.4.2
RIP2=192.168.4.3

while :
do
    for IP in $RIP1 $RIP2
    do
        curl http://$IP &> /dev/null
        web_stat=$?
        ipvsadm -Ln | grep $IP &> /dev/null
        web_in_lvs=$?
        if [ $web_stat -ne 0 -a $web_in_lvs -eq 0 ]; then
            ipvsadm -d -t $VIP -r $IP
        elif [ $web_stat -eq 0 -a $web_in_lvs -ne 0 ]; then
            ipvsadm -a -t $VIP -r $IP -m
        fi
    done
    sleep 1
done
