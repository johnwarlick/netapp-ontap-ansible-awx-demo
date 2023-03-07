#!/bin/sh
cd /root/
curl https://raw.githubusercontent.com/johnwarlick/netapp-ontap-ansible-awx-demo/main/_bootstrap.yml -o _bootstrap.yml
ansible-playbook _bootstrap.yml