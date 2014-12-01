import csv

f = open('lahman-csv_2014-02-14/Batting.csv')

csv_f = csv.reader(f)

playerHolder = {}

#We're going to have our own 
# LahmanID/Games/AB/R/H/2B/3B/HR/RBI/SB/CS/BB/SO/IBB/HBP/SH/SF/GIDP

i = 0

def myInt(value):
	if value == '':
		return 0
	else:
		return int(value)

for row in csv_f:
	if row[0] != 'playerID':
		if row[0] not in playerHolder:
			newDict = {}
			newDict["LahmanID"] = row[0]
			newDict["G"] = myInt(row[5])
			newDict["AB"] = myInt(row[7])
			newDict["R"] = myInt(row[8])
			newDict["H"] = myInt(row[9])
			newDict["2B"] = myInt(row[10])
			newDict["3B"] = myInt(row[11])
			newDict["HR"] = myInt(row[12])
			newDict["RBI"] = myInt(row[13])
			newDict["SB"] = myInt(row[14])
			newDict["CS"] = myInt(row[15])
			newDict["BB"] = myInt(row[16])
			newDict["SO"] = myInt(row[17])
			newDict["IBB"] = myInt(row[18])
			newDict["HBP"] = myInt(row[19])
			newDict["SH"] = myInt(row[20])
			newDict["SF"] = myInt(row[21])
			newDict["GIDP"] = myInt(row[22])

			playerHolder[row[0]] = newDict 

		else:
			playerHolder[row[0]]["G"] += myInt(row[5])
			playerHolder[row[0]]["AB"] += myInt(row[7])
			playerHolder[row[0]]["R"] += myInt(row[8])
			playerHolder[row[0]]["H"] += myInt(row[9])
			playerHolder[row[0]]["2B"] += myInt(row[10])
			playerHolder[row[0]]["3B"] += myInt(row[11])
			playerHolder[row[0]]["HR"] += myInt(row[12])
			playerHolder[row[0]]["RBI"] += myInt(row[13])
			playerHolder[row[0]]["SB"] += myInt(row[14])
			playerHolder[row[0]]["CS"] += myInt(row[15])
			playerHolder[row[0]]["BB"] += myInt(row[16])
			playerHolder[row[0]]["SO"] += myInt(row[17])
			playerHolder[row[0]]["IBB"] += myInt(row[18])
			playerHolder[row[0]]["HBP"] += myInt(row[19])
			playerHolder[row[0]]["SH"] += myInt(row[20])
			playerHolder[row[0]]["SF"] += myInt(row[21])
			playerHolder[row[0]]["GIDP"] += myInt(row[22])

for key, value in playerHolder.iteritems():
	print value


