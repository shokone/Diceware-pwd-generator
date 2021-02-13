# Diceware-pwd-generator

[Diceware](https://theworld.com/~reinhold/diceware.html) pwd generator is a method used to generate cryptographically strong passphrases.
This tool is a python implementation of the diceware algorithm.


## How Diceware PWD Generator Generate Passwords?

Traditional Diceware uses rolls of physical dice, this application uses a strong random number generator in place of the dice. 
A virtual dice is roled 5 times, and the 5 digit number used against a lookup [table of words](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt). 
6 dice rolls gives you 6 random words which are easy for a human being to remember, yet have a high amount of entropy which makes them hard to crack.

__WARNING__ : [Using a computer to generate your passphrases is not as secure as rolling physical die with a paper reference of the diceware list.](https://theworld.com/~reinhold/dicewarefaq.html#:~:text=Generating%20truly%20random%20numbers%20using%20a,better%20way%20to%20select%20passphrase%20words.)

For more details check out the diceware passphrase [home page](https://theworld.com/~reinhold/diceware.html).


### Requirements
Python 3.7 or above


## Git Installation
```
# clone the repo
$ git clone https://github.com/shokone/Diceware-pwd-generator.git

# change the working directory to Diceware-pwd-generator
$ cd Diceware-pwd-generator/
```


## Usage

```
usage: python dcpwdgen.py -h 

 ____  ____  ____  _      ____  _____ _____ _     
/  _ \/   _\/  __\/ \  /|/  _ \/  __//  __// \  /|
| | \||  /  |  \/|| |  ||| | \|| |  _|  \  | |\ ||
| |_/||  \__|  __/| |/\||| |_/|| |_//|  /_ | | \||
\____/\____/\_/   \_/  \|\____/\____\\____\\_/  \|
                                                  
	(Diceware PWD Generator by Shokone)
	
usage: dpwdgen.py [-h] [-v] [-n NUM]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show version number and exit.
  -n NUM, --number NUM  Specify the number of words use to generate password

```


## License
Diceware Password Generator is made by [shokone](https://byte-mind.net) and it is released under the MIT license.

**Diceware** is a **trademark** of [Arnold Reinhold](https://theworld.com/~reinhold/).