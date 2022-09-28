# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:33:02 2022

@author: lasse
"""

class RailFence:
        
    def encrypt(self, plaintext):
        
        msgLength = len(plaintext)
        evenChars = ""
        oddChars = ""
        
        for i in range(msgLength):
            if i % 2 == 0:
                evenChars = evenChars + plaintext[i]
            else:
                oddChars = oddChars + plaintext[i]
                    
            ciphertext = oddChars + evenChars
            
        return ciphertext        
    
    def decrypt(self, ciphertext):
        plaintext = ''
        halfLength = len(ciphertext) // 2
        oddText = ciphertext[:halfLength]
        evenText = ciphertext[halfLength:]
        
        for i in range(halfLength):
            plaintext = plaintext + evenText[i]
            plaintext = plaintext + oddText[i]
        
        if len(evenText) > len(oddText):
            plaintext = plaintext + evenText[-1]
        
        return plaintext
        
if __name__ == '__main__':
    railFence = RailFence()
    print(railFence.encrypt('It was a dark and stormy night!'))
    print(railFence.decrypt('twsadr n tryngtI a  akadsom ih!'))