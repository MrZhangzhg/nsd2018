#!/usr/bin/env python3
# coding: utf8
'模块用于把远程主机的一个文件拷贝到另一目录'

import shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mudi=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mudi'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
