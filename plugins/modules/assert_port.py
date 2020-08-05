#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, xxxx
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: assert_port
short_description: Port listen check
author:
  - sky-joker (@sky-joker)
description:
  - This module can check specific ports is listening.
requirements:
  - python >= 2.7
options:
  ports:
    description:
      - Port list to be check.
    type: list
    elements: str
    required: True
  state:
    description:
      - Choice a protocol to be to use when checking.
    type: str
    default: tcp
    choices:
      - tcp
      - udp
'''

EXAMPLES = r'''
- name: "Listen port check"
  sample.assert_collection.assert_port:
    ports:
      - 22
    state: tcp
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
import socket


def main():
    module = AnsibleModule(
        argument_spec=dict(
            ports=dict(type='list', elements='int', required=True),
            state=dict(type='str', choices=['tcp', 'udp'], default='tcp')
        ),
        supports_check_mode=True
    )

    ports = module.params['ports']
    state = module.params['state']

    if state == 'tcp':
        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('127.0.0.1', port))
                s.close()
            except Exception as e:
                module.fail_json(msg="port: %s, error: %s" % (port, e))
    else:
        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('127.0.0.1', port))
                s.close()
            except Exception as e:
                module.fail_json(msg="port: %s, error: %s" % (port, e))

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
