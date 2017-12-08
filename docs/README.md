# ENIGMA
A CLI engima machine that keeps your wartime messages secret!

This program simulates the enigma machine used by the Nazis during World War II. It allows the user to translate messages of any length, containing nearly all ASCII characters, into an encrypted format that can only be decoded by a separate enigma machine with the same settings.

The German enigma machine worked using a system of rotors, plugboards and reflectors to translate characters into different characters. The rotors turned as the message was translated, so identical characters in different parts of the message would be encoded as different characters, making this encoding method much more complicated and difficult to decipher than simple character substitution.

This program includes options to support file input/output as well as 31 days worth of options for encryption, much like the original machine had.

This  program  was  written mostly to further my personal knowledge of Python, encryption, packaging and command line interfaces. It should not be used to encrypt any important messages, and is only intended to be used for fun.

# INSTALLATION
If python3 or pip are not installed, run these commands (for Ubuntu):
```
$ sudo apt install python3 
$ sudo apt install python3-pip
```
Other Linux distros and non-Linux operating systems will require different instructions to install python and pip. To install enigma, run:
```
$ sudo pip3 install enigmamachine
```

# FLAGS
```
-h, --help:   
    display a help menu for quick reference

-i, --infile:   
    specify  the  location  of  an  input file, path can be relative or absolute

-o, --outfile:  
    specify the location of an output file, path  can  be  relative  or absolute

-d, --day:  
   encrypt/decrypt  using  this  day's rotor, plugboard, and reflector settings

-v, --version:  
   display version information
```

# EXAMPLES

Translate a message using the enigma machine:   
```
$ enigma "translate this message"
```
Translate a message using a specific day's settings:   
```
$ enigma -d 10 "translate this message"
```
Translate a text file:
```
$ enigma -i "translate.txt"
```
Send translated message to a text file:
```
$ enigma -o "translated.txt" "translate this message"
```

Chain options to translate a file using a specific day's settings:
```
$ enigma -d 25 -i "translate.txt"
```
Show version information
```
$ enigma --version
```

# CREDITS
Author: [Tiger Sachse](https://github.com/tgsachse)  
Version: 1.0.0  
License: [MIT](LICENSE.txt)  
