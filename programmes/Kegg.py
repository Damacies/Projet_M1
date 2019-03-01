import requests

def kegg_id(N_id,output_file):
	print("Quering Kegg for id...\n")
	Liste_id=[]
	requestURL="http://rest.kegg.jp/conv/genes/ncbi-geneid:{}".format(N_id[0])
	r = requests.get(requestURL)
	l = r.text.rstrip("\n").split('\t')
	output_file.write('<td><div style="max-height:300px;width:120%;overflow-x:auto"><a href="https://www.kegg.jp/dbget-bin/www_bget?{}'.format(l[1])+'">'+l[1]+'</a></div></td>\n')
	return(l[1])

def kegg_paths(kegg_id,output_file):
	print("Quering Kegg for pathways...\n")
	gene_paths = requests.get('http://rest.kegg.jp/link/pathway/{}'.format(kegg_id))
	lines = gene_paths.text.splitlines()
	paths_id = []
	for l in lines:
		if l not in paths_id:
			inter = l.split('\t')[1]
			paths_id.append(inter.split(':')[1])	
	j = 0
	while j < len(paths_id):
		if j == 0:
			output_file.write('<td><div style="max-height:300px;width:auto;overflow-x:auto">')
		if j >= 0:
			gene_paths_name = requests.get('http://rest.kegg.jp/get/{}'.format(paths_id[j]))
			d1 = []
			d1.append(gene_paths_name.text)
			d2 = gene_paths_name.text.split('\n')
			d3 = d2[1]
			d4 = d3.split(" ")
			del d4[0:8]
			del d4[-4:]
			i = 0
			d5 = " ".join(d4)
			output_file.write('<a href="https://www.kegg.jp/kegg-bin/show_pathway?{}'.format(paths_id[j])+'">'+paths_id[j]+'</a>'+" "+d5+"</a><br>\n")
		if j == len(paths_id):
			output_file.write("</div></td>")
		j = j + 1





"""
gene_paths = requests.get('http://rest.kegg.jp/link/pathway/hsa:675')
print(gene_paths.text)
lines = gene_paths.text.splitlines()
paths_id = []
for l in lines:
    # récupérer chaque réseau une seule et unique fois
    if l not in paths_id:
        paths_id.append(l.split('\t')[1])
print(paths_id)



url = "http://rest.kegg.jp/get/hsa:675"
r = requests.get(URL, headers={ "Accept" : "application/json"})
"""


"""
#sauvegarder les images
import shutil
for p in paths_id:
    # récupérer un flux d'entrée
    path_img = requests.get('http://rest.kegg.jp/get/' + p + '/image', stream = True)
    # remplacer le caractère : par un _ dans le nom de l'image enregistrée
    path_name = p.replace(':', '_')
    print(path_name)
    with open(path_name + '.png', 'wb') as f:
        shutil.copyfileobj(path_img.raw, f)
"""
