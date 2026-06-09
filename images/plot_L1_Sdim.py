import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [[2, 0.01596],
        [4, 0.014236],
        [8, 0.013141],
        [16,0.011649],
        [32, 0.010179],
        [64, 0.0093984],
        [128, 0.0089286],
        [256, 0.0096211]
]
df = pd.DataFrame(data, columns=["Sdim", "L1loss"])

sns.set_theme()
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Sdim", y="L1loss", marker="o", ax=ax)
# ax.set_xscale("log", base=2)
ax.set_xlabel("$S^n$")
ax.set_ylabel("L1 validation loss")
# ax.set_title("L1 Loss vs $S^n$")
plt.tight_layout()
plt.savefig("images/L1_Sdim.png", dpi=150)

