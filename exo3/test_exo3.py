import unittest
from exo3 import processLines


class TestExo3(unittest.TestCase):
    def test_input_1(self):
        # Lire les lignes d'input1.txt
        with open("sample/input1.txt") as input1:
            lines = input1.readlines()

        # Lire le résultat attendu dans output1.txt
        with open("sample/output1.txt") as output1:
            expected = output1.read().strip()

        # Vérifier que le résultat de processLines est bien égal au résultat attendu
        self.assertEqual(expected, processLines(lines))

    def test_input_2(self):
        # Lire les lignes d'input2.txt
        with open("sample/input2.txt") as input2:
            lines = input2.readlines()

        # Lire le résultat attendu dans output2.txt
        with open("sample/output2.txt") as output2:
            expected = output2.read().strip()

        # Vérifier que le résultat de processLines est bien égal au résultat attendu
        self.assertEqual(expected, processLines(lines))


if __name__ == '__main__':
    unittest.main()
