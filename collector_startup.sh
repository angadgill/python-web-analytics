#!/bin/bash

# Config NGINX
cp /home/ubuntu/collector_nginx_config /etc/nginx/sites-available/collector
ln -s /etc/nginx/sites-available/collector /etc/nginx/sites-enabled
sudo service nginx restart

# Config collector upstart script
cp /home/ubuntu/collector.conf /etc/init/collector.conf
sudo service collector start

