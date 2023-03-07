This demo shows how Ansible AWX/Tower can empower storage admins to focus on higher-value work by automating new ONTAP storage requests and cutting time to complete other infrastructure tasks to minutes instead of hours. It is made for the [Getting Started With ONTAP Automation Using Ansible](https://handsonlabs.netapp.com/lab/ontapansible) lab but can be easily adapted for other labs as needed. 

To get up and running quickly, ssh into the awx vm once your lab is up and run this: 

`curl https://raw.githubusercontent.com/johnwarlick/netapp-ontap-ansible-awx-demo/main/_bootstrap.sh | bash`

This lab contains a rather outdated version of AWX. This will install k0s, deploy a newer AWX, and set up the config/projects. 

# TODO
- Look into installing newer AWX on K0s 
- Put API calls to AWX in the mock provisioning app and make it load in the browser.
- Add input masking / validation to mock provisioning app 


