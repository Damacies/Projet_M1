import requests

def database(symbol,species):
	databases_list=["www","plants","fungi","Bacteria","Protists","Metazoa"]
	for database in databases_list:
		url = "https://{}.ensembl.org/{}/Gene/Summary?db=core;g={};".format(database,species,symbol)
		url_bis = "https://{}.ensembl.org/{}".format(database,species)
		r_test = requests.get(url, headers = {"Content-Type" : "application/json"})
		if r_test.ok: break
	return(url_bis)

def ensembl_id(symbol,species,output_file,url):
	print("Quering ensembl id...\n")
	server = "https://rest.ensembl.org"
	ext = "/xrefs/symbol/{}/{}?".format(species,symbol)
	result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
	decoded = result.json()
	i = 0
	ensembl_id_list=[]
	while i < len(decoded):
		j = 0
		if i == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
		if result.ok:
			ensembl_id_list.append(decoded[i]["id"])
			output_file.write("<a href="+'"'+url+"/Gene/Summary?db=core;g={}".format(decoded[i]["id"])+'"'+">"+decoded[i]["id"]+"</a>"+"<br>\n")
		if not result.ok:
			server = "https://rest.ensemblgenomes.org"
			ext = "/xrefs/symbol/{}/{}?".format(species,symbol)
			result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
			decoded = result.json()
			ensembl_id_list.append(decoded[i]["id"])
			output_file.write("<a href="+'"'+url+"/Gene/Summary?db=core;g={}".format(decoded[i]["id"])+'"'+">"+decoded[i]["id"]+"</a>"+"<br>\n")
		if i == len(decoded)-1:
			output_file.write("</div></td>\n")
		i = i + 1
	return(ensembl_id_list)


def ensembl_orthologue(ensembl_id,symbol,species,output_file,url):
	print("Quering ensembl Orthologues...\n")
	z = 0
	while z < len(ensembl_id):
		if z == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
		try:
			output_file.write('<a href="'+url+'/Gene/Compara_Ortholog?db=core;g={}'.format(ensembl_id[z])+'">Orthologues</a>\n')
		except:
			output_file.write("<a href="+'"'+url+'/Gene/Compara_Ortholog?db=core;g={}'.format(species,ensembl_id[z])+'">Orthologues</a>\n')
		if z == len(ensembl_id) - 1:
			output_file.write("</div></td>\n")
		z = z + 1
	return()

def ensembl_genome_browser(ensembl_id,symbol,species,output_file,url):
	#print("ensembl_id = ",ensembl_id)	
	print("Quering ensembl Genome Browser...\n")
	z = 0
	while z < len(ensembl_id):
		if z == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
		try:
			output_file.write('<a href="'+url+"/Location/View?db=core;g={}".format(ensembl_id[z])+'"'+'>Genome Browser</a><br>\n')
		except:
			server = "https://rest.ensemblgenomes.org"
			ext = "/xrefs/symbol/{}/{}?".format(species,symbol)
			result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
			decoded = result.json()
			results.append(decoded[z]["id"])
			output_file.write("<a href="+'"'+url+"/Location/View?db=core;g={}".format(decoded[z]["id"])+'"'+">Genome Browser</a><br>\n")
		if z == len(ensembl_id)-1:
			output_file.write("</div></td>\n")
		z = z + 1
	return()

def ensembl_transcripts(ensembl_id,symbol,species,output_file,url):
	print("Quering ensembl transcripts...\n")
	w = 0
	while w < len(ensembl_id):
		server = "https://rest.ensembl.org"
		ext = "/lookup/id/{}?expand=1".format(ensembl_id[w])
		result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
		decoded = result.json()
		j = 0
		if w == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
		while j < len(decoded):
		#print(decoded)
			try:
				if result.ok:
					output_file.write("<a href="+'"'+url+"/Transcript/Summary?db=core;t={}".format(decoded["Transcript"][j]["id"])+'"'+">"+decoded["Transcript"][j]["id"]+"</a><br>\n")
				if not result.ok:
					server = "https://rest.ensemblgenomes.org"
					ext = "/lookup/id/{}?expand=1".format(ensembl_id[w])
					result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
					decoded = result.json()
					output_file.write("<a href="+'"'+url+"/Transcript/Summary?db=core;t={}".format(decoded["Transcript"][j]["id"])+'"'+">"+decoded["Transcript"][j]["id"]+"</a><br>\n")
			except:
				if j == len(decoded)+9:
					output_file.write("</div></td>\n")
			j = j + 1
		if w == len(decoded)-1:
			output_file.write("</div></td>\n")
		w = w + 1
	return()

def ensembl_protein(ensembl_id,symbol,species,output_file,url):
	print("Quering ensembl proteins...\n")
	w = 0
	while w < len(ensembl_id):
		server = "https://rest.ensembl.org"
		ext = "/lookup/id/{}?expand=1".format(ensembl_id[w])
		result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
		decoded = result.json()
		j = 0
		if w == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
		#print(decoded)
		while j < len(decoded):
			try:
				if result.ok:
					output_file.write("<a href="+'"'+url.format(species)+"/Transcript/ProteinSummary?db=core;p={}".format(decoded["Transcript"][j]["Translation"]["id"])+'"'+">"+decoded["Transcript"][j]["Translation"]["id"]+"</a><br>\n")
				if not result.ok:
					server = "https://rest.ensemblgenomes.org"
					ext = "/lookup/id/{}?expand=1".format(ensembl_id[w])
					result = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
					decoded = result.json()
					output_file.write("<a href="+'"'+url+"/Transcript/ProteinSummary?db=core;p={}".format(decoded["Transcript"][j]["Translation"]["id"])+'"'+">"+decoded["Transcript"][j]["Translation"]["id"]+"</a><br>\n")
			except:
				if j == len(decoded)+9:
					output_file.write("</div></td>\n")
			j = j + 1
		if w == len(decoded)-1:
			output_file.write("</div></td>\n")
		w = w + 1
	return()

