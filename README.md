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

2) Run ansible playbook `main.yml` to setup image correctly

  ```shell
  ansible-playbook main.yml
  ```
