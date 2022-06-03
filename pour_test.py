
#import imp
import os 
import glob
import pandas as pd 
from Parser import parser
from configuration import getPathBySection

import pdfplumber
import re  
code = ''
import collections
#file = "test2.pdf"
my_dico = {   # lines starts with decimal 
    'code_unique':'Unique identifier code of the product type',
    'Purpose':'Purpose',
    'Manufacturer': 'Manufacturer',
    'Authorised representative': 'Authorised representative',
    'System for assessment and verification of the constancy of performance': 'System for assessment and verification of the constancy of performance',
    'Declared performance': 'Declared performance',
    'Specific technical characteristics': 'Specific technical characteristics',
   

}

my_dico_list = {   # another instruction for informations into this lines 
     'Declared performance': 'Declared performance',
     'Specific technical characteristics': 'Specific technical characteristics',
}

my_dico2 = {
    'Harmonised standard': 'Harmonised standard',
    'Number of layers': 'Number of layers',
    'Notified body' : 'Notified body' ,
    'Diffusion resistance µ' : 'Diffusion resistance µ',
    'Heat conductivity λ':'Heat conductivity λ',
    'Emission class ' : 'Emission class',
    'Reaction to fire' : 'Reaction to fire'
}

data = {}  # stock keys with their values 

def get_key(val):   # retourne  clé et sa valeur  dans une liste 
    for key, value in my_dico.items():
         if val == value:
             return key
 
    return 0

def get_key2(val):   # pour les inf a extraire d'autres manières 
    for key, value in my_dico2.items():
            if val == value:
                return key

    return cle
  
test = {}
test_list = {}

pathdirectory = getPathBySection('SECTION1')
print(pathdirectory)

files = os.listdir(pathdirectory)
for file in files:
    if file.endswith(".pdf") :
        data = parser(pathdirectory+'/'+file)



