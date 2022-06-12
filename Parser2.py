import pdfplumber
import string, sys
#file = 'declaration-of-performance_wall180.pdf'
def parser2(file, data):

    data.setdefault('Nom fichier', []).append(str(file))
    dico_of_dop = {'Manufacturor':'Fabricant',
        'Identification code' : 'Code Unique',
        'Application': 'Categorie',
        'Authorized person': 'Organisme Notifié',
        'System of assessment': 'Système(s) d’évaluation et de vérification',
        'Base oft he DoP': 'Norme',
        'Compression strength kPa': 'Résistance à la compression',
        'W/(m*K': 'Resistance Thermique',
        'the board' : 'Resistance à la traction/flexion',
        'Water vapor permeability µ': 'Perméabilité au passage de la vapeur d’eau',
        'coefficient': 'Absorption acoustique',
        'Fire resistance': 'Reaction au feu',
        'Eberhardzell, den': 'Date D\'émission'
        

    }
    with pdfplumber.open(file) as pdf:
            allTexts = ''
            for i in range(len(pdf.pages)):
                page = pdf.pages[i]
                text = page.extract_text()
                allTexts = allTexts+str(text)   # texte de l'ensemble des pages 

    my_text_list =[]
    list_f = []
    for row in allTexts.split('\n'):   # chaque fois on a retour a la linge  => nouvelle ligne 
        if row.strip():
            my_text_list.append(row.strip())
    list_data = []
    for text in my_text_list:
        for key in dico_of_dop.keys():
            if key in text:
                result = (text.split(key)[-1].strip())
                of_head_csv = dico_of_dop[key]
                data.setdefault(of_head_csv, []).append(str(result))    
            
    return data

    