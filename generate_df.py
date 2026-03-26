import pandas as pd
import numpy as np

# Thiết lập số lượng mẫu
n_samples = 200
np.random.seed(2024)

# Sinh dữ liệu ngẫu nhiên cho các biến độc lập
nam_sx = np.random.randint(2010, 2024, n_samples)
km_di = np.random.uniform(5000, 150000, n_samples)
dung_tich = np.random.choice([1.0, 1.5, 2.0, 2.5, 3.0], n_samples)
bao_tri = np.random.uniform(1, 10, n_samples)

# Tạo DataFrame
df = pd.DataFrame({
    'Nam_SX': nam_sx,
    'KM_Da_Di': km_di,
    'Dung_Tich': dung_tich,
    'Diem_Bao_Tri': bao_tri
})

# Tạo biến mục tiêu (Gia_Xe) dựa trên công thức tuyến tính + Nhiễu (noise)
# Giả sử: Giá = 50*(Năm-2010) - 0.002*KM + 100*DungTich + 20*BaoTri + 300
df['Gia_Xe_USD'] = (
    50 * (df['Nam_SX'] - 2010)
    - 0.002 * df['KM_Da_Di']
    + 100 * df['Dung_Tich']
    + 20 * df['Diem_Bao_Tri']
    + 300
    + np.random.normal(0, 25, n_samples) # Thêm nhiễu để thực tế hơn
).round(2)

df.to_csv('data.csv', index=False)