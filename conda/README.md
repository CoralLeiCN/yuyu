# Installing Miniconda

[Official Miniconda installation guide](https://docs.anaconda.com/miniconda/install/)

1. Download miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
2. Verify installer's integrity
> sha256sum <FILE_NAME>

3. Install 
```bash
bash ~/Miniconda3-latest-Linux-x86_64.sh
```

4. (optional) conda's base environment not be activated on startup
```bash
conda config --set auto_activate_base false
```
