import pandas as pd 

df = pd.read_csv('AttendanceFile.csv')

df.drop_duplicates(subset="ID",inplace = True)
df.to_csv('Updated_attendance.csv')