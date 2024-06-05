"{} {}".format(123, 456) 
"{1}, {0}".format('hell', 'word')
"{year}Year{month}Month".format(year=2023, month=4)
from datetime import datetime
"{:%Y-%m-%d}".format(datetime(2023, 4, 1))
"{data[year]}Year".format(data={'year': 2023})
"{0[0]}和{0[1]}".format(['apple', 'banana'])
f'{6:02d},{1/3:+.6f}'
"{:>10}".format("test")
"{:->10}".format("test")
"{:<10}".format("test")
"{{{}Year}}".format(2023)