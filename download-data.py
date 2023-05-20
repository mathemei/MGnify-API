#!/usr/bin/env python
# -*- coding: utf-8 -*

import requests, os, sys
from pandas import *

#================================================
# INPUT : file resulting from mgnify-api.py
# download all genome using MGnify IDs
#================================================
def main(file):
    # test if input file exists 
    FILE_NAME = file
    if not os.path.isfile(FILE_NAME):
        print(FILE_NAME + "does not exists.")
        exit()
    # read csv file in pandas dataframe
    genomes = read_csv(FILE_NAME)
    # get list of IDs and download links
    accessions = genomes['accession'].tolist()
    download_links = genomes['download-link'].tolist()
    N_download = len(download_links)
    # create download diretory
    PATH_OUT = "./genomes"
    if not os.path.exists(PATH_OUT):
        print("Creating output directory : " + PATH_OUT)
        os.makedirs(PATH_OUT)
    # download genomes with requests
    print("Downloading...")
    d = 0
    for link in download_links :
        url = "https://www.ebi.ac.uk/metagenomics/api/v1/genomes/" + accessions[d] + "/downloads/" + accessions[d] + ".fna"
        r = requests.get(url, allow_redirects=True)
        GENOME_FILE = "./genomes/" + accessions[d] + ".fna"
        open(GENOME_FILE, 'wb').write(r.content)
        d = d+1
        print("Genome {} / ".format(d) + str(N_download) + " downloaded.")

if __name__ == "__main__":
    main(sys.argv[1])