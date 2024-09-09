- Two computers:
  - 192.168.1.10
  - 192.168.1.11
- Like 
```commandline
ping db
```
- Tell system A that system B, has db.
/etc/hosts. 
192.168.1.11    db
- look /etc/hosts file. name resolution. 
- But this does not scale. If one server ip change, need to modify the entries.
- Move the entries to DNS server.
- How do we point the host to DNS server.
```commandline
cat /etc/resolv.conf
nameserver 192.168.1.100
```
- The order of lookup
```commandline
cat /etc/nsswitch.conf
hosts: files dns
```
- added nameserver- configure DNS server to public name server: 8.8.8.8

- Domain name:
- www.facebook.com
- Last portion - top level domain. 
- Root -> .com dns server -> google dns server. Cache the IP.

/etc/resolve.conf
```commandline
search mycompany.com
```

# DNS Records
 A record
AAAA record
CNAME record name to name mapping.
```commandline
nslookup www.google.com
```
```commandline
dig www.google.com
```



