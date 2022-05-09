# Pi-Image-Initializer

Setup a Raspberry Pi Image with Ansible.

## Usage:

1) Update image and install ansible

    ```shell
    source install.sh
    ```
   
2) You need to set values in [vars.yml](./roles/setup-ssh/vars/main.yml) to match your LAN.

3) Once the above parameters have been set, run the ansible playbook `main.yml` to setup image correctly

    ```shell
    ansible-playbook main.yml
    ```
