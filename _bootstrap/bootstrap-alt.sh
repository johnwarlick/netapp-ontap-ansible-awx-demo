#!/bin/sh
cd ~/Desktop
git clone https://github.com/johnwarlick/netapp-ontap-ansible-awx-demo.git
sudo apt update 
sudo apt-get install python3.9 python3.9-venv sshpass -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --set python3 /usr/bin/python3.9
cd netapp-ontap-ansible-awx-demo
python3 -m venv venv
source venv/bin/activate
sudo apt install python3-pip -y
sudo pip3 install ansible -y
pip3 install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml
# Finally run boostrap.sh on the awx host to set that all up
scp _bootstrap/bootstrap.sh root@awx.demo.netapp.com:/root
ssh root@awx.demo.netapp.com "bash bootstrap.sh"