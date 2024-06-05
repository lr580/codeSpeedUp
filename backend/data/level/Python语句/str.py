'1'.center(4,'-')
'a'.join(('bc','','d','e')) == 'bcaadae'
'123 abc def'.capitalize()
from functools import reduce
reduce(lambda x,y:x+y,list(filter(str.strip,'\n _1\n\t 1\n  \n')))