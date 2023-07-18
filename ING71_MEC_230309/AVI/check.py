import numpy as np
from matplotlib import pyplot as plt

f = np.load("ING71_MEC_230309\AVI\ING71_MEC_230309_000_Behav_Fr1-9973_proc.npy", allow_pickle=True).item()

print(f['pupil'][0]['area'])
print(f)

plt.plot(f['pupil'][0]['area'])
plt.show()

