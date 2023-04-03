#!/bin/sh
cd /root
git clone https://github.com/johnwarlick/netapp-ontap-ansible-awx-demo.git
# This Centos8 is busted so we gotta fix dnf first
yes | \cp -rf netapp-ontap-ansible-awx-demo/_bootstrap/CentOS-Base.repo /etc/yum.repos.d/
yes | \cp -rf netapp-ontap-ansible-awx-demo/_bootstrap/CentOS-AppStream.repo /etc/yum.repos.d/
#rpm --rebuilddb
# 3.9 gives an error I don't have time to dive into right now 
dnf install python3.8 -y
sudo alternatives --set python3 /usr/bin/python3.8
# Add custom venv to projects folder since it's already mounted in the countainers
cd /var/lib/awx/projects
python3 -m venv custom-venv
source custom-venv/bin/activate
umask 0022
pip install --upgrade pip setuptools
pip install -r /root/netapp-ontap-ansible-awx-demo/requirements.txt
if [ x"${TOWER_PASS}" == "x" ]; then 
    read -s -p "Password for AWX: " TOWER_PASS
fi
if [ x"${ONTAP_PASS}" == "x" ]; then 
    read -s -p "Password for ONTAP Clusters: " ONTAP_PASS
fi
export ONTAP_PASSWORD=$ONTAP_PASS
export TOWER_PASSWORD=$TOWER_PASS
cd /root/netapp-ontap-ansible-awx-demo/_bootstrap
ansible-playbook bootstrap.yml
