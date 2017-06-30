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
print response
