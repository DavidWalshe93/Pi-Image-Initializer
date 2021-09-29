# Pi-Image-Initializer

Setup a Raspberry Pi Image with Ansible.


Tasks:
- Setup Static IP Address.
- Enable SSH for remote login.
- Set new password for security
- Setup custom aliases.

## Usage:

1) Update image and install ansible

  ```shell
  source install.sh
  ```
2) You need to set the following in `vars.yml` to match your LAN

```shell
ip_address: "X.X.X.X/N"
routers: "X.X.X.X"
domain_name_servers: "X.X.X.X"
```

3) Once the above parameters have been set, run the ansible playbook `main.yml` to setup image correctly

  ```shell
  ansible-playbook main.yml
  ```
