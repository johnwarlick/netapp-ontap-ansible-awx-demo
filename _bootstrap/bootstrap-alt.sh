#!/bin/sh
cd ~/Desktop
git clone https://github.com/johnwarlick/netapp-ontap-ansible-awx-demo.git
sudo apt update 
dnf install python3.9 -y
sudo alternatives --set python3 /usr/bin/python3.9
sudo apt install python3-pip -y
sudo pip3 install ansible -y
cd netapp-ontap-ansible-awx-demo
pip3 install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml
read -s -p "Password for ONTAP Clusters: " ONTAP_PASS
read -s -p "Password for AWX: " TOWER_PASS
export ONTAP_PASSWORD=$ONTAP_PASS
export TOWER_PASSWORD=$TOWER_PASS
ansible-playbook _bootstrap/bootstrap.yml