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
`python crypto.py --mode encrypt --cipher playfair --phrase "It was a dark and stormy night.`

## Cipher Rules
### Playfair Cipher
Uses the 4 main rules of the playfair cipher creating a group of 5x5 letters and checking if certain letters in the string after removing duplicates are located within either the same row, same columnn or different row and different columnns.
### Railroad Cipher
### Substitution Cipher
## Testing 
Call the playfair cipher file using console and for the arguements with encryption type in a message,
for decryption type in the encrypted message and you will get the original.
