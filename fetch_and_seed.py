# fetch_and_seed.py

import sqlite3
import requests
import json

def main():
	print "=== Fetch and Seed is starting ===\n\n"

	astros = fetchAstroData()

	db = sqlite3.connect('mydb')


	# cursor = db.cursor()
	createAstronautTable(db)
	print("=== database has been connected to===\n\n")

	insertAstroData(astros, db)

	astroData = getAstroData(db)

	db.close()
	print "=== Fetch and Seed is terminating ===\n\n"

# Creates table to hold astronaut data
def createAstronautTable(db):
	cursor = db.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS astronauts(name TEXT PRIMARY KEY, craft TEXT)''')
	db.commit()
	cursor.close()

# Inserts astronaut data into the astronaut table
def insertAstroData(astros, db):
	print "TODO"
	cursor = db.cursor()
	for astro in astros:
		craft = astro["craft"]
		name = astro["name"]
		cursor.execute('''INSERT INTO astronauts(name, craft) VALUES(?,?)''', (name, craft))

	cursor.close()


# Selects astronaut data from the astonaut table to verify that it is there
def getAstroData(db):
	cursor = db.cursor()
	cursor.execute('''SELECT * FROM astronauts''')
	all_rows = cursor.fetchall()
	cursor.close()

	print "=== data from db===\n\n"
	print all_rows


	return all_rows

# Pulls astronaut data from the NASA open api
def fetchAstroData():
	r = requests.get('http://api.open-notify.org/astros.json')

	astroData = r.json()
	# print astroData["people"]
	return astroData["people"]


if __name__ == "__main__":
	main()
