import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negatiivinen_varasto = Varasto(-10)
        self.negatiivinen_alku_saldo = Varasto(10, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uusi_varasto_negatiivisella_tilavuudella(self):
        self.assertAlmostEqual(self.negatiivinen_varasto.tilavuus, 0)

    def test_uusi_varasto_negatiivisella_saldolla(self):
        self.assertAlmostEqual(self.negatiivinen_alku_saldo.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays_ei_lisaa_saldoa(self):
        nykyinen_salso = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, nykyinen_salso)

    def test_saldoa_suurempi_lisays_ei_lisaa_yli(self):
        lisattava_maara = self.varasto.paljonko_mahtuu() + 1
        self.varasto.lisaa_varastoon(lisattava_maara)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        otto = self.varasto.ota_varastosta(-100)
        self.assertEqual(otto, 0)

    def test_saldoa_suurempi_otto_nollaa_saldon(self):
        otto = self.varasto.saldo + 10
        saatu = self.varasto.ota_varastosta(otto)
        self.assertEqual(self.varasto.saldo, 0)
        self.assertEqual(saatu, otto-10)

    def test_str_palauttaa_oikein_lauseen(self):
        saldo = self.varasto.saldo
        tilavuus = self.varasto.tilavuus
        haluttu_tulostus = f"saldo = {saldo}, vielä tilaa {tilavuus}"
        self.assertEqual(haluttu_tulostus, str(self.varasto))
