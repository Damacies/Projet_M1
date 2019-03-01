import requests

"""
But : Récupérer les id Uniprot
Méthode : requests.get
Inscrit les résultats dans le result.html
Retourne : La liste des id Uniprot
"""
def Uniprot_id(symbol,species,output_file):
	print("Quering Uniprot for id...\n")
	url = 'http://www.uniprot.org/uniprot/'
	payload = {'query':'gene_exact:{} AND taxonomy:"{}" AND fragment:no'.format(symbol,species),'format':'list'} #On ne prend pas les fragments
	try:
		result = requests.get(url, params=payload)
	except:
		output_file.write('<td>Error</td>')
	results = result.text.split('\n')
	if results[0]!="":
		del results[-1]
		output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">')
		for id_data in results:
			output_file.write("<a href=\"https://www.uniprot.org/uniprot/{}".format(id_data)+'"'+">"+id_data+"</a><br>\n")
		output_file.write("</div></td>\n")
	if results[0]=="":
		results[0]="No_data"
		output_file.write("<td>"+results[0]+"<br>\n")
	return(results)

"""
But : Récupérer les nom des protéines sur Uniprot
Méthode : requests.get
Inscrit les résultats dans le result.html
Retourne : //
"""
def Uniprot_name(symbol,species,output_file):
	print("Quering Uniprot for name...\n")
	url = 'http://www.uniprot.org/uniprot/'
	resultat_names=[]
	payload = {'query':'gene_exact:{} AND taxonomy:"{}" AND reviewed:yes'.format(symbol,species),'format':'tab','columns':'protein_names'}
	r_names = requests.get(url, params=payload)
	if r_names.ok:
		result = r_names.text.split("\n")
		if result[0] != '':
			result = result[1]
			resultat_names.append(result)
			resultat_names[-1]=resultat_names[-1].rstrip('\n')
			if resultat_names[-1]!="":
				output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">'+resultat_names[-1]+"<br></div></td>\n")
		elif result[0] == "":
			output_file.write("<td>No_data<br>\n")
	else: 
		print("Pas OK")
	return()

