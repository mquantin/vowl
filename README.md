# vowl
Visualize ontology localy with WebVOWL.

This is just a simple script to manage localy 
1. converting OWL ontology files to VOWL
2. serving the webowl static folder through http



# how to

1. download and unzip this git repository
2. download and unzip [WebVOWL (version 1.1.7)](http://vowl.visualdataweb.org/downloads/webvowl_1.1.7.zip) in the previoulsy created repository folder
3. download and unzip [OWL2VOWL (beta 0.3.7)](http://vowl.visualdataweb.org/downloads/owl2vowl_0.3.7.zip) in the previoulsy created repository folder
5. run vowl.py 
  `python3 vowl.py`
7. feed it with an owl (file path or URI) as asked by the terminal
  
It should open a new tab in your browser and display the ontology.  
A copy of the displayed ontology is placed in the 'VOWLfiles' folder. So you can re-display all processed ontologies, loading it in the webvowl app.

