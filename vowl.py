#!/usr/bin/python3
import subprocess
from shutil import copyfile
from rdflib import Graph
from rdflib.namespace import RDF, OWL , VANN
import http.server
import socketserver
import webbrowser
import os


outputFolderPath = './VOWLfiles/'
webvowlDataFilePath = './webvowl_1.1.7/data/default.json'

# WEB app serve data
PORT = 8000
DIRECTORY = './webvowl_1.1.7'
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


c = None

while not c:
    print('Choose: visualize ontology by file path (1) or by IRI (2)')
    choice = input()
    if choice == '1':
        c = 'file path'
        option = '-file'
    if choice == '2':
        c = 'IRI'
        option = '-iri'

print(f'Enter the {c} :')
ontoRDFdata = input().strip()

#name of the ontology
ontologyShortName = os.path.basename(ontoRDFdata)
#retrieve the namespace of the ontology
g=Graph()
try:
    g.parse(ontoRDFdata)
    for ontology in g.subjects(RDF.type, OWL.Ontology):
        for prefix in g.objects(ontology, VANN.preferredNamespacePrefix):
            print(f'loading data from {prefix} ontology')
            ontologyShortName = prefix
            break
except Exception as err:
    print('cannot parse rdf file')
    print(err)

outputFilePath = outputFolderPath+ontologyShortName+'.json'

subprocess.call(['java', '-jar', './owl2vowl_0.3.7/owl2vowl.jar', option, ontoRDFdata, '-output', outputFilePath])
#this creates a copy of the output vowl file in the webvowl data,
#file is renamed "default.json" so it loads on next webvowl start
copyfile(outputFilePath, webvowlDataFilePath)

webbrowser.open("http://localhost:"+str(PORT))

#this closes automatically on KeyboardInterrupt
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
