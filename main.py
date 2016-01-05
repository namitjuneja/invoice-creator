from flask import Flask, render_template, request, make_response, Response
from modify import *
from pdfs import create_pdf

app = Flask(__name__)

#basic testing route
@app.route('/try')
def try1():
    return render_template('new.html')

#root display route
@app.route('/')
def hello_world():
    return render_template('index.html')

#route when new is pressed -> renders create parchi form
@app.route('/new') 
def new():
    return render_template('input_form.html')

#creates the parchi by rendering the data from the previous route into an html template
@app.route('/createnew',  methods=['GET', 'POST']) 
def createnew():
    num = int(request.form["manas"])
    main_data = []
    total_amt = total_qty = 0
    for i in range(1, num+1):
    	main_data.append({"sno":request.form["sno" + str(i)], "qty":request.form["qty" + str(i)], "product":request.form["product" + str(i)], "at":request.form["at" + str(i)], "amt":request.form["amt" + str(i)]})
    	total_amt += int(request.form["amt" + str(i)])
    	total_qty += int(request.form["qty" + str(i)])
    data = {"company_name": str(request.form["company_name"]), "company_add": str(request.form["company_add"]), "person_name": str(request.form["person_name"]), "person_contact": str(request.form["person_contact"]), "date": str(request.form["date"]), "bill_data": main_data, "total_qty":total_qty, "total_amt":total_amt}
    return render_template("try1.html", data = data)

#modify button
@app.route('/modify') 
def modify():
    return render_template("modify.html")

#modify button -> modify action
@app.route('/modify_action', methods=['GET']) 
def modify_action():
    addelete = str(request.args["addelete"])
    database = str(request.args["database"])
    return modify_render(addelete, database)

#modify ->delete(datadisplay) -> deletion of data
@app.route('/delete_data', methods=['GET']) 
def delete_data():
    delete_list = request.args.getlist('data')
    database = str(request.args["database"])
    return delete_data_back(delete_list, database)

#modify -> add(input form) -> adds data to the json
@app.route('/add_data', methods=['GET', 'POST']) 
def add_data():
    new_data = request.args["data"]
    database = str(request.args["database"])
    return add_data_back(new_data, database)

if __name__ == '__main__':
    app.run(debug=True)