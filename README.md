# H3BERTa: A CDR-H3 specific language model for antibody repertoire analysis
10.5281/zenodo.17505849

This repository contains the code, pretrained models, and datasets used in the study:

> **Chiara Rodella & Thomas Lemmin**  
> *H3BERTa: A CDR-H3 specific language model for antibody repertoire analysis*  
> Institute of Biochemistry and Molecular Medicine, University of Bern (Switzerland)

---

## Overview

**H3BERTa** is a transformer-based protein language model trained exclusively on the **CDR-H3 region** of antibody heavy chains.  
By focusing on this short but highly variable segment, the model captures **immunologically meaningful sequence features** like:
- B-cell maturation states  
- Comparison of healthy vs. HIV-1 antibody repertoires  
- Classification of **broadly neutralizing antibodies (bnAbs)** using minimal labeled data  

Despite being trained only on CDR-H3 loops, H3BERTa reproduces biologically coherent repertoire structures and supports functional predictions.

---
