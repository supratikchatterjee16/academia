apt install nginx ufw ssh -y
touch /etc/hosts.allow
touch /etc/hosts.deny
local_ip=$(hostname -I)
# echo 'sshd : '$local_ip/24 >> /etc/hosts.allow
# echo 'sshd : ALL' >> /etc/hosts.deny
ufw default deny incoming
ufw allow ssh
ufw allow 80
ufw allow 443
ufw enable
systemctl start ufw
systemctl start ssh
systemctl start nginx
