#!/bin/bash
# This is for Ubuntu 20.04 only
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
if [ $? != 0 ]
then
	sudo apt install gnupg
	wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
fi
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
if [ $? != 0 ]
then
	sudo systemctl daemon-reload
	sudo systemctl start mongod
fi
sudo systemctl status mongod
sudo systemctl enable mongod
# Use mongosh for further requirements
