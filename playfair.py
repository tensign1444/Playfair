# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:10:39 2022

@author: Jordan, Charles, Tanner
"""


class Playfair:

  def __init__(self, key='CUI'):
    """
    Constructor, takes the key that will be used for the playfair cipher. Will create the graph with the key.
    """
    self.key = key
    self.grid = self.create_playfair_grid(key)

  def encode_playfair_digrams(self, text, letter):
    '''Encodes the text into a list every two letters, then adds a Q if the letters are the same.'''
    
    text = ''.join(char if char.isalnum() else '' for char in text)
    
    list = []
    x = 0
    while x in range(len(text)):
      try:
        if (text[x] == text[x + 1]):
          list.append(text[x] + letter)
          x += 1
        else:
          list.append(text[x] + text[x + 1])
          x += 2
      except:
        list.append(text[x] + letter)
        break
    return list

  def removeDuplicates(self, text):
    """Removes duplicate letters from specific text"""
    newText = ''
    for x in text:
        if x not in newText:
            newText += x.capitalize()
    return newText

  def create_playfair_grid(self, text):
    """
    GetGrid creates a 2D array to simulate a grid
    of our text (key) by every 5 letters. Returns the 2D Array.
    """
    alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    text = self.removeDuplicates(self.key + alpha).replace(" ", "")
    grid = []
    cols = 5
    for i in range(cols):
      row = []
      for x in range(0,5):
        row.append(text[x])
      grid.append(row)     
      text = text[5:]
    return grid

  def get_playfair_indices(self, char):
    '''
    Get's the index of a character, returns the row and col of it. Will throw an exception if the character isn't found.
    '''
    for i in range(len(self.grid)):
      for x in range(len(self.grid[i])):
        if self.grid[i][x] == char:
          return i, x
    raise Exception("No character found.")

  def encrypt(self, plaintext):
    '''
    Encrypts the ciphertext with the rules from wikipedia.
    '''
    plaintext = self.encode_playfair_digrams(plaintext.upper(),'Q') 
    ciphertext = ''
    for element in plaintext:
      row1, col1 = self.get_playfair_indices(element[0])
      row2, col2 = self.get_playfair_indices(element[1])

      if row1 == row2:
        ciphertext += self.grid[row1][(col1 + 1) % 5] + self.grid[row2][(col2 + 1) % 5]
      elif col1 == col2:
        ciphertext += self.grid[(row1 + 1) % 5][col1] + self.grid[(row2 + 1) % 5][col2]
      else:
        ciphertext += self.grid[row1][col2] + self.grid[row2][col1]

    return ciphertext

  def decrypt(self, ciphertext):
    '''
    Decrypts the plaintext with the rules from wikipedia.
    '''
    ciphertext = self.encode_playfair_digrams(ciphertext.upper(),'Q')
    plaintext = ''
    for element in ciphertext:
      row1, col1 = self.get_playfair_indices(element[0])
      row2, col2 = self.get_playfair_indices(element[1])

      if row1 == row2:
        plaintext += self.grid[row1][(col1 - 1) % 5] + self.grid[row2][(col2 - 1) % 5]
      elif col1 == col2:
        plaintext += self.grid[(row1 - 1) % 5][col1] + self.grid[(row2 - 1) % 5][col2]
      else:
        plaintext += self.grid[row1][col2] + self.grid[row2][col1]

    plaintext = plaintext.replace('Q','')
    return plaintext