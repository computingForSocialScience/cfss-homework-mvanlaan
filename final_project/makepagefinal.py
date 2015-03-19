import sys
import requests
import pymysql
from flask import Flask, render_template, request, redirect, url_for
from acsdatafinal import *
import numpy as np
import pandas as pd

dbname="acsdata"
host="localhost"
user="root"
passwd="mvanlaan"
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

webpage = Flask(__name__)
@webpage.route('/')
def make_index_resp():
    """# this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    all_cols = []
    for i in IDs:
    	tableInfo, colIdOrder = getTableInfo(i)
    	all_cols.append(colIdOrder)
    	print all_cols
    print all_cols
    return render_template('index.html', all_cols = all_cols)
    """
    c = db.cursor()
    c.execute("SELECT colID, colName FROM columnInfoTable")
    tables = c.fetchall() 
    print tables
    return render_template('index.html', all_cols = tables)


#@webpage.route('/compare?state=[FIPSCode]&col1=[columnId1]&col2=[columnId2]')
@webpage.route('/compare/')
def basic_comparison():
	return str(request.args)
	FIPSCode = request.args['state']
	columnID1 = request.args['col1']
	secondgroupID = request.args['col2']
	c = db.cursor()
	#get tableID from selected columns
	table1 = "SELECT tableID FROM columnInfoTable WHERE colID = "+columnId1
	table2 = "SELECT tableID FROM columnInfoTable WHERE colID = "+columnId2
	c.execute(table1)
	table1 = str(c.fetchall())
	c.execute(table2)
	table2 = str(c.fetchall())

	db.commit()
	c.close()
	return render_template('compare.html', comparisons = comparisons)

if __name__ == "__main__":
	webpage.debug=True
	webpage.run(port=5005)