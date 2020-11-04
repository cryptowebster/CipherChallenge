import numpy as np


class Cipher:
    '''
    Represents the object of the cipher we need to decode
    '''


    def __init__(self, text):
        '''
        Initialises the Cipher object

        :param text: The raw, undeciphered input text

        :return None
        '''

        
        self.raw_text = text # TODO: convert this to np.array



        self.cipher = self.find_cipher()


    def get_cipher(self):
        '''
        Gets the ioc value for the cipher

        :return cipher_name: The name of the cipher 
        '''

        # TODO: write up the algorithm to find which cipher it is
        

        # return cipher_name



    def decipher(self):
        '''
        Converts the cipher text to english

        :return result: the english text
        '''
        # return result


    def solve_caesar(self):

        # return result
        
    
    def solve_vigenere(self):
        # return result


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


    


