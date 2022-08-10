# Custom Bioinformatics Scripts for De Novo RNA Sequencing and Analysis
Align.py - Creates new fa files from excel data
align_Single.sh - Aligns an fa file via Mafft and blastp search from makeblastdb (Works best with Trinotate.pep transcoder file)
MafftShell.sh - runs and cross references align_Single on an entire folder of fa/fasta files
terminal_PyBlast.py - creates bar plots and pie charts based on blast_out.txt files from blastx queries
QCPyPipe.py - multiprocessing application for processing fastqc in parallel (designed for Unix systems)
PyKoala.py - Creates Pie charts of split BlastKoala results by custom input of data
QCStat.py - generates reports of essential data from fastqc (i.e GC Content etc)
