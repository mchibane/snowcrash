# Exploring the binary

`./level09` requires an argument

first test with token outputs `tpmhr`

By trial and error we deduced that the binary takes a string as argument and adds the value of the index to each character.

ie. `aaaaa` becomes `abcde`

We naturally `cat token` and put it as input in the binary but it outputs non printable character so we had to find something else.


# Exploring INSIDE the binary

ltrace once again on the binary show us a `puts` call

`puts("You should not reverse this")`


# Reversing the string

We put together a python script that does the inverse operation on the input string (substracting the index to the value of each char)


# Executing

`./our_script \`cat token\` ` gives us the password to flag09 user then getflag and we are done !
