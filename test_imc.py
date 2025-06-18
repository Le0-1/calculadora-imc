import unittest
from calculadora_imc import calcular_imc, classificar_imc


class TestCalculadoraIMC(unittest.TestCase):

    def test_imc_peso_normal(self):
        self.assertAlmostEqual(calcular_imc(70, 1.75), 22.86, places=2)
        self.assertEqual(classificar_imc(22.86), "Peso normal")

    def test_imc_abaixo_do_peso(self):
        self.assertAlmostEqual(calcular_imc(50, 1.75), 16.33, places=2)
        self.assertEqual(classificar_imc(16.33), "Abaixo do peso")

    def test_imc_sobrepeso(self):
        self.assertAlmostEqual(calcular_imc(85, 1.75), 27.76, places=2)
        self.assertEqual(classificar_imc(27.76), "Sobrepeso")

    def test_imc_obesidade_grau_I(self):
        self.assertAlmostEqual(calcular_imc(95, 1.72), 32.11, places=2)
        self.assertEqual(classificar_imc(32.12), "Obesidade Grau I")

    def test_altura_invalida_lanca_erro(self):
        with self.assertRaises(ValueError):
            calcular_imc(70, 0)

    def test_peso_invalido_lanca_erro(self):
        with self.assertRaises(ValueError):
            calcular_imc(-70, 1.75)


if __name__ == "__main__":
    unittest.main()
