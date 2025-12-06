import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.decomposition import PCA
import umap.umap_ as umap
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from tqdm import tqdm
import os

def load_model_and_tokenizer(model_name):
    """Loads the specified model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to("cpu")
    model.resize_token_embeddings(len(tokenizer))
    return tokenizer, model


def get_embeddings(sequence, tokenizer, model):
    """Computes embeddings for a given sequence using the specified model."""
    inputs = tokenizer(sequence, return_tensors="pt", truncation=True, max_length=256, padding="max_length")
    inputs = {key: value.to('cpu') for key, value in inputs.items()}  # Sposta gli input su CUDA
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    
    return embeddings.cpu().numpy()  # Sposta su CPU prima di convertire in NumPy

def load_or_compute_embeddings(data, tokenizer, model, output_file):
    """Loads embeddings from a file or computes and saves them if not found."""
    try:
        with open(output_file, "rb") as f:
            data = pickle.load(f)
        print(f"Embeddings loaded from {output_file}")
    except FileNotFoundError:
        print("Computing embeddings...")
        tqdm.pandas()
        # Apply with progress bar
        print(data)
        data = data.dropna(subset=["sequence"])
        #print(data["sequence"])
        print('ANTIBERTA NEEDS SPACE BETWEEN AA:')
        data["sequence"] = data["sequence"].apply(lambda x: ' '.join(x))
        print(data["sequence"])
        data["embeddings"] = data["sequence"].progress_apply(lambda x: get_embeddings(x, tokenizer, model))
        #data["embeddings"] = data["seq"].apply(lambda x: get_embeddings(x, tokenizer, model))
        with open(output_file, "wb") as f:
            pickle.dump(data, f)
        print(f"Embeddings saved to {output_file}")
    return data


def PCA_reduce_and_visualize_embeddings(data, plot_title,hue_class, img_output_file=None, reduction_output_path=None ):
    """Reduces embeddings with PCA and visualizes the results."""
    embeddings = list(data["embeddings"])
    
    reduction_output_file =  reduction_output_path
    if reduction_output_file and os.path.exists(reduction_output_file):
        # Load UMAP coordinates from file
        print(f"Loading UMAP coordinates from {reduction_output_file}")
        pca_data = pd.read_csv(reduction_output_file, sep='\t')
        data["pca1"] = pca_data["pca1"]
        data["pca2"] = pca_data["pca2"]
    else:
        # Compute UMAP from embeddings
        print("Computing PCA coordinates...")
        pca = PCA(n_components=2,  svd_solver='randomized')
        reduced_embeddings = pca.fit_transform(embeddings)
        explained_variance = pca.explained_variance_ratio_ * 100
        data["pca1"] = reduced_embeddings[:, 0]
        data["pca2"] = reduced_embeddings[:, 1]

        # Save PCA coordinates 
        if reduction_output_file:
            data.to_csv(reduction_output_file, sep=',', index=False)
            print(f"PCA coordinates saved to {reduction_output_file}")
                

    # Visualization
    g = sns.jointplot(
        x="pca1",
        y="pca2",
        hue=hue_class,
        palette="Set2",
        data=data,
        s=10,
        marginal_kws={'common_norm': False, 'fill':False}
    )
    
    g.figure.suptitle(plot_title,fontsize=12)
    g.ax_joint.set_xlim(data['pca1'].min() - 6, data['pca1'].max() + 6)
    g.ax_joint.set_ylim(data['pca2'].min() - 6, data['pca2'].max() + 6)
    # Aggiungi nomi agli assi con la percentuale di varianza spiegata
    plt.xlabel(f'PC1 ({explained_variance[0]:.2f}% explained variance)',fontsize=12)
    plt.ylabel(f'PC2 ({explained_variance[1]:.2f}% explained variance)',fontsize=12)
    plt.xticks(fontsize=12)  # Font size for x-axis ticks
    plt.yticks(fontsize=12)
    plt.legend(title=None,loc='best', bbox_to_anchor=(0.5, -0.35), borderaxespad=0.)
    #plt.legend(title=None)
    plt.tight_layout()
    # Save
    #g.savefig(os.path.join(save_dir, f'{name}_PCA_with_marginals{label_identifier}.png'))
    #g.savefig(os.path.join(save_dir, f'{name}_PCA_with_marginals{label_identifier}.svg'),format='svg')
    plt.show()

    if img_output_file:
        g.savefig(img_output_file, format='png')
        print(f"IMG saved to {img_output_file}")
        

def UMAP_reduce_and_visualize_embeddings(data, plot_title, hue_class, img_output_file=None, reduction_output_path=None ):
    """Reduces embeddings with UMAP and visualizes the results."""
    # Extract embeddings from the dataset
    embeddings = list(data["embeddings"])
    reduction_output_file =  reduction_output_path
    if reduction_output_file and os.path.exists(reduction_output_file):
        # Load UMAP coordinates from file
        print(f"Loading UMAP coordinates from {reduction_output_file}")
        umap_data = pd.read_csv(reduction_output_file, sep='\t')
        data["umap1"] = umap_data["umap1"]
        data["umap2"] = umap_data["umap2"]
    else:
        # Compute UMAP from embeddings
        print("Computing UMAP coordinates...")
        embeddings = list(data["embeddings"])
        pca = PCA(n_components=100)
        reduced_embeddings = pca.fit_transform(embeddings)
        reducer = umap.UMAP(n_components=2, random_state=42)
        reduced_embeddings = reducer.fit_transform(reduced_embeddings)
        data["umap1"] = reduced_embeddings[:, 0]
        data["umap2"] = reduced_embeddings[:, 1]

        # Save UMAP coordinates if requested
        if reduction_output_file:
            data.to_csv(reduction_output_file, sep=',', index=False)
            print(f"UMAP coordinates saved to {reduction_output_file}")

    # Visualization using Seaborn's jointplot
    g = sns.jointplot(
        x="umap1",
        y="umap2",
        hue=hue_class,  # Color points by the "class" column
        palette="Set2",
        data=data,
        s=10,  # Point size
        marginal_kws={'common_norm': False, 'fill': False}  # Marginal settings
    )
    
    # Add title to the plot
    g.figure.suptitle(plot_title, fontsize=12)
    
    # Set axis limits
    g.ax_joint.set_xlim(data['umap1'].min() - 6, data['umap1'].max() + 6)
    g.ax_joint.set_ylim(data['umap2'].min() - 6, data['umap2'].max() + 6)
    
    # Add axis labels
    plt.xlabel('UMAP Dimension 1', fontsize=12)
    plt.ylabel('UMAP Dimension 2', fontsize=12)
    plt.xticks(fontsize=12)  # Font size for x-axis ticks
    plt.yticks(fontsize=12)  # Font size for y-axis ticks
    
    # Remove legend title for cleaner appearance
    plt.legend(title=None,loc='best', bbox_to_anchor=(0.5, -0.35), borderaxespad=0.)
    #plt.legend(title=None)
    plt.tight_layout()
    
    # Save the plot if an output file is provided
    if img_output_file:
        g.savefig(img_output_file, format='png')
        print(f"IMG saved to {img_output_file}")

    # Show the plot
    plt.show()



def main(model_name, model_path, csv_file, embedding_file, plot_title, hue_class, reduction_output_path, umap=False, pca=False):
    """Main function to manage the program flow."""
    import os
    # Nome della cartella da creare
    cartella = "img"
    # Creazione della cartella se non esiste
    if not os.path.exists(cartella):
        os.makedirs(cartella)
        print(f"Cartella '{cartella}' creata con successo!")
    else:
        print(f"La cartella '{cartella}' esiste già.")

    # Load the dataset
    data = pd.read_csv(csv_file, header=0)
    print(data)

    # Load the model and tokenizer
    tokenizer, model = load_model_and_tokenizer(model_path)
    
    # Compute or load embeddings
    data = load_or_compute_embeddings(data, tokenizer, model, embedding_file)
    if umap == True:
        # Reduce and visualize embeddings
        out = reduction_output_path + '/UMAP_'+plot_title+'.csv'
        UMAP_reduce_and_visualize_embeddings(data, plot_title + ' UMAP', hue_class, img_output_file='img/UMAP_'+plot_title+'.png', reduction_output_path = out )
    if pca == True:
        # Reduce and visualize embeddings
        out = reduction_output_path + '/PCA_'+plot_title+'.csv'
        PCA_reduce_and_visualize_embeddings(data, plot_title + ' PCA', hue_class, img_output_file='img/PCA_'+plot_title+'.png', reduction_output_path = out )


# Run the program specifying the desired model
if __name__ == "__main__":
    MODEL_NAME ='H3BERTA_DISEASED_TAILS'
    CSV_FILE = './tails_analysis/diseased_with_tail_labels.csv'
    EMBEDDING_FILE = f"./tails_analysis/{MODEL_NAME}_embeddings.pkl"
    PLOT_TITLE = MODEL_NAME+' PCA embeddings'
    HUE_CLASS = 'tail'
    REDUCTION_OUTPUT_PATH = './tails_analysis'
    main(MODEL_NAME, MODEL_PATH, CSV_FILE, EMBEDDING_FILE, PLOT_TITLE, HUE_CLASS, REDUCTION_OUTPUT_PATH, umap=True, pca=True)
