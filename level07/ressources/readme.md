# understanding the binay

the executable seem to always output "level07"
however we need to analyze it closer


# ltrace ./level07

ltrace helps us track the function calls inside a binary file - more specificaly library calls


# getenv("LOGNAME")

by analysing ltrace we can see the binary is looking for a env variable named 'LOGNAME'

by simply replacing this variable with the clever use of backticks we get what we want


# export LOGNAME='\`getflag\`'

launch the binary and GG
