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

## More Reading:
- http://docs.ansible.com/intro_inventory.html

## License

CC0 Public Domain - http://creativecommons.org/publicdomain/zero/1.0/


## Contact me

Contact jayrajput@gmail.com for any questions.
