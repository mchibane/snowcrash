# analyzing the script

the script takes 2 args, reads the output of argv[1] and then does a bunch of regex replacement
the script level06.php is copied here with good indentation for better readability
a little bit of research tells us that the /e regex modifier can be used to inject code into the next argument of preg_replace()


# trial and error

finally understanding the regex tells us that the code we want to inject must be passed in a file which outputs something like
[x inject code here]


# back ticks

our previous knowledge helped us deduce that we will need to feed the output of the getflag command in a convinient way
create a file:
``[x ${`getflag`}]``

./level06 /where/your/file/is
