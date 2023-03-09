#!/bin/sh
cd /root
git clone https://github.com/johnwarlick/netapp-ontap-ansible-awx-demo.git
# This Centos8 is busted so we gotta fix dnf first
yes | \cp -rf netapp-ontap-ansible-awx-demo/_bootstrap/CentOS-Base.repo /etc/yum.repos.d
rpm --rebuilddb
# 3.9 gives an error I don't have time to dive into right now 
dnf install python3.8 -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives  --set python /usr/bin/python3.8
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
cd netapp-ontap-ansible-awx-demo/_bootstrap
ansible-playbook bootstrap.yml