# ssh-hosts

Script to mange ssh hosts in an ini file similar to ansible inventory file.
Script is built up on asible python scripts. Here are the steps to use it:

- Install ansible

```
yum -y install ansible
```

- git commands
```
git clone https://github.com/jayrajput/ssh-hosts.git && cd ssh-hosts
```

- Create ./ssh/config from the your ini file. Replace examples/example.ini with
your ini file. Backup you existing .ssh/config before you decide to overwrite it.

```
./ssh-hosts.py examples/example.ini > ~/.ssh/config
```
