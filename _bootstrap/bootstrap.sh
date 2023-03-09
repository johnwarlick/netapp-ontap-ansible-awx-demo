#!/bin/sh
cd /root
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install ansible requests docker
# This lab has a pretty old AWX install
ansible-galaxy collection install awx.awx:17.0.0 
read -s -p "Password for AWX: " TOWER_PASS
read -s -p "Password for ONTAP Clusters: " ONTAP_PASS
export ONTAP_PASSWORD=$ONTAP_PASS
export TOWER_PASSWORD=$TOWER_PASS
git clone https://github.com/johnwarlick/netapp-ontap-ansible-awx-demo.git
cd netapp-ontap-ansible-awx-demo/_bootstrap
ansible-playbook bootstrap.yml