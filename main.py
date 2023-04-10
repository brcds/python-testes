from _ctypes_test import func

from bytebank import Funcionario


# bruno = Funcionario('Bruno Cristiano', '13/12/2000', 1000)
# print(bruno.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()
