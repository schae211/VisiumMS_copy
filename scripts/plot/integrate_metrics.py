<<<<<<< HEAD

# python scripts/plot/integrate_metrics.py --output cellbender
# python scripts/plot/integrate_metrics.py --output cellranger

=======
>>>>>>> 4059a4c8e2af9c39af787ebee1439fc854d311d6
import scanpy as sc
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import argparse
<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> 4059a4c8e2af9c39af787ebee1439fc854d311d6
import os

"""
Script to plot different metrics after integration.
"""

<<<<<<< HEAD
# add command line flag arguments to specify either "cellbender" or "cellranger" output
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=str, required=True)
args = parser.parse_args()

# set up relative paths within the project
current_folder = Path(__file__).parent
output_dir = current_folder / ".." / ".." / "data" / "prc" / "sc"
if args.output == "cellbender":
    input_path = current_folder / ".." / ".." / "data" / "prc" / "sc" / "cellbender_integrated.h5ad"
    output_dir = current_folder / ".." / ".." / "out" / "cellbender_integrated"
elif args.output == "cellranger":
    input_path = current_folder / ".." / ".." / "data" / "prc" / "sc" / "cellranger_integrated.h5ad"
    output_dir = current_folder / ".." / ".." / "out" / "cellranger_integrated"
else:
    raise ValueError("output must be either 'cellbender' or 'cellranger'")
output_dir.mkdir(parents=True, exist_ok=True)

# verbose
print("input_path: ", input_path)
print("output_dir: ", output_dir)

version = "0"

=======
# Read command line and set args
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', help='Input path to object', required=True)
parser.add_argument('-v', '--version', help='Version of the merging', required=False)
parser.add_argument('-o', '--output_dir', help='Output directory', required=True)
args = vars(parser.parse_args())

input_path = args['input_path']
version = args['version']
output_path = args['output_dir']
>>>>>>> 4059a4c8e2af9c39af787ebee1439fc854d311d6
###############################

# Read merged object
adata = sc.read_h5ad(input_path)

# Plot HVG filtering QC plots
fig = plt.figure(figsize=(12,6), dpi=150, tight_layout=True, facecolor='white')
fig.suptitle('HVG filtering QC plots', fontsize=11)
gs = fig.add_gridspec(2, 3)

ax = fig.add_subplot(gs[0,0])
sc.pl.umap(adata, color='sample_id', ax=ax, frameon=False, return_fig=False, show=False)

ax = fig.add_subplot(gs[0,1])
sc.pl.umap(adata, color='lesion_type', ax=ax, frameon=False, return_fig=False, show=False)

ax = fig.add_subplot(gs[0,2])
sc.pl.umap(adata, color='doublet_score', ax=ax, frameon=False, return_fig=False, show=False)

ax = fig.add_subplot(gs[1,0])
sc.pl.umap(adata, color='diss_score', ax=ax, frameon=False, return_fig=False, show=False)

ax = fig.add_subplot(gs[1,1])
sc.pl.umap(adata, color='n_genes_by_counts', ax=ax, frameon=False, return_fig=False, show=False)

ax = fig.add_subplot(gs[1,2])
sc.pl.umap(adata, color='pct_counts_mt', ax=ax, frameon=False, return_fig=False, show=False)

# Save
if version is not None:
    fname = 'integrated_summary_{0}.png'.format(version)
else:
    fname = 'integrated_summary.png'
<<<<<<< HEAD
fig.savefig(os.path.join(output_dir, fname))
=======
fig.savefig(os.path.join(output_path, fname))
>>>>>>> 4059a4c8e2af9c39af787ebee1439fc854d311d6
