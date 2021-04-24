# Cipher-text-using-MCMC
## Training with L'assommoir 
First, we have to make a matrix of first-order transitions from a character to another.
As an exemple source of data to learn myself, i will use "l'assommoir" from the french writer "Emile Zola". After that we obviously change the dataset because of the book were written in 1877 but it's a good source of french sentence.
### Extract data
I take it from a word document, so I use python-docx and lower every character with doc_to_list_of_letter function.
To better use i lower character and put it in a list.
```python
def doc_to_list_of_letter(doc_path) :
    doc = docx.Document(doc_path)
    
    list_of_letter = []
    for para in doc.paragraphs:
        list_of_letter += list(para.text.lower())
    return list_of_letter
```
### Create probability matrix
We make it with 2 function, generate_occurence_matrix and generate_probability_matrix. Initialize a dictionnay with every different character and fill it another dictionary with the number of occurrences of the following first letter.
```python
def generate_occurence_matrix(list_of_letter):
    occurence_matrix = { i : {} for i in list_of_letter }


    for i in range(0, len(list_of_letter) - 1):
            if(list_of_letter[i+1] in occurence_matrix[list_of_letter[i]]):
                occurence_matrix[list_of_letter[i]][list_of_letter[i+1]] += 1
            else:
                occurence_matrix[list_of_letter[i]][list_of_letter[i+1]] = 1

    return occurence_matrix
```
After that we pass it in generate_probability_matrix that is going to make to change the number of occurence by the probability.
```python
def generate_probability_matrix(occurence_matrix):
    for key in occurence_matrix:
        total = sum(occurence_matrix[key].values())
        for value in occurence_matrix[key] :
            occurence_matrix[key][value] /= total
    return occurence_matrix
```
## Encryption script
Here we are going to see the script for 3 different simple encryption generate pseudo-randomly with a seed : Caesar cipher, Substitution cipher, Transposition cipher
## Sources
* Diaconis, P., 2008. The Markov chain Monte Carlo revolution. Bulletin of the American Mathematical Society, 46(2), pp.179-205.
* Chen, J., Rosenthal, J.S. Decrypting classical cipher text using Markov chain Monte Carlo. Stat Comput 22, 397–413 (2012).

