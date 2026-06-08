import pandas as pd
import matplotlib.pyplot as plt

data = [[2, 0.01596],
        [4, 0.014236],
        [8, 0.013141],
        [16,0.011649],
        [32, 0.010179],
        [64, 0.0093984],
        [128, 0.0089286]]
df = pd.DataFrame(data, columns=["Sdim", "L1loss"])

fig, ax = plt.subplots()
ax.plot(df["Sdim"], df["L1loss"], marker="o")
ax.set_xscale("log", base=2)
ax.set_xlabel("Sdim")
ax.set_ylabel("L1 loss")
ax.set_title("L1 Loss vs Sdim")
plt.tight_layout()
plt.savefig("images/L1_Sdim.png", dpi=150)

