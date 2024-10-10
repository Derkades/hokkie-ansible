# Ansible

![computers in de kelder](https://downloads.rkslot.nl/img/kelder.jpg)

Deploy on other machine, for testing:
```
ansible-playbook -i inventory.yaml playbook.yaml
```

Pull to this machine (do not run on your personal system!):
```
ansible-pull --url https://github.com/Derkades/hokkie-ansible -i local.ini playbook.yaml
```
