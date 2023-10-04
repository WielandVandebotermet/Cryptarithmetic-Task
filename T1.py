
#Importeert de benodigheden
from simpleai.search import CspProblem, backtrack
import streamlit as st

st.title('Cryptarithmetic Task')

#De Benodigd heden om te weten wat bereken
Word1 = st.text_input('First word', "A")
Word2 = st.text_input('Second word', "BC")
Result = st.text_input('The Result', "AAA")
#om te weten hoe we deze bereken
options = ("Additive", "Multiplatif", "Subtraction" )
Type = st.selectbox("Type", options, index=0, label_visibility="visible")


variables = ()
#voegt alle unieke letter toe in variables(tuples)
for letter in range(len(Word1)):
    if Word1[letter] not in variables:
        variables += (Word1[letter],)

for letter in range(len(Word2)):
    if Word2[letter] not in variables:
        variables += (Word2[letter],)

for letter in range(len(Result)):
    if Result[letter] not in variables:
        variables += (Result[letter],)

domains = {}
#voegt alle variabele, toe in domains(dict) en geeft ze een list mee van 1 tot 9 of 0 tot 9. Afhankelijk of het de eerste letter is of niet
if(len(variables) > 2):
    for letter in range(len(variables)):
        if((variables[letter] == Word1[0]) or (variables[letter] == Word2[0]) or (variables[letter] == Result[0])):
            domains[variables[letter]] = list(range(1, 10))
        else:
            domains[variables[letter]] = list(range(0, 10))


#De functie zorgt ervoor dat ze uniek zijn
def constraint_unique(variables, values):
    return len(values) == len(set(values))

#De functie koppelt waarden aan letters en check of deze opgeteld kunnen worden 
def constraint_add(variables, values):
    factor1 = ""
    factor2 = ""
    result= ""  
    for letter in Word1:
        factor1 += str(values[variables.index(letter)])
    for letter in Word2:
        factor2 += str(values[variables.index(letter)])
    for letter in Result:
        result += str(values[variables.index(letter)])
    return (int(factor1) + int(factor2)) == int(result)

#De functie koppelt waarden aan letters en check of deze afgetrokken kunnen worden 
def constraint_sub(variables, values):
    factor1 = ""
    factor2 = ""
    result= ""  
    for letter in Word1:
        factor1 += str(values[variables.index(letter)])
    for letter in Word2:
        factor2 += str(values[variables.index(letter)])
    for letter in Result:
        result += str(values[variables.index(letter)])
    return (int(factor1) - int(factor2)) == int(result)

#De functie koppelt waarden aan letters en check of deze vermenigdvuldig kunnen worden 
def constraint_mulp(variables, values):
    factor1 = ""
    factor2 = ""
    result= ""  
    for letter in Word1:
        factor1 += str(values[variables.index(letter)])
    for letter in Word2:
        factor2 += str(values[variables.index(letter)])
    for letter in Result:
        result += str(values[variables.index(letter)])
    return (int(factor1) * int(factor2)) == int(result)

#Dit zorgt ervoor dat de juiste berekening wordt berekend
if(Type == "Multiplatif"):
    constraints = [
        (variables, constraint_unique),
        (variables, constraint_mulp),
    ]
elif(Type == "Subtraction"):
    constraints = [
        (variables, constraint_unique),
        (variables, constraint_sub),
    ]
else:
    constraints = [
        (variables, constraint_unique),
        (variables, constraint_add),
    ]

output = ""
#dit berekend dan de oplossing
if st.button('Calculate'):
    output = backtrack(CspProblem(variables, domains, constraints))

st.text(output)