import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from scipy.stats import chi2_contingency, mannwhitneyu

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

def perform_analysis(group1, group2, name1="Group1", name2="Group2", suffix="comparison"):

    print(f"\n==== {name1} vs {name2} ====")

    # Length
    len_1 = [len(seq) for seq in group1['sequence']]
    len_2 = [len(seq) for seq in group2['sequence']]
    p_len = mannwhitneyu(len_1, len_2, alternative="two-sided").pvalue
    print(f"Length (Mann-Whitney): p = {p_len:.4f}")
    print("→ Significant difference in length." if p_len < 0.05 else "→ No significant difference in length.")

    # AA Frequencies
    freq1, raw1 = count_aa(group1['sequence'])
    freq2, raw2 = count_aa(group2['sequence'])
    aa_set = sorted(set(freq1.keys()).union(freq2.keys()))
    raw_table = [
        [raw1.get(aa, 0) for aa in aa_set],
        [raw2.get(aa, 0) for aa in aa_set]
    ]
    chi2, p_chi2, _, _ = chi2_contingency(raw_table)
    print(f"Amino acids (Chi-squared): p = {p_chi2:.4f}")
    print("→ Significant difference in amino acid composition." if p_chi2 < 0.05 else "→ No significant difference in amino acid composition.")

    # Properties
    charge1, hydro1 = compute_properties(group1['sequence'])
    charge2, hydro2 = compute_properties(group2['sequence'])
    p_charge = mannwhitneyu(charge1, charge2, alternative="two-sided").pvalue
    p_hydro = mannwhitneyu(hydro1, hydro2, alternative="two-sided").pvalue

    print(f"Net charge (pH 5): p = {p_charge:.4f}")
    print("→ Significant difference in net charge." if p_charge < 0.05 else "→ No significant difference in net charge.")

    print(f"Hydrophobicity: p = {p_hydro:.4f}")
    print("→ Significant difference in hydrophobicity." if p_hydro < 0.05 else "→ No significant difference in hydrophobicity.")

    # Plot
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    fig.suptitle(f"CDRH3 Analysis: {name1} vs {name2}", fontsize=16)

    axes[0].hist([len_1, len_2], bins=range(5, 30), label=[name1, name2], alpha=0.7)
    axes[0].set_title("CDRH3 Length")
    axes[0].set_xlabel("Length")
    axes[0].set_ylabel("Count")
    axes[0].legend()

    df_freqs = pd.DataFrame({
        'Amino Acid': aa_set,
        name1: [freq1.get(aa, 0) for aa in aa_set],
        name2: [freq2.get(aa, 0) for aa in aa_set]
    }).set_index('Amino Acid')
    df_freqs.plot(kind='bar', ax=axes[1])
    axes[1].set_title("AA Frequencies")
    axes[1].set_ylabel("Rel. Frequency")
    axes[1].legend(title="Group")

    sns.boxplot(data=[charge1, charge2], ax=axes[2])
    axes[2].set_xticklabels([name1, name2])
    axes[2].set_title("Net Charge @ pH 7")
    axes[2].set_ylabel("Net Charge")

    sns.boxplot(data=[hydro1, hydro2], ax=axes[3])
    axes[3].set_xticklabels([name1, name2])
    axes[3].set_title("Hydrophobicity (GRAVY)")
    axes[3].set_ylabel("GRAVY Score")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f"{suffix}_combined_plot.png")
    plt.close()

# === First: Tails vs Middle ===
#perform_analysis(tails, middle, name1="Tails", name2="Middle", suffix="tails_vs_middle")

# === Then: Upper vs Lower vs Middle ===
# Puoi farlo con pairwise test e plotting separato se serve
#perform_analysis(upper, middle, name1="Upper", name2="Middle", suffix="upper_vs_middle")
#perform_analysis(lower, middle, name1="Lower", name2="Middle", suffix="lower_vs_middle")
#perform_analysis(upper, lower, name1="Upper", name2="Lower", suffix="upper_vs_lower")

# === Then: Healthy vs Diseased ===
#perform_analysis(healthy, diseased, name1="healthy", name2="diseased", suffix="healthy_vs_diseased")

#perform_analysis(healthy[healthy['tail']=='upper'], diseased[diseased['tail']=='upper'], name1="healthy_upper", name2="diseased_upper", suffix="healthy_vs_diseased_upper")
#perform_analysis(healthy[healthy['tail']=='lower'], diseased[diseased['tail']=='lower'], name1="healthy_lower", name2="diseased_lower", suffix="healthy_vs_diseased_lower")
#perform_analysis(healthy[healthy['tail']=='middle'], diseased[diseased['tail']=='middle'], name1="healthy_middle", name2="diseased_middle", suffix="healthy_vs_diseased_middle")

def plot_tail_aa_enrichment(healthy, diseased, output_path="PAPER_tail_aa_enrichment"):
    import matplotlib.pyplot as plt
    import pandas as pd

    plt.rcParams.update({
        'font.size': 14,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'axes.titlesize': 15,
        'axes.labelsize': 13,
        'legend.fontsize': 14
    })

    groups = {
        'Healthy – High PPL': healthy[healthy['tail'] == 'upper'],
        'Healthy – Low PPL': healthy[healthy['tail'] == 'lower'],
        'bnAbs – High PPL': diseased[diseased['tail'] == 'upper'],
        'bnAbs – Low PPL': diseased[diseased['tail'] == 'lower']
    }

    colors = {
        'Healthy – High PPL': "#D62728",
        'Healthy – Low PPL': "#FF9896",
        'bnAbs – High PPL': "#2CA02C",
        'bnAbs – Low PPL': "#98DF8A"
    }

    from collections import Counter
    def count_aa(seq_list):
        counts = Counter()
        total = 0
        for seq in seq_list:
            counts.update(seq)
            total += len(seq)
        freqs = {aa: counts[aa]/total for aa in counts}
        return freqs

    freqs_dict = {}
    aa_set_total = set()
    for label, df in groups.items():
        freqs = count_aa(df['sequence'])
        freqs_dict[label] = freqs
        aa_set_total.update(freqs.keys())

    aa_set_total = sorted(aa_set_total)
    df_freqs = pd.DataFrame({'Amino Acid': aa_set_total})
    for label in groups:
        df_freqs[label] = [freqs_dict[label].get(aa, 0) for aa in aa_set_total]
    df_freqs = df_freqs.set_index('Amino Acid')

    ax = df_freqs.plot(kind='bar', figsize=(7, 4),
                    color=[colors[col] for col in df_freqs.columns],
                    edgecolor='black', linewidth=0.5)  # Linee più spesse

    ax.set_ylabel("Relative Frequency")
    ax.set_xlabel("Amino Acid")
    ax.grid(False)
    ax.legend(frameon=False, loc="upper left")
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    plt.xticks(rotation=0)
    plt.tight_layout()
    #plt.savefig(output_path+'.png', format='svg', dpi=600, bbox_inches='tight', pad_inches=0.1)
    plt.savefig(output_path+'.svg', dpi=600, bbox_inches='tight', pad_inches=0.1)
    plt.close()

def plot_tail_length_density(healthy, diseased, output_path="PAPER_tail_length_density"):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.rcParams.update({
        'font.size': 14,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'axes.titlesize': 15,
        'axes.labelsize': 13,
        'legend.fontsize': 14
    })

    groups = {
        'Healthy – High PPL': healthy[healthy['tail'] == 'upper'],
        'Healthy – Low PPL': healthy[healthy['tail'] == 'lower'],
        'bnAbs – High PPL': diseased[diseased['tail'] == 'upper'],
        'bnAbs – Low PPL': diseased[diseased['tail'] == 'lower']
    }

    colors = {
        'Healthy – High PPL': "#D62728",
        'Healthy – Low PPL': "#FF9896",
        'bnAbs – High PPL': "#2CA02C",
        'bnAbs – Low PPL': "#98DF8A"
    }

    fig, ax = plt.subplots(figsize=(7, 4))  # usa subplots per ottenere l'oggetto Axes
    for label, df in groups.items():
        lengths = [len(seq) for seq in df['sequence']]
        sns.kdeplot(lengths, label=label, linewidth=3,  # Linee KDE più spesse
                    fill=False, alpha=1.0, color=colors[label],
                    bw_adjust=1.2, clip=(0, 40))

    plt.xlabel("CDR-H3 length")
    plt.ylabel("Density")
    plt.xlim(0, 40)
    plt.grid(False)
    plt.legend(frameon=False, loc="upper right")
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    plt.tight_layout()
    #plt.savefig(output_path+'.png', format='svg', dpi=600, bbox_inches='tight', pad_inches=0.1)
    plt.savefig(output_path+'.svg', dpi=600, bbox_inches='tight', pad_inches=0.1)
    plt.close()

#plot_tail_aa_enrichment(healthy, diseased)
plot_tail_length_density(healthy, diseased)
