from unittest import TestCase, main
from app import romeu_julieta

class TestRomeuJulieta(TestCase):

    def teste_espera_queijo(self):
        entrada = 3
        esperado = 'queijo'
        self.assertEqual(romeu_julieta(entrada),esperado)
        

    def teste_espera_goiabada(self):
        entrada = 5
        esperado = 'goiabada'
        self.assertEqual(romeu_julieta(entrada),esperado)

    def teste_espera_queijo_goiabada(self):
        entrada = 15
        esperado = 'romeu e julieta'
        self.assertEqual(romeu_julieta(entrada),esperado)

main()

