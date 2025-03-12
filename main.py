def tinh_chi_phi_giao_hang(W, D):
    # Kiểm tra tính hợp lệ của đầu vào
    if not (0.5 <= W <= 100):
        return "Đầu vào không hợp lệ"
    if not (1 <= D <= 500):
        return "Đầu vào không hợp lệ"
    
    # Tính chi phí giao hàng theo công thức
    cost = 10 + (W * 0.5) + (D * 0.2)
    return cost