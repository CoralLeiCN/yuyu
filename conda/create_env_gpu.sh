conda create -y --name py311 -c conda-forge python=3.11
source activate base
conda activate py311
conda install -y cuda -c nvidia
pip install -r requirements311.txt