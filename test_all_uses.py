import unittest
from main import tinh_chi_phi_giao_hang

class TestTinhChiPhiGiaoHang(unittest.TestCase):
    def test1(self):
        self.assertEqual(tinh_chi_phi_giao_hang(200, 5), "Đầu vào không hợp lệ")
    def test2(self):
        self.assertEqual(tinh_chi_phi_giao_hang(60, 10), 42)
    def test3(self):    
        self.assertEqual(tinh_chi_phi_giao_hang(50, 0), "Đầu vào không hợp lệ")
    def test4(self):
        self.assertEqual(tinh_chi_phi_giao_hang(60, 10), 42)
    def test5(self):
        self.assertEqual(tinh_chi_phi_giao_hang(60, 10), 42)

if __name__ == '__main__':
    unittest.main()