# Playfair
Project that utilizes the Playfair cypher for encryption/decryption purposes.

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
`python crypto.py --mode encrypt --cipher playfair --phrase "It was a dark and stormy night."`

## Cipher Rules
### Playfair Cipher
The Playfair cipher uses a 5 by 5 table containing a key word or phrase.

#### Encryption
To encrypt a message using the playfair cipher, a phrase is broken into digrams (groups of 2 letters) If there is a letter left over, a 'Q' will be appended onto the phrase i.e. CONCORDIA = CO NC OR DI AQ. The two letters of the digram are considered opposite corners of a rectangle in the key table. To perform the substitution, apply the following 4 rules, in order, to each pair of letters in the plaintext:


**1. If both letters are the same (or only one letter is left), add a 'Q' after the first letter. Encrypt the new pair and continue.
2. If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row).
3. If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).
4. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.**

#### Decryption
**
To decrypt, use the inverse (opposite) of the two shift rules, selecting the letter to the left or upwards as appropriate. The last rule remains unchanged, as the transformation switches the selected letters of the rectangle to the opposite diagonal, and a repeat of the transformation returns the selection to its original state. 
**
### Railroad Cipher
### Substitution Cipher
## Testing 
Call the playfair cipher file using console and for the arguements with encryption type in a message,
for decryption type in the encrypted message and you will get the original.
