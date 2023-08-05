# Oracle Linux VM Commands

# To see the /opt file system size

	df -h /opt

#moving .rpm file to other loccation

	mv OracleDatabase-19c.rpm /mnt/oem/yum-packages

# adding new hardisk and mount to the vm

	https://www.tutorialspoint.com/how-to-create-add-a-new-virtual-disk-for-an-existing-linux-virtual-machine

# adding VM FQDN to domain on oracle linux 

	sudo yum install realmd sssd oddjob oddjob-mkhomedir adcli samba-common-tools
	sudo realm discover DOMAIN
	sudo realm join --user=USERNAME DOMAIN
	# in the sssd file make "use_fully_qualified_names" value to "False"
	sudo vi /etc/sssd/sssd.conf
	sudo systemctl restart sssd
	
# to create new local user and assign admin access to the user
	
	sudo useradd newuser
	sudo passwd newuser
	sudo usermod -aG wheel newuser
	id newuser
	#optinal configs
	sudo visudo
	#add below value in the file
	newuser ALL=(ALL) ALL

