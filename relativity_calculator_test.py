import unittest
import relativity_calculator

rc = relativity_calculator.RelativityCalculator()

class TestGammaToVelocity(unittest.TestCase):
    '''Test for gamma_to_speed function'''

    def test_gamma_to_speed_1(self):
        actual = rc.gamma_to_speed(1)
        expected = 0.0
        self.assertAlmostEqual(actual, expected)

    def test_gamma_to_speed_2(self):
        actual = rc.gamma_to_speed(1.5)
        expected = 223606797.74997896
        self.assertAlmostEqual(actual, expected)

    def test_gamma_to_speed_3(self):
        actual = rc.gamma_to_speed(10)
        expected = 298496231.13198596
        self.assertAlmostEqual(actual, expected)

class TestSpeedToGamma(unittest.TestCase):
    '''Test for spped_to_gamma function'''

    def test_speed_to_gamma_1(self):
        actual = rc.speed_to_gamma(0)
        expected = 1.0
        self.assertAlmostEqual(actual, expected)

    def test_speed_to_gamma_2(self):
        actual = rc.speed_to_gamma(3000000)
        expected = 1.0000500037503126
        self.assertAlmostEqual(actual, expected)

    def test_speed_to_gamma_3(self):
        actual = rc.speed_to_gamma(297000000)
        expected = 7.088812050083354
        self.assertAlmostEqual(actual, expected)

    def test_speed_to_gamma_4(self):
        actual = rc.speed_to_gamma(300000000)
        expected = -1
        self.assertAlmostEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
