## Ansible Hands On Based on Best Practice Directory

http://docs.ansible.com/ansible/playbooks_best_practices.html#directory-layout

### Require

- virtual box
- vagrant

### Goal

- Run nginx
- Display index.html

for stage and production

### Option

ansible for local

### Get Started

#### Up servers

- host
- stage
- production

`vagrant up`

#### Install Ansible

```
$ vagrant ssh host
vagrant@host$ wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
vagrant@host$ sudo rpm -Uvh epel-release-6-8.noarch.rpm
vagrant@host$ sudo yum -y install ansible
vagrant@host$ ansible --version
```

### Set up ssh

```
vagrant@host$ touch ~/.ssh/config
```

`~/.ssh/config`

```
Host stage
 HostName 192.168.43.52
Host production
 HostName 192.168.43.53
```

```
vagrant@host$ chmod 600 .ssh/config
vagrant@host$ ssh-keygen -t rsa
vagrant@host$ ssh-copy-id stage
# Enter yes,vagrant
vagrant@host$ ssh-copy-id production
# Enter yes,vagrant
```

`cd /var/www/html`

### ansible stage

```
ansible-playbook -i stage site.yml
```

### ansible production

```
ansible-playbook -i production site.yml
```

### About filter-plugin

ex)

`filter_plugins/uppercase.py`

```
from ansible import errors

def uppercase_all(txt):
    return txt.upper()


class FilterModule(object):
    def filters(self):
        return {'uppercase_all': uppercase_all}
```

is called by

`{{ 'text' | uppercase_all }}`

### ansible localhost

use ansible-galaxy first

#### About ansible galaxy

`ansible-galaxy install -p ./roles username.common`

success

`./roles/username.common`

ex)

`ansible-galaxy install -p ./roles geerlingguy.java`

https://galaxy.ansible.com/geerlingguy/java/

#### ansible localhost

```
ansible-playbook -i localhost localhost.yml
```

to confirm

`java -version`

etc
