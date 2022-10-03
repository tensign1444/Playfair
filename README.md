# Playfair
Project that utilizes the **Playfair Cypher** for encryption/decryption purposes.  
Additional cyphers such as the **Rail Fence Cipher** and **Substitution Cipher** can also be utilized to encrypt and decrypt a phrase.

# Files
* playfair.py 
* substitution.py
* railfence.py
* crypto.py


## Version
Requires:
* python3
* argparse module

## Usage
`--mode` choose between `encrypt` or `decrypt`  

`--cipher` choose `playfair`, `railfence` or `substitution` as an encryption/decryption method.  

`--phrase` enter the phrase you wish to be encrypted/decrypted  

`--key` an optional argument that allows you to randomize the encryption process. \**Only works with the Playfair and Substitution ciphers*  

`python crypto.py --mode encrypt --cipher playfair --phrase "It was a dark and stormy night." --key CUI`  

`python crypto.py --mode decrypt --cipher playfair --phrase "BRYUYGGCPMGSGPZTXRASAFOZ" --key CUI`  

## Cipher Rules
### Playfair Cipher
The Playfair Cipher utilizes a 5x5 table containing every letter of the alphabet except 'J'. 

#### Encryption
To encrypt a message using the Playfair Cipher, a phrase is broken into 2 letter digrams. If there is a letter left over, a 'Q' will be appended onto the phrase i.e. CONCORDIA = CO NC OR DI AQ. The two letters of the digram are considered opposite corners of a rectangle in the key table. To perform the substitution, apply the following 4 rules to each pair of letters in the phrase:


1. If both letters are the same (or only one letter is left), add a 'Q' after the first letter. Encrypt the new pair and continue.
2. If the letters appear on the same row of your table, replace them with the letters to their immediate right (wrap around the row if necessary).
3. If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrap around the column if necessary).
4. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair.

#### Decryption
To decrypt, use the inverse of the two shift rules, selecting the letter to the left or upwards as appropriate. The last rule remains unchanged, as the transformation switches the selected letters of the rectangle to the opposite diagonal, and a repeat of the transformation returns the selection to its original state. 
### Rail Fence Cipher
The Rail Fence Cipher utilizes the even and odd indexed letters of a phrase to encrypt a message. All of the letters at the even indexes of the phrase are combined into a string. Following this, a string of all of the odd index letters of the phrase is created. These 2 strings are then merged, with the string made up of even indexes appearing first.
### Substitution Cipher
This Substitution Cipher utilizes a 26 character key containing every letter of the alphabet (and a space character) that will swap out all occurrences of one letter for another. i.e. all instances of the letter `a` in a phrase will be replaced with the letter `e`.
