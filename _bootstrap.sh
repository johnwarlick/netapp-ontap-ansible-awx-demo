#!/bin/sh
cd /root/
curl -O https://raw.githubusercontent.com/johnwarlick/netapp-ontap-ansible-awx-demo/main/_bootstrap.yml
sleep 5
ansible-playbook _bootstrap.yml