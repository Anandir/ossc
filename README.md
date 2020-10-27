# oVirt Simple Script Collections

Here's a, small, collection of scripts that I've made for managing oVirt VMs.

* [`scripts\suspend_vms.py`](./scripts/suspend_vms.py): As the name suggests it suspends _**all the running**_ VMs; The VMs in a different state than "UP", will be ignored. This script can be run as a normal user
* [`scripts\resume_vms.py`](./scripts/resume_vms.py): As the name suggests it resume all the VMs marked as _**SUSPENDED**_; The VMs in a different state than "SUSPENDED", will be ignored. This script **must** be run as `root`, because, in the end, it will execute the `engine-backup` command to backup the state of the oVirt Engine. This file, also, should be run directly on the oVirt Host machine or, more in general, in the machine where the `engine-backup` program is installed.

I use them on my oVirt installation that is a simple oVirt Standalone Server, but they should be ok, with minor modifications, even with more complex deploy.

## Compatibility

The scripts are written in Python 3 and they need the Python [ovirtsdk4](https://github.com/oVirt/ovirt-engine-sdk), because of this dependence, they can be used **only** with oVirt 4.0+ (the script are used/tested on an oVirt 4.4+ environment). 

More info about the SDK can be found on their GitHub repo.

## Configuration / usage

Before using the scripts you need to modify them. Just replace the placeholders with your actual values:

* `_URL_`: Your API endpoint, something like `https://<host>/ovirt-engine/api`
* `_USER_NAME_`: An admin login for oVirt, usually `admin@internal`
* `_PASSWORD_`: The admin user password
* `_CA_FILE_`: Complete path to the CA file used on the server, usually something like `/etc/pki/ovirt-engine/ca.pem`

Only for the `resume_vms.py`, you need to set also the:

* `_BACKUP_PATH_`: The full path where to place the backup files

## License

The scripts are released under [CC0 1.0 Universal](./LICENSE) license.