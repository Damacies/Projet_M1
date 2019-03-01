import requests, re

def pdb_id(Uniprot_id,output_file):
	print("Quering PDB...\n")
	results=[]
	url = 'http://www.rcsb.org/pdb/rest/search'
	if Uniprot_id != "No_data":
		Uniprot_liste_id = ",".join(Uniprot_id)
		queryText = """
<?xml version="1.0" encoding="UTF-8"?>

<orgPdbQuery>

<queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>

<accessionIdList>"""+Uniprot_liste_id+ """</accessionIdList>

</orgPdbQuery>

"""
		header={'Content-Type':'Application/x-www-form-urlencoded'}
		req = requests.post(url, data=queryText,headers=header)
		results_int = req.text.rstrip('\n')
		results_int = re.sub("(:\d)","",results_int)
		results = results_int.split('\n')
		i = 0
		while i < len(results):
			if i == 0:
				output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
			if results[i] != "null":
				output_file.write("<a href="+'"'+"http://www.rcsb.org/structure/{}".format(results[i])+'"'+">"+results[i]+"</a>"+"<br>\n")
			if results[i] == "null":
				output_file.write("No_data<br>\n")
			if i == len(results)-1:
				output_file.write("</div></td>\n")
			i = i + 1
		j = 0
		while j < len(results):
			url_desc = "http://www.rcsb.org/pdb/rest/customReport.xml?pdbids={}".format(results[j])+"&customReportColumns=structureId,structureTitle" 
			header = {'Content-Type':'Application/x-www-form-urlencoded'}
			results_desc = requests.get(url_desc,headers=header)
			if j == 0:
				output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">\n')
			if results[j] != "null":
				re_inter = results_desc.text.split('\n')
				struct_desc = re.sub("(<dimStructure.structureTitle>)|(</dimStructure.structureTitle>)","",re_inter[4])
				output_file.write(re_inter[4]+"<br>\n<br>\n")
			if results[j] == "null":
				output_file.write("No_data<br>\n")
			if j == len(results)-1:
				output_file.write("</div></td>\n")
			j = j + 1
	else:
		output_file.write("<td>Pas d'id Uniprot</td>\n")
	return()




#output_file.write("<td>"+"<a href="+'"'+"https://www.rcsb.org/structure/{}".format(PDB_id[i])+'"'+">"+"</a>"+PDB_id[i]+"</td>\n")

#resultat_filtre = re.sub("(:\d)","<br>",resultat)

#https://cdn.rcsb.org/images/rutgers/n0/1n0w/1n0w.pdb1-500.jpg

#http://www.rcsb.org/pdb/rest/customReport.xml?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,structureTitle,experimentalTechnique 
