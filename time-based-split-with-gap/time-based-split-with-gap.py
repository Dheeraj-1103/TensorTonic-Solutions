import numpy as np

def time_based_split(timestamps: list, train_end: int, gap: int, val_end: int) -> dict:
    timestamps = np.asarray(timestamps)

    train_idx = np.where(timestamps < train_end)[0]

    val_start = train_end + gap
    val_idx = np.where((timestamps >= val_start) & (timestamps < val_end))[0]

    return {
        "train_idx": train_idx,
        "val_idx": val_idx
    }