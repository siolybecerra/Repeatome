#!/usr/bin/env python3

# Sioly Becerra sioly@usal.es

# USAGE:
# create a folder with all assemblies with files format fasta 
# Run from Server
# python3 repeatome_code_LTR.py /path_folder/

# loading libraries
import os
import sys
import shutil
import pdb
import subprocess

path=sys.argv[1]

lista_files=os.listdir(path)

for file in lista_files:
    
    namedir=file[:-6]
    os.makedirs(path + namedir)
    shutil.move(path + file, path + namedir) 
    os.chdir(path + namedir)
    
    ## Create a Database for RepeatModeler
    args=[namedir, file]
    subprocess.run(["/PATH/RepeatModeler-2.0.3/BuildDatabase", "-name", args[0], args[1]]) # version with LTR pipeline
    
    ## Run RepeatModeler
    args=[namedir, "10"]
    subprocess.run(["/PATH/RepeatModeler-2.0.3/RepeatModeler", "-database", args[0], "-pa", args[1], "-LTRStruct"])
    
    # Interpret the results   
    ## Running Repeat Masker
    args=["10", "ncbi", namedir + "-families.fa", file]
    subprocess.run(["/PATH/RepeatMasker/RepeatMasker", "-pa", args[0], "-e", args[1], "-lib", args[2], "-gff", args[3], "-norna", "-no_is"])