import pandas as pd
import numpy as np

# Cấu hình
n_rows = 100000
np.random.seed(42)

# Sinh Features
gia_ban = np.random.uniform(10, 50, n_rows)        # x1
ngan_sach_qc = np.random.uniform(10, 1000, n_rows) # x2
danh_gia_sao = np.random.uniform(1, 5, n_rows)      # x3
do_hot_trend = np.random.uniform(0, 10, n_rows)    # x4

# Công thức Phi Tuyến tính (Target: Doanh số)
# y = 500 - 2*x1 + 5*sqrt(x2) + exp(x3/2) + 10*sin(x4/10) + noise
y = (500
     - 1.5 * gia_ban
     + 8 * np.sqrt(ngan_sach_qc)
     + 2 * np.exp(danh_gia_sao / 1.5)
     + 20 * np.sin(do_hot_trend / 5)
     #+ np.random.normal(0, 10, n_rows)
     ) # Thêm nhiễu ngẫu nhiên

df = pd.DataFrame({
    'Gia_Ban': gia_ban,
    'Ngan_Sach_QC': ngan_sach_qc,
    'Danh_Gia_Sao': danh_gia_sao,
    'Do_Hot_Trend': do_hot_trend,
    'Doanh_So': y
})

df.to_csv('data_multiD.csv', index=False)
print("Đã tạo file data_thick_nonlinear.csv thành công!")