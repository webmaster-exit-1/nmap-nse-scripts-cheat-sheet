## **NMap NSE Scripts Cheat Sheet**

# 

- This **NMAP NSE SCRIPTS CHEAT SHEET** was created to show the correct usage for each of the official nmap nse scripts.

#

afp-ls.nse

```bash
nmap -p 548 --script afp-ls --script-args afp-ls.timeout=4s,afp-ls.max-retries=3 <target>
```

afp-path-vuln.nse

```bash
nmap -p 548 --script afp-path-vuln --script-args afp-path-vuln.timeout=4s,afp-path-vuln.max-retries=3 <target>
```

Afp-serverinfo.nse

```bash
nmap -p 548 --script afp-serverinfo --script-args afp-serverinfo.timeout=4s,afp-serverinfo.max-retries=3 <target>
```

afp-showmount.nse

```bash
nmap -p 548 --script afp-showmount --script-args afp-showmount.timeout=4s,afp-showmount.max-retries=3 <target>
```

ajp-auth.nse

```bash
nmap -p 8009 --script ajp-auth --script-args ajp-auth.path=/manager/html,ajp-auth.user=tomcat,ajp-auth.pass=s3cret <target>
```

ajp-brute.nse

```bash
nmap -p 8009 --script ajp-brute --script-args ajp-brute.path=/manager/html,ajp-brute.userdb=users.txt,ajp-brute.passdb=passwords.txt,ajp-brute.timeout=4s,ajp-brute.max-retries=3 <target>
```

ajp-headers.nse

```bash
nmap -p 8009 --script ajp-headers --script-args ajp-headers.path=/manager/html <target>
```

ajp-methods.nse

```bash
nmap -p 8009 --script ajp-methods --script-args ajp-methods.path=/manager/html <target>
```

ajp-request.nse

```bash
nmap -p 8009 --script ajp-request --script-args ajp-request.path=/manager/html <target>
```

allseeingeye-info.nse

```bash
nmap -p 8009 --script allseeingeye-info --script-args allseeingeye-info.timeout=4s,allseeingeye-info.max-retries=3 <target>
```

amqp-info.nse

```bash
nmap -p 5672 --script amqp-info --script-args amqp-info.timeout=4s,amqp-info.max-retries=3 <target>
```

asn-query.nse

```bash
nmap -p 53 --script asn-query --script-args asn-query.timeout=4s,asn-query.max-retries=3 <target>
```

auth-owners.nse

```bash
nmap -p 22 --script auth-owners --script-args auth-owners.timeout=4s,auth-owners.max-retries=3 <target>
```

auth-spoof.nse

```bash
nmap -p 22 --script auth-spoof --script-args auth-spoof.timeout=4s,auth-spoof.max-retries=3 <target>
```

backorifice-brute.nse

```bash
nmap -p 80 --script backorifice-brute --script-args backorifice-brute.userdb=users.txt,backorifice-brute.passdb=passwords.txt,backorifice-brute.timeout=4s,backorifice-brute.max-retries=3 <target>
```

backorifice-info.nse

```bash
nmap -p 80 --script backorifice-info --script-args backorifice-info.timeout=4s,backorifice-info.max-retries=3 <target>
```

bacnet-info.nse

```bash
nmap -p 47808 --script bacnet-info --script-args bacnet-info.timeout=4s,bacnet-info.max-retries=3 <target>
```

banner.nse

```bash
nmap -p 22,80 --script banner --script-args banner.timeout=4s,banner.max-retries=3 <target>
```

bitcoin-getaddr.nse

```bash
nmap -p 9332 --script bitcoin-getaddr --script-args bitcoin-getaddr.timeout=4s,bitcoin-getaddr.max-retries=3 <target>
```

bitcoin-info.nse

```bash
nmap -p 8332 --script bitcoin-info --script-args bitcoin-info.timeout=4s,bitcoin-info.max-retries=3 <target>
```

bitcoinrpc-info.nse

```bash
nmap -p 8332 --script bitcoinrpc-info --script-args bitcoinrpc-info.timeout=4s,bitcoinrpc-info.max-retries=3 <target>
```

bittorrent-discovery.nse

```bash
nmap -p 6881 --script bittorrent-discovery --script-args bittorrent-discovery.timeout=4s,bittorrent-discovery.max-retries=3 <target>
```

bjnp-discover.nse

```bash
nmap -p 623 --script bjnp-discover --script-args bjnp-discover.timeout=4s,bjnp-discover.max-retries=3 <target>
```

broadcast-ataoe-discover.nse

```bash
nmap -p 427 --script broadcast-ataoe-discover --script-args broadcast-ataoe-discover.timeout=4s,broadcast-ataoe-discover.max-retries=3 <target>
```

broadcast-avahi-dos.nse

```bash
nmap -p 5353 --script broadcast-avahi-dos --script-args broadcast-avahi-dos.timeout=4s,broadcast-avahi-dos.max-retries=3 <target>
```

broadcast-bjnp-discover.nse

```bash
nmap -p 623 --script broadcast-bjnp-discover --script-args broadcast-bjnp-discover.timeout=4s,broadcast-bjnp-discover.max-retries=3 <target>
```

broadcast-db2-discover.nse

```bash
nmap -p 623 --script broadcast-db2-discover --script-args broadcast-db2-discover.timeout=4s,broadcast-db2-discover.max-retries=3 <target>
```

broadcast-dhcp-discover.nse

```bash
nmap -p 67 --script broadcast-dhcp-discover --script-args broadcast-dhcp-discover.timeout=4s,broadcast-dhcp-discover.max-retries=3 <target>
```

broadcast-dhcp6-discover.nse

```bash
nmap -p 547 --script broadcast-dhcp6-discover --script-args broadcast-dhcp6-discover.timeout=4s,broadcast-dhcp6-discover.max-retries=3 <target>
```

broadcast-dns-service-discovery.nse

```bash
nmap -p 5353 --script broadcast-dns-service-discovery --script-args broadcast-dns-service-discovery.timeout=4s,broadcast-dns-service-discovery.max-retries=3 <target>
```

broadcast-dropbox-listener.nse

```bash
nmap -p 17500 --script broadcast-dropbox-listener --script-args broadcast-dropbox-listener.timeout=4s,broadcast-dropbox-listener.max-retries=3 <target>
```

broadcast-eigrp-discovery.nse

```bash
nmap -p 521 --script broadcast-eigrp-discovery --script-args broadcast-eigrp-discovery.timeout=4s,broadcast-eigrp-discovery.max-retries=3 <target>
```

broadcast-hid-discoveryd.nse

```bash
nmap -p 635 --script broadcast-hid-discoveryd --script-args broadcast-hid-discoveryd.timeout=4s,broadcast-hid-discoveryd.max-retries=3 <target>
```

broadcast-igmp-discovery.nse

```bash
nmap -p 521 --script broadcast-igmp-discovery --script-args broadcast-igmp-discovery.timeout=4s,broadcast-igmp-discovery.max-retries=3 <target>
```

broadcast-jenkins-discover.nse

```bash
nmap -p 8080 --script broadcast-jenkins-discover --script-args broadcast-jenkins-discover.timeout=4s,broadcast-jenkins-discover.max-retries=3 <target>
```

broadcast-listener.nse

```bash
nmap -p 5353 --script broadcast-listener --script-args broadcast-listener.timeout=4s,broadcast-listener.max-retries=3 <target>
```

broadcast-ms-sql-discover.nse

```bash
nmap -p 1434 --script broadcast-ms-sql-discover --script-args broadcast-ms-sql-discover.timeout=4s,broadcast-ms-sql-discover.max-retries=3 <target>
```

broadcast-netbios-master-browser.nse

```bash
nmap -p 137 --script broadcast-netbios-master-browser --script-args broadcast-netbios-master-browser.timeout=4s,broadcast-netbios-master-browser.max-retries=3 <target>
```

broadcast-networker-discover.nse

```bash
nmap -p 137 --script broadcast-networker-discover --script-args broadcast-networker-discover.timeout=4s,broadcast-networker-discover.max-retries=3 <target>
```

broadcast-novell-locate.nse

```bash
nmap -p 137 --script broadcast-novell-locate --script-args broadcast-novell-locate.timeout=4s,broadcast-novell-locate.max-retries=3 <target>
```

broadcast-ospf2-discover.nse

```bash
nmap -p 89 --script broadcast-ospf2-discover --script-args broadcast-ospf2-discover.timeout=4s,broadcast-ospf2-discover.max-retries=3 <target>
```

broadcast-pc-anywhere.nse

```bash
nmap -p 5350 --script broadcast-pc-anywhere --script-args broadcast-pc-anywhere.timeout=4s,broadcast-pc-anywhere.max-retries=3 <target>
```

broadcast-pc-duo.nse

```bash
nmap -p 5351 --script broadcast-pc-duo --script-args broadcast-pc-duo.timeout=4s,broadcast-pc-duo.max-retries=3 <target>
```

broadcast-pim-discovery.nse

```bash
nmap -p 521 --script broadcast-pim-discovery --script-args broadcast-pim-discovery.timeout=4s,broadcast-pim-discovery.max-retries=3 <target>
```

broadcast-ping.nse

```bash
nmap -p 7 --script broadcast-ping --script-args broadcast-ping.timeout=4s,broadcast-ping.max-retries=3 <target>
```

broadcast-pppoe-discover.nse

```bash
nmap -p 4379 --script broadcast-pppoe-discover --script-args broadcast-pppoe-discover.timeout=4s,broadcast-pppoe-discover.max-retries=3 <target>
```

broadcast-rip-discover.nse

```bash
nmap -p 520 --script broadcast-rip-discover --script-args broadcast-rip-discover.timeout=4s,broadcast-rip-discover.max-retries=3 <target>
```

broadcast-ripng-discover.nse

```bash
nmap -p 521 --script broadcast-ripng-discover --script-args broadcast-ripng-discover.timeout=4s,broadcast-ripng-discover.max-retries=3 <target>
```

broadcast-sonicwall-discover.nse

```bash
nmap -p 1900 --script broadcast-sonicwall-discover --script-args broadcast-sonicwall-discover.timeout=4s,broadcast-sonicwall-discover.max-retries=3 <target>
```

broadcast-sybase-asa-discover.nse

```bash
nmap -p 1521 --script broadcast-sybase-asa-discover --script-args broadcast-sybase-asa-discover.timeout=4s,broadcast-sybase-asa-discover.max-retries=3 <target>
```

broadcast-tellstick-discover.nse

```bash
nmap -p 1900 --script broadcast-tellstick-discover --script-args broadcast-tellstick-discover.timeout=4s,broadcast-tellstick-discover.max-retries=3 <target>
```

broadcast-upnp-info.nse

```bash
nmap -p 1900 --script broadcast-upnp-info --script-args broadcast-upnp-info.timeout=4s,broadcast-upnp-info.max-retries=3 <target>
```

broadcast-versant-locate.nse

```bash
nmap -p 137 --script broadcast-versant-locate --script-args broadcast-versant-locate.timeout=4s,broadcast-versant-locate.max-retries=3 <target>
```

broadcast-wake-on-lan.nse

```bash
nmap -p 9 --script broadcast-wake-on-lan --script-args broadcast-wake-on-lan.timeout=4s,broadcast-wake-on-lan.max-retries=3 <target>
```

broadcast-wpad-discover.nse

```bash
nmap -p 3702 --script broadcast-wpad-discover --script-args broadcast-wpad-discover.timeout=4s,broadcast-wpad-discover.max-retries=3 <target>
```

broadcast-wsdd-discover.nse

```bash
nmap -p 3702 --script broadcast-wsdd-discover --script-args broadcast-wsdd-discover.timeout=4s,broadcast-wsdd-discover.max-retries=3 <target>
```

broadcast-xdmcp-discover.nse

```bash
nmap -p 6000 --script broadcast-xdmcp-discover --script-args broadcast-xdmcp-discover.timeout=4s,broadcast-xdmcp-discover.max-retries=3 <target>
```

cassandra-brute.nse

```bash
nmap -p 9160 --script cassandra-brute --script-args cassandra-brute.userdb=users.txt,cassandra-brute.passdb=passwords.txt,cassandra-brute.timeout=4s,cassandra-brute.max-retries=3 <target>
```

cassandra-info.nse

```bash
nmap -p 9160 --script cassandra-info --script-args cassandra-info.timeout=4s,cassandra-info.max-retries=3 <target>
```

cccam-version.nse

```bash
nmap -p 5200 --script cccam-version --script-args cccam-version.timeout=4s,cccam-version.max-retries=3 <target>
```

cics-enum.nse

```bash
nmap -p 3270 --script cics-enum --script-args cics-enum.timeout=4s,cics-enum.max-retries=3 <target>
```

cics-info.nse

```bash
nmap -p 3270 --script cics-info --script-args cics-info.timeout=4s,cics-info.max-retries=3 <target>
```

cics-user-brute.nse

```bash
nmap -p 3270 --script cics-user-brute --script-args cics-user-brute.userdb=users.txt,cics-user-brute.passdb=passwords.txt,cics-user-brute.timeout=4s,cics-user-brute.max-retries=3 <target>
```

cics-user-enum.nse

```bash
nmap -p 3270 --script cics-user-enum --script-args cics-user-enum.timeout=4s,cics-user-enum.max-retries=3 <target>
```

citrix-brute-xml.nse

```bash
nmap -p 443 --script citrix-brute-xml --script-args citrix-brute-xml.userdb=users.txt,citrix-brute-xml.passdb=passwords.txt,citrix-brute-xml.timeout=4s,citrix-brute-xml.max-retries=3 <target>
```

citrix-enum-apps-xml.nse

```bash
nmap -p 443 --script citrix-enum-apps-xml --script-args citrix-enum-apps-xml.timeout=4s,citrix-enum-apps-xml.max-retries=3 <target>
```

citrix-enum-apps.nse

```bash
nmap -p 443 --script citrix-enum-apps --script-args citrix-enum-apps.timeout=4s,citrix-enum-apps.max-retries=3 <target>
```

citrix-enum-servers-xml.nse

```bash
nmap -p 443 --script citrix-enum-servers-xml --script-args citrix-enum-servers-xml.timeout=4s,citrix-enum-servers-xml.max-retries=3 <target>
```

citrix-enum-servers.nse

```bash
nmap -p 443 --script citrix-enum-servers --script-args citrix-enum-servers.timeout=4s,citrix-enum-servers.max-retries=3 <target>
```

clamav-exec.nse

```bash
nmap -p 3310 --script clamav-exec --script-args clamav-exec.cmd="ls",clamav-exec.timeout=4s,clamav-exec.max-retries=3 <target>
```

clock-skew.nse

```bash
nmap -p 13,37,53,123 --script clock-skew --script-args clock-skew.timeout=4s,clock-skew.max-retries=3 <target>
```

coap-resources.nse

```bash
nmap -p 5683 --script coap-resources <target>
```

couchdb-databases.nse

```bash
nmap -p 5984 --script couchdb-databases <target>
```

couchdb-stats.nse

```bash
nmap -p 5984 --script couchdb-databases <target>
```

creds-summary.nse

```bash
nmap -p 5984 --script couchdb-stats <target>
```

cups-info.nse

```bash
nmap -p 631 --script cups-info <target>
```

cups-queue-info.nse

```bash
nmap -p 631 --script cups-queue-info <target>
```

cvs-brute-repository.nse

```bash
nmap --script cvs-brute-repository --script-args cvs-brute-repository.repository=<repo>,cvs-brute-repository.module=<module> <target>
```

cvs-brute.nse

```bash
nmap -p 2401 --script cvs-brute --script-args cvs-brute.host=<host>,cvs-brute.module=<module> <target>
```

daap-get-library.nse

```bash
nmap -p 3689 --script daap-get-library <target>
```

daytime.nse

```bash
nmap -p 13 --script daytime <target>
```

db2-das-info.nse

```bash
nmap -p 50000 --script db2-das-info <target>
```
'deluge-rpc-brute.nse

```bash
nmap -p 58846 --script deluge-rpc-brute --script-args deluge-rpc-brute.passwords=<password_file> <target>
```

dhcp-discover.nse

```bash
nmap -p 67 --script dhcp-discover <target>
```

dicom-brute.nse

```bash
nmap -p 104 --script dicom-brute --script-args dicom-brute.hostname=<host>,dicom-brute.password=<password> <target>
```

dicom-ping.nse

```bash
nmap -p 104 --script dicom-ping <target>
```

dict-info.nse

```bash
nmap -p 21 --script dict-info <target>
```

distcc-cve2004-2687.nse

```bash
nmap -p 3632 --script distcc-cve2004-2687 <target>
```

dns-blacklist.nse

```bash
nmap --script dns-blacklist --script-args dns-blacklist.hostname=<hostname> <target>
```

dns-brute.nse

```bash
nmap --script dns-brute --script-args dns-brute.domain=<domain> <target>
```

dns-cache-snoop.nse

```bash
nmap -p 53 --script dns-cache-snoop <target>
```

dns-check-zone.nse

```bash
nmap --script dns-check-zone --script-args dns-check-zone.domain=<domain> <target>
```

dns-client-subnet-scan.nse

```bash
nmap -p 53 --script dns-client-subnet-scan --script-args dns-client-subnet-scan.domain=<domain> <target>
```

dns-fuzz.nse

```bash
nmap -p 53 --script dns-fuzz <target>
```

dns-ip6-arpa-scan.nse

```bash
nmap -p 53 --script dns-ip6-arpa-scan --script-args dns-ip6-arpa-scan.domain=<domain> <target>
```

dns-nsec-enum.nse

```bash
nmap -p 53 --script dns-nsec3-enum --script-args dns-nsec3-enum.domain=<domain> <target>
```

dns-nsec3-enum.nse

```bash
nmap -p 53 --script dns-nsec3-enum --script-args dns-nsec3-enum.domain=<domain> <target>
```

dns-nsid.nse

```bash
nmap -p 53 --script dns-nsid <target>
```

dns-random-srcport.nse

```bash
nmap -p 53 --script dns-random-srcport <target>
```

dns-random-txid.nse

```bash
nmap -p 53 --script dns-random-txid <target>
```

dns-recursion.nse

```bash
nmap -p 53 --script dns-service-discovery <target>
```

dns-service-discovery.nse

```bash
nmap -p 53 --script dns-service-discovery <target>
```

dns-srv-enum.nse

```bash
nmap -p 53 --script dns-srv-enum --script-args dns-srv-enum.domain=<domain> <target>
```

dns-update.nse

```bash
nmap -p 53 --script dns-update --script-args dns-update.domain=<domain> <target>
```

dns-zeustracker.nse

```bash
nmap -p 53 --script dns-zeustracker <target>
```

dns-zone-transfer.nse

```bash
nmap -p 53 --script dns-zone-transfer --script-args dns-zone-transfer.domain=<domain> <target>
```

docker-version.nse

```bash
nmap -p 2375 --script docker-version <target>
```

domcon-brute.nse

```bash
nmap -p 135 --script domcon-brute --script-args domcon-brute.domain=<domain> <target>
```

domcon-cmd.nse

```bash
nmap -p 135 --script domcon-cmd --script-args domcon-cmd.command=<command>,domcon-cmd.domain=<domain> <target>
```

domino-enum-users.nse

```bash
nmap -p 135 --script domino-enum-users --script-args domino-enum-users.domain=<domain> <target>
```

dpap-brute.nse

```bash
nmap -p 161 --script dpap-brute --script-args dpap-brute.username=<username>,dpap-brute.password=<password> <target>
```

drda-brute.nse

```bash
nmap -p 102 --script drda-brute --script-args drda-brute.username=<username>,drda-brute.password=<password> <target>
```

drda-info.nse

```bash
nmap -p 102 --script drda-info <target>
```

duplicates.nse

```bash
nmap --script duplicates <target>
```

eap-info.nse

```bash
nmap -p 1812 --script eap-info <target>
```

enip-info.nse

```bash
nmap -p 44818 --script enip-info <target>
```

epmd-info.nse

```bash
nmap -p 4369 --script epmd-info <target>
```

eppc-enum-processes.nse

```bash
nmap -p 102 --script eppc-enum-processes <target>
```

fcrdns.nse

```bash
nmap --script fcrdns --script-args fcrdns.nameservers=<nameservers> <target>
```

finger.nse

```bash
nmap -p 79 --script finger <target>
```

fingerprint-strings.nse

```bash
nmap -p <port> --script fingerprint-strings <target>
```

firewalk.nse

```bash
nmap -p 21 --script firewalk <target>
```

firewall-bypass.nse

```bash
nmap --script firewall-bypass <target>
```

flume-master-info.nse

```bash
nmap -p 41414 --script flume-master-info <target>
```

fox-info.nse

```bash
nmap -p 1919 --script fox-info <target>
```

freelancer-info.nse

```bash
nmap -p 12345 --script freelancer-info <target>
```

ftp-anon.nse

```bash
nmap -p 21 --script ftp-anon <target>
```

ftp-bounce.nse

```bash
nmap -p 21 --script ftp-bounce --script-args ftp-bounce.max-retries=<max_retries> <target>
```

ftp-brute.nse

```bash
nmap -p 21 --script ftp-brute --script-args ftp-brute.userdb=<userdb>,ftp-brute.passdb=<passdb> <target>
```

ftp-libopie.nse

```bash
nmap -p 21 --script ftp-libopie <target>
```

ftp-proftpd-backdoor.nse

```bash
nmap -p 21 --script ftp-proftpd-backdoor <target>
```

ftp-syst.nse

```bash
nmap -p 21 --script ftp-syst <target>
```

ftp-vsftpd-backdoor.nse

```bash
nmap -p 21 --script ftp-vsftpd-backdoor <target>
```

ftp-vuln-cve2010-4221.nse

```bash
nmap -p 21 --script ftp-vuln-cve2010-4221 <target>
```

ganglia-info.nse

```bash
nmap -p 8649 --script ganglia-info <target>
```

giop-info.nse

```bash
nmap -p 3260 --script giop-info <target>
```

gkrellm-info.nse

```bash
nmap -p 2605 --script gkrellm-info <target>
```

gopher-ls.nse

```bash
nmap -p 70 --script gopher-ls <target>
```

gpsd-info.nse

```bash
nmap -p 2947 --script gpsd-info <target>
```

hadoop-datanode-info.nse

```bash
nmap -p 50075 --script hadoop-datanode-info <target>
```

hadoop-jobtracker-info.nse

```bash
nmap -p 50030 --script hadoop-jobtracker-info <target>
```

hadoop-namenode-info.nse

```bash
nmap -p 50070 --script hadoop-namenode-info <target>
```

hadoop-secondary-namenode-info.nse

```bash
nmap -p 50090 --script hadoop-secondary-namenode-info <target>
```

hadoop-tasktracker-info.nse

```bash
nmap -p 50060 --script hadoop-tasktracker-info <target>
```

hbase-master-info.nse

```bash
nmap -p 60010 --script hbase-master-info <target>
```

hbase-region-info.nse

```bash
nmap -p 60030 --script hbase-region-info <target>
```

hddtemp-info.nse

```bash
nmap -p 7634 --script hddtemp-info <target>
```

hnap-info.nse

```bash
nmap -p 8080 --script hnap-info <target>
```

hostmap-bfk.nse

```bash
nmap --script hostmap-bfk <target>
```

hostmap-crtsh.nse

```bash
nmap --script hostmap-crtsh <target>
```

hostmap-robtex.nse

```bash
nmap --script hostmap-robtex <target>
```

http-adobe-coldfusion-apsa1301.nse

```bash
nmap -p 80,443 --script http-adobe-coldfusion-apsa1301 <target>
```

http-affiliate-id.nse

```bash
nmap -p 80,443 --script http-affiliate-id <target>
```

http-apache-negotiation.nse

```bash
nmap -p 80,443 --script http-apache-negotiation <target>
```

http-apache-server-status.nse

```bash
nmap -p 80,443 --script http-apache-server-status <target>
```

http-aspnet-debug.nse

```bash
nmap -p 80,443 --script http-aspnet-debug <target>
```

http-auth-finder.nse

```bash
nmap -p 80,443 --script http-auth-finder <target>
```

http-auth.nse

```bash
nmap -p 80,443 --script http-auth <target>
```

http-avaya-ipoffice-users.nse

```bash
nmap -p 80,443 --script http-avaya-ipoffice-users --script-args http-avaya-ipoffice-users.path=<path> <target>
```

http-awstatstotals-exec.nse

```bash
nmap -p 80,443 --script http-awstatstotals-exec <target>
```

http-axis2-dir-traversal.nse

```bash
nmap -p 80,443 --script http-axis2-dir-traversal <target>
```

http-backup-finder.nse

```bash
nmap -p 80,443 --script http-backup-finder <target>
```

http-barracuda-dir-traversal.nse

```bash
nmap -p 80,443 --script http-barracuda-dir-traversal <target>
```

http-bigip-cookie.nse

```bash
nmap -p 80,443 --script http-bigip-cookie <target>
```

http-brute.nse

```bash
nmap -p 80,443 --script http-brute --script-args http-brute.paths=<paths>,http-brute.userdb=<userdb>,http-brute.passdb=<passdb> <target>
```

http-cakephp-version.nse

```bash
nmap -p 80,443 --script http-cakephp-version <target>
```

http-chrono.nse

```bash
nmap -p 80,443 --script http-chrono <target>
```

http-cisco-anyconnect.nse

```bash
nmap -p 80,443 --script http-cisco-anyconnect <target>
```

http-coldfusion-subzero.nse

```bash
nmap -p 80,443 --script http-coldfusion-subzero <target>
```

http-comments-displayer.nse

```bash
nmap -p 80,443 --script http-comments-displayer <target>
```

http-config-backup.nse

```bash
nmap -p 80,443 --script http-config-backup --script-args http-config-backup.backup=<backup_file> <target>
```

http-cookie-flags.nse

```bash
nmap -p 80,443 --script http-cookie-flags <target>
```

http-cors.nse

```bash
nmap -p 80,443 --script http-cors <target>
```

http-cross-domain-policy.nse

```bash
nmap -p 80,443 --script http-cross-domain-policy <target>
```

http-csrf.nse

```bash
nmap -p 80,443 --script http-csrf <target>
```

http-date.nse

```bash
nmap -p 80,443 --script http-date <target>
```

http-default-accounts.nse

```bash
nmap -p 80,443 --script http-default-accounts <target>
```

http-devframework.nse

```bash
nmap -p 80,443 --script http-devframework <target>
```

http-dlink-backdoor.nse

```bash
nmap -p 80,443 --script http-dlink-backdoor <target>
```

http-dombased-xss.nse

```bash
nmap -p 80,443 --script http-dombased-xss <target>
```

http-domino-enum-passwords.nse

```bash
nmap -p 80,443 --script http-domino-enum-passwords --script-args http-domino-enum-passwords.domain=<domain> <target>
```

http-drupal-enum-users.nse

```bash
nmap -p 80,443 --script http-drupal-enum-users --script-args http-drupal-enum-users.url=<url> <target>
```

http-drupal-enum.nse

```bash
nmap -p 80,443 --script http-drupal-enum <target>
```

http-enum.nse

```bash
nmap -p 80,443 --script http-enum <target>
```

http-errors.nse

```bash
nmap -p 80,443 --script http-errors <target>
```

http-exif-spider.nse

```bash
nmap -p80,443 --script http-exif-spider <target>
```

http-favicon.nse

```bash
nmap -p80,443 --script http-favicon <target>
```

http-feed.nse

```bash
nmap -p80,443 --script http-feed <target>
```

http-fetch.nse

```bash
nmap -p80,443 --script http-fetch --script-args http-fetch.url="/robots.txt" <target>
```

http-fileupload-exploiter.nse

```bash
nmap -p80,443 --script http-fileupload-exploiter --script-args http-fileupload-exploiter.cmd="whoami" <target>
```

http-form-brute.nse

```bash
nmap -p80,443 --script http-form-brute --script-args http-form-brute.paths="/login.php,/admin.php" <target>
```

http-form-fuzzer.nse

```bash
nmap -p80,443 --script http-form-fuzzer --script-args http-form-fuzzer.paths="/login.php,/admin.php" <target>
```

http-frontpage-login.nse

```bash
nmap -p80,443 --script http-frontpage-login <target>
```

http-generator.nse

```bash
nmap -p80,443 --script http-generator <target>
```

http-git.nse

```bash
nmap -p80,443 --script http-git <target>
```

http-gitweb-projects-enum.nse

```bash
nmap -p80,443 --script http-gitweb-projects-enum <target>
```

http-google-malware.nse

```bash
nmap -p80,443 --script http-google-malware <target>
```

http-grep.nse

```bash
nmap -p80,443 --script http-grep --script-args http-grep.url="/robots.txt",http-grep.pattern="root" <target>
```

http-headers.nse

```bash
nmap -p80,443 --script http-headers <target>
```

http-hp-ilo-info.nse

```bash
nmap -p80,443 --script http-hp-ilo-info <target>
```

http-huawei-hg5xx-vuln.nse

```bash
nmap -p80,443 --script http-huawei-hg5xx-vuln <target>
```

http-icloud-findmyiphone.nse

```bash
nmap -p80,443 --script http-icloud-findmyiphone <target>
```

http-icloud-sendmsg.nse

```bash
nmap -p80,443 --script http-icloud-sendmsg <target>
```

http-iis-short-name-brute.nse

```bash
nmap -p80,443 --script http-iis-short-name-brute <target>
```

http-iis-webdav-vuln.nse

```bash
nmap -p80,443 --script http-iis-webdav-vuln <target>
```

http-internal-ip-disclosure.nse

```bash
nmap -p80,443 --script http-internal-ip-disclosure <target>
```

http-joomla-brute.nse

```bash
nmap -p80,443 --script http-joomla-brute <target>
```

http-jsonp-detection.nse

```bash
nmap -p80,443 --script http-jsonp-detection <target>
```

http-litespeed-sourcecode-download.nse

```bash
nmap -p80,443 --script http-litespeed-sourcecode-download <target>
```

http-ls.nse

```bash
nmap -p80,443 --script http-ls <target>
```

http-majordomo2-dir-traversal.nse

```bash
nmap -p80,443 --script http-majordomo2-dir-traversal <target>
```

http-malware-host.nse

```bash
nmap -p80,443 --script http-malware-host <target>
```

http-mcmp.nse

```bash
nmap -p80,443 --script http-mcmp <target>
```

http-method-tamper.nse

```bash
nmap -p80,443 --script http-method-tamper <target>
```

http-methods.nse

```bash
nmap -p80,443 --script http-methods <target>
```

http-mobileversion-checker.nse

```bash
nmap -p80,443 --script http-mobileversion-checker <target>
```

http-ntlm-info.nse

```bash
nmap -p80,443 --script http-ntlm-info <target>
```

http-open-proxy.nse

```bash
nmap -p80,443 --script http-open-proxy <target>
```

http-open-redirect.nse

```bash
nmap -p80,443 --script http-open-redirect <target>
```

http-passwd.nse

```bash
nmap -p80,443 --script http-passwd <target>
```

http-php-version.nse

```bash
nmap -p80,443 --script http-php-version <target>
```

http-phpmyadmin-dir-traversal.nse

```bash
nmap -p80,443 --script http-phpmyadmin-dir-traversal <target>
```

http-phpself-xss.nse

```bash
nmap -p80,443 --script http-phpself-xss <target>
```

http-proxy-brute.nse

```bash
nmap -p80,443 --script http-proxy-brute <target>
```

http-put.nse

```bash
nmap -p80,443 --script http-put <target>
```

http-qnap-nas-info.nse

```bash
nmap -p80,443 --script http-qnap-nas-info <target>
```

http-referer-checker.nse

```bash
nmap -p80,443 --script http-referer-checker <target>
```

http-rfi-spider.nse

```bash
nmap -p80,443 --script http-rfi-spider <target>
```

http-robots.txt.nse

```bash
nmap -p80,443 --script http-robots.txt <target>
```

http-robtex-reverse-ip.nse

```bash
nmap -p80,443 --script http-robtex-reverse-ip <target>
```

http-robtex-shared-ns.nse

```bash
nmap -p80,443 --script http-robtex-shared-ns <target>
```

http-sap-netweaver-leak.nse

```bash
nmap -p80,443 --script http-sap-netweaver-leak <target>
```

http-security-headers.nse

```bash
nmap -p80,443 --script http-security-headers <target>
```

http-server-header.nse

```bash
nmap -p80,443 --script http-server-header <target>
```

http-shellshock.nse

```bash
nmap -p80,443 --script http-shellshock <target>
```

http-sitemap-generator.nse

```bash
nmap -p80,443 --script http-sitemap-generator <target>
```

http-slowloris-check.nse

```bash
nmap -p80,443 --script http-slowloris-check <target>
```

http-slowloris.nse

```bash
nmap -p80,443 --script http-slowloris <target>
```

http-sql-injection.nse

```bash
nmap -p80,443 --script http-sql-injection <target>
```

http-stored-xss.nse

```bash
nmap -p80,443 --script http-stored-xss <target>
```

http-svn-enum.nse

```bash
nmap -p80,443 --script http-svn-enum <target>
```

http-svn-info.nse

```bash
nmap -p80,443 --script http-svn-info <target>
```

http-title.nse

```bash
nmap -p80,443 --script http-title <target>
```

http-tplink-dir-traversal.nse

```bash
nmap -p80,443 --script http-tplink-dir-traversal <target>
```

http-trace.nse

```bash
nmap -p80,443 --script http-trace <target>
```

http-trace.nse

```bash
nmap -p80,443 --script http-trace <target>
```

http-traceroute.nse

```bash
nmap -p80,443 --script http-traceroute <target>
```

http-trane-info.nse

```bash
nmap -p80,443 --script http-trane-info <target>
```

http-unsafe-output-escaping.nse

```bash
nmap -p80,443 --script http-unsafe-output-escaping <target>
```

http-useragent-tester.nse

```bash
nmap -p80,443 --script http-useragent-tester <target>
```

http-userdir-enum.nse

```bash
nmap -p80,443 --script http-userdir-enum <target>
```

http-vhosts.nse

```bash
nmap -p80,443 --script http-vhosts <target>
```

http-virustotal.nse

```bash
nmap -p80,443 --script http-virustotal <target>
```

http-vlcstreamer-ls.nse

```bash
nmap -p80,443 --script http-vlcstreamer-ls <target>
```

http-vmware-path-vuln.nse

```bash
nmap -p80,443 --script http-vmware-path-vuln <target>
```

http-vuln-cve2006-3392.nse

```bash
nmap -p80,443 --script http-vuln-cve2006-3392 <target>
```

http-vuln-cve2009-3960.nse

```bash
nmap -p80,443 --script http-vuln-cve2009-3960 <target>
```

http-vuln-cve2010-0738.nse

```bash
nmap -p80,443 --script http-vuln-cve2010-0738 <target>
```

http-vuln-cve2010-2861.nse

```bash
nmap -p80,443 --script http-vuln-cve2010-2861 <target>
```

http-vuln-cve2011-3192.nse

```bash
nmap -p80,443 --script http-vuln-cve2011-3192 <target>
```

http-vuln-cve2011-3368.nse

```bash
nmap -p80,443 --script http-vuln-cve2011-3368 <target>
```

http-vuln-cve2012-1823.nse

```bash
nmap -p80,443 --script http-vuln-cve2012-1823 <target>
```

http-vuln-cve2013-0156.nse

```bash
nmap -p80,443 --script http-vuln-cve2013-0156 <target>
```

http-vuln-cve2013-6786.nse

```bash
nmap -p80,443 --script http-vuln-cve2013-6786 <target>
```

http-vuln-cve2013-7091.nse

```bash
nmap -p80,443 --script http-vuln-cve2013-7091 <target>
```

http-vuln-cve2014-2126.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-2126 <target>
```

http-vuln-cve2014-2127.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-2127 <target>
```

http-vuln-cve2014-2128.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-2128 <target>
```

http-vuln-cve2014-2129.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-2129 <target>
```

http-vuln-cve2014-3704.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-3704 <target>
```

http-vuln-cve2014-8877.nse

```bash
nmap -p80,443 --script http-vuln-cve2014-8877 <target>
```

http-vuln-cve2015-1427.nse

```bash
nmap -p80,443 --script http-vuln-cve2015-1427 <target>
```

http-vuln-cve2015-1635.nse

```bash
nmap -p80,443 --script http-vuln-cve2015-1635 <target>
```

http-vuln-cve2017-1001000.nse

```bash
nmap -p80,443 --script http-vuln-cve2017-1001000 <target>
```

http-vuln-cve2017-5638.nse

```bash
nmap -p80,443 --script http-vuln-cve2017-5638 <target>
```

http-vuln-cve2017-5689.nse

```bash
nmap -p80,443 --script http-vuln-cve2017-5689 <target>
```

http-vuln-cve2017-8917.nse

```bash
nmap -p80,443 --script http-vuln-cve2017-8917 <target>
```

http-vuln-misfortune-cookie.nse

```bash
nmap -p80,443 --script http-vuln-misfortune-cookie <target>
```

http-vuln-wnr1000-creds.nse

```bash
nmap -p80,443 --script http-vuln-wnr1000-creds <target>
```
http-waf-detect.nse

```bash
nmap -p80,443 --script http-waf-detect <target>
```

http-waf-fingerprint.nse

```bash
nmap -p80,443 --script http-waf-fingerprint <target>
```

http-webdav-scan.nse

```bash
nmap -p80,443 --script http-webdav-scan <target>
```

http-wordpress-brute.nse

```bash
nmap -p80 --script http-wordpress-brute --script-args userdb=/path/to/user/list.txt <target>
```

http-wordpress-enum.nse

```bash
nmap -p80 --script http-wordpress-enum <target>
```

http-wordpress-users.nse

```bash
nmap -p80 --script http-wordpress-users --script-args limit=50 <target>
```

http-xssed.nse

```bash
nmap -p80 --script http-xssed <target>
```

https-redirect.nse

```bash
nmap -p443 --script https-redirect <target>
```

iax2-brute.nse

```bash
nmap -p5034 --script iax2-brute --script-args userdb=/path/to/user/list.txt <target>
```

iax2-version.nse

```bash
nmap -p5034 --script iax2-version <target>
```

icap-info.nse

```bash
nmap -p1344 --script icap-info <target>
```

iec-identify.nse

```bash
nmap -p6000-6005 --script iec-identify <target>
```

ike-version.nse

```bash
nmap -p500 --script ike-version <target>
```

imap-brute.nse

```bash
nmap -p143 --script imap-brute --script-args userdb=/path/to/user/list.txt <target>
```

imap-capabilities.nse

```bash
nmap -p143 --script imap-capabilities <target>
```

imap-ntlm-info.nse

```bash
nmap -p143 --script imap-ntlm-info <target>
```

impress-remote-discover.nse

```bash
nmap -p3251 --script impress-remote-discover <target>
```

informix-brute.nse

```bash
nmap -p9088 --script informix-brute --script-args userdb=/path/to/user/list.txt <target>
```

informix-query.nse

```bash
nmap -p9088 --script informix-query <target>
```

informix-tables.nse

```bash
nmap -p9088 --script informix-tables <target>
```

ip-forwarding.nse

```bash
nmap -p80 --script ip-forwarding <target>
```

ip-geolocation-geoplugin.nse

```bash
nmap -p80 --script ip-geolocation-geoplugin <target>
```

ip-geolocation-ipinfodb.nse

```bash
nmap -p80 --script ip-geolocation-ipinfodb <target>
```

ip-geolocation-map-bing.nse

```bash
nmap -p80 --script ip-geolocation-map-bing <target>
```

ip-geolocation-map-google.nse

```bash
nmap -p80 --script ip-geolocation-map-google <target>
```

ip-geolocation-map-kml.nse

```bash
nmap -p80 --script ip-geolocation-map-kml <target>
```

ip-geolocation-maxmind.nse

```bash
nmap -p80 --script ip-geolocation-maxmind <target>
```

ip-https-discover.nse

```bash
nmap -p443 --script ip-https-discover <target>
```

ipidseq.nse

```bash
nmap -p1645 --script ipidseq <target>
```

ipmi-brute.nse

```bash
nmap -p623 --script ipmi-brute --script-args userdb=/path/to/user/list.txt <target>
```

ipmi-cipher-zero.nse

```bash
nmap -p623 --script ipmi-cipher-zero <target>
```

ipmi-version.nse

```bash
nmap -p623 --script ipmi-version <target>
```

ipv6-multicast-mld-list.nse

```bash
nmap -p5890 --script ipv6-multicast-mld-list <target>
```

ipv6-node-info.nse

```bash
nmap -p5890 --script ipv6-node-info <target>
```

ipv6-ra-flood.nse

```bash
nmap -p5890 --script ipv6-ra-flood <target>
```

irc-botnet-channels.nse

```bash
nmap -p6667 --script irc-botnet-channels <target>
```

irc-brute.nse

```bash
nmap -p6667 --script irc-brute --script-args userdb=/path/to/user/list.txt <target>
```

irc-info.nse

```bash
nmap -p6667 --script irc-info <target>
```

irc-sasl-brute.nse

```bash
nmap -p6667 --script irc-sasl-brute --script-args userdb=/path/to/user/list.txt <target>
```

irc-unrealircd-backdoor.nse

```bash
nmap -p6667 --script irc-unrealircd-backdoor <target>
```

iscsi-brute.nse

```bash
nmap -p3260 --script iscsi-brute --script-args userdb=/path/to/user/list.txt <target>
```

iscsi-info.nse

```bash
nmap -p3260 --script iscsi-info <target>
```

isns-info.nse

```bash
nmap -p1900 --script isns-info <target>
```

jdwp-exec.nse

```bash
nmap -p8080 --script jdwp-exec <target>
```

jdwp-info.nse

```bash
nmap -p8080 --script jdwp-info <target>
```

jdwp-inject.nse

```bash
nmap -p8080 --script jdwp-inject <target>
```

jdwp-version.nse

```bash
nmap -p8080 --script jdwp-version <target>
```

knx-gateway-discover.nse

```bash
nmap -p3671 --script knx-gateway-discover <target>
```

knx-gateway-info.nse:

```bash
nmap -p3671 --script knx-gateway-info <target>
```

krb5-enum-users.nse

```bash
nmap -p88 --script krb5-enum-users --script-args userdb=/path/to/user/list.txt <target>
```

ldap-brute.nse

```bash
nmap -p389 --script ldap-brute --script-args userdb=/path/to/user/list.txt <target>
```

ldap-novell-getpass.nse

```bash
nmap -p389 --script ldap-novell-getpass <target>
```

ldap-rootdse.nse

```bash
nmap -p389 --script ldap-rootdse <target>
```

ldap-search.nse

```bash
nmap -p389 --script ldap-search --script-args 'base="dc=example,dc=com"' <target>
```

lexmark-config.nse

```bash
nmap -p9100 --script lexmark-config <target>
```

llmnr-resolve.nse

```bash
nmap -p5353 --script llmnr-resolve <target>
```

lltd-discovery.nse

```bash
nmap -p8080 --script lltd-discovery <target>
```

lu-enum.nse

```bash
nmap -p8080 --script lu-enum <target>
```

maxdb-info.nse

```bash
nmap -p7299 --script maxdb-info <target>
```

mcafee-epo-agent.nse

```bash
nmap -p80 --script mcafee-epo-agent <target>
```

membase-brute.nse

```bash
nmap -p11210 --script membase-brute --script-args userdb=/path/to/user/list.txt <target>
```

membase-http-info.nse

```bash
nmap -p8091 --script membase-http-info <target>
```

memcached-info.nse

```bash
nmap -p11211 --script memcached-info <target>
```

metasploit-info.nse

```bash
nmap -p4444 --script metasploit-info <target>
```

metasploit-msgrpc-brute.nse

```bash
nmap -p55553 --script metasploit-msgrpc-brute --script-args userdb=/path/to/user/list.txt <target>
```

metasploit-xmlrpc-brute.nse

```bash
nmap -p55552 --script metasploit-xmlrpc-brute --script-args userdb=/path/to/user/list.txt <target>
```

mikrotik-routeros-brute.nse

```bash
nmap -p8728 --script mikrotik-routeros-brute --script-args userdb=/path/to/user/list.txt <target>
```

mmouse-brute.nse

```bash
nmap -p4004 --script mmouse-brute --script-args userdb=/path/to/user/list.txt <target>
```

mmouse-exec.nse

```bash
nmap -p4004 --script mmouse-exec <target>
```

modbus-discover.nse

```bash
nmap -p502 --script modbus-discover <target>
```

mongodb-brute.nse

```bash
nmap -p27017 --script mongodb-brute --script-args userdb=/path/to/user/list.txt <target>
```

mongodb-databases.nse

```bash
nmap -p27017 --script mongodb-databases <target>
```

mongodb-info.nse

```bash
nmap -p27017 --script mongodb-info <target>
```

mqtt-subscribe.nse

```bash
nmap -p1883 --script mqtt-subscribe <target>
```

mrinfo.nse

```bash
nmap -p870 --script mrinfo <target>
```

ms-sql-brute.nse

```bash
nmap -p1433 --script ms-sql-brute --script-args userdb=/path/to/user/list.txt <target>
```

ms-sql-config.nse

```bash
nmap -p1433 --script ms-sql-config <target>
```

ms-sql-dac.nse

```bash
nmap -p1433 --script ms-sql-dac <target>
```

ms-sql-dump-hashes.nse

```bash
nmap -p1433 --script ms-sql-dump-hashes <target>
```

ms-sql-empty-password.nse

```bash
nmap -p1433 --script ms-sql-empty-password <target>
```

ms-sql-hasdbaccess.nse

```bash
nmap -p1433 --script ms-sql-hasdbaccess <target>
```

ms-sql-info.nse

```bash
nmap -p1433 --script ms-sql-info <target>
```

ms-sql-ntlm-info.nse

```bash
nmap -p1433 --script ms-sql-ntlm-info <target>
```

ms-sql-query.nse

```bash
nmap -p1433 --script ms-sql-query --script-args mssql.username=sa,mssql.password=Password123,ms-sql-query.query="SELECT * FROM users" <target>
```

ms-sql-tables.nse

```bash
nmap -p1433 --script ms-sql-tables <target>
```

ms-sql-xp-cmdshell.nse

```bash
nmap -p1433 --script ms-sql-xp-cmdshell <target>
```

msrpc-enum.nse

```bash
nmap -p135 --script msrpc-enum <target>
```

mtrace.nse

```bash
nmap -p8080 --script mtrace <target>
```

mtrace.nse

```bash
nmap -p8080 --script mtrace <target>
```

murmur-version.nse

```bash
nmap -p64738 --script murmur-version <target>
```

mysql-audit.nse

```bash
nmap -p3306 --script mysql-audit --script-args mysql-audit.username=root,mysql-audit.password=password <target>
```

mysql-brute.nse

```bash
nmap -p3306 --script mysql-brute --script-args userdb=/path/to/user/list.txt <target>
```

mysql-databases.nse

```bash
nmap -p3306 --script mysql-databases --script-args mysql-databases.username=root,mysql-databases.password=password <target>
```

mysql-dump-hashes.nse

```bash
nmap -p3306 --script mysql-dump-hashes --script-args mysql-dump-hashes.username=root,mysql-dump-hashes.password=password <target>
```

mysql-empty-password.nse

```bash
nmap -p3306 --script mysql-empty-password <target>
```

mysql-enum.nse

```bash
nmap -p3306 --script mysql-enum <target>
```

mysql-info.nse

```bash
nmap -p3306 --script mysql-info <target>
```

mysql-query.nse

```bash
nmap -p3306 --script mysql-query --script-args mysql-query.username=root,mysql-query.password=password,mysql-query.query="SELECT * FROM users" <target>
```

mysql-users.nse

```bash
nmap -p3306 --script mysql-users --script-args mysql-users.username=root,mysql-users.password=password <target>
```

mysql-variables.nse

```bash
nmap -p3306 --script mysql-variables --script-args mysql-variables.username=root,mysql-variables.password=password <target>
```

mysql-vuln-cve2012-2122.nse

```bash
nmap -p3306 --script mysql-vuln-cve2012-2122 <target>
```

nat-pmp-info.nse

```bash
nmap -p5351 --script nat-pmp-info <target>
```

nat-pmp-mapport.nse

```bash
nmap -p5351 --script nat-pmp-mapport --script-args nat-pmp-mapport.port=1234 <target>
```

nbd-info.nse

```bash
nmap -p10000 --script nbd-info <target>
```

nbns-interfaces.nse

```bash
nmap -p137 --script nbns-interfaces <target>
```

nbstat.nse

```bash
nmap -p137 --script nbstat <target>
```

ncp-enum-users.nse

```bash
nmap -p1524 --script ncp-enum-users --script-args ncp-enum-users.username=admin,ncp-enum-users.password=password <target>
```

ncp-serverinfo.nse

```bash
nmap -p1524 --script ncp-serverinfo <target>
```

ndmp-fs-info.nse

```bash
nmap -p1006 --script ndmp-fs-info <target>
```

ndmp-version.nse

```bash
nmap -p1006 --script ndmp-version <target>
```

nessus-brute.nse

```bash
nmap -p8834 --script nessus-brute --script-args userdb=/path/to/user/list.txt <target>
```

nessus-xmlrpc-brute.nse

```bash
nmap -p8834 --script nessus-xmlrpc-brute --script-args userdb=/path/to/user/list.txt <target>
```

netbus-auth-bypass.nse

```bash
nmap -p1536 --script netbus-auth-bypass --script-args netbus-auth-bypass.username=admin,netbus-auth-bypass.password=password <target>
```

netbus-brute.nse

```bash
nmap -p1536 --script netbus-brute --script-args userdb=/path/to/user/list.txt <target>
```

netbus-info.nse

```bash
nmap -p1536 --script netbus-info <target>
```

netbus-version.nse

```bash
nmap -p1536 --script netbus-version <target>
```

nexpose-brute.nse

```bash
nmap -p3780 --script nexpose-brute --script-args userdb=/path/to/user/list.txt <target>
```

nfs-ls.nse

```bash
nmap -p111 --script nfs-ls <target>
```

nfs-showmount.nse

```bash
nmap -p111 --script nfs-showmount <target>
```

nfs-statfs.nse

```bash
nmap -p111 --script nfs-statfs <target>
```

nje-node-brute.nse

```bash
nmap -p4444 --script nje-node-brute --script-args userdb=/path/to/user/list.txt <target>
```

nje-pass-brute.nse

```bash
nmap -p4444 --script nje-pass-brute --script-args userdb=/path/to/user/list.txt <target>
```

nntp-ntlm-info.nse

```bash
nmap -p119 --script nntp-ntlm-info <target>
```

nping-brute.nse

```bash
nmap -p80 --script nping-brute --script-args userdb=/path/to/user/list.txt <target>
```

nrpe-enum.nse

```bash
nmap -p5666 --script nrpe-enum <target>
```

ntp-info.nse

```bash
nmap -p123 --script ntp-info <target>
```

ntp-monlist.nse

```bash
nmap -p123 --script ntp-monlist <target>
```

omp2-brute.nse

```bash
nmap -p10800 --script omp2-brute --script-args userdb=/path/to/user/list.txt <target>
```

omp2-enum-targets.nse

```bash
nmap -p10800 --script omp2-enum-targets <target>
```
