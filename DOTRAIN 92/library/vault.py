from ansible.module_utils.basic import *

from ansible_vault import Vault


def main():

    fields = {
        "path": {"default": True, "type": "str"},
        "secret": {"default": True, "type": "str"},
        "type": {"default": True, "type": "str"},
        "msg": {"default": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)

    if module.params['type'] == 'decrypt':
        mess = Vault(module.params['secret']).load_raw(module.params['path'])
        module.params['msg'] = mess

    if module.params['type'] == 'encrypt':
        mess = Vault(module.params['secret']).dump_raw(module.params['path'])
        module.params['msg'] = mess

    module.exit_json(changed=True, meta=module.params)


if __name__ == '__main__':
    main()