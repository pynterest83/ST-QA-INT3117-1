import unittest
from main import tinh_chi_phi_giao_hang

class TestTinhChiPhiGiaoHang(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(tinh_chi_phi_giao_hang(50, 100), 55)

    def test_invalid_weight(self):
        self.assertEqual(tinh_chi_phi_giao_hang(0, 100), "Đầu vào không hợp lệ")

    def test_invalid_distance(self):
        self.assertEqual(tinh_chi_phi_giao_hang(50, 600), "Đầu vào không hợp lệ")

if __name__ == '__main__':
    unittest.main()