#!/usr/bin/env python
# coding: utf-8

# # Calculadora PYTHON

# In[ ]:


Operator = int(input('Selecione o número da operação desejada: \n \n 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - MULTIPLICAÇÃO \n 4 - DIVISÃO \n \n Digite sua opção (1/2/3/4):'))
result = 0

if (Operator == 1):
    Valor1 = int(input('Digite o primeiro número: '))
    Valor2 = int(input('Digite o segundo número: '))
    result = int(Valor1 + Valor2)
    print(Valor1 , ' + ' , Valor2 , ' = ' , result)
    
if (Operator == 2):
    Valor1 = int(input('Digite o primeiro número: '))
    Valor2 = int(input('Digite o segundo número: '))
    result = int(Valor1 - Valor2)
    print(Valor1 , ' - ' , Valor2 , ' = ' , result)
    
if (Operator == 3):
    Valor1 = int(input('Digite o primeiro número: '))
    Valor2 = int(input('Digite o segundo número: '))
    result = int(Valor1 * Valor2)
    print(Valor1 , ' * ' , Valor2 , ' = ' , result)
    
if (Operator == 4):
    Valor1 = int(input('Digite o primeiro número: '))
    Valor2 = int(input('Digite o segundo número: '))
    result = int(Valor1 / Valor2)
    print(Valor1 , ' / ' , Valor2 , ' = ' , result)


# In[ ]:




