#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, xxxx
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: assert_file
short_description: Check the existence of the file or directory.
author:
  - sky-joker (@sky-joker)
description:
  - This module can check the existence of the file or directory.
requirements:
  - python >= 2.7
options:
  paths:
    description:
      - File or Directory list to be check.
    type: list
    elements: str
    required: True
  state:
    description:
      - Choice a type to be to use when checking
    type: str
    default: file
    choices:
      - file
      - directory
'''

EXAMPLES = r'''
- name: "Check existence of directories"
  sample.assert_collection.assert_file:
    paths:
      - /root
      - /tmp
    state: directory
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
import os


def main():
    module = AnsibleModule(
        argument_spec=dict(
            paths=dict(type='list', elements='str', required=True),
            state=dict(type='str', choices=['file', 'directory'], default='file')
        ),
        supports_check_mode=True
    )

    paths = module.params['paths']
    state = module.params['state']

    if state == 'file':
        for path in paths:
            if os.path.isfile(path) is False:
                module.fail_json(msg="file not found: %s" % path)
    else:
        for path in paths:
            if os.path.isdir(path) is False:
                module.fail_json(msg="directory not found: %s " % path)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
