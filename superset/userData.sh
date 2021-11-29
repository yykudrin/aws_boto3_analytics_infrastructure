#!/bin/bash
git clone https://github.com/yykudrin/aws_boto3_analytics_infrastructure.git
cd aws_boto3_analytics_infrastructure/superset
sudo cp superset.service /lib/systemd/system/
sudo cp superset.sh /usr/bin/
sudo chmod +x superset_install.sh
sudo chmod 644 /lib/systemd/system/superset.service
sudo chmod +x /usr/bin/superset.sh
sudo ./superset_install.sh
sudo systemctl daemon-reload
sudo systemctl enable superset.service
sudo systemctl start superset.service
sudo systemctl status superset.service