#! /usr/bin/python3
#####
# A simple script that resume all suspend VMs
# 
# Author: Giacomo "Anandir" Succi
# Version: 1.0
# License: License: CC0 1.0 Universal
#####
import os
import time
import ovirtsdk4 as sdk
from ovirtsdk4 import types

# Create a connection to the server:
connection = sdk.Connection(
    url='_URL_',
    username='_USER_NAME_',
    password='_PASSWORD_',
    ca_file='_CA_FILE_',
)

vms_service = connection.system_service().vms_service()
vms = vms_service.list()

# Restart all suspended VMs
for vv in vms:
    vm_service = vms_service.vm_service(vv.id)
    vm = vm_service.get()
    
    if vm.status == types.VmStatus.SUSPENDED:
        print('Resuming {} VM...'.format(vv.name))
        vm_service.start(async=False)

        # Just be sure that the VM is up and running
        while True:
            time.sleep(5)
            vm = vm_service.get()
            
            if vm.status == types.VmStatus.UP:
                break
    else:
        print('{} VM is not in a suspended state, skipping...'.format(vv.name))

connection.close()

# Backup system files
os.system("engine-backup --mode=backup --scope=all --file=_BACKUP_PATH_/enginebackup --log=_BACKUP_PATH_/enginebackup.log")

