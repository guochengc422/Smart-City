# -*- coding: utf-8 -*- 

import sys
from operator import add
from pyspark import SparkContext

# # 区块人流
# def extract(line):
# 	import time
# 	try:
# 		part = line.strip().split(",")
# 		TTIME, LAC, CI, IMSI = part[1].split(" "), part[3], part[4], part[5]
# 		pt1, pt2, pt3 = TTIME[0].split("-"), TTIME[1].split("."), TTIME[2]
# 		year, month, day, hour, minute, second = int("20"+pt1[2]), {"AUG":8}[pt1[1]], int(pt1[0]), int(pt2[0]), int(pt2[1]), int(pt2[2])
# 		hour = hour if hour != 12 else 0
# 		hour = hour if pt3 == "AM" else hour+12
# 		secs = hour*3600+minute*60+second
# 		key = LAC+" "+CI
# 		sl = secs/(60*60)
# 		if bss.has_key(key):
# 			bs = bss[key]
# 			lng, lat = bs["lng"], bs["lat"]
# 			# if 120.02<=lng<120.48 and 30.15<=lat<30.42:
# 			# 	gx, gy = int((lng-120.02)/(120.48-120.02)*225), int((lat-30.15)/(30.42-30.15)*150)
# 			if 120.04<=lng<120.24 and 30.16<=lat<30.34:
# 				gx, gy = int((lng-120.04)/(120.24-120.04)*200), int((lat-30.16)/(30.34-30.16)*200)
# 				return (str(gx)+","+str(gy), sl, IMSI)
# 			else:
# 				return ("", -1, "")
# 		else:
# 			return ("", -1, "")
# 	except:
# 		return ("", -1, "")

# global bss

# if __name__ == "__main__":
# 	import fileinput
# 	bss = {}
# 	for line in fileinput.input("data/hz_base.txt"):
# 		part = line.strip().split(" ")
# 		num, lng, lat = part[1]+" "+part[2], float(part[3]), float(part[4])
# 		bss[num] = {"lng":lng, "lat":lat}
# 	fileinput.close()
# 	sc = SparkContext('spark://namenode.omnilab.sjtu.edu.cn:7077',appName="Extract")
# 	lines = sc.textFile('hdfs://namenode.omnilab.sjtu.edu.cn/user/wanghaiyang/mobile_utf8/0826.csv', 1)
# 	counts = lines.map(lambda x : extract(x)) \
# 			.filter(lambda x : x[0]!="" and x[1]!=-1 and x[2]!="") \
# 			.distinct() \
# 			.map(lambda x : ((x[0],x[1]),1)) \
# 			.reduceByKey(add) \
# 			.sortByKey() \
# 			.map(lambda x : str(x[0][0])+" "+str(x[0][1])+" "+str(x[1]))
# 	output = counts.saveAsTextFile("./cityfunction/0826_user_count.csv")

# # 用户轨迹 step 1
# def extract(line):
# 	import time
# 	try:
# 		part = line.strip().split(",")
# 		TTIME, LAC, CI, IMSI = part[1].split(" "), part[3], part[4], part[5]
# 		pt1, pt2, pt3 = TTIME[0].split("-"), TTIME[1].split("."), TTIME[2]
# 		year, month, day, hour, minute, second = int("20"+pt1[2]), {"AUG":8}[pt1[1]], int(pt1[0]), int(pt2[0]), int(pt2[1]), int(pt2[2])
# 		hour = hour if hour != 12 else 0
# 		hour = hour if pt3 == "AM" else hour+12
# 		secs = hour*3600+minute*60+second
# 		key = LAC+" "+CI
# 		sl = secs/(60*10)
# 		if bss.has_key(key):
# 			bs = bss[key]
# 			lng, lat = bs["lng"], bs["lat"]
# 			# if 120.02<=lng<120.48 and 30.15<=lat<30.42:
# 			# 	gx, gy = int((lng-120.02)/(120.48-120.02)*225), int((lat-30.15)/(30.42-30.15)*150)
# 			if 120.04<=lng<120.24 and 30.16<=lat<30.34:
# 				gx, gy = int((lng-120.04)/(120.24-120.04)*200), int((lat-30.16)/(30.34-30.16)*200)
# 				return (IMSI, sl, gx, gy)
# 			else:
# 				return ("", -1, -1, -1)
# 		else:
# 			return ("", -1, -1, -1)
# 	except:
# 		return ("", -1, -1, -1)

# global bss

# if __name__ == "__main__":
# 	import fileinput
# 	bss = {}
# 	for line in fileinput.input("data/hz_base.txt"):
# 		part = line.strip().split(" ")
# 		num, lng, lat = part[1]+" "+part[2], float(part[3]), float(part[4])
# 		bss[num] = {"lng":lng, "lat":lat}
# 	fileinput.close()
# 	sc = SparkContext('spark://namenode.omnilab.sjtu.edu.cn:7077',appName="Extract")
# 	lines = sc.textFile('hdfs://namenode.omnilab.sjtu.edu.cn/user/wanghaiyang/mobile_utf8/0826.csv', 1)
# 	counts = lines.map(lambda x : extract(x)) \
# 			.filter(lambda x : x[0]!="" and x[1]!=-1 and x[2]!=-1 and x[3]!=-1) \
# 			.map(lambda x : ((x[0],x[1]),(x[2],x[3]))) \
# 			.distinct() \
# 			.groupByKey() \
# 			.map(lambda x : (x[0][0],(x[0][1],(max([i[0] for i in x[1]])+min([i[0] for i in x[1]]))/2,(max([i[1] for i in x[1]])+min([i[1] for i in x[1]]))/2))) \
# 			.groupByKey() \
# 			.map(lambda x : x[0]+" "+" ".join([str(i[0])+","+str(i[1])+","+str(i[2]) for i in sorted(x[1])]))
# 	output = counts.saveAsTextFile("./cityfunction/0826_user_trace.csv")

# 用户轨迹 step 2
def euclidean(p1,p2):
	from math import sqrt
	dist = sqrt(sum([pow(i-j,2) for i,j in zip(p1,p2)]))
	return dist

def extract(line):
	part = line.strip().split(" ")
	status, seq = int(part[0]), [[int(j) for j in i.split(",")] for i in part[2:]]
	result, items, i, j = [], [], 0, 1
	while i<=len(seq)-2:
		ps = [tuple(seq[i][1:])]
		while j<=len(seq)-1:
			if euclidean(seq[i][1:],seq[j][1:]) <= 10: #1000 meters
				ps.append(tuple(seq[j][1:]))
				j+=1
			else:
				for k in range(j+1,min(j+6,len(seq)-1)): #stable leave?
					if seq[k][0]-seq[j][0]<=5 and euclidean(seq[i][1:],seq[k][1:])<=5:
						j = k
				if euclidean(seq[i][1:],seq[j][1:])>5 and seq[j-1][0]-seq[i][0]>=6:
					items.append((seq[i][0],seq[j-1][0],set(ps)))
				break
		i, j = j, j+1
	for i in xrange(len(items)):
		for p in items[i][2]:
			if status == 1:
				result.append(str(p[0])+","+str(p[1])+" 1 "+str(items[i][0]/6)+" 1")
				result.append(str(p[0])+","+str(p[1])+" 1 "+str(items[i][1]/6)+" 0")
			if status == 0:
				result.append(str(p[0])+","+str(p[1])+" 0 "+str(items[i][0]/6)+" 1")
				result.append(str(p[0])+","+str(p[1])+" 0 "+str(items[i][1]/6)+" 0")
	return "*\t"+"\t".join(result)

global bss

if __name__ == "__main__":
	import fileinput
	sc = SparkContext('spark://namenode.omnilab.sjtu.edu.cn:7077',appName="Extract")
	lines = sc.textFile('hdfs://namenode.omnilab.sjtu.edu.cn/user/qiangsiwei/cityfunction/move.txt', 1)
	counts = lines.map(lambda x : extract(x))
output = counts.saveAsTextFile("./cityfunction/move_statistic.csv")
