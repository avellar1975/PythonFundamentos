https://codestack.club/questions/1585817/problemas-ao-instalar-o-mongodb-no-ubuntu-2004

sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock

sudo service mongod restart