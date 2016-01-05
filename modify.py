import json
from flask import render_template


def modify_render(addelete, database):
	with open('static/data/' + database + '.json') as data_file:
		data = json.load(data_file)
	if addelete == "delete":
		data = {"database" : database, "list" : data}
		return render_template("delete.html", data = data)
	elif addelete == "add":
		return render_template("add.html", data = {"database" : database})

def delete_data_back(delete_list, database):
	with open('static/data/' + database + '.json') as data_file:
		data = json.load(data_file)
	for name in delete_list:
		data.remove(name)
	with open('static/data/' + database + '.json', 'w') as outfile:
 		json.dump(data, outfile)
	return "Delete Successful"

def add_data_back(new_data, database):
	with open('static/data/' + database + '.json') as data_file:
		data = json.load(data_file)
	data.append(new_data)
	with open('static/data/' + database + '.json', 'w') as outfile:
 		json.dump(data, outfile)
 	return "Add Successful"

