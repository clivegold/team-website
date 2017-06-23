import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainmenu():

    ## I need to edit "main.html" so that there is link to my function "alberto"
    return render_template('main.html')

@app.route('/alberto')
def alberto():

    ## First thing in my function: read the text file "alberto.txt"
    ## then build my own page based on the contents of the file
    response = """<html><body>
    <h1>Alberto's page<br/><h3>Add your dynamic content here</html>"""
    
    return response

@app.route('/theo')
def theo():

    ## First thing in my function: read the text file "theo.txt"
    ## then build my own page based on the contents of the file

    file = open("theo.txt")
    filecontents = file.read()
    file.close()

    html_header = """<html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon.png">
    <title>Pied Piper - Homework 1</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    </head><body><div class="container center-block">"""

    html_body = """<div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title">Theo's Page</h3></div><div class="panel-body">"""
    filesplit = filecontents.split(':')
    html_body += """<table class="table table-bordered table-striped"><colgroup><col class="col-xs-1"><col class="col-xs-7"></colgroup>"""
    html_body += """<tr><th>Name:</th><td>{}</td></tr>""".format(filesplit[0])
    html_body += """<tr><th>Hobbies:</th><td>"""
    for item in filesplit[1].split(','):
        html_body += """<li>{}</li>""".format(item)
    html_body += """</td><tr>"""
    html_body += """<tr><th>Ideal Holiday:</th><td>{}</td></tr></table></div></div>""".format(filesplit[2])

    html_footer = """</div></body></html>"""

    response = html_header + html_body + html_footer
    
    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
