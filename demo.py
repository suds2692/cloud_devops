#!/usr/bin/python

from ansible.module_utils.basic import*
import os
import socket

def main():
	module = AnsibleModule(
		argument_spec = dict( 
			showname = dict( required=False, type='bool')
		)
	)	
	ipaddress=socket.gethostbyname(socket.gethostname())
	
	if module.params.get('showname'):
		module.exit_json(changed=True, name=os.name, ipaddress=ipaddress)
	else:
		module.exit_json(changed=True, ipaddress=ipaddress)

if __name__ == "__main__":
	main()


  
