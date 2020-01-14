import pandas as pd
import sys
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
tablename = 'something'

csv_path=sys.argv[1] #First command line parameter is the filename
query = sys.argv[2] #Second command line parameter is the where query
c_size = 500	#Chunk size you want to read
#query = "Country = 'India' "
for gm_chunk in pd.read_csv(csv_path,chunksize=c_size):
		#print(gm_chunk.shape)
		gm_chunk.to_sql(tablename, conn, if_exists='replace', index=False)
		#Convert the csv file to a sqlite table
		conn.commit()
		c.execute("SELECT * FROM {} WHERE {} ".format(tablename, query))
		for row in c:
			print(row)
		inp = input("Continue? y/n")
		if inp == 'n':
			break
conn.close()