## Detecting Fuzzy Information Entropy-based Outlier Detection (FIEOD) algorithm
## Please refer to the following papers:
## Yuan Zhong, Chen Hongmei, Li Tianrui, Liu Jia, ShuWang.
## Fuzzy information entropy-based adaptive approach for hybrid feature outlier detection,Fuzzy Sets and Systems,2021, 421: 1-28.
## Uploaded by Yuan Zhong on May 30, 2024. E-mail:yuanzhong2799@foxmail.com.
import numpy as np
from scipy.io import loadmat
from sklearn.preprocessing import MinMaxScaler


def ufrs_kersim(a, x, e):
    if abs(a - x) > e:
        return 0
    else:
        if e == 0:
            return 1 if a == x else 0
        else:
            return 1 - abs(a - x)

def FIEOD(data, delta):
    ## input:
    # data is data matrix without decisions, where rows for samples and columns for attributes.
    # numeric attributes are normalized to [0,1].
    # delta is used to adjust the adaptive fuzzy radius.
    ## output
    # fuzzy entropy outlier factor (FEOF).
    n, m = data.shape

    FE = np.zeros(m)
    FE_x = np.zeros((n, m))
    FRC_x = np.zeros((n, m))
    weight = np.zeros((n, m))

    Epsilon = np.zeros(m)
    for j in range(m):
        if np.min(data[:, j]) == 0 and np.max(data[:, j]) == 1:
            Epsilon[j] = np.std(data[:, j], ddof=1) / delta

    ssr = {}
    for l in range(m):
        r = np.zeros((n, n))
        for j in range(n):
            a = data[j, l]
            x = data[:, l]
            for k in range(j + 1):
                r[j, k] = ufrs_kersim(a, x[k], Epsilon[l])
                r[k, j] = r[j, k]
        ssr[l] = r

    for l in range(m):
        RM = ssr[l]
        FE_tem = np.mean(-np.log2(np.sum(RM, axis=1) / n))
        t = 0
        while t < n:
            RM_temp = np.delete(np.delete(RM, t, axis=0), t, axis=1)
            FE_xtem = np.mean(-np.log2(np.sum(RM_temp, axis=1) / (n - 1)))
            FE_x[t, l] = FE_xtem
            FRC_x[t, l] = np.sum(RM[t, :]) - np.sum(RM_temp) / (n - 1)
            weight[t, l] = np.sqrt(np.sum(RM[t, :]) / n)
            t += 1
        FE[l] = FE_tem

    FRC_x[np.isnan(FRC_x)] = n
    RFE = 1 - FE_x / FE
    RFE = np.clip(RFE, 0, 1)

    FOD_Xl = np.zeros((n, m))
    for r in range(n):
        for s in range(m):
            if FRC_x[r, s] > 0:
                FOD_Xl[r, s] = RFE[r, s] * ((n - abs(FRC_x[r, s])) / (2 * n))
            else:
                FOD_Xl[r, s] = RFE[r, s] * np.sqrt((n + abs(FRC_x[r, s])) / (2 * n))

    sorted_indices = np.argsort(FE)[::-1]

    ssr_deA = [0] * m  # 使用包含 0 的列表来初始化
    for L in range(m, 0, -1):
        lA_de = sorted_indices[:L]
        ssr_de_tmp = ssr[lA_de[0]]
        for j in range(L):
            ssr_de_tmp = np.minimum(ssr_de_tmp, ssr[lA_de[j]])
        ssr_deA[L-1] = ssr_de_tmp

    FE_deA = np.zeros(m)
    FE_deA_x = np.zeros((n, m))
    FRC_deA_x = np.zeros((n, m))
    weightA_de = np.zeros((n, m))

    for l in range(m):
        RM_deA = ssr_deA[l]
        FE_deA_tem = np.mean(-np.log2(np.sum(RM_deA, axis=1) / n))
        t = 0
        while t < n:
            RM_deA_temp = np.delete(np.delete(RM_deA, t, axis=0), t, axis=1)
            FE_deA_xtem = np.mean(-np.log2(np.sum(RM_deA_temp, axis=1) / (n - 1)))
            FE_deA_x[t, l] = FE_deA_xtem
            FRC_deA_x[t, l] = np.sum(RM_deA[t, :]) - np.sum(RM_deA_temp) / (n - 1)
            weightA_de[t, l] = np.sqrt(np.sum(RM_deA[t, :]) / n)
            t += 1
        FE_deA[l] = FE_deA_tem

    FRC_deA_x[np.isnan(FRC_deA_x)] = n
    RFE_deA = 1 - FE_deA_x / FE_deA
    RFE_deA = np.clip(RFE_deA, 0, 1)

    FOD_deA_Xl = np.zeros((n, m))
    for r in range(n):
        for s in range(m):
            if FRC_deA_x[r, s] > 0:
                FOD_deA_Xl[r, s] = RFE_deA[r, s] * ((n - abs(FRC_deA_x[r, s])) / (2 * n))
            else:
                FOD_deA_Xl[r, s] = RFE_deA[r, s] * np.sqrt((n + abs(FRC_deA_x[r, s])) / (2 * n))

    FEOF = np.zeros(n)
    for j in range(n):
        temp1 = FOD_Xl[j, :]
        temp2 = FOD_deA_Xl[j, :]
        FEOF[j] = 1 - ((np.sum((1 - temp1) * weight[j, :]) + np.sum((1 - temp2) * weightA_de[j, :])) / (2 * m))

    return FEOF

if __name__ == "__main__":
    load_data = loadmat('Example.mat')
    trandata = load_data['Example']

    scaler = MinMaxScaler()
    trandata[:, 1:3] = scaler.fit_transform(trandata[:, 1:3])

    delta = 1
    out_factors = FIEOD(trandata, delta)
    print(out_factors)

