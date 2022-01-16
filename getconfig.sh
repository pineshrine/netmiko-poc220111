#!/bin/bash

cat machinelist | grep -e Cisco -e Arista | awk '{print $3" > configs/"$1}' | xargs -IXXXX sh -c 'clogin -c "show run" XXXX'
cat machinelist | grep Juniper | awk '{print $3" > configs/"$1}' | xargs -IXXXX sh -c 'jlogin -c "show config | dis set" XXXX'
cat machinelist | grep Huawei | awk '{print $3" > configs/"$1}' | xargs -IXXXX sh -c 'xilogin -c "disp cu" XXXX'
cat machinelist | grep VyOS | awk '{print $3" > configs/"$1}' | xargs -IXXXX sh -c 'vlogin -c "show configuration commands" XXXX'

#IOS1 Cisco 192.168.6.20 pocadmin/password/password
#XRV1 Cisco 192.168.6.21 pocadmin/password/password;xradmin/xrpassword
#NXV1 Cisco 192.168.6.22 pocadmin/password;admin/password
#VMX1 Juniper 192.168.6.23 pocadmin/Password;root/Password
#EOS1 Arista 192.168.6.24 pocadmin/password
#CSR1 Cisco 192.168.6.25 pocadmin/password/password
#CLE1 Huawei 192.168.6.26 pocadmin/password
#VOS1 VyOS 192.168.6.27 pocadmin/password

# clogin -c "show run" 192.168.6.20 | less
# clogin -c "show run" 192.168.6.21 | less
# clogin -c "show run" 192.168.6.22 | less
# jlogin -c "show config | dis set" 192.168.6.23 | less
# clogin -c "show run" 192.168.6.24 | less
# clogin -c "show run" 192.168.6.25 | less
# xilogin -c "disp cu" 192.168.6.26 | less
# vlogin -c "show configuration commands" 192.168.6.27 | less
