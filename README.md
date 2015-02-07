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

## Similar Tools:
- https://github.com/dbrady/ssh-config
- https://github.com/emre/storm

The tools are good in there own way. I like the ini file way as there can be
more tools built up over text files. Like you can just grep the ini file to
find the HostName for a host. Also you can just send your ini file. Or if you
have a project team managing a lot of servers, the ini file can be shared
across all the teams.

## License

CC0 Public Domain - http://creativecommons.org/publicdomain/zero/1.0/

## Contact me

Contact jayrajput@gmail.com for any questions.
