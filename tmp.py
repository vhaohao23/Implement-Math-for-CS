import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data.csv", header=None)

# df là DataFrame trong ảnh của bạn
X = StandardScaler().fit_transform(df)   # nên chuẩn hóa trước khi PCA

pca = PCA(n_components=0.90)             # tự chọn số thành phần để giữ >= 90% phương sai
X_pca = pca.fit_transform(X)

print("Số thành phần:", pca.n_components_)
print("Tỉ lệ phương sai:", pca.explained_variance_ratio_)
print("Tổng:", pca.explained_variance_ratio_.sum())