from codigo.bytebank import Funcionario

import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # when-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Bruno_Cristiano_deve_retornar_Cristiano(self):
        entrada = ' Bruno Cristiano '  # Given
        esperado = 'Cristiano'

        bruno = Funcionario(entrada, '11/11/2000', 1111)
        resultado = bruno.sobrenome()  # when

        assert resultado == esperado  # Then

    # @mark.skip
    def test_quando_decrecismo_salario_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when

        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then

