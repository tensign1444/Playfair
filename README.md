# Playfair
Project that utilizes the Playfair cypher for encryption/decryption purposes.

# Files
playfair.py 
substitution.py
railfence.py
crypto.py


## Version
Requires:
 Markup : * python3
          * argparse module

## Usage
Use console and pass in strings to encrypt and decrypt methods using the select functions for their respective uses

## Language Rules 
Uses the 4 main rules of the playfair cipher creating a group of 5x5 letters and checking if certain letters in the string after removing duplicates are located within either the same row, same columnn or different row and different columnns.

## Testing 
Call the playfair cipher file using console and for the arguements with encryption type in a message,
for decryption type in the encrypted message and you will get the original.
