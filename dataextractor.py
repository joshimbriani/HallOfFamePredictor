import csv

def extract():

	batting = open('lahman-csv_2014-02-14/Batting.csv')
	master = open('lahman-csv_2014-02-14/Master.csv')
	hof = open('lahman-csv_2014-02-14/HallOfFame.csv')

	csv_batting = csv.reader(batting)
	csv_master = csv.reader(master)
	csv_hof = csv.reader(hof)

	playerHolder = {}

	i = 0

	def myInt(value):
		if value == '':
			return 0
		else:
			return int(value)

	for row in csv_batting:
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
				newDict["firstYear"] = myInt(row[1])
				newDict["lastYear"] = myInt(row[1])
				newDict["inHof"] = 'N'

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

				if myInt(row[1]) < playerHolder[row[0]]["firstYear"]:
					playerHolder[row[0]]["firstYear"] = myInt(row[1])

				if myInt(row[1]) > playerHolder[row[0]]["lastYear"]:
					playerHolder[row[0]]["lastYear"] = myInt(row[1])

	for row in csv_master:
		if row[0] in playerHolder:
			playerHolder[row[0]]["firstName"] = row[13]
			playerHolder[row[0]]["lastName"] = row[14]

	for row in csv_hof:
		if row[0] in playerHolder and row[6] == 'Y':
			playerHolder[row[0]]["inHof"] = 'Y'
			print "Here"

	classification = []
	for key, value in playerHolder.iteritems():
		if value["inHof"] == 'Y':
			classification.append('Y')
		else:
			classification.append('N')
		del value["inHof"]

	return playerHolder, classification

