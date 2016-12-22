from dataextractor import extract
from sklearn import svm

data, classification = extract()

for key, value in data.iteritems():
	#if value["inHof"] == 'Y':
	print value

print classification

clf = svm.SVC()
clf.fit(data, classification)
