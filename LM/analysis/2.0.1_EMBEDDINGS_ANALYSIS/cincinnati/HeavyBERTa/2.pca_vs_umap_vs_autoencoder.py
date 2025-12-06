"""
This script compares dimensionality reduction techniques (PCA, UMAP, Autoencoder) on high-dimensional embedding data.

Steps:
1. Load embedding data from a pickle file as label data from a CSV file and extract a column to use for coloring the plots.
3. Normalize the embeddings.
4. Apply:
   - PCA for linear dimensionality reduction.
   - UMAP for non-linear manifold-preserving projection.
   - An autoencoder (deep learning-based) for non-linear compression and reconstruction.
5. Generate 2D scatter plots for each method, colored by the provided label class.
6. Calculate and compare:
   - Reconstruction error (only for PCA and autoencoder).
   - Distance correlation between original and reduced space (for all three).
7. Save numerical results to a CSV file.

Reconstruction error: misura quanto bene un metodo può ricostruire l’embedding originale (più basso = meglio).
Distance correlation: quanto bene la struttura delle distanze tra punti è preservata nello spazio ridotto (più alto = meglio).


Run via command line:
python 2.pca_vs_umap_vs_autoencoder.py --embedding_file EMBEDDING_FILE  --hue_class v_gene --output_appendix MODEL_NAME
python 2.pca_vs_umap_vs_autoencoder.py --embedding_file ../tails_analysis/H3BERTA_DISEASED_TAILS_embeddings.pkl --hue_class tail --output_appendix diseased"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import pairwise_distances
from scipy.stats import spearmanr
from cuml.manifold import UMAP as cuUMAP
from cuml.decomposition import PCA as cuPCA
#import umap
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import pickle
import argparse
import os
import seaborn as sns
import matplotlib.gridspec as gridspec


# ---------- Config ----------
SEED = 42
BATCH_SIZE = 512
EPOCHS = 30
LATENT_DIM = 2

np.random.seed(SEED)
torch.manual_seed(SEED)

import matplotlib.gridspec as gridspec

def plot_2d_with_marginals(X_2d, title, filename, labels=None, explained_variance=None):
    df = pd.DataFrame({"x": X_2d[:, 0], "y": X_2d[:, 1], "Tail": labels})
    # Palette fissa: puoi modificarla a tuo gusto
    palette = {
        "upper": "#E74C3C",   # rosso
        "lower": "#3498DB",   # blu
        "middle": "#7F8C8D",  # grigio
    }

    g = sns.JointGrid(data=df, x="x", y="y", hue="Tail", height=8, palette=palette)
    g.plot_joint(sns.scatterplot, s=10, alpha=0.3)
    g.plot_marginals(sns.kdeplot, fill=False, common_norm=False, alpha=0.5)

    if explained_variance is not None:
        title += f"\nExplained variance: {explained_variance[0]*100:.2f}%, {explained_variance[1]*100:.2f}%"

    plt.suptitle(title, y=1.02)
    g.figure.tight_layout()
    g.figure.savefig(filename)
    plt.close()
    
# ---------- Autoencoder Model ----------
class AE(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, LATENT_DIM)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(LATENT_DIM, 64), nn.ReLU(),
            nn.Linear(64, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, input_dim)
        )

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon, z

# ---------- Distance Preservation ----------

def distance_preservation(X_full, X_proj):
    idx = np.random.choice(X_full.shape[0], size=min(5000, X_full.shape[0]), replace=False)
    dist_orig = pairwise_distances(X_full[idx])
    dist_proj = pairwise_distances(X_proj[idx])
    return spearmanr(dist_orig.ravel(), dist_proj.ravel()).correlation

def maybe_load_pickle(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    return None


# ---------- Main ----------
def main(embedding_file, hue_class, output_appendix):
    suffix = f"{output_appendix}_" if output_appendix else ""

    # Load embedding data
    with open(embedding_file, "rb") as f:
        print(f'Loading embeddings and metadata from {embedding_file}')
        df = pickle.load(f)
        print(df.columns)
        X = df['embeddings']
        labels = df[hue_class]
        if isinstance(X, pd.Series):
            X = np.stack(X.values)

    X = StandardScaler().fit_transform(X)

    results = []

    # ----- PCA -----
    pca_file = f"{suffix}pca_2d_projection.pkl"
    print('Processing PCA...')
    pca = cuPCA(n_components=LATENT_DIM, random_state=SEED)

    if not os.path.exists(pca_file):
        X_pca = pca.fit_transform(X)
        X_pca_recon = pca.inverse_transform(X_pca)
        with open(pca_file, 'wb') as f:
            pickle.dump(X_pca, f)
    else:
        print(f'Loading from file {pca_file}')
        X_pca = maybe_load_pickle(pca_file)
        pca.fit(X)
        X_pca_recon = pca.inverse_transform(X_pca)

    explained_var = pca.explained_variance_ratio_
    recon_error_pca = mean_squared_error(X, X_pca_recon)
    dist_corr_pca = distance_preservation(X, X_pca)
    #print('Creating plot...')
    #plot_2d_with_marginals(X_pca, "PCA Visualization", f"{suffix}pca_plot.png", labels, explained_variance=explained_var)
    results.append(("PCA", recon_error_pca, dist_corr_pca))

    # ----- UMAP -----
    umap_file = f"{suffix}umap_2d_projection.pkl"

    if not os.path.exists(umap_file):
        print('Running UMAP...')
        umap_model = cuUMAP(n_components=LATENT_DIM, random_state=SEED, init="random")
        X_umap = umap_model.fit_transform(X)
        with open(umap_file, 'wb') as f:
            pickle.dump(X_umap, f)
    else:
        print(f'Loading from file {umap_file}')
        X_umap = maybe_load_pickle(umap_file)

    dist_corr_umap = distance_preservation(X, X_umap)
    #print('Creating plot...')
    #plot_2d_with_marginals(X_umap, "UMAP Visualization", f"{suffix}umap_plot.png", labels)
    results.append(("UMAP", np.nan, dist_corr_umap))
    
    # ----- Autoencoder -----
    # ae_file = f"{suffix}autoencoder_2d_projection.pkl"
    # if not os.path.exists(ae_file):
    #     print('Training autoencoder...')
    #     X_tensor = torch.tensor(X, dtype=torch.float32)
    #     dataset = TensorDataset(X_tensor)
    #     dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    #     ae = AE(input_dim=X.shape[1])
    #     optimizer = optim.Adam(ae.parameters(), lr=1e-3)
    #     criterion = nn.MSELoss()

    #     for epoch in range(EPOCHS):
    #         ae.train()
    #         total_loss = 0
    #         for batch in dataloader:
    #             x_batch = batch[0]
    #             recon, _ = ae(x_batch)
    #             loss = criterion(recon, x_batch)
    #             optimizer.zero_grad()
    #             loss.backward()
    #             optimizer.step()
    #             total_loss += loss.item()
    #         print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {total_loss / len(dataloader):.4f}")

    #     ae.eval()
    #     with torch.no_grad():
    #         X_ae_recon, X_ae_latent = ae(X_tensor)
    #         X_ae_latent = X_ae_latent.numpy()
    #         X_ae_recon = X_ae_recon.numpy()
    #     with open(ae_file, 'wb') as f:
    #         pickle.dump((X_ae_latent, X_ae_recon), f)
    # else:
    #     print(f'Loading from file {ae_file}')
    #     X_ae_latent, X_ae_recon = maybe_load_pickle(ae_file)

    # recon_error_ae = mean_squared_error(X, X_ae_recon)
    # dist_corr_ae = distance_preservation(X, X_ae_latent)
    # print('Creating plot...')
    # plot_2d_with_marginals(X_ae_latent, "Autoencoder Visualization", f"{suffix}ae_plot.png", labels)
    # results.append(("Autoencoder", recon_error_ae, dist_corr_ae))
    
    # Save results
    results_df = pd.DataFrame(results, columns=["Method", "Reconstruction_Error", "Distance_Correlation"])
    results_df.to_csv(f"{suffix}dimensionality_reduction_results.tsv", sep="\t", index=False)
    
        # Aggiungi le proiezioni 2D al DataFrame originale
    df[f'{suffix}PCA_1'] = X_pca[:, 0]
    df[f'{suffix}PCA_2'] = X_pca[:, 1]
    df[f'{suffix}UMAP_1'] = X_umap[:, 0]
    df[f'{suffix}UMAP_2'] = X_umap[:, 1]
    #df[f'{suffix}AE_1'] = X_ae_latent[:, 0]
    #df[f'{suffix}AE_2'] = X_ae_latent[:, 1]

    # Salva il DataFrame aggiornato
    with open(f"{suffix}embedding_with_projections.pkl", "wb") as f:
        pickle.dump(df, f)
    
    print(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--embedding_file", type=str, required=True)
    parser.add_argument("--hue_class", type=str, required=True)
    parser.add_argument("--output_appendix", type=str, default="")
    args = parser.parse_args()

    main(args.embedding_file, args.hue_class, args.output_appendix)