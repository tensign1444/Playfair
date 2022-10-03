# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:59:11 2022

@author: lasse
"""
class Substitution:
        
    def __init__(self, key=" zyxwvutsrqponmlkjihgfedcba"):
        self.key = key
        
    def encrypt(self, plaintext):
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        ciphertext = ""
        plaintext = plaintext.lower()
        for ch in plaintext:
            idx = alphabet.find(ch)
            ciphertext = ciphertext + self.key[idx]
        return ciphertext
    
    def decrypt(self, ciphertext):
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        plaintext = ""
        for ch in ciphertext:
            idx = self.key.find(ch)
            plaintext = plaintext + alphabet[idx]
        return plaintext
        
if __name__ == '__main__':
    substitution = Substitution()
    print(substitution.encrypt('I THINK coding is fun'))
    print(substitution.decrypt('sahtsnqaymxsnuasiavgn'))

