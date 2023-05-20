#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import sys
from urllib.parse import urlencode

# conda environment : conda activate mgnify-api
from jsonapi_client import Filter, Session

# see MGnify API docuøentation to select an API base URL
API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"

# if you change the filters you may want to rename the output file
FILE_NAME = "MGnify-genomes_g_Clostridium_toNCBI.csv"

# list of lineages to extract from MGnify
LINEAGE_LIST = ["g__Clostridium"]

print("Starting...")

with open(FILE_NAME, "w") as csvfile:
    # CSV initialization
    fieldnames = [
        "accession",
        "biome",
        "taxon-lineage",
        "geographic-origin",
        "download-link",
        "ncbi-genome-accession",
        "ncbi-sample-accession"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # API call
    with Session(API_BASE) as session:
        # configure filters
        params = {
            # completeness, contamination, coverage ...          
        }
        # configure the request URL with filters
        api_filter = Filter(urlencode(params))
        total = 0
        # sessions.iterate : fill the csv file
        for genome in session.iterate(
            "genomes", api_filter
        ):
            # add row to csv if the genome is from a lineage of interest
            if any(map(genome.taxon_lineage.__contains__,LINEAGE_LIST)) :
                total += 1
                row = {
                    "accession": genome.id,
                    "biome": genome.biome.id,
                    "taxon-lineage": genome.taxon_lineage,
                    "geographic-origin":genome.geographic_origin,
                    "download-link": "https://www.ebi.ac.uk/metagenomics/api/v1/genomes/" + genome.id + "/downloads/" + genome.id + ".fna",
                    "ncbi-genome-accession" : genome.ncbi_genome_accession,
                    "ncbi-sample-accession" : genome.ncbi_sample_accession
                }
                writer.writerow(row)
        print("Data retrieved from the API")