# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:45:38 2022

@author: lasse
"""

import railfence
import substitution
import argparse
import playfair


def main():
  ''' Main Program for Cipher Program. Utilizes the argparse module to allow the user to select from 3 different ciphers (railfence, substitution, and playfair), and then choose to either encrypt or decrypt a phrase, with an optional cipher key.
    '''

  parser = argparse.ArgumentParser(
    description='Decrypts and Encrypts text using the Rail Fence Cipher')
  parser.add_argument(
    '--cipher',
    type=str,
    choices=['railfence', 'substitution', 'playfair'],
    help='choose the playfair, railfence or substitution cipher',
    required=True)
  parser.add_argument('--mode',
                      type=str,
                      choices=['encrypt', 'decrypt'],
                      help='choose to encrypt or decrypt a message',
                      required=True)
  parser.add_argument('--key',
                      type=str,
                      help='key for the substitution cipher',
                      required=False)
  parser.add_argument('--phrase',
                      type=str,
                      help='message to translate',
                      required=True)

  args = parser.parse_args()

  if args.cipher == 'railfence':
    translator = railfence.RailFence()
  elif args.cipher == 'substitution':
    if len(str(args.key)) == 27:
      translator = substitution.Substitution(args.key)
    else:
      translator = substitution.Substitution()
      print("Using default key value")
  elif args.cipher == 'playfair':
    if args.key:
      translator = playfair.Playfair(args.key)
    else:
      translator = playfair.Playfair()
  if args.mode == 'encrypt':
    print(translator.encrypt(args.phrase))
  elif args.mode == 'decrypt':
    print(translator.decrypt(args.phrase))
  else:
    print('Error: unexpected translation mode')

  return


if __name__ == '__main__':
  main()
