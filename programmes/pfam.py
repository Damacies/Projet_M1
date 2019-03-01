import requests
import re


def pfam(Uniprot_id,output_file):
	print("Quering pfam for id...\n")
	requestURL="https://pfam.xfam.org/protein/{}?output=xml".format(Uniprot_id[0])
	r = requests.get(requestURL)
	match_acc = re.findall('(PF\d\d\d\d\d)',r.text)
	iden = re.findall('(id="\D.*"\s)',r.text)
	output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">')
	output_file.write('<a href="https://pfam.xfam.org/protein/{}'.format(Uniprot_id[0])+'">Graphical view</a><br><br>\n')
	i = 0
	while i < len(match_acc):
		output_file.write('<a href="https://pfam.xfam.org/family/{}'.format(match_acc[i])+'">'+match_acc[i]+"</a><br>\n")
		output_file.write(iden[i]+"</a><br><br>\n")
		i = i + 1
	output_file.write("</div></td>")
	

	
	
	

