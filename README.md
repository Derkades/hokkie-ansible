# Ansible

![computers in de kelder](https://downloads.rkslot.nl/img/kelder.jpg)

TODO:
 - Ansible voor klokkies?
 - KDE Panels
 - Grub timeout op 0

## Introductie

Installeer eerst Ansible.

Op Fedora:
```
sudo dnf install ansible
```

Op Debian/Ubuntu;
```
sudo apt install pipx
pipx install --include-deps ansible
```

## Desktops

Voer playbook uit voor alle computers:
```
ansible-playbook plays/desktops.yaml
```

Verzamel specs naar een specs.txt bestand in je home dir:
```
ansible-playbook plays/specs.yaml
```

Updaten naar nieuwe Fedora versie:
```
ansible-playbook plays/desktops-upgrade.yaml
```

## Gog (backup server)
```
ansible-playbook plays/gog.yaml
```

## 106 forum
```
ansible-playbook plays/gog.yaml
```

## Installatie desktops (en laptops)

Het proces gaat als volgt:

 1. Boot een USB-stick met daarop iPXE, gecompileerd met een embedded script die boot vanaf http://10.0.1.1:4455/boot.ipxe. De TP-Link router heeft een static route voor 10.0.1.0/24 naar 10.131.12.2 (server) die het via een VPN tunnel naar 10.0.1.1 (HHW) stuurt.
 2. Selecteer "Raphson desktop installatie" in het boot menu
 3. Een Fedora installatie wordt gestart met de kickstartconfiguratie uit deze git repository (kickstart.cfg)
 4. De kickstart configuratie installeert Fedora met Plasma desktop op de grootste schijf in de PC. Er wordt een `raphson` gebruiker gemaakt zonder wachtwoord. Er wordt een SSH key geïnstalleerd zodat de PC later ingesteld kan worden met ansible.
 5. Als dit een nieuwe PC is, moet een DHCP-reservering gemaakt worden in de TP-link router. Zie https://projects.raphson.nl/wiki/netwerk/
 6. Voeg het IP adres toe aan inventory.yaml
 6. Uiteindelijk kan via Ansible het systeem voor de rest ingesteld worden.
