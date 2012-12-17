'''
Created on 17 Dec 2012

@author: cgueret
'''
import csv

def go():
	# Get the number of instances of classes
	numberOfInstances = {}
	with open('data/Class Frequency.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		head = True
		for row in reader:
			if head:
				head = False
				continue
			c = row[0]
			n = row[2]
			if c != '' and n != '':
				numberOfInstances[c] = int(n)
	
	# Count the number of links there is and the maximum number of links
	linkageCount = {}
	with open('data/Link Properties Detailed.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		head = True
		for row in reader:
			if head:
				head = False
				continue
			p = row[0]
			count = int(row[2])
			domainClass = row[3]
			rangeClass = row[4]
			if domainClass != '' and rangeClass != '':
				if domainClass in numberOfInstances and rangeClass in numberOfInstances:
					if p not in linkageCount:
						linkageCount[p] = {}
						linkageCount[p]['count'] = 0
						linkageCount[p]['upper'] = 0
						linkageCount[p]['type'] = None
					count2 = numberOfInstances[domainClass]*numberOfInstances[rangeClass]
					linkageCount[p]['count'] += count
					linkageCount[p]['upper'] += count2
	
	# Load extra information about the links
	with open('data/Link Properties.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		head = True
		for row in reader:
			if head:
				head = False
				continue
			p = row[0]
			linkType = row[8]
			if row[8] != '' and p in linkageCount:
				linkageCount[p]['type'] = linkType
	
	# Display the results
	for p in linkageCount.iterkeys():
		if linkageCount[p]['type'] != None:
			print p
			print linkageCount[p]
			print ""
			
			
if __name__ == '__main__':
		go()