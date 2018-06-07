import csv

def generate_csv_from_dict(comments_dict):
	with open('comments_occurrence.csv', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		for comment in comments_dict:
			 spamwriter.writerow([comment, comments_dict[comment]])