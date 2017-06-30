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

@app.route('/PhilD')
def PhilD():

    BLUE = "#33ccff"
    COLOR = BLUE
    
    ## First thing in my function: read the text file "PhilD.txt"
    ## then build my own page based on the contents of the file
    
    response = ""

    with open("PhilD.txt") as f:
        mylist = f.read().split(':')
    f.close()

    Page_Header      = "<HTML><HEAD></HEAD><BODY bgcolor={}><CENTER><HR><H1>Who Am I</H1><HR>\n<br><br>".format(COLOR)
    Page_Footer      = "</BODY></HTML>\n"

    Page_Mid         = "<TABLE border = 1>\n"
    Page_Mid        += "<TR><TH colspan=2>Who Am I</TH></TR>\n"
    Page_Mid        += "<TR><TD><STRONG>Name</STRONG></TD><TD>" + mylist[0] + "</TD>"
    Page_Mid        += "<TR><TD><STRONG>Hobbies</STRONG></TD><TD>"    
        
    for item in mylist[1].split(','):
        Page_Mid += item + "<br>"

    Page_Mid        += "</TD></TR>"
    Page_Mid        += "<TR><TD><STRONG>Ideal Holiday</STRONG></TD>"
    Page_Mid        += "<TD>" 

    for item in mylist[2].split(','):
        Page_Mid += item + "<br>"

    Page_Mid        += "</TD></TR></TABLE>\n"

    response = Page_Header + Page_Mid + Page_Footer
    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
