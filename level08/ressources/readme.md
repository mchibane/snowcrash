# Again, ltrace on the binary

The binary wants us to input a file as argument. When we input the token file provided in /home/level08 we get an error message.

ltracing the binary shows us that a simple strstr function is used to check the NAME of the file input.


# SYMLINK

By simply using a symlink with a different name we can bypass this 'security' check

ln -s ~/token /tmp/easypeasy


# Final Command...

./level08 /tmp/easypeasy


# ... Or not

`su level09 [previous command output]` does not work !

We simply have to `su flag08` and then launch getflag ;)
