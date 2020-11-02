class Cipher:
    '''
    Represents the object of the cipher we need to decode
    '''


    def __init__(self, text):

        
        self.raw_text = text



        self.cipher = self.find_cipher()


    def find_cipher(self):
        cipher_name = None  # TODO: write up the algorithm to find 
                            # which cipher it is

        

        return cipher_name



    def decipher(self):
        '''
        deciphers it into english depending on which cipher it is.
        Use the method for solving ciphers to do this (e.g. solve_caesar)
        '''
        pass


    def solve_caesar(self):
        pass

    
    def solve_vigenere(self):
        pass


    


