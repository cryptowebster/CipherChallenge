import numpy as np



def to_list(strng):
    lst = [char for char in list(strng)]
    return lst


class Alphabet:

    def __init__(self):
        self.strng = 'abcdefghijklmnopqrstuvwxyz'
        self.list = to_list(self.strng)


class Cipher:
    '''
    Represents the object of the cipher we need to decode
    '''

    alpha = Alphabet()


    def __init__(self, raw_text):
        '''
        Initialises the Cipher object

        :param text: The raw, undeciphered input text

        :return None
        '''

        
        self.raw_text = raw_text
        

    def get_cipher(self):
        '''
        Gets the ioc value for the cipher

        :return cipher_name: The name of the cipher 
        '''
        # self.get_ioc()

        # TODO: write up the algorithm to find which cipher it is
        

        # return cipher_name


    def get_ioc(self):
        '''
        Returns the ioc value for the cipher

        :return ioc: The ioc value
        '''

        # return ioc



    @staticmethod
    def is_english(text, is_blocks=False):
        pass












    def decipher(self):
        '''
        Converts the cipher text to english

        :return result: the english text
        '''
        # return result
        pass


    def solve_caesar(self):
        # result = ''
        # result = to_list(result)
        # for i in range(26):
        #     for letter in to_list(self.raw_text):
        #         # get the number it is in the alphabet
        #         ind = self.alpha.list.index(letter)
        #         new_letter = self.alpha.list[ind + i]
        #         result
        pass
        
        
    
    def solve_vigenere(self):
        # return result
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



