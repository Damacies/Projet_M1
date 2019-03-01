from .Uniprot import *
from .ensembl import *
from .PDB import *
from .NCBI import *
from .QuickGO import *
from .String import *
from .Kegg import *
from .prosite import *
from .pfam import *
from .afficher import *
#import os
#import sys
import re
import tkinter as Tk
from tkinter.filedialog import *
import webbrowser

def main(fichier_input,interface,var_label):
	fichier = open(fichier_input,"r")
	output_file=open("result_projet.html","w")
	template=open("programmes/template.html","r")
	liste=fichier.readlines()
	l2=[]
	symbol = []
	species=[]

	for line in liste:
		l2 = line.split("\t")
		l2[-1]=l2[-1].rstrip('\n')
		l2[-1]=l2[-1].rstrip(' ')
		l2[1] = re.sub('\s','_',l2[1])
		symbol.append(l2[0])
		species.append(l2[1])

	output_file.write(template.read())

	len_symbol = len(symbol)
	go_aspect=['biological_process','molecular_function','cellular_component']
	z=0
	print("\n")
	p = 0
	progression = "Progression en cours: "+str(p)+"/"+str(len_symbol)
	var_label.set(progression)
	interface.update()
	print("\n")
	while z < len_symbol:
		print("Species = ",species[z],"Gene = ",symbol[z],"\n")
		if z < len_symbol:
			output_file.write("<tr><td>"+symbol[z]+"</td>\n")
		if z == len_symbol:
			output_file.write("<tr><td>"+symbol[z]+"</td>\n</tr>")
		output_file.write("<td>"+species[z]+"</td>\n")
		Uni_id = Uniprot_id(symbol[z],species[z],output_file)
		Uniprot_name(symbol[z],species[z],output_file)
		url = database(symbol[z],species[z])
		ens_id = ensembl_id(symbol[z],species[z],output_file,url)
		"""
		ensembl_genome_browser(ens_id,symbol[z],species[z],output_file,url)
		ensembl_orthologue(ens_id,symbol[z],species[z],output_file,url)
		ensembl_transcripts(ens_id,symbol[z],species[z],output_file,url)
		ensembl_protein(ens_id,symbol[z],species[z],output_file,url)
		pdb_id(Uni_id,output_file)
		try:
			N_id = NCBI_id(symbol[z],species[z],output_file)
		except:
			output_file.write('<td>**Error**</td>')
		try:
			NCBI_name(N_id,symbol[z],species[z],output_file)
		except:
			output_file.write('<td>**Error**</td>')
		try:
			NCBI_transcripts(symbol[z],species[z],output_file)
		except:
			output_file.write('<td>**Error**</td>')
		try:
			NCBI_proteins(symbol[z],species[z],output_file)
		except:
			output_file.write('<td>**Error**</td>')
		quick_go(Uni_id,go_aspect[0],output_file)
		quick_go(Uni_id,go_aspect[1],output_file)
		quick_go(Uni_id,go_aspect[2],output_file)
		string(Uni_id,output_file)
		kegg_ID = kegg_id(N_id,output_file)
		kegg_paths(kegg_ID,output_file)
		prosite(Uni_id,output_file)
		pfam(Uni_id,output_file)
		"""
		##
		p = p + 1
		progression = "Progression en cours: "+str(p)+"/"+str(len_symbol)
		var_label.set(progression)
		interface.update()
		print("\n")
		##
		z = z + 1
	progression = "Terminé!!"
	var_label.set(progression)
	print("Terminé!!!")
	output_file.write("</tbody>\n")
	output_file.write("</table>\n")
	output_file.write("</body>\n")
	output_file.write("</html>\n")

