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

@app.route('/michael')
def michael():

    ## First thing in my function: read the text file "michael.txt"
    ## then build my own page based on the contents of the file

    with open("michael.txt") as f:
        mylist = f.read().split(':')
    f.close()


    hobbies ="<ul>"
    
    for h in mylist[1].split(','):
        hobbies += "<li>" + h + "</li>"
    hobbies += "</ul>"
            
    dynamic = """<table style="width:50%"><tr><th>Name</th>"""
    dynamic += "<th>" + mylist[0] + "</th></tr>"
    dynamic += "<tr><td>Hobbies" + "</td><td>" + hobbies + "</td></tr>"
    dynamic += "<tr><td>Ideal Holiday" + "</td><td>" + mylist[2] + "</td></tr>"
    
    response = """<html><body>
                <style>
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    th {
                        text-align: left;
                    }
                </style>
    <h1>Michael's page<br/>""" + dynamic + """</html>"""
    
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

@app.route('/daniel')
def daniel():

    ## THe nature of the web... I built on Theo's code. I have no problem with royalties... ;)
    ## Note that it doesn't wrap well for mobile phone size screens ("yet")

    file = open("daniel.txt")
    filecontents = file.read()
    file.close()

    html_header = """<html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>img { margin: 15px 15px; } </style>
    <link rel="apple-touch-icon" href="/static/apple-touch-icon.png">
    <title>Pied Piper - Homework 1</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    </head><body><div class="container center-block">"""

    html_body = """<br><div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title">Daniel's Page</h3></div><div class="panel-body">"""
    filesplit = filecontents.split('#')
    html_body += """<table class="table table-bordered table-striped"><colgroup><col class="col-xs-2"><col class="col-xs-7"></colgroup>"""
    html_body += """<tr><th>Name:</th><td>{}</td></tr>""".format(filesplit[0])
    html_body += """<tr><th>Hobbies:</th><td>"""
    for item in filesplit[1].split(','):
        html_body += """<li>{}</li>""".format(item)
    html_body += """</td><tr>"""
    html_body += """<tr><th>Ideal Holiday:</th><td>{}</td>""".format(filesplit[2])
    html_body += """<tr><td></td><td><img src="{}" width="300">""".format(filesplit[3])
    html_body += """<img src="{}" width="305"></td></tr></table></div></div>""".format(filesplit[4])

    html_footer = """</div></body></html>"""

    response = html_header + html_body + html_footer
    
    return response

@app.route('/elliot')
def elliot():

    f = open('Elliot.txt')
    about_me = f.readlines()
    f.close()
    
    me_info = []
    for sections in about_me:
        me_info = sections.split(':')

    ## First thing in my function: read the text file "alberto.txt"
    ## then build my own page based on the contents of the file
    response = """<html><body>
    <h1>Elliot's page</h1></br>
    <h3>Name: {}</br>
    Hobbies: {}</br>
    Ideal Holiday: {}</html>""".format(me_info[0], me_info[1], me_info[2])
    
    return response


@app.route('/Warren')
def wpj():

    start_page = """<HTML><HEAD></HEAD><BODY><body bgcolor="#777799"><center><h1><font color="white"><p><a href=/>Back to Member List</a></p></center>"""
    end_page = "</body>"
    mid_page = """<font color="white">
    <style>
    table, th, td {
       border: 1px solid white;
       color: white;
    }
    </style>"""
    strings = []
    hobbylist = ""

    filename = 'warren.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            strings.append(line)
        file_object.close()
 
        for string in strings:
            person = string.split(":")
            hobbies = person[1].split(",")
            for hobby in hobbies:
                hobbylist = hobbylist + "<li>{}</li>".format(hobby)

            mid_page = mid_page + """
                <table>
                    <tr>
                        <td>Name</td>
                        <td>{}</td>
                    </tr>
                    <tr>
                        <td>Hobbies</td>
                        <td><ul>
                            {}
                            </ul></td>
                    </tr>
                    <tr>
                        <td>Ideal Holiday</td>
                        <td>{}</td>
                    </tr>
                </table>

            """.format(person[0],hobbylist,person[2])
    
    full_page = start_page + mid_page + end_page
    return full_page
    
@app.route('/clive')
def clive():

    f = open('Clive.txt')
    about_me = f.readlines()
    f.close()
    
    me_info = []
    for sections in about_me:
        me_info = sections.split(':')

    ## First thing in my function: read the text file "alberto.txt"
    ## then build my own page based on the contents of the file
    response = """<html><body>
    <h1>Clive's page</h1></br>
    <h3>Name: {}</br>
    Hobbies: {}</br>
    Ideal Holiday: {}</html>""".format(me_info[0], me_info[1], me_info[2])
    
    return response
	
if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
