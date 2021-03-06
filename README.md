# Pi-Image-Initializer

Setup a Raspberry Pi Image with Ansible.


## Fresh Pi Image (Lite OS)

1) Once logged in, use `sudo raspi-config` to set the region/wifi SSID/password.
2) Install `git` with `sudo apt-get install git`.
3) Clone the repository.
   
   ```bash
   git clone https://github.com/DavidWalshe93/Pi-Image-Initializer.git
   ```

## Usage:

1) Update image and install ansible

    ```shell
    sudo bash install.sh
    ```
   
2) You need to set values in [vars.yml](./roles/setup-ssh/vars/main.yml) to match your LAN.

3) Once the above parameters have been set, run the ansible playbook `main.yml` to setup image correctly

    ```shell
    ansible-playbook main.yml
    ```
