## Python scripts to retrieve genomes from MGnify [1]  

### Directory content  

**mgnify-api.py** : retrieve MGnify genomes IDs for a user specified taxonomy + a customizable set of metadata in a tsv file.   
MGnify API documentation : https://www.ebi.ac.uk/metagenomics/api/docs/  
  
**download-data.py** : download MGnify using IDs retrieved by mgnify-api.py.  

### Usage  
1. Create a [Conda](https://docs.conda.io/en/latest/index.html) environment.  
```bash
conda create -n mgnify-api python=3.8
conda activate mgnify-api
pip install pandas numpy scipy plotnine jsonapi-client mg-toolkit requests
```
2. Run scripts 
```bash
# get genomes IDs + metadata
./mgnify-api.py
# download genomes
./download-data.py
```
 Eample of the API structure for the genomes database :  
 ```python
"data": [
    {
      "type": "genomes",
      "id": "MGYG000000001",
      "attributes": {
        "genome-id": 4888,
        "geographic-origin": "Europe",
        "geographic-range": [
          "North America",
          "Europe"
        ],
        "accession": "MGYG000000001",
        "ena-genome-accession": null,
        "ena-sample-accession": "ERS370061",
        "ena-study-accession": "ERP105624",
        "ncbi-genome-accession": null,
        "ncbi-sample-accession": null,
        "ncbi-study-accession": null,
        "img-genome-accession": null,
        "patric-genome-accession": null,
        "length": 3219617,
        "num-contigs": 137,
        "n-50": 47258,
        "gc-content": 28.26,
        "type": "Isolate",
        "completeness": 98.59,
        "contamination": 0.7,
        "rna-5s": 88.24,
        "rna-16s": 99.74,
        "rna-23s": 99.83,
        "trnas": 20,
        "nc-rnas": 63,
        "num-proteins": 3182,
        "eggnog-coverage": 93.78,
        "ipr-coverage": 86.42,
        "taxon-lineage": "d__Bacteria;p__Firmicutes_A;c__Clostridia;o__Peptostreptococcales;f__Peptostreptococcaceae;g__GCA-900066495;s__GCA-900066495 sp902362365",
        "num-genomes-total": 4,
        "pangenome-size": 3154,
        "pangenome-core-size": 1350,
        "pangenome-accessory-size": 1804,
        "last-update": "2021-12-07T18:06:34.765782",
        "first-created": "2021-12-07T18:06:34.762463"
      },  
```
### Contact
mathe.meije@gmail.com  

### Bibliography
[1] MGnify: the microbiome sequence data analysis resource in 2023 Nucleic Acids Research (2023) doi:10.1093/nar/gkac1080
Richardson LJ, Allen B, Baldi G, Beracochea M, Bileschi M, Burdett T, Burgin J, Caballero-Pérez J, Cochrane G, Colwell L, Curtis T, Escobar-Zepeda A, Gurbich T, Kale V, Korobeynikov A, Raj S, Rogers AB, Sakharova E, Sanchez S, Wilkinson D and Finn RD .
