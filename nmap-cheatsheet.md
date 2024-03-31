# NMap NSE Cheat Sheet

This nmap nse cheatsheet was created to show the correct usage for each of the official nse scripts.

- afp-ls.nse
`nmap -p 548 --script afp-ls --script-args afp-ls.timeout=4s,afp-ls.max-retries=3 <target>`

- afp-path-vuln.nse
`nmap -p 548 --script afp-path-vuln --script-args afp-path-vuln.timeout=4s,afp-path-vuln.max-retries=3 <target>`

- afp-serverinfo.nse
`nmap -p 548 --script afp-serverinfo --script-args afp-serverinfo.timeout=4s,afp-serverinfo.max-retries=3 <target>`

- afp-showmount.nse
`nmap -p 548 --script afp-showmount --script-args afp-showmount.timeout=4s,afp-showmount.max-retries=3 <target>`

- ajp-auth.nse
`nmap -p 8009 --script ajp-auth --script-args ajp-auth.path=/manager/html,ajp-auth.user=tomcat,ajp-auth.pass=s3cret <target>`

- ajp-brute.nse
`nmap -p 8009 --script ajp-brute --script-args ajp-brute.path=/manager/html,ajp-brute.userdb=users.txt,ajp-brute.passdb=passwords.txt,ajp-brute.timeout=4s,ajp-brute.max-retries=3 <target>`

- ajp-headers.nse
`nmap -p 8009 --script ajp-headers --script-args ajp-headers.path=/manager/html <target>`

- ajp-methods.nse
`nmap -p 8009 --script ajp-methods --script-args ajp-methods.path=/manager/html <target>`

- ajp-request.nse
`nmap -p 8009 --script ajp-request --script-args ajp-request.path=/manager/html <target>`

- allseeingeye-info.nse
`nmap -p 8009 --script allseeingeye-info --script-args allseeingeye-info.timeout=4s,allseeingeye-info.max-retries=3 <target>`

- amqp-info.nse
`nmap -p 5672 --script amqp-info --script-args amqp-info.timeout=4s,amqp-info.max-retries=3 <target>`

- asn-query.nse
`nmap -p 53 --script asn-query --script-args asn-query.timeout=4s,asn-query.max-retries=3 <target>`

- auth-owners.nse
`nmap -p 22 --script auth-owners --script-args auth-owners.timeout=4s,auth-owners.max-retries=3 <target>`

- auth-spoof.nse
`nmap -p 22 --script auth-spoof --script-args auth-spoof.timeout=4s,auth-spoof.max-retries=3 <target>`

- backorifice-brute.nse
`nmap -p 80 --script backorifice-brute --script-args backorifice-brute.userdb=users.txt,backorifice-brute.passdb=passwords.txt,backorifice-brute.timeout=4s,backorifice-brute.max-retries=3 <target>`

- backorifice-info.nse
`nmap -p 80 --script backorifice-info --script-args backorifice-info.timeout=4s,backorifice-info.max-retries=3 <target>`

- bacnet-info.nse
`nmap -p 47808 --script bacnet-info --script-args bacnet-info.timeout=4s,bacnet-info.max-retries=3 <target>`

- banner.nse
`nmap -p 22,80 --script banner --script-args banner.timeout=4s,banner.max-retries=3 <target>`

- bitcoin-getaddr.nse
`nmap -p 9332 --script bitcoin-getaddr --script-args bitcoin-getaddr.timeout=4s,bitcoin-getaddr.max-retries=3 <target>`

- bitcoin-info.nse
`nmap -p 8332 --script bitcoin-info --script-args bitcoin-info.timeout=4s,bitcoin-info.max-retries=3 <target>`

- bitcoinrpc-info.nse
`nmap -p 8332 --script bitcoinrpc-info --script-args bitcoinrpc-info.timeout=4s,bitcoinrpc-info.max-retries=3 <target>`

- bittorrent-discovery.nse
`nmap -p 6881 --script bittorrent-discovery --script-args bittorrent-discovery.timeout=4s,bittorrent-discovery.max-retries=3 <target>`

- bjnp-discover.nse
`nmap -p 623 --script bjnp-discover --script-args bjnp-discover.timeout=4s,bjnp-discover.max-retries=3 <target>`

- broadcast-ataoe-discover.nse
`nmap -p 427 --script broadcast-ataoe-discover --script-args broadcast-ataoe-discover.timeout=4s,broadcast-ataoe-discover.max-retries=3 <target>`

- broadcast-avahi-dos.nse
`nmap -p 5353 --script broadcast-avahi-dos --script-args broadcast-avahi-dos.timeout=4s,broadcast-avahi-dos.max-retries=3 <target>`

- broadcast-bjnp-discover.nse
`nmap -p 623 --script broadcast-bjnp-discover --script-args broadcast-bjnp-discover.timeout=4s,broadcast-bjnp-discover.max-retries=3 <target>`

- broadcast-db2-discover.nse
`nmap -p 623 --script broadcast-db2-discover --script-args broadcast-db2-discover.timeout=4s,broadcast-db2-discover.max-retries=3 <target>`

- broadcast-dhcp-discover.nse
`nmap -p 67 --script broadcast-dhcp-discover --script-args broadcast-dhcp-discover.timeout=4s,broadcast-dhcp-discover.max-retries=3 <target>`

- broadcast-dhcp6-discover.nse
`nmap -p 547 --script broadcast-dhcp6-discover --script-args broadcast-dhcp6-discover.timeout=4s,broadcast-dhcp6-discover.max-retries=3 <target>`

- broadcast-dns-service-discovery.nse
`nmap -p 5353 --script broadcast-dns-service-discovery --script-args broadcast-dns-service-discovery.timeout=4s,broadcast-dns-service-discovery.max-retries=3 <target>`

- broadcast-dropbox-listener.nse
`nmap -p 17500 --script broadcast-dropbox-listener --script-args broadcast-dropbox-listener.timeout=4s,broadcast-dropbox-listener.max-retries=3 <target>`

- broadcast-eigrp-discovery.nse
`nmap -p 521 --script broadcast-eigrp-discovery --script-args broadcast-eigrp-discovery.timeout=4s,broadcast-eigrp-discovery.max-retries=3 <target>`

- broadcast-hid-discoveryd.nse
`nmap -p 635 --script broadcast-hid-discoveryd --script-args broadcast-hid-discoveryd.timeout=4s,broadcast-hid-discoveryd.max-retries=3 <target>`

- broadcast-igmp-discovery.nse
`nmap -p 521 --script broadcast-igmp-discovery --script-args broadcast-igmp-discovery.timeout=4s,broadcast-igmp-discovery.max-retries=3 <target>`

- broadcast-jenkins-discover.nse
`nmap -p 8080 --script broadcast-jenkins-discover --script-args broadcast-jenkins-discover.timeout=4s,broadcast-jenkins-discover.max-retries=3 <target>`

- broadcast-listener.nse
`nmap -p 5353 --script broadcast-listener --script-args broadcast-listener.timeout=4s,broadcast-listener.max-retries=3 <target>`

- broadcast-ms-sql-discover.nse
`nmap -p 1434 --script broadcast-ms-sql-discover --script-args broadcast-ms-sql-discover.timeout=4s,broadcast-ms-sql-discover.max-retries=3 <target>`

- broadcast-netbios-master-browser.nse
`nmap -p 137 --script broadcast-netbios-master-browser --script-args broadcast-netbios-master-browser.timeout=4s,broadcast-netbios-master-browser.max-retries=3 <target>`

- broadcast-networker-discover.nse
`nmap -p 137 --script broadcast-networker-discover --script-args broadcast-networker-discover.timeout=4s,broadcast-networker-discover.max-retries=3 <target>`

- broadcast-novell-locate.nse
`nmap -p 137 --script broadcast-novell-locate --script-args broadcast-novell-locate.timeout=4s,broadcast-novell-locate.max-retries=3 <target>`

- broadcast-ospf2-discover.nse
`nmap -p 89 --script broadcast-ospf2-discover --script-args broadcast-ospf2-discover.timeout=4s,broadcast-ospf2-discover.max-retries=3 <target>`

- broadcast-pc-anywhere.nse
`nmap -p 5350 --script broadcast-pc-anywhere --script-args broadcast-pc-anywhere.timeout=4s,broadcast-pc-anywhere.max-retries=3 <target>`

- broadcast-pc-duo.nse
`nmap -p 5351 --script broadcast-pc-duo --script-args broadcast-pc-duo.timeout=4s,broadcast-pc-duo.max-retries=3 <target>`

- broadcast-pim-discovery.nse
`nmap -p 521 --script broadcast-pim-discovery --script-args broadcast-pim-discovery.timeout=4s,broadcast-pim-discovery.max-retries=3 <target>`

- broadcast-ping.nse
`nmap -p 7 --script broadcast-ping --script-args broadcast-ping.timeout=4s,broadcast-ping.max-retries=3 <target>`

- broadcast-pppoe-discover.nse
`nmap -p 4379 --script broadcast-pppoe-discover --script-args broadcast-pppoe-discover.timeout=4s,broadcast-pppoe-discover.max-retries=3 <target>`

- broadcast-rip-discover.nse
`nmap -p 520 --script broadcast-rip-discover --script-args broadcast-rip-discover.timeout=4s,broadcast-rip-discover.max-retries=3 <target>`

- broadcast-ripng-discover.nse
`nmap -p 521 --script broadcast-ripng-discover --script-args broadcast-ripng-discover.timeout=4s,broadcast-ripng-discover.max-retries=3 <target>`

- broadcast-sonicwall-discover.nse
`nmap -p 1900 --script broadcast-sonicwall-discover --script-args broadcast-sonicwall-discover.timeout=4s,broadcast-sonicwall-discover.max-retries=3 <target>`

- broadcast-sybase-asa-discover.nse
`nmap -p 1521 --script broadcast-sybase-asa-discover --script-args broadcast-sybase-asa-discover.timeout=4s,broadcast-sybase-asa-discover.max-retries=3 <target>`

- broadcast-tellstick-discover.nse
`nmap -p 1900 --script broadcast-tellstick-discover --script-args broadcast-tellstick-discover.timeout=4s,broadcast-tellstick-discover.max-retries=3 <target>`

- broadcast-upnp-info.nse
`nmap -p 1900 --script broadcast-upnp-info --script-args broadcast-upnp-info.timeout=4s,broadcast-upnp-info.max-retries=3 <target>`

- broadcast-versant-locate.nse
`nmap -p 137 --script broadcast-versant-locate --script-args broadcast-versant-locate.timeout=4s,broadcast-versant-locate.max-retries=3 <target>`

- broadcast-wake-on-lan.nse
`nmap -p 9 --script broadcast-wake-on-lan --script-args broadcast-wake-on-lan.timeout=4s,broadcast-wake-on-lan.max-retries=3 <target>`

- broadcast-wpad-discover.nse
`nmap -p 3702 --script broadcast-wpad-discover --script-args broadcast-wpad-discover.timeout=4s,broadcast-wpad-discover.max-retries=3 <target>`

- broadcast-wsdd-discover.nse
`nmap -p 3702 --script broadcast-wsdd-discover --script-args broadcast-wsdd-discover.timeout=4s,broadcast-wsdd-discover.max-retries=3 <target>`

- broadcast-xdmcp-discover.nse
`nmap -p 6000 --script broadcast-xdmcp-discover --script-args broadcast-xdmcp-discover.timeout=4s,broadcast-xdmcp-discover.max-retries=3 <target>`

- cassandra-brute.nse
`nmap -p 9160 --script cassandra-brute --script-args cassandra-brute.userdb=users.txt,cassandra-brute.passdb=passwords.txt,cassandra-brute.timeout=4s,cassandra-brute.max-retries=3 <target>`

- cassandra-info.nse
`nmap -p 9160 --script cassandra-info --script-args cassandra-info.timeout=4s,cassandra-info.max-retries=3 <target>`

- cccam-version.nse
`nmap -p 5200 --script cccam-version --script-args cccam-version.timeout=4s,cccam-version.max-retries=3 <target>`

- cics-enum.nse
`nmap -p 3270 --script cics-enum --script-args cics-enum.timeout=4s,cics-enum.max-retries=3 <target>`

- cics-info.nse
`nmap -p 3270 --script cics-info --script-args cics-info.timeout=4s,cics-info.max-retries=3 <target>`

- cics-user-brute.nse
`nmap -p 3270 --script cics-user-brute --script-args cics-user-brute.userdb=users.txt,cics-user-brute.passdb=passwords.txt,cics-user-brute.timeout=4s,cics-user-brute.max-retries=3 <target>`

- cics-user-enum.nse
`nmap -p 3270 --script cics-user-enum --script-args cics-user-enum.timeout=4s,cics-user-enum.max-retries=3 <target>`

- citrix-brute-xml.nse
`nmap -p 443 --script citrix-brute-xml --script-args citrix-brute-xml.userdb=users.txt,citrix-brute-xml.passdb=passwords.txt,citrix-brute-xml.timeout=4s,citrix-brute-xml.max-retries=3 <target>`

- citrix-enum-apps-xml.nse
`nmap -p 443 --script citrix-enum-apps-xml --script-args citrix-enum-apps-xml.timeout=4s,citrix-enum-apps-xml.max-retries=3 <target>`

- citrix-enum-apps.nse
`nmap -p 443 --script citrix-enum-apps --script-args citrix-enum-apps.timeout=4s,citrix-enum-apps.max-retries=3 <target>`

- citrix-enum-servers-xml.nse
`nmap -p 443 --script citrix-enum-servers-xml --script-args citrix-enum-servers-xml.timeout=4s,citrix-enum-servers-xml.max-retries=3 <target>`

- citrix-enum-servers.nse
`nmap -p 443 --script citrix-enum-servers --script-args citrix-enum-servers.timeout=4s,citrix-enum-servers.max-retries=3 <target>`

- clamav-exec.nse
`nmap -p 3310 --script clamav-exec --script-args clamav-exec.cmd="ls",clamav-exec.timeout=4s,clamav-exec.max-retries=3 <target>`

- clock-skew.nse
`nmap -p 13,37,53,123 --script clock-skew --script-args clock-skew.timeout=4s,clock-skew.max-retries=3 <target>`

- coap-resources.nse
`nmap -p 5683 --script coap-resources <target>`

- couchdb-databases.nse
`nmap -p 5984 --script couchdb-databases <target>`

- couchdb-stats.nse
`nmap -p 5984 --script couchdb-databases <target>`

- creds-summary.nse
`nmap -p 5984 --script couchdb-stats <target>`

- cups-info.nse
`nmap -p 631 --script cups-info <target>`

- cups-queue-info.nse
`nmap -p 631 --script cups-queue-info <target>`

- cvs-brute-repository.nse
`nmap --script cvs-brute-repository --script-args cvs-brute-repository.repository=<repo>,cvs-brute-repository.module=<module> <target>`

- cvs-brute.nse
`nmap -p 2401 --script cvs-brute --script-args cvs-brute.host=<host>,cvs-brute.module=<module> <target>`

- daap-get-library.nse
`nmap -p 3689 --script daap-get-library <target>`

- daytime.nse
`nmap -p 13 --script daytime <target>`

- db2-das-info.nse
`nmap -p 50000 --script db2-das-info <target>`

- deluge-rpc-brute.nse
`nmap -p 58846 --script deluge-rpc-brute --script-args deluge-rpc-brute.passwords=<password_file> <target>`

- dhcp-discover.nse
`nmap -p 67 --script dhcp-discover <target>`

- dicom-brute.nse
`nmap -p 104 --script dicom-brute --script-args dicom-brute.hostname=<host>,dicom-brute.password=<password> <target>`

- dicom-ping.nse
`nmap -p 104 --script dicom-ping <target>`

- dict-info.nse
`nmap -p 21 --script dict-info <target>`

- distcc-cve2004-2687.nse
`nmap -p 3632 --script distcc-cve2004-2687 <target>`

- dns-blacklist.nse
`nmap --script dns-blacklist --script-args dns-blacklist.hostname=<hostname> <target>`

- dns-brute.nse
`nmap --script dns-brute --script-args dns-brute.domain=<domain> <target>`

- dns-cache-snoop.nse
`nmap -p 53 --script dns-cache-snoop <target>`

- dns-check-zone.nse
`nmap --script dns-check-zone --script-args dns-check-zone.domain=<domain> <target>`

- dns-client-subnet-scan.nse
`nmap -p 53 --script dns-client-subnet-scan --script-args dns-client-subnet-scan.domain=<domain> <target>`

- dns-fuzz.nse
`nmap -p 53 --script dns-fuzz <target>`

- dns-ip6-arpa-scan.nse
`nmap -p 53 --script dns-ip6-arpa-scan --script-args dns-ip6-arpa-scan.domain=<domain> <target>`

- dns-nsec-enum.nse
`nmap -p 53 --script dns-nsec3-enum --script-args dns-nsec3-enum.domain=<domain> <target>`

- dns-nsec3-enum.nse
`nmap -p 53 --script dns-nsec3-enum --script-args dns-nsec3-enum.domain=<domain> <target>`

- dns-nsid.nse
`nmap -p 53 --script dns-nsid <target>`

- dns-random-srcport.nse
`nmap -p 53 --script dns-random-srcport <target>`

- dns-random-txid.nse
`nmap -p 53 --script dns-random-txid <target>`

- dns-recursion.nse
`nmap -p 53 --script dns-service-discovery <target>`

- dns-service-discovery.nse
`nmap -p 53 --script dns-service-discovery <target>`

- dns-srv-enum.nse
`nmap -p 53 --script dns-srv-enum --script-args dns-srv-enum.domain=<domain> <target>`

- dns-update.nse
`nmap -p 53 --script dns-update --script-args dns-update.domain=<domain> <target>`

- dns-zeustracker.nse
`nmap -p 53 --script dns-zeustracker <target>`

- dns-zone-transfer.nse
`nmap -p 53 --script dns-zone-transfer --script-args dns-zone-transfer.domain=<domain> <target>`

- docker-version.nse
`nmap -p 2375 --script docker-version <target>`

- domcon-brute.nse
`nmap -p 135 --script domcon-brute --script-args domcon-brute.domain=<domain> <target>`

- domcon-cmd.nse
`nmap -p 135 --script domcon-cmd --script-args domcon-cmd.command=<command>,domcon-cmd.domain=<domain> <target>`

- domino-enum-users.nse
`nmap -p 135 --script domino-enum-users --script-args domino-enum-users.domain=<domain> <target>`

- dpap-brute.nse
`nmap -p 161 --script dpap-brute --script-args dpap-brute.username=<username>,dpap-brute.password=<password> <target>`

- drda-brute.nse
`nmap -p 102 --script drda-brute --script-args drda-brute.username=<username>,drda-brute.password=<password> <target>`

- drda-info.nse
`nmap -p 102 --script drda-info <target>`

- duplicates.nse
`nmap --script duplicates <target>`

- eap-info.nse
`nmap -p 1812 --script eap-info <target>`

- enip-info.nse
`nmap -p 44818 --script enip-info <target>`

- epmd-info.nse
`nmap -p 4369 --script epmd-info <target>`

- eppc-enum-processes.nse
`nmap -p 102 --script eppc-enum-processes <target>`

- fcrdns.nse
`nmap --script fcrdns --script-args fcrdns.nameservers=<nameservers> <target>`

- finger.nse
`nmap -p 79 --script finger <target>`

- fingerprint-strings.nse
`nmap -p <port> --script fingerprint-strings <target>`

- firewalk.nse
`nmap -p 21 --script firewalk <target>`

- firewall-bypass.nse
`nmap --script firewall-bypass <target>`
