#this script is called automatically by install.sh

#add Zabbix user parameters
"UserParameter=temp.pull[*], python3 /home/pi/temp.py" | Add-Content -Path /etc/zabbix/zabbix_agentd.conf
"UserParameter=door.status[*], python3 /home/pi/door.py" | Add-Content -Path /etc/zabbix/zabbix_agentd.conf

#add GPIO permissions to the Zabbix user
sudo usermod -G GPIO -a zabbix


#turn the cam.ps1 script into a service
#######################################

#service file
#$system_service = "[Unit]`nDescription=Camera script`n[Service]`nExecStart=/etc/powershell/pwsh /home/pi/cam.ps1`nUser=pi`nGroup=pi`n[Install]`nWantedBy=multi-user.target"

#create file
#$system_service | Out-File /lib/systemd/system/monitorpi-camera.service

#register service and enable it
#sudo systemctl daemon-reload
#sudo systemctl enable monitorpi-camera.service
#sudo systemctl start monitorpi-camera.service

