'''
Cipher object class

Don't paste any ciphers into this file, ciphers are for main.py
'''


import numpy as np


class Cipher:
    '''
    Represents the object of the cipher we need to decode
    '''


    def __init__(self, text):

        
        self.raw_text = text # TODO: convert this to np.array



        self.cipher = self.find_cipher()


    def find_cipher(self):
        # TODO: write up the algorithm to find which cipher it is
        cipher_name = None
        

        return cipher_name



    def decipher(self):
        '''
        deciphers it into english depending on which cipher it is.
        Use the methods for solving ciphers to do this (e.g. solve_caesar)
        '''
        pass


    def solve_caesar(self):
        pass

    
    def solve_vigenere(self):
        pass


    def col_tranps(self):
        '''
        for decoding columnar transposition
        '''
        pass


    def decode_enigma(self):
        '''
        I don't know if enigma is one of the ciphers, I'll just put it here anyway
        '''
        pass


    


