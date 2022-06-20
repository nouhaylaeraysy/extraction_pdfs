import pdfplumber
import re  
import collections
import string, sys




def parser(file):
    my_dico = {   # lines starts with decimal
        'Fabricant' : 'Manufacturer',
        'Code Unique':'Unique identifier code of the product type',
        'Categorie ':'Purpose',
        ' Système(s) d’évaluation et de vérification': 'System for assessment and verification of the constancy of performance',
        'Declared performance': 'Declared performance',
        'Specific technical characteristics': 'Specific technical characteristics'
    }
    my_dico_list = {   # another instruction for informations into this lines 
        'Declared performance': 'Declared performance',
        'Specific technical characteristics': 'Specific technical characteristics'
        }
    my_dico2 = {
        'Harmonised standard': 'Norme',
        'Number of layers': 'Number of layers',
        'Organisme Notifié' : 'Notified body' ,
        'Perméabilité au passage de la vapeur d’eau' : 'Diffusion resistance µ',
        'Resistance Thermique':'Heat conductivity λ',
        'Emission de substances dangereuses à l’intérieur des bâtiments ' : 'Emission class',
        'Reaction au feu' : 'Reaction to fire'
    }

    data = {'Nom du Fichier ' : file , 'Nom de Produit' :'' }  # stock keys with their values 
    def get_key(val):   # retourne  clé et sa valeur  dans une liste 
        for key, value in my_dico.items():
            if val == value:
                return key
 
        return 0

    def get_key2(val):   # pour les inf a extraire d'autres manières 
        for key, value in my_dico2.items():
            if val == value:
                return key

        return 0
    test = {}
    test_list = {}
    with pdfplumber.open(file) as pdf:
        allTexts = ''
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            allTexts = allTexts+text   # texte de l'ensemble des pages 
    my_list = []

    for row in allTexts.split('\n'):   # chaque fois on a retour a la linge  => nouvelle ligne 
        if row.rstrip():
            my_list.append(row.strip())
    #print(my_list)

    for index,row1 in enumerate(my_list):
        if row1 == 'Declaration of performance':
            data['Nom de Produit'] = my_list[index +2 ]
    regex = re.compile(r'(^\d.$)') # pour 6.

    for index, row1 in enumerate(my_list) :
        if regex.match(row1):
            a = index
            test_list[index] = 'none'  # test_list va prendre l'indice 15   de 6.
    for index, row1 in enumerate(my_list) :
        for i, s in enumerate(my_dico.values()):
            if (s in row1.strip()):
                key = get_key(s)
                test[index] =  row1.strip()   ##### la premiere partie de pdf 
        for i, s in enumerate(my_dico_list.values()):
            if (s in row1.strip()):
                key = get_key(s)
                test_list[index] =  row1.strip()  ##### prend l'indice correspond a la ligne 7... et 8...
    dictionary_items = test.items()
    test = collections.OrderedDict(sorted(test.items()))##### assosier chaque indice a sa valeur dans le dictionnaire 
    atest = {}   # prend les valeurs de test 
    for k, v in test.items(): 
        atest[k]= v  
    test = atest
    testvalues = (test.keys())
    t = len(testvalues)   ### t = la longueur de liste test qui prend les  premiere valeurs 7
    for k, value in enumerate(testvalues) :
        if(k+1 <= t-1):
            keyend = k+1
        else:
            keyend = t-1        ##### 1/2/3/4/5/6/6
    
        end = list(testvalues)[keyend] ##### 5/8/11/13/23/38/38
    
        if(k< keyend):   # 1 er instruction si < 6 
            if(len(my_list[value:end])):
                for e, r in enumerate(my_list[value+1:end]):
                    if(r.find(": ") ==-1):    # trouver la derniere occurence de : 
                        for i, s in enumerate(my_dico.values()):
                     
                            substring_in_list = False
                            for teststring in ((test_list.values())):
                                if s in teststring:
                                    substring_in_list = True
                    
                            if(s in test[value] and substring_in_list == False):
                                z = get_key(s)
                                if z in data.keys():
                                    data[z] = data[z] + ' ' +r+' --'
                                else:
                                    data[z] = r
                    else:
                        if(r.find(":  ")>-1):   # apres : espace 
                         
                            #for t in r.split('\n'):
                            a = r.split('\n') 
                            if(len(a) ==1):
                               y =a[0].split(':  ')
                            for i2, s2 in enumerate(my_dico2.values()):
                                if(s2 in y[0].strip()):
                                       
                                        z2 = get_key2(s2)
                                        if z2 in data.keys():
                                           data[s2] = data[z2] + ' ' +y[1].strip()
                                        else:
                                           data[s2] = y[1].strip()
    for value in my_list:
        if value.startswith('Eberhardzell,'):
            data['Date D\'émission '] =  value.split()[-1]
   
    return(data)


