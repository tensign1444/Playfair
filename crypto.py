# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:45:38 2022

@author: lasse
"""

import railfence
import substitution
import argparse

def main():
    ''' Main Program for Rail Fence Cipher Program '''

    parser = argparse.ArgumentParser(description='Decrypts and Encrypts text using the Rail Fence Cipher')
    parser.add_argument('cipher', type=str, choices=['railfence', 'substitution'], help='choose either the railfence or substitution cipher')
    parser.add_argument('mode', type=str, choices=['encrypt', 'decrypt'], help='choose to encrypt or decrypt a message')
    parser.add_argument('phrase', type=str, help='message to translate')
    parser.add_argument('key', type=str, help='key for the substitution cipher', nargs='?')
    
    args = parser.parse_args()

    if args.cipher == 'railfence':
        translator = railfence.RailFence()
    elif args.cipher == 'substitution':
        if args.key:    
            translator = substitution.Substitution(args.key)
        else:
            translator = substitution.Substitution(" zyxwvutsrqponmlkjihgfedcba")
    if args.mode == 'encrypt':
        print(translator.encrypt(args.phrase))
    elif args.mode == 'decrypt':
        print(translator.decrypt(args.phrase))
    else:
        print('Error: unexpected translation mode')

    return


if __name__ == '__main__':
    main()