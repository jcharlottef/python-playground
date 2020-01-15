# by Jackie and Johnathon 

from datetime import datetime


birthday = "1-May-12"

#parse date
parsed_date = datetime.strptime(birthday, "%d-%B-%y")
print(parsed_date)

# sterftime output 

date_str = parsed_date.strftime("%-m/%d/%Y")
print(date_str)