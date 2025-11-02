from scipy.stats import kruskal, chi2_contingency
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# === Load Data ===
healthy = pd.read_pickle(f"../healthy_embedding_with_projections.pkl")
healthy = healthy.rename(columns={"healthy_PCA_1": "PCA_1", "healthy_PCA_2": "PCA_2"})

diseased = pd.read_pickle(f"../diseased_embedding_with_projections.pkl")
diseased = diseased.rename(columns={"diseased_PCA_1": "PCA_1", "diseased_PCA_2": "PCA_2"})

df_con = pd.concat([diseased, healthy], ignore_index=True)

# === Define groups ===
df = df_con.copy()
middle = df[df['tail'] == 'middle']
upper = df[df['tail'] == 'upper']
lower = df[df['tail'] == 'lower']
tails = pd.concat([upper, lower])

# === Helper functions ===
def count_aa(seq_list):
    counts = Counter()
    total = 0
    for seq in seq_list:
        counts.update(seq)
        total += len(seq)
    freqs = {aa: counts[aa]/total for aa in counts}
    return freqs, counts

def compute_properties(seq_list):
    charge, hydrophobicity = [], []
    for seq in seq_list:
        try:
            analysis = ProteinAnalysis(seq)
            charge.append(analysis.charge_at_pH(7.0))
            hydrophobicity.append(analysis.gravy())
        except:
            continue
    return charge, hydrophobicity

# === Load data and define groups ===
df = pd.concat([diseased, healthy], ignore_index=True)
upper = df[df['tail'] == 'upper']
lower = df[df['tail'] == 'lower']
middle = df[df['tail'] == 'middle']

# === 1. Length ===
len_upper = [len(s) for s in upper['sequence']]
len_lower = [len(s) for s in lower['sequence']]
len_middle = [len(s) for s in middle['sequence']]

# p_len = kruskal(len_upper, len_lower, len_middle).pvalue
# print(f"Length (Kruskal-Wallis): p = {p_len:.4f}")
# print("→ Significant difference in length." if p_len < 0.05 else "→ No significant difference in length.")

# === 2. Amino acid frequencies ===
freq_up, raw_up = count_aa(upper['sequence'])
freq_lo, raw_lo = count_aa(lower['sequence'])
freq_mid, raw_mid = count_aa(middle['sequence'])

aa_set = sorted(set(freq_up) | set(freq_lo) | set(freq_mid))
raw_table = [
    [raw_up.get(aa, 0) for aa in aa_set],
    [raw_lo.get(aa, 0) for aa in aa_set],
    [raw_mid.get(aa, 0) for aa in aa_set]
]

# chi2, p_chi2, _, _ = chi2_contingency(raw_table)
# print(f"Amino acid composition (Chi-squared): p = {p_chi2:.4f}")
# print("→ Significant difference in amino acid composition." if p_chi2 < 0.05 else "→ No significant difference in amino acid composition.")

# === 3. Charge and hydrophobicity ===
charge_up, hydro_up = compute_properties(upper['sequence'])
charge_lo, hydro_lo = compute_properties(lower['sequence'])
charge_mid, hydro_mid = compute_properties(middle['sequence'])

# p_charge = kruskal(charge_up, charge_lo, charge_mid).pvalue
# print(f"Net charge (Kruskal-Wallis): p = {p_charge:.4f}")
# print("→ Significant difference in net charge." if p_charge < 0.05 else "→ No significant difference in net charge.")

# p_hydro = kruskal(hydro_up, hydro_lo, hydro_mid).pvalue
# print(f"Hydrophobicity (Kruskal-Wallis): p = {p_hydro:.4f}")
# print("→ Significant difference in hydrophobicity." if p_hydro < 0.05 else "→ No significant difference in hydrophobicity.")

# # === Plot ===
# fig, axes = plt.subplots(1, 4, figsize=(22, 5))
# fig.suptitle("CDRH3 Comparative Analysis: Upper vs Lower vs Middle", fontsize=16)

# # Length
# sns.boxplot(data=[len_upper, len_lower, len_middle], ax=axes[0])
# axes[0].set_xticklabels(["Upper", "Lower", "Middle"])
# axes[0].set_title("CDRH3 Length")
# axes[0].set_ylabel("Length")

# # AA Frequencies
# df_freqs = pd.DataFrame({
#     'Amino Acid': aa_set,
#     'Upper': [freq_up.get(aa, 0) for aa in aa_set],
#     'Lower': [freq_lo.get(aa, 0) for aa in aa_set],
#     'Middle': [freq_mid.get(aa, 0) for aa in aa_set],
# }).set_index('Amino Acid')
# df_freqs.plot(kind='bar', ax=axes[1])
# axes[1].set_title("AA Frequencies")
# axes[1].set_ylabel("Rel. Frequency")
# axes[1].legend(title="Group")

# # Net Charge
# sns.boxplot(data=[charge_up, charge_lo, charge_mid], ax=axes[2])
# axes[2].set_xticklabels(["Upper", "Lower", "Middle"])
# axes[2].set_title("Net Charge @ pH 7")
# axes[2].set_ylabel("Net Charge")

# # Hydrophobicity
# sns.boxplot(data=[hydro_up, hydro_lo, hydro_mid], ax=axes[3])
# axes[3].set_xticklabels(["Upper", "Lower", "Middle"])
# axes[3].set_title("Hydrophobicity (GRAVY)")
# axes[3].set_ylabel("GRAVY Score")

# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.savefig("upper_lower_middle_global_comparison.png")
# plt.close()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="ticks", font_scale=1.6)  # aumenta tutto in modo proporzionale

fig, axes = plt.subplots(1, 4, figsize=(28, 6))  # figura più larga e alta
fig.suptitle("CDRH3 Comparative Analysis: High vs Low vs Median PPL", fontsize=20)

boxplot_linewidth = 2
xtick_labels = ["High PPL", "Low PPL", "Median PPL"]

# === Length ===
sns.boxplot(data=[len_upper, len_lower, len_middle], ax=axes[0], linewidth=boxplot_linewidth)
axes[0].set_xticklabels(xtick_labels, fontsize=12)
axes[0].set_title("CDRH3 Length", fontsize=16)
axes[0].set_ylabel("Length", fontsize=14)
axes[0].tick_params(axis='y', labelsize=12)

# === AA Frequencies ===
df_freqs = pd.DataFrame({
    'Amino Acid': aa_set,
    'High PPL': [freq_up.get(aa, 0) for aa in aa_set],
    'Low PPL': [freq_lo.get(aa, 0) for aa in aa_set],
    'Median PPL': [freq_mid.get(aa, 0) for aa in aa_set],
}).set_index('Amino Acid')

df_freqs.plot(kind='bar', ax=axes[1], linewidth=1.5, width=0.8)
axes[1].set_title("AA Frequencies", fontsize=16)
axes[1].set_ylabel("Rel. Frequency", fontsize=14)
axes[1].tick_params(axis='x', labelrotation=60, labelsize=10)
axes[1].tick_params(axis='y', labelsize=12)
axes[1].legend(title="Group", fontsize=12, title_fontsize=13)

# === Net Charge ===
sns.boxplot(data=[charge_up, charge_lo, charge_mid], ax=axes[2], linewidth=boxplot_linewidth)
axes[2].set_xticklabels(xtick_labels, fontsize=12)
axes[2].set_title("Net Charge @ pH 7", fontsize=16)
axes[2].set_ylabel("Net Charge", fontsize=14)
axes[2].tick_params(axis='y', labelsize=12)

# === Hydrophobicity ===
sns.boxplot(data=[hydro_up, hydro_lo, hydro_mid], ax=axes[3], linewidth=boxplot_linewidth)
axes[3].set_xticklabels(xtick_labels, fontsize=12)
axes[3].set_title("Hydrophobicity (GRAVY)", fontsize=16)
axes[3].set_ylabel("GRAVY Score", fontsize=14)
axes[3].tick_params(axis='y', labelsize=12)

plt.tight_layout(rect=[0, 0.03, 1, 0.92])
plt.savefig("ppl_tail_comparison_improved.png", dpi=300)
plt.close()

