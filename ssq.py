import json, urllib 
from urllib import urlencode
import csv
import time
import os

url1 = "http://apis.juhe.cn/lottery/history?lottery_id=ssq&page_size=50&page=%s&key=922ff4b71160881dd127e7ec03921d16"
csv_file = "ssq"+time.strftime("%Y%m%d", time.localtime())+".csv"


def load_data():
	list1 = []

	name = csv_file

	with open(name) as csvf:
		csvr = csv.reader(csvf)
		list1 = []#next(csvr)
		for row in csvr:
			list1.append(row)
	return list1
		
'''	
				
				
	list1 = []	
	with open("ssq.csv") as csvf:
		csvr = csv.reader(csvf)
		header = next(csvr)
		for row in csvr:
		list1.append(row)

	if list1 == []:
		for i in range(1,52):
			f = urllib.urlopen(url1 %i)
			content = f.read()
			res = json.loads(content)
			if res["error_code"] == "0":
				list1.append(res["result"]["lotteryResList"])
	
		with open('ssq.csv','w') as csvf:
			writer = csv.writer(csvf,dialect='excel')
			writer.writerow(list1[0].keys())
			for row in list1:
				writer.writerow(row.values())
				
	for i in range(1,52):
		f = urllib.urlopen(url1 %i)
		content = f.read()
		res = json.loads(content)
		for res_row in reversed(res["result"]["lotteryResList"])
	

with open("ssq.csv") as csvf:
	csvr = csv.reader(csvf)
	header = next(csvr)
	for row in csvr:
	list1.append(row)

 l[0][header.index("lottery_no")]+","+l[0][header.index("lottery_res")]
l2=l[0][header.index("lottery_res")].split(",")

 res["result"]["lotteryResList"] == None

for i in range(1,52):
	f = urllib.urlopen(url1 %i)
	content = f.read()
	res = json.loads(content)
	if res["error_code"] == "0":
		list1.append(res["result"]["lotteryResList"])



with open('ssq.csv','w') as csvf:
	writer = csv.writer(csvf,dialect='excel')
	writer.writerow(list1[0].keys())
	for row in list1:
		writer.writerow(row.values())

'''

def main():
	ssq_list = load_data()
	ssq_num = []
	print ssq_list[0]
	print ssq_list[1]
	print ssq_list[2]
	print ssq_list[10]
#	print ssq_list[len(ssq_list)-1]
	
	header = ssq_list[0]
	for row in ssq_list:
		ssq_num.append((row[header.index("lottery_no")]+","+row[header.index("lottery_res")]).split(","))
	ssq_num[0] = ["lottery_no","b1","b2","b3","b4","b5","b6","r"]
	print ssq_num[0:4]
	

	exit(0)


if __name__ == '__main__':
	main()
	



