We have two dns server. dns1 and dns2. Its OS is Suse, 10 years old. Never updated. 
The software namd is bind. Configure file is /etc/named.conf
Service is named
```bash
/etc/init.d/named status
```

# configure in named.conf

```bash

# look forward
zone "mbi.nus.edu.sg" in {
    type master;
    file "master/mbi.nus.edu.sg";
    # allow-update {update-aci;} # newly added
};
# look reverse
# let the system know if this type search coming, go to where to find the defination.
zone "0.10.in-addr.arpa" in {
    type master;
    file "master/0.10.in-addr.arpa";
};

```

# in the define file
\$TTL is the cache hold time

"serial number" each edit will upto a new biger number. The rule is "the date + modified times"