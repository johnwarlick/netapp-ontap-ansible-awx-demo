#!/bin/sh
cd /root/
curl -O https://raw.githubusercontent.com/johnwarlick/netapp-ontap-ansible-awx-demo/main/_bootstrap.yml
ansible-playbook _bootstrap.yml