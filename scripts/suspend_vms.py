#! /usr/bin/python3
#####
# A simple script that suspend all running VMs for backup
# 
# Author: Giacomo "Anandir" Succi
# Version: 1.0
# License: License: CC0 1.0 Universal
#####
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

# Suspend all running VMs
for vv in vms:
    vm_service = vms_service.vm_service(vv.id)
    vm = vm_service.get()
    
    if vm.status == types.VmStatus.UP:
        print('Suspend {} VM...'.format(vv.name))
        vm_service.suspend(async=False,wait=True)

        # Just to be sure that the VM is properly suspended
        while True:
            time.sleep(5)
            vm = vm_service.get()
            
            if vm.status == types.VmStatus.SUSPENDED:
                break
    else:
        print('{} VM not up, skipping...'.format(vv.name))

connection.close()

