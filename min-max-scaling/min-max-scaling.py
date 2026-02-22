import numpy as np

def min_max_scaling(data):
    data = np.array(data, dtype=float)
    
    num_col = data.shape[1]
    
    for i in range(num_col):
        col = data[:, i]
        min_val = np.min(col)
        max_val = np.max(col)
        
        # Tránh chia cho 0 nếu cột constant
        if max_val != min_val:
            data[:, i] = (col - min_val) / (max_val - min_val)
        else:
            data[:, i] = 0.0
            
    return data.tolist()