# Custom Bioinformatics Scripts for De Novo RNA Sequencing and Analysis
* Align.py - Creates new fa files from excel data
* align_Single.sh - Aligns an fa file via Mafft and blastp search from makeblastdb (Works best with Trinotate.pep transcoder file)
* MafftShell.sh - runs and cross references align_Single on an entire folder of fa/fasta files
* terminal_PyBlast.py - creates bar plots and pie charts based on blast_out.txt files from blastx queries
* QCPyPipe.py - multiprocessing application for processing fastqc in parallel (designed for Unix systems)
* PyKoala.py - Creates Pie charts of split BlastKoala results by custom input of data
* QCStat.py - generates reports of essential data from fastqc (i.e GC Content etc)
### Poster.pptx ###
* A scientific poster made by myself for the 5 Previously Unknown Ochryphte Species my advisor and I discovered. It details the pipeline and methodology bhind our research 

**Results from terminal_PyBlast.py**

![Bailleu_blast_box](https://user-images.githubusercontent.com/60492061/183866552-f4cfa712-fefb-4819-9ea4-724f4a3d8b92.png)
![Bailleu_blast_pie](https://user-images.githubusercontent.com/60492061/183866708-525ae647-a47b-4b8c-9f25-6370d138f6cc.png)

**Results from PyKoala.py**
![pyKoala_Glossomastix-Chrysoplastos-Bailleu1](https://user-images.githubusercontent.com/60492061/183867287-ee26919f-f7db-4c16-bf3f-4245a2eca334.png)

