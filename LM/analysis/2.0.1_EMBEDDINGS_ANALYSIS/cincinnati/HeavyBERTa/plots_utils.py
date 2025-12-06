##########################################################################
# ------------------------- UTILS -------------------------------------- #
##########################################################################

import matplotlib.colors as mcolors
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#!mkdir img


# LAB LABELED DATA: COLORS AND DETAILS
custom_palette = {
"BRO": {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=3)[2], alpha=1.0), 'size': 55, 'marker':'d'},
"diseased" : {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=3)[2], alpha=1.0), 'size': 55, 'marker':'d'},
"TEST": {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=4)[3], alpha=1.0), 'size': 55, 'marker':'D'},
"NON": {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=3)[0], alpha=1.0), 'size': 55, 'marker':'s'},
"healthy": {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=3)[0], alpha=1.0), 'size': 55, 'marker':'s'},
"NEU": {'color': mcolors.to_rgba(sns.color_palette("Set1", n_colors=3)[1], alpha=1.0), 'size': 55, 'marker':'v'},
"UNK": {'color': mcolors.to_rgba(sns.color_palette("Greys", n_colors=2)[1], alpha=0.2), 'size': 3, 'marker':'o'},
"IGHV1": {'color': mcolors.to_rgba("#56B4E9", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV2": {'color': mcolors.to_rgba("#E69F00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV3": {'color': mcolors.to_rgba("#D55E00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV4": {'color': mcolors.to_rgba("#CC79A7", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV5": {'color': mcolors.to_rgba("#F0E442", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV6": {'color': mcolors.to_rgba("#009E73", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHV7": {'color': mcolors.to_rgba("#0072B2", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ1": {'color': mcolors.to_rgba("#56B4E9", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ2": {'color': mcolors.to_rgba("#E69F00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ3": {'color': mcolors.to_rgba("#D55E00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ4": {'color': mcolors.to_rgba("#CC79A7", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ5": {'color': mcolors.to_rgba("#F0E442", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHJ6": {'color': mcolors.to_rgba("#009E73", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD1": {'color': mcolors.to_rgba("#56B4E9", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD2": {'color': mcolors.to_rgba("#E69F00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD3": {'color': mcolors.to_rgba("#D55E00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD4": {'color': mcolors.to_rgba("#CC79A7", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD5": {'color': mcolors.to_rgba("#F0E442", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD6": {'color': mcolors.to_rgba("#009E73", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHD7": {'color': mcolors.to_rgba("#0072B2", alpha=0.8), 'size': 3, 'marker': 'o'}, 
"XXXX": {'color': mcolors.to_rgba(sns.color_palette("Greys", n_colors=2)[1], alpha=0.2), 'size': 3, 'marker':'o'},
"XXXXX": {'color': mcolors.to_rgba(sns.color_palette("Greys", n_colors=2)[1], alpha=0.2), 'size': 3, 'marker':'o'},
"IGHA1": {'color': mcolors.to_rgba("#56B4E9", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHA2": {'color': mcolors.to_rgba("#E69F00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHM": {'color': mcolors.to_rgba("#D55E00", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHG2": {'color': mcolors.to_rgba("#CC79A7", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHG3": {'color': mcolors.to_rgba("#F0E442", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHG4": {'color': mcolors.to_rgba("#009E73", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHG1": {'color': mcolors.to_rgba("#0072B2", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHG": {'color': mcolors.to_rgba("#56B4E9", alpha=0.8), 'size': 3, 'marker': 'o'},
"IGHA": {'color': mcolors.to_rgba("#E69F00", alpha=0.8), 'size': 3, 'marker': 'o'},
"Human": {'color': mcolors.to_rgba("#009E73", alpha=0.9), 'size': 3, 'marker': 'o'},
"Humanized": {'color': mcolors.to_rgba("#E69F00", alpha=0.9), 'size': 3, 'marker': 'o'},
"Chimeric": {'color': mcolors.to_rgba("#56B4E9", alpha=0.9), 'size': 3, 'marker': 'o'},
"Mouse": {'color': mcolors.to_rgba("#CC79A7", alpha=0.9), 'size': 3, 'marker': 'o'},
}

def safe_keep_before_special_char(s):
    import re
    if not isinstance(s, str):
        return s
    return re.split(r'[^A-Za-z0-9]+', s)[0]

def extract_colors(custom_palette):
    return {k: v["color"] for k, v in custom_palette.items()}

########################################################################
######################### PCA OVERVIEW #################################
########################################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# se non l’hai già, definisci (o importa) custom_palette
try:
    custom_palette
except NameError:
    custom_palette = {}

def plot_pca_overview(df, file_suffix="output"):
    # ──────────────────── pulizia preliminare ────────────────────
    for col in ['v_family', 'j_family', 'd_family']:
        df[col] = df[col].astype(str).str.split('-', n=1).str[0]
    df.replace("nan", np.nan, inplace=True)

    # ───────── helper: plot categoriale con densità marginali ─────────
    def plot_joint_pca_with_marginals_no_title(fig, gs, df, category_col, show_ylabel=False):
        ax_joint   = fig.add_subplot(gs[1, 0])
        ax_marg_x  = fig.add_subplot(gs[0, 0], sharex=ax_joint)
        ax_marg_y  = fig.add_subplot(gs[1, 1], sharey=ax_joint)

        handles, labels = [], []
        for cat in df[category_col].dropna().unique():
            sub_df = df[df[category_col] == cat]
            style  = custom_palette.get(cat, {'color': 'grey', 'size': 10, 'marker': 'o'})

            sc = ax_joint.scatter(
                sub_df['pca1'], sub_df['pca2'],
                c=[style['color']] * len(sub_df),
                s=style['size'], marker=style['marker'],
                alpha=0.3, label=cat
            )
            handles.append(sc)
            labels.append(cat)

            sns.kdeplot(sub_df['pca1'], ax=ax_marg_x,
                        color=style['color'], fill=False,
                        linewidth=2, common_norm=False)
            sns.kdeplot(sub_df['pca2'], ax=ax_marg_y,
                        color=style['color'], fill=False,
                        linewidth=2, common_norm=False, vertical=True)

        ax_joint.set_xticks([]); ax_joint.set_yticks([])
        ax_marg_x.axis('off');   ax_marg_y.axis('off')
        ax_joint.set_xlabel("PCA 1", fontsize=16)
        ax_joint.set_ylabel("PCA 2" if show_ylabel else "", fontsize=16)

        ax_joint.legend(
            handles, labels, title='', loc='best', fontsize=10,
            frameon=False, markerscale=3, ncol=2,
            columnspacing=0.0, handletextpad=0.0, borderpad=0.0
        )

        for ax in (ax_joint, ax_marg_x, ax_marg_y):
            for spine in ax.spines.values():
                spine.set_linewidth(1.5)

    # ───────── helper: plot continuo con color-map e colorbar ─────────
    def plot_pca_continuous(df, ax, value_col, title):
        sc = ax.scatter(df['pca1'], df['pca2'],
                        c=df[value_col], cmap='coolwarm',
                        s=10, alpha=0.7)
        ax.set_xlabel("PCA 1", fontsize=16)
        ax.set_ylabel("", fontsize=16)
        ax.set_xticks([]); ax.set_yticks([])

        cb = plt.colorbar(sc, ax=ax)
        cb.set_label(title, fontsize=14)
        cb.ax.tick_params(labelsize=12)
        for spine in cb.ax.spines.values():
            spine.set_linewidth(1.5)

    # ─────────────────────── figure & griglia ────────────────────────
    fig   = plt.figure(figsize=(20, 5))
    outer = gridspec.GridSpec(1, 4, wspace=0.15)

    # ▸ 2 plot categoriali (v_family, j_family)
    cat_cols   = ['v_family', 'j_family']
    cat_titles = ['V Gene',   'J Gene']

    for i, (col, title) in enumerate(zip(cat_cols, cat_titles)):
        inner = gridspec.GridSpecFromSubplotSpec(
            2, 2, subplot_spec=outer[i],
            width_ratios=[4, 1], height_ratios=[1, 4],
            wspace=0.0, hspace=0.0
        )
        plot_joint_pca_with_marginals_no_title(
            fig, inner, df,
            category_col=col,
            show_ylabel=(i == 0)
        )

    # ▸ plot continuo su v_identity (colonna 2)
    inner_v = gridspec.GridSpecFromSubplotSpec(
        2, 2, subplot_spec=outer[2],
        width_ratios=[4, 1], height_ratios=[1, 4],
        wspace=0.0, hspace=0.0
    )
    ax_v      = fig.add_subplot(inner_v[1, 0])
    ax_v_mx   = fig.add_subplot(inner_v[0, 0], sharex=ax_v)
    ax_v_my   = fig.add_subplot(inner_v[1, 1], sharey=ax_v)
    plot_pca_continuous(df, ax_v, 'v_identity', 'V identity')
    ax_v_mx.axis('off'); ax_v_my.axis('off')
    for ax in (ax_v, ax_v_mx, ax_v_my):
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    # ▸ nuovo plot continuo su j_identity (colonna 3)
    inner_j = gridspec.GridSpecFromSubplotSpec(
        2, 2, subplot_spec=outer[3],
        width_ratios=[4, 1], height_ratios=[1, 4],
        wspace=0.0, hspace=0.0
    )
    ax_j      = fig.add_subplot(inner_j[1, 0])
    ax_j_mx   = fig.add_subplot(inner_j[0, 0], sharex=ax_j)
    ax_j_my   = fig.add_subplot(inner_j[1, 1], sharey=ax_j)
    plot_pca_continuous(df, ax_j, 'j_identity', 'J identity')
    ax_j_mx.axis('off'); ax_j_my.axis('off')
    for ax in (ax_j, ax_j_mx, ax_j_my):
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    # ─────────────── layout, salvataggio, display ────────────────
    plt.tight_layout()
    plt.subplots_adjust(left=0.03, right=0.80, top=0.95,
                        bottom=0.10, wspace=0.00)

    plt.savefig(f"{file_suffix}_pca_overview.png", dpi=300,
                bbox_inches='tight')
    plt.savefig(f"{file_suffix}_pca_overview.svg", dpi=300,
                bbox_inches='tight')
    plt.show()
    plt.close()

########################################################################
######################### UMAP OVERVIEW ################################
########################################################################

# Funzione principale
def plot_umap_overview(df, file_suffix="output"):
    # Pulizia nomi geni
    for col in ['v_family', 'j_family', 'd_family']:
        df[col] = df[col].astype(str).str.split('-', n=1).str[0]
    df.replace("nan", np.nan, inplace=True)

    fig = plt.figure(figsize=(30, 5))  # aumentata larghezza
    outer = gridspec.GridSpec(1, 5, wspace=0.15)

    cols = ['v_family', 'j_family', 'd_family']
    titles = ['V Gene', 'J Gene', 'D Gene']

    for i, (col, title) in enumerate(zip(cols, titles)):
        inner = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer[i],
                                                width_ratios=[4, 1], height_ratios=[1, 4],
                                                wspace=0.0, hspace=0.0)
        plot_joint_umap_with_marginals_no_title(fig, inner, df, col, legend_title='', show_ylabel=(i == 0))

    # LC CDR3 Length
    inner_lc = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer[3],
                                                width_ratios=[4, 1], height_ratios=[1, 4],
                                                wspace=0.0, hspace=0.0)
    ax_main_lc = fig.add_subplot(inner_lc[1, 0])
    ax_marg_x_lc = fig.add_subplot(inner_lc[0, 0], sharex=ax_main_lc)
    ax_marg_y_lc = fig.add_subplot(inner_lc[1, 1], sharey=ax_main_lc)
    plot_umap_continuous(df, ax_main_lc, 'v_identity', 'V identity')
    ax_marg_x_lc.axis('off')
    ax_marg_y_lc.axis('off')

    # HC CDR3 Length
    inner_hc = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer[4],
                                                width_ratios=[4, 1], height_ratios=[1, 4],
                                                wspace=0.0, hspace=0.0)
    ax_main_hc = fig.add_subplot(inner_hc[1, 0])
    ax_marg_x_hc = fig.add_subplot(inner_hc[0, 0], sharex=ax_main_hc)
    ax_marg_y_hc = fig.add_subplot(inner_hc[1, 1], sharey=ax_main_hc)
    plot_umap_continuous(df, ax_main_hc, 'j_identity', 'J identity')
    ax_marg_x_hc.axis('off')
    ax_marg_y_hc.axis('off')

    plt.tight_layout()
    plt.subplots_adjust(left=0.03, right=0.98, top=0.95, bottom=0.1, wspace=0.00)
    plt.savefig(f"{file_suffix}_umap_overview.png", dpi=300, bbox_inches='tight')
    plt.savefig(f"{file_suffix}_umap_overview.svg", dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

########################################################################
######################### LDA OVERVIEW #################################
########################################################################
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import pandas as pd
import re

def compute_multiple_ldas(df, embedding_col='embeddings', target_cols=['v_family', 'j_family', 'd_family'], n_components=2):
    """
    Applies LDA to embeddings using multiple target columns.
    Adds separate LDA projections to the dataframe for each target.

    Returns:
    - df with new columns: lda1_{target}, lda2_{target}, ...
    """

    def clean_and_convert_embedding(s):
        if isinstance(s, np.ndarray):
            return s
        if isinstance(s, str):
            s_clean = re.sub(r'\s+', ' ', s.strip())
            s_clean = re.sub(r'(?<=\d)-', ' -', s_clean)
            s_clean = re.sub(r'(?<=[0-9]) (?=[-+]?\d)', ',', s_clean)
            return np.fromstring(s_clean.strip("[]"), sep=",")
        return np.array(s)

    # Clean embeddings
    df.replace("nan", np.nan, inplace=True)
    df[embedding_col] = df[embedding_col].apply(clean_and_convert_embedding)
    embedding_matrix = np.vstack(df[embedding_col].values)

    for target_col in target_cols:
        labels = df[target_col].astype(str).values  # ensure categorical strings
        lda = LinearDiscriminantAnalysis(n_components=n_components)
        lda_result = lda.fit_transform(embedding_matrix, labels)
        for i in range(n_components):
            df[f'lda{i+1}_{target_col[0]}'] = lda_result[:, i]

    return df


def plot_lda_overview(df, file_suffix="output"):
    fig = plt.figure(figsize=(20, 5))
    outer = gridspec.GridSpec(1, 4, wspace=0.15)

    genes = ['v_family', 'j_family', 'd_family']
    titles = ['V Gene', 'J Gene', 'D Gene']

    def plot_joint(fig, gs, x, y, category_col, legend_title, show_ylabel):
        ax_joint = fig.add_subplot(gs[1, 0])
        ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_joint)
        ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_joint)

        handles, labels = [], []

        for cat in df[category_col].dropna().unique():
            sub_df = df[df[category_col] == cat]
            style = custom_palette.get(cat, {'color': 'grey', 'size': 10, 'marker': 'o'})
            sc = ax_joint.scatter(sub_df[x], sub_df[y],
                                  c=[style['color']] * len(sub_df),
                                s=style['size'], marker=style['marker'],
                                alpha=0.3, label=cat)
            handles.append(sc)
            labels.append(cat)

            sns.kdeplot(sub_df[x], ax=ax_marg_x, color=style['color'],
                        fill=False, linewidth=2, common_norm=False)
            sns.kdeplot(sub_df[y], ax=ax_marg_y, color=style['color'],
                        fill=False, linewidth=2, common_norm=False, vertical=True)

        ax_joint.set_xticks([])
        ax_joint.set_yticks([])
        ax_joint.set_xlabel("LDA 1", fontsize=16)
        ax_joint.set_ylabel("LDA 2" if show_ylabel else "", fontsize=16)
        ax_marg_x.axis('off')
        ax_marg_y.axis('off')

        # ax_joint.legend(handles, labels, title=legend_title, loc='upper center',
        #                 bbox_to_anchor=(0.5, -0.1), fontsize=14, title_fontsize=16,
        #                 ncol=3, frameon=False, markerscale=3)
        ax_joint.legend(handles, labels, title='', loc='best', fontsize=10, title_fontsize=10,
                frameon=False, markerscale=3, ncol=2,
                columnspacing=0.0, handletextpad=0.0, borderpad=0.0)
        # >>> Qui aumenta lo spessore dei bordi
        for ax in [ax_joint, ax_marg_x, ax_marg_y]:
            for spine in ax.spines.values():
                spine.set_linewidth(1.5)

    # Plot each LDA projection (v, j, d)
    for i, (gene, title) in enumerate(zip(genes, titles)):
        inner = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer[i],
                                                width_ratios=[4, 1], height_ratios=[1, 4],
                                                wspace=0.0, hspace=0.0)
        plot_joint(fig, inner,
                f'lda1_{gene[0]}', f'lda2_{gene[0]}',
                category_col=gene,
                legend_title='',
                show_ylabel=(i == 0))

    plt.tight_layout()
    plt.subplots_adjust(left=0.03, right=0.80, top=0.95, bottom=0.1)
    plt.savefig(f"{file_suffix}_lda_overview.png", dpi=300, bbox_inches='tight')
    plt.savefig(f"{file_suffix}_lda_overview.svg", dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

########################################################################
######################### UMAP 1 GENE ##################################
########################################################################
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_umap_single_gene(df, gene_col, title, file_suffix="output_umap"):
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import matplotlib.gridspec as gridspec

    # Pulizia della colonna del gene
    df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

    # Layout con marginali
    fig = plt.figure(figsize=(5.5, 5))
    gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4],
                        wspace=0.05, hspace=0.05)

    ax_main = fig.add_subplot(gs[1, 0])
    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_main)

    handles = []
    labels = []

    for gene_val in df[gene_col].dropna().unique():
        sub_df = df[df[gene_col] == gene_val]
        style = custom_palette.get(gene_val, {'color': 'grey', 'size': 10, 'marker': 'o'})
        
        # Main scatter
        sc = ax_main.scatter(sub_df['umap1'], sub_df['umap2'],
                             c=[style['color']] * len(sub_df),
                            s=style['size'], marker=style['marker'],
                            alpha=0.4, label=gene_val)
        handles.append(sc)
        labels.append(gene_val)

        # KDE marginali
        sns.kdeplot(sub_df['umap1'], ax=ax_marg_x, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False)
        sns.kdeplot(sub_df['umap2'], ax=ax_marg_y, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False, vertical=True)

    # Main plot settings
    ax_main.set_xticks([])
    ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)

    # Marginali: nascondi assi e label
    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # Legenda compatta
    ax_main.legend(handles, labels, title='',
                loc='best', fontsize=12, title_fontsize=14,
                frameon=False, markerscale=5, ncol=2,
                columnspacing=0.0, handletextpad=0.0, borderpad=0.0)
    # >>> Qui aumenta lo spessore dei bordi
    for ax in [ax_main, ax_marg_x, ax_marg_y]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig(f"{file_suffix}_umap_{gene_col}.png", dpi=300, bbox_inches='tight')
    plt.savefig(f"{file_suffix}_umap_{gene_col}.svg", dpi=300, bbox_inches='tight')
    plt.show()

# Funzione con marginal KDE per variabili categoriche
def plot_joint_umap_with_marginals_no_title(fig, gs, df, category_col, legend_title=None, show_ylabel=False):
    ax_joint = fig.add_subplot(gs[1, 0])
    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_joint)
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_joint)

    handles = []
    labels = []

    for cat in df[category_col].dropna().unique():
        sub_df = df[df[category_col] == cat]
        style = custom_palette.get(cat, {'color': 'grey', 'size': 10, 'marker': 'o'})
        sc = ax_joint.scatter(sub_df['umap1'], sub_df['umap2'],
                              c=[style['color']] * len(sub_df),
                            s=style['size'], marker=style['marker'],
                            alpha=0.3, label=cat)
        handles.append(sc)
        labels.append(cat)

        sns.kdeplot(sub_df['umap1'], ax=ax_marg_x, color=style['color'],
                    fill=False, linewidth=2, common_norm=False)
        sns.kdeplot(sub_df['umap2'], ax=ax_marg_y, color=style['color'],
                    fill=False, linewidth=2, common_norm=False, vertical=True)

    ax_joint.set_xticks([])
    ax_joint.set_yticks([])
    ax_marg_x.axis('off')
    ax_marg_y.axis('off')
    ax_joint.set_xlabel("UMAP 1", fontsize=16)
    ax_joint.set_ylabel("UMAP 2" if show_ylabel else "", fontsize=16)

    ax_joint.legend(handles, labels, title='' , loc='best', fontsize=10, title_fontsize=10,
                    frameon=False, markerscale=3, ncol=2,
                    columnspacing=0.0, handletextpad=0.0, borderpad=0.0) #title=legend_title

    for ax in [ax_joint, ax_marg_x, ax_marg_y]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

# Funzione per variabile continua
def plot_umap_continuous(df, ax, value_col, title):
    sc = ax.scatter(df['umap1'], df['umap2'], c=df[value_col],
                    cmap='coolwarm', s=10, alpha=0.7)
    ax.set_xlabel("UMAP 1", fontsize=16)
    ax.set_ylabel("", fontsize=16)
    ax.set_xticks([])
    ax.set_yticks([])
    cb = plt.colorbar(sc, ax=ax)
    cb.set_label(title, fontsize=14)
    cb.ax.tick_params(labelsize=12)

    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

def plot_umap_single_gene_INSCAPE(df, gene_col, title, file_suffix="output_umap"):
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import matplotlib.gridspec as gridspec

    # Pulizia della colonna del gene
    df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

    # Layout con marginali
    fig = plt.figure(figsize=(5.5, 5))
    gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4],
                        wspace=0.05, hspace=0.05)

    ax_main = fig.add_subplot(gs[1, 0])
    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_main)

    handles = []
    labels = []

    for gene_val in df[gene_col].dropna().unique():
        sub_df = df[df[gene_col] == gene_val]
        style = custom_palette.get(gene_val, {'color': 'grey', 'size': 10, 'marker': 'o'})
        
        # Main scatter
        sc = ax_main.scatter(sub_df['umap1'], sub_df['umap2'],
                             c=[style['color']] * len(sub_df),
                             s=style['size'], marker=style['marker'],
                             alpha=0.4, label=gene_val)
        handles.append(sc)
        labels.append(gene_val)

        # KDE marginali
        sns.kdeplot(sub_df['umap1'], ax=ax_marg_x, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False)
        sns.kdeplot(sub_df['umap2'], ax=ax_marg_y, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False, vertical=True)

    # Main plot settings
    ax_main.set_xticks([])
    ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)

    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # Bordi più spessi
    for ax in [ax_main, ax_marg_x, ax_marg_y]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    # Salva la figura senza legenda
    plt.tight_layout()
    plt.savefig(f"{file_suffix}_umap_{gene_col}_NO_LEGEND.png", dpi=300, bbox_inches='tight')

    # Crea figura separata solo per la legenda
    fig_legend = plt.figure(figsize=(3, 1))  # Adatta le dimensioni come necessario
    legend = fig_legend.legend(handles, labels, title=title,
                               loc='center', fontsize=12, title_fontsize=14,
                               frameon=False, markerscale=5, ncol=2,
                               columnspacing=0.0, handletextpad=0.4, borderpad=0.0)
    fig_legend.canvas.draw()
    fig_legend.savefig(f"{file_suffix}_umap_{gene_col}_LEGEND.svg", dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)
    plt.close(fig_legend)



def plot_umap_single_gene_INSCAPE_biggerpoints(df, gene_col, title, file_suffix="output_umap"):
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import matplotlib.gridspec as gridspec

    # Pulizia della colonna del gene
    df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

    # Layout con marginali
    fig = plt.figure(figsize=(5.5, 5))
    gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4],
                        wspace=0.05, hspace=0.05)

    ax_main = fig.add_subplot(gs[1, 0])
    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_main)

    handles = []
    labels = []

    for gene_val in df[gene_col].dropna().unique():
        sub_df = df[df[gene_col] == gene_val]
        style = custom_palette.get(gene_val, {'color': 'grey', 'size': 40, 'marker': 'o'})
        
        # Main scatter
        sc = ax_main.scatter(sub_df['umap1'], sub_df['umap2'],
                             c=[style['color']] * len(sub_df),
                             s=style['size'], marker=style['marker'],
                             alpha=1.0, label=gene_val)
        handles.append(sc)
        labels.append(gene_val)

        # KDE marginali
        sns.kdeplot(sub_df['umap1'], ax=ax_marg_x, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False)
        sns.kdeplot(sub_df['umap2'], ax=ax_marg_y, color=style['color'],
                    fill=False, linewidth=1.5, common_norm=False, vertical=True)

    # Main plot settings
    ax_main.set_xticks([])
    ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)

    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # Bordi più spessi
    for ax in [ax_main, ax_marg_x, ax_marg_y]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    # Salva la figura senza legenda
    plt.tight_layout()
    plt.savefig(f"{file_suffix}_umap_{gene_col}_NO_LEGEND.png", dpi=300, bbox_inches='tight')

    # Crea figura separata solo per la legenda
    fig_legend = plt.figure(figsize=(3, 1))  # Adatta le dimensioni come necessario
    legend = fig_legend.legend(handles, labels, title=title,
                               loc='center', fontsize=12, title_fontsize=14,
                               frameon=False, markerscale=5, ncol=2,
                               columnspacing=0.0, handletextpad=0.4, borderpad=0.0)
    fig_legend.canvas.draw()
    fig_legend.savefig(f"{file_suffix}_umap_{gene_col}_LEGEND.svg", dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)
    plt.close(fig_legend)

########################################################################
######################### PCA 1 GENE ###################################
########################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.gridspec as gridspec


# ──────────────────────────────────────────────────────────────────────
# 1)  PCA per un singolo gene con marginal KDE
# ──────────────────────────────────────────────────────────────────────
def plot_pca_single_gene(df, gene_col, title, file_suffix="output_pca"):
    # Pulizia della colonna del gene (rimuove eventuale suffisso dopo '-')
    df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

    # Layout con marginali
    fig = plt.figure(figsize=(5.5, 5))
    gs  = gridspec.GridSpec(
        2, 2, width_ratios=[4, 1], height_ratios=[1, 4],
        wspace=0.05, hspace=0.05
    )

    ax_main   = fig.add_subplot(gs[1, 0])
    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=ax_main)

    handles, labels = [], []

    for gene_val in df[gene_col].dropna().unique():
        sub_df = df[df[gene_col] == gene_val]
        style  = custom_palette.get(gene_val, {'color': 'grey',
                                            'size': 10, 'marker': 'o'})
        # Scatter principale
        sc = ax_main.scatter(
            sub_df['pca1'], sub_df['pca2'],
            c=[style['color']] * len(sub_df),
            s=style['size'], marker=style['marker'],
            alpha=0.4, label=gene_val
        )
        handles.append(sc)
        labels.append(gene_val)

        # KDE marginali
        sns.kdeplot(sub_df['pca1'], ax=ax_marg_x,
                    color=style['color'], fill=False,
                    linewidth=1.5, common_norm=False)
        sns.kdeplot(sub_df['pca2'], ax=ax_marg_y,
                    color=style['color'], fill=False,
                    linewidth=1.5, common_norm=False, vertical=True)

    # Main plot settings
    ax_main.set_xticks([]); ax_main.set_yticks([])
    ax_main.set_xlabel("PCA 1", fontsize=16)
    ax_main.set_ylabel("PCA 2", fontsize=16)

    # Marginali: nascondi assi
    ax_marg_x.axis('off'); ax_marg_y.axis('off')

    # Legenda compatta
    ax_main.legend(handles, labels, title='',
                   loc='best', fontsize=12, frameon=False,
                   markerscale=5, ncol=2,
                   columnspacing=0.0, handletextpad=0.0, borderpad=0.0)

    # Bordi più evidenti
    for ax in (ax_main, ax_marg_x, ax_marg_y):
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig(f"{file_suffix}_pca_{gene_col}.png", dpi=300,
                bbox_inches='tight')
    plt.savefig(f"{file_suffix}_pca_{gene_col}.svg", dpi=300,
                bbox_inches='tight')
    plt.show()
    plt.close()


########################################################################
######################### 4 UMAP 1 GENE #################################
########################################################################
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
import pandas as pd
from typing import List, Dict, Any


def plot_umap_four_datasets(
    dfs: List[pd.DataFrame],
    gene_col: str,
    file_suffix: str = "output_umap_four",
    custom_palette=custom_palette
) :
    """
    Disegna 4 UMAP con distribuzioni marginali e **unica legenda** posta a destra
    dei pannelli. I titoli dei singoli pannelli sono rimossi.

    Parameters
    ----------
    dfs : list[pd.DataFrame]
        Esattamente 4 dataframe, ciascuno con colonne ``umap1`` e ``umap2``.
    gene_col : str
        Colonna da usare per la colorazione dei punti.
    file_suffix : str, default ``'output_umap_four'``
        Prefisso del file SVG in output.
    custom_palette : dict, optional
        Mapping ``gene_val -> dict(color, size, marker)``.
    """
    if custom_palette is None:
        custom_palette = {}

    # 5.5" per ognuno dei quattro pannelli + ~2" per la legenda
    fig = plt.figure(figsize=(5.5 * 4 + 2, 5))
    # 2 righe × 8 colonne (= 4 × [scatter, margY])
    gs = gridspec.GridSpec(
        2,
        8,
        width_ratios=[4, 1] * 4,
        height_ratios=[1, 4],
        wspace=0.05,
        hspace=0.05,
    )

    handles_dict: dict[str, Any] = {}

    for i, df in enumerate(dfs):
        # Normalizziamo la colonna gene (prima del '-')
        df = df.copy()
        df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

        ax_main = fig.add_subplot(gs[1, 2 * i])
        ax_marg_x = fig.add_subplot(gs[0, 2 * i], sharex=ax_main)
        ax_marg_y = fig.add_subplot(gs[1, 2 * i + 1], sharey=ax_main)

        for gene_val in df[gene_col].dropna().unique():
            style = custom_palette.get(
                gene_val, {"color": "grey", "size": 10, "marker": "o"}
            )
            sub_df = df[df[gene_col] == gene_val]

            sc = ax_main.scatter(
                sub_df["umap1"],
                sub_df["umap2"],
                c=[style["color"]] * len(sub_df),
                s=style["size"],
                marker=style["marker"],
                alpha=0.4,
                label=gene_val,
            )
            # teniamo un solo handle per gene
            if gene_val not in handles_dict:
                handles_dict[gene_val] = sc

            sns.kdeplot(
                sub_df["umap1"],
                ax=ax_marg_x,
                color=style["color"],
                fill=False,
                linewidth=1.5,
                common_norm=False,
            )
            sns.kdeplot(
                sub_df["umap2"],
                ax=ax_marg_y,
                color=style["color"],
                fill=False,
                linewidth=1.5,
                common_norm=False,
                vertical=True,
            )

        # Estetica assi (niente titoli)
        ax_main.set_xticks([])
        ax_main.set_yticks([])
        ax_main.set_xlabel("UMAP 1", fontsize=16)
        if i == 0:
            ax_main.set_ylabel("UMAP 2", fontsize=16)
        ax_marg_x.axis("off")
        ax_marg_y.axis("off")

        for ax in (ax_main, ax_marg_x, ax_marg_y):
            for spine in ax.spines.values():
                spine.set_linewidth(1.5)

    # --------------- Legenda comune -----------------
    handles = list(handles_dict.values())
    labels = list(handles_dict.keys())
    fig.legend(
        handles,
        labels,
        title=gene_col.replace('_',' ').replace('family','gene').capitalize()      ,
        loc="center left",
        bbox_to_anchor=(0.90, 0.5),
        frameon=False,
        ncol=1,
        markerscale=5,
        fontsize=14,
        title_fontsize=13,
        borderpad=0.0,
        labelspacing=0.4,
    )

    plt.tight_layout()
    output_path = f"{file_suffix}.svg"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    output_path = f"{file_suffix}.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    print(f"✓  Salvato UMAP multiplo con legenda in: {output_path}")


########################################################################
######################### 4 PCA 1 GENE #################################
########################################################################


def plot_pca_four_datasets(
    dfs: List[pd.DataFrame],
    gene_col: str,
    file_suffix: str = "output_pca_four",
    custom_palette=custom_palette
) :
    """
    Disegna 4 PCA con distribuzioni marginali e **unica legenda** posta a destra
    dei pannelli. I titoli dei singoli pannelli sono rimossi.

    Parameters
    ----------
    dfs : list[pd.DataFrame]
        Esattamente 4 dataframe, ciascuno con colonne ``pca1`` e ``pca2``.
    gene_col : str
        Colonna da usare per la colorazione dei punti.
    file_suffix : str, default ``'output_pca_four'``
        Prefisso del file SVG in output.
    custom_palette : dict, optional
        Mapping ``gene_val -> dict(color, size, marker)``.
    """
    if custom_palette is None:
        custom_palette = {}

    # 5.5" per ognuno dei quattro pannelli + ~2" per la legenda
    fig = plt.figure(figsize=(5.5 * 4 + 2, 5))
    # 2 righe × 8 colonne (= 4 × [scatter, margY])
    gs = gridspec.GridSpec(
        2,
        8,
        width_ratios=[4, 1] * 4,
        height_ratios=[1, 4],
        wspace=0.05,
        hspace=0.05,
    )

    handles_dict: dict[str, Any] = {}

    for i, df in enumerate(dfs):
        # Normalizziamo la colonna gene (prima del '-')
        df = df.copy()
        df[gene_col] = df[gene_col].astype(str).str.split('-', n=1).str[0]

        ax_main = fig.add_subplot(gs[1, 2 * i])
        ax_marg_x = fig.add_subplot(gs[0, 2 * i], sharex=ax_main)
        ax_marg_y = fig.add_subplot(gs[1, 2 * i + 1], sharey=ax_main)

        for gene_val in df[gene_col].dropna().unique():
            style = custom_palette.get(
                gene_val, {"color": "grey", "size": 10, "marker": "o"}
            )
            sub_df = df[df[gene_col] == gene_val]

            sc = ax_main.scatter(
                sub_df["pca1"],
                sub_df["pca2"],
                c=[style["color"]] * len(sub_df),
                s=style["size"],
                marker=style["marker"],
                alpha=0.4,
                label=gene_val,
            )
            # teniamo un solo handle per gene
            if gene_val not in handles_dict:
                handles_dict[gene_val] = sc

            sns.kdeplot(
                sub_df["pca1"],
                ax=ax_marg_x,
                color=style["color"],
                fill=False,
                linewidth=1.5,
                common_norm=False,
            )
            sns.kdeplot(
                sub_df["pca2"],
                ax=ax_marg_y,
                color=style["color"],
                fill=False,
                linewidth=1.5,
                common_norm=False,
                vertical=True,
            )

        # Estetica assi (niente titoli)
        ax_main.set_xticks([])
        ax_main.set_yticks([])
        ax_main.set_xlabel("PCA 1", fontsize=16)
        if i == 0:
            ax_main.set_ylabel("PCA 2", fontsize=16)
        ax_marg_x.axis("off")
        ax_marg_y.axis("off")

        for ax in (ax_main, ax_marg_x, ax_marg_y):
            for spine in ax.spines.values():
                spine.set_linewidth(1.5)

    # --------------- Legenda comune -----------------
    handles = list(handles_dict.values())
    labels = list(handles_dict.keys())
    fig.legend(
        handles,
        labels,
        title=gene_col.replace('_',' ').replace('family','gene').capitalize()      ,
        loc="center left",
        bbox_to_anchor=(0.90, 0.5),
        frameon=False,
        ncol=1,
        markerscale=5,
        fontsize=14,
        title_fontsize=13,
        borderpad=0.0,
        labelspacing=0.4,
    )

    plt.tight_layout()
    output_path = f"{file_suffix}.svg"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    output_path = f"{file_suffix}.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    print(f"✓  Salvato PCA multiplo con legenda in: {output_path}")        
    
    
    
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import pandas as pd

def plot_umap_single_gene_numeric_INSCAPE(
    df, gene_col, title, file_suffix="output_umap",
    value_range=(0, 1), figsize=(5.5, 5), cmap_name="viridis"
):
    # 0) copy + numeric conversion
    df = df.copy()
    df[gene_col] = pd.to_numeric(df[gene_col], errors="coerce")

    # 1) layout a griglia 2×2
    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs  = gridspec.GridSpec(
        2, 2,
        width_ratios =[4, 1],
        height_ratios=[1, 4],
        wspace=0.05, hspace=0.05,
        figure=fig
    )

    ax_marg_x = fig.add_subplot(gs[0, 0], sharex=None)   # solo per dimensionare
    ax_main   = fig.add_subplot(gs[1, 0])                # qui scatter
    ax_marg_y = fig.add_subplot(gs[1, 1], sharey=None)   # solo per dimensionare
    ax_cbar   = fig.add_subplot(gs[0, 1])                # colorbar “vero”

    # 2) scatter nel main
    cmap = get_cmap(cmap_name)
    norm = Normalize(vmin=value_range[0], vmax=value_range[1])
    sc   = ax_main.scatter(
        df['umap1'], df['umap2'],
        c=df[gene_col], cmap=cmap, norm=norm,
        s=20, alpha=0.6, marker='o', edgecolors='none'
    )
    sc.set_clim(*value_range)

    # 3) due KDE “di contorno” (ma non usiamo i loro assi per nient'altro)
    sns.kdeplot(x=df['umap1'], ax=ax_marg_x,
                color='black', linewidth=1.5, fill=False)
    sns.kdeplot(y=df['umap2'], ax=ax_marg_y,
                color='black', linewidth=1.5, fill=False)

    # 4) pulizia assi UMAP
    ax_main.set_xticks([]); ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)
    for spine in ax_main.spines.values():
        spine.set_linewidth(1.5)

    # 5) colorbar sul suo asse dedicato (ax_cbar)
    cbar = fig.colorbar(sc, cax=ax_cbar, orientation='vertical')
    cbar.set_label(title, fontsize=12)
    ax_cbar.yaxis.set_label_position('right')
    ax_cbar.yaxis.tick_right()
    for sp in ax_cbar.spines.values():
        sp.set_visible(True)
    ax_cbar.set_xticks([])
    
    # --- Aumenta la dimensione del font dei tick label e del label
    cbar.ax.tick_params(labelsize=14)                # tick numerici più grandi
    cbar.set_label(title, fontsize=16)               # etichetta a lato più grande

    # --- Aggiungi un bordo nero all'intero riquadro della colorbar
    # Assicurati che la cornice (frame) sia visibile
    cbar.ax.set_frame_on(True)
    cbar.outline.set_edgecolor('black')
    cbar.outline.set_linewidth(1.0)

    # 6) nascondo solo i veri marginali (assiali), MA NON ax_cbar
    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # 7) save & show
    fig.savefig(f"{file_suffix}_umap_{gene_col}_smallcmap.png",
                dpi=300, bbox_inches='tight')
    fig.savefig(f"{file_suffix}_umap_{gene_col}_smallcmap.svg",
                dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)


def plot_umap_single_gene_numeric_INSCAPE_cmapgrande(
    df, gene_col, title, file_suffix="output_umap",
    value_range=(0, 1), figsize=(5.5, 5), cmap_name="viridis"
):
    df = df.copy()
    df[gene_col] = pd.to_numeric(df[gene_col], errors="coerce")

    # 1) Layout 2×2: colonna 0 per UMAP, colonna 1 (più larga) per la colorbar
    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs  = gridspec.GridSpec(
        2, 2,
        width_ratios =[4, 0.8],    # <-- qui ingrandisci la colonna della cbar
        height_ratios=[1, 4],
        wspace=0.05, hspace=0.05,
        figure=fig
    )

    # Axes
    ax_marg_x = fig.add_subplot(gs[0, 0])
    ax_main   = fig.add_subplot(gs[1, 0])
    ax_marg_y = fig.add_subplot(gs[1, 1])
    # cbar che occupa entrambe le righe della colonna 1
    ax_cbar   = fig.add_subplot(gs[:, 1])

    # 2) scatter
    cmap = get_cmap(cmap_name)
    norm = Normalize(vmin=value_range[0], vmax=value_range[1])
    sc   = ax_main.scatter(
        df['umap1'], df['umap2'],
        c=df[gene_col], cmap=cmap, norm=norm,
        s=40, alpha=0.6, edgecolors='none'
    )

    # 3) marginali “in prestito”
    sns.kdeplot(x=df['umap1'], ax=ax_marg_x,
                color='black', linewidth=1.5, fill=False)
    sns.kdeplot(y=df['umap2'], ax=ax_marg_y,
                color='black', linewidth=1.5, fill=False)

    # 4) pulizia main
    ax_main.set_xticks([]); ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)
    for spine in ax_main.spines.values():
        spine.set_linewidth(1.5)

    # 5) colorbar
    cbar = fig.colorbar(sc, cax=ax_cbar, orientation='vertical')
    cbar.set_label(title, fontsize=12)
    ax_cbar.yaxis.set_label_position('right')
    ax_cbar.yaxis.tick_right()
    ax_cbar.set_xticks([])
    for sp in ax_cbar.spines.values():
        sp.set_visible(False)
        
    # --- Aumenta la dimensione del font dei tick label e del label
    cbar.ax.tick_params(labelsize=14)                # tick numerici più grandi
    cbar.set_label(title, fontsize=16)               # etichetta a lato più grande

    # --- Aggiungi un bordo nero all'intero riquadro della colorbar
    # Assicurati che la cornice (frame) sia visibile
    cbar.ax.set_frame_on(True)
    # Colora di nero e rendi più spesso ciascuno dei quattro spines
    for spine in cbar.ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1.5)


    # 6) spegni solo i marginali veri
    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # 7) salva e mostra
    fig.savefig(f"{file_suffix}_umap_{gene_col}_bigcbar.png",
                dpi=300, bbox_inches='tight')
    fig.savefig(f"{file_suffix}_umap_{gene_col}_bigcbar.svg",
                dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)

from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import seaborn as sns
import pandas as pd

def plot_umap_single_gene_numeric_INSCAPE_cmaporizzontale(
    df, gene_col, title, file_suffix="output_umap",
    value_range=(0, 1), figsize=(6, 6), cmap_name="viridis"
):
    df = df.copy()
    df[gene_col] = pd.to_numeric(df[gene_col], errors="coerce")

    # 1) Layout 3×2
    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs = gridspec.GridSpec(
        3, 2,
        height_ratios=[0.3, 1, 4],    # riga 0 piccola per cbar, 1 per marginale X, 4 per main
        width_ratios =[4, 0.8],       # colonna 0 larga per UMAP, colonna 1 stretta per marg Y
        figure=fig
    )

    # 2) Axes
    ax_cbar   = fig.add_subplot(gs[0, 0:2])   # colorbar orizzontale sopra entrambe le colonne
    ax_marg_x = fig.add_subplot(gs[1, 0])     # marginale X (se vuoi ancora mostrarlo)
    ax_marg_y = fig.add_subplot(gs[2, 1])     # marginale Y
    ax_main   = fig.add_subplot(gs[2, 0])     # plot UMAP

    # 3) scatter sul main
    cmap = get_cmap(cmap_name)
    norm = Normalize(vmin=value_range[0], vmax=value_range[1])
    sc   = ax_main.scatter(
        df['umap1'], df['umap2'],
        c=df[gene_col], cmap=cmap, norm=norm,
        s=50, alpha=0.9, edgecolors='none'
    )

    # 4) marginali (opzionali)
    sns.kdeplot(x=df['umap1'], ax=ax_marg_x,
                color='black', linewidth=1.5, fill=False)
    sns.kdeplot(y=df['umap2'], ax=ax_marg_y,
                color='black', linewidth=1.5, fill=False)

    ax_marg_x.axis('off')
    ax_marg_y.axis('off')

    # 5) pulizia main
    ax_main.set_xticks([]); ax_main.set_yticks([])
    ax_main.set_xlabel("UMAP 1", fontsize=16)
    ax_main.set_ylabel("UMAP 2", fontsize=16)
    for spine in ax_main.spines.values():
        spine.set_linewidth(1.5)

    # 6) colorbar orizzontale
    cbar = fig.colorbar(
        sc,
        cax=ax_cbar,
        orientation='horizontal'
    )
    # posiziona ticks e label sopra
    cbar.ax.xaxis.set_ticks_position('top')
    cbar.ax.xaxis.set_label_position('top')
    cbar.ax.set_xlabel(title, fontsize=18, labelpad=10)
    cbar.ax.tick_params(labelsize=18)

    # bordo nero sulla cbar
    cbar.ax.set_frame_on(True)
    for spine in cbar.ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1.2)

    # 7) salva e mostra
    fig.savefig(f"{file_suffix}_umap_{gene_col}_cbarhoriz.png",
                dpi=300, bbox_inches='tight')
    fig.savefig(f"{file_suffix}_umap_{gene_col}_cbarhoriz.svg",
                dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)