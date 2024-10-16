# Ansible

![computers in de kelder](https://downloads.rkslot.nl/img/kelder.jpg)

Automatisch computers installeren in de werkplaats.

Het proces gaat als volgt:

 1. Boot een USB-stick met daarop iPXE, gecompileerd met een embedded script die boot vanaf http://10.0.1.1:4455/boot.ipxe. De TP-Link router heeft een static route voor 10.0.1.0/24 naar 10.131.12.2 (server) die het via een VPN tunnel naar 10.0.1.1 (HWW) stuurt.
 2. Selecteer "Raphson desktop installatie" in het boot menu
 3. Een Fedora installatie wordt gestart met de kickstartconfiguratie uit deze git repository (kickstart.cfg)
 4. De kickstart configuratie installeert Fedora met Plasma desktop op de grootste schijf in de PC. Er wordt een `raphson` gebruiker gemaakt zonder wachtwoord. Er wordt een SSH key geïnstalleerd zodat de PC later ingesteld kan worden met ansible.
 5. Als dit een nieuwe PC is, moet een DHCP-reservering gemaakt worden in de TP-link router en moet het nieuwe IP adres van de computer toegevoegd worden aan inventory.yaml
 6. Uiteindelijk kan via Ansible het systeem voor de rest ingesteld worden:  `ansible-playbook -i inventory.yaml playbook.yaml`

TODO:
 - Ansible voor klokkies?
 - Installeren op computers: casey, links, rechts, kelder TV-laptop, "horrie" muziek computer boven, nog meer?
