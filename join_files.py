from os import listdir
from os.path import isfile, join
import json

files_path = "fs tips"
json_files = [ f for f in listdir(files_path) if isfile(join(files_path,f)) ]

master_json = {}
for json_file_name in json_files:
	json_file = open(files_path + "/" + json_file_name)
	j = json.load(json_file)
	master_json.update(j)
	for vid, reviews in j.iteritems():
		for review in reviews:
			if review['sentiment'] not in ['P', 'N', 'U']:
				print review['sentiment'] + ' --> ' + json_file_name 
	json_file.close()
with open('master_json.txt', 'w') as outfile:
	json.dump(master_json, outfile)
