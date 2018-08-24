from bs4 import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print (soup.prettify())
'''C:\Users\User\AppData\Local\Programs\Python\Python36\lib\site-packages\bs4\__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
The code that caused this warning is on line 8 of the file new 1.txt. To get rid of this warning, change code that looks like this:
 BeautifulSoup(YOUR_MARKUP})
to this:
 BeautifulSoup(YOUR_MARKUP, "html.parser")

  markup_type=markup_type))
<html>
 <head>
  <title>
   Page title
  </title>
 </head>
 <body>
  <p align="center" id="firstpara">
   This is paragraph
   <b>
    one
   </b>
   .
   <p align="blah" id="secondpara">
    This is paragraph
    <b>
     two
    </b>
    .
   </p>
  </p>
 </body>
</html>'''