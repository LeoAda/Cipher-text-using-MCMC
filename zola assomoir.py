import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import docx
import unicodedata

def doc_to_list_of_letter(doc_path) :
    doc = docx.Document(doc_path)
    
    list_of_letter = []
    for para in doc.paragraphs:
        list_of_letter += list(para.text.lower())
    return list_of_letter

def generate_occurence_matrix(list_of_letter):
    occurence_matrix = { i : {} for i in list_of_letter }


    for i in range(0, len(list_of_letter) - 1):
            if(list_of_letter[i+1] in occurence_matrix[list_of_letter[i]]):
                occurence_matrix[list_of_letter[i]][list_of_letter[i+1]] += 1
            else:
                occurence_matrix[list_of_letter[i]][list_of_letter[i+1]] = 1

    return occurence_matrix

def generate_probability_matrix(occurence_matrix):
    for key in occurence_matrix:
        total = sum(occurence_matrix[key].values())
        for value in occurence_matrix[key] :
            occurence_matrix[key][value] /= total
    return occurence_matrix

def display_heatmap_dictionnary(dictionnary):
    df = pd.DataFrame.from_dict(dictionnary)
    ax = sns.heatmap(df,xticklabels=1, yticklabels=1,cbar=False)
    return("Done")

list_assommoir = doc_to_list_of_letter('zola_assommoir_source.docx')

matrix_assommoir = generate_occurence_matrix(list_assommoir)

matrix_assommoir = generate_probability_matrix(matrix_assommoir)

display_heatmap_dictionnary(matrix_assommoir)



