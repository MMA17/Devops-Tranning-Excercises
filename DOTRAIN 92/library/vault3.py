from ansible.module_utils.basic import AnsibleModule
from ansible import constants as C
from ansible.parsing.vault import VaultLib
from ansible.cli import CLI
from ansible.parsing.dataloader import DataLoader


def main():

    fields = {
        "path": {"default": True, "type": "str"},
        "secret": {"default": True, "type": "str"},
        "type": {"default": True, "type": "str"},
        "msg": {"default": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)

    loader = DataLoader()
    vault_secret = CLI.setup_vault_secrets(
        loader=loader,
        vault_ids=C.DEFAULT_VAULT_IDENTITY_LIST
    )
    vault = VaultLib(vault_secret)

    if module.params['type'] == 'encrypt':
        vault.encrypt(open(module.params['path']).read())
        module.params['msg'] = "encrypted"

    if module.params['type'] == 'decrypt':
        vault.decrypt(open(module.params['path']).read())
        module.params['msg'] = "decrypted"

    module.exit_json(changed=True, meta=module.params)


if __name__ == '__main__':
    main()
