# cat /etc/passwd

[...]
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
[...]


# copy the file to kali environment

scp -P 4242 level01@[hostip]:/etc/passwd dest


# use john the ripper to crack the password

john -show passwd

output: flag01:abcdefg:3001:3001::/home/flag/flag01:/bin/bash
