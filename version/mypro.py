# -*- coding: utf-8 -*- 

import fileinput

# weekend:19,25,26
# weekday:20,21,22,23,24

def test():
	# draw grid
	# GR = 50
	# file = open("grid.txt","w")
	# for i in xrange(GR+1):
	# 	lat1, lat2 = 30.15, 30.35
	# 	lng1 = 120.05+i*((120.25-120.05)/GR)
	# 	lng2 = 120.05+i*((120.25-120.05)/GR)
	# 	file.write("map.addOverlay(new BMap.Polyline([new BMap.Point("+str(lng1)+","+str(lat1)+"),new BMap.Point("+str(lng2)+","+str(lat2)+")], {strokeColor:\"red\", strokeWeight:1, strokeOpacity:0.25}));\n")
	# for i in xrange(GR+1):
	# 	lng1, lng2 = 120.05, 120.25
	# 	lat1 = 30.15+i*((30.35-30.15)/GR)
	# 	lat2 = 30.15+i*((30.35-30.15)/GR)
	# 	file.write("map.addOverlay(new BMap.Polyline([new BMap.Point("+str(lng1)+", "+str(lat1)+"),new BMap.Point("+str(lng2)+", "+str(lat2)+")], {strokeColor:\"red\", strokeWeight:1, strokeOpacity:0.25}));\n")
	# file.close()

	rangex, rangey = 225, 150

	# # merge spark result
	# import fileinput
	# grid_wd_es = [[[0 for i in xrange(24)] for j in xrange(rangey)] for k in xrange(rangex)]
	# grid_wd_ds = [[[0 for i in xrange(24)] for j in xrange(rangey)] for k in xrange(rangex)]
	# grid_we_es = [[[0 for i in xrange(24)] for j in xrange(rangey)] for k in xrange(rangex)]
	# grid_we_ds = [[[0 for i in xrange(24)] for j in xrange(rangey)] for k in xrange(rangex)]
	# for line in fileinput.input("move_statistic.txt"):
	# 	part = line.split("\t")[1:]
	# 	for p in part:
	# 		try:
	# 			a, w, i, s = p.split(" ")[0], int(p.split(" ")[1]), int(p.split(" ")[2]), int(p.split(" ")[3])
	# 			if w == 0 and s == 0:
	# 				grid_we_ds[int(a.split(",")[0])][int(a.split(",")[1])][i] += 1
	# 			if w == 0 and s == 1:
	# 				grid_we_es[int(a.split(",")[0])][int(a.split(",")[1])][i] += 1
	# 			if w == 1 and s == 0:
	# 				grid_wd_ds[int(a.split(",")[0])][int(a.split(",")[1])][i] += 1
	# 			if w == 1 and s == 1:
	# 				grid_wd_es[int(a.split(",")[0])][int(a.split(",")[1])][i] += 1
	# 		except:
	# 			continue
	# fileinput.close()
	# list = []
	# for i in xrange(rangex):
	# 	for j in xrange(rangey):
	# 		list.append({"g":str(i)+","+str(j),"s":sum(grid_wd_es[i][j])+sum(grid_wd_ds[i][j])+sum(grid_we_es[i][j])+sum(grid_we_ds[i][j]),"l":"\t".join([str(k) for k in grid_wd_es[i][j]])+"\t"+"\t".join([str(k) for k in grid_wd_ds[i][j]])+"\t"+"\t".join([str(k) for k in grid_we_es[i][j]])+"\t"+"\t".join([str(k) for k in grid_we_ds[i][j]])})
	# list = sorted(list, key=lambda x:x["s"], reverse=True)
	# # count = 0
	# # for item in list:
	# # 	count += 1
	# # 	if count >= 1000:
	# # 		print count, 120.05+(120.25-120.05)/50*int(item["g"].split(",")[0]), 30.15+(30.35-30.15)/50*int(item["g"].split(",")[1])
	# # 		fig = plt.figure()
	# # 		ax = fig.add_subplot(111)
	# # 		ax.plot([i for i in xrange(24)], [int(i) for i in item["l"].split("\t")[0:24]], c="red", alpha=0.5)
	# # 		ax.plot([i for i in xrange(24)], [int(i) for i in item["l"].split("\t")[24:48]], c="orange", alpha=0.5)
	# # 		ax.plot([i for i in xrange(24)], [int(i) for i in item["l"].split("\t")[48:72]], c="yellow", alpha=0.5)
	# # 		ax.plot([i for i in xrange(24)], [int(i) for i in item["l"].split("\t")[72:96]], c="green", alpha=0.5)
	# # 		plt.show()
	# file = open("statistic_move.txt","w")
	# for item in list:
	# 	file.write(str(item["g"])+"\t"+str(item["s"])+"\t"+item["l"]+"\n")
	# file.close()

	# generate document
	# file = open("out.txt","w")
	# file.write("1687\n")
	# c = 0
	# for line in fileinput.input("statistic_move.txt"):
	# 	part = line.split("\t")
	# 	grid, total, feature = part[0], int(part[1]), [int(i) for i in part[2:]]
	# 	feature = [int(feature[i]/5.0) if 0<=i<24*2 else int(feature[i]/3.0) for i in xrange(len(feature))]
	# 	for i in xrange(24):
	# 		for j in xrange(feature[i]+1):
	# 			file.write(str(i)+",1,E ")
	# 	for i in xrange(24):
	# 		for j in xrange(feature[24+i]+1):
	# 			file.write(str(i)+",1,D ")
	# 	for i in xrange(24):
	# 		for j in xrange(feature[48+i]+1):
	# 			file.write(str(i)+",0,E ")
	# 	for i in xrange(24):
	# 		for j in xrange(feature[72+i]+1):
	# 			file.write(str(i)+",0,D ")
	# 	file.write("\n")
	# 	c += 1
	# 	if c == 1687:
	# 		break
	# fileinput.close()
	# file.close()

	# movement func 1
	# gridmap = {}
	# c = 0
	# for line in fileinput.input("statistic_move.txt"):
	# 	grid = line.strip().split("\t")[0]
	# 	lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
	# 	gridmap[c] = (lng, lat)
	# 	c += 1
	# colormap = [[0 for j in xrange(rangey)] for i in xrange(rangex)]
	# c = 0
	# for line in fileinput.input("GibbsLDA++/model-final.theta"):
	# 	prob = [float(i) for i in line.strip().split(" ")]
	# 	# colormap[gridmap[c][0]][gridmap[c][1]] = float(prob.index(max(prob))+2)/10
	# 	if prob.index(max(prob)) == 0:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.65
	# 	if prob.index(max(prob)) == 1:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 1.00
	# 	if prob.index(max(prob)) == 2:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.25
	# 	if prob.index(max(prob)) == 3:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.72
	# 	if prob.index(max(prob)) == 4:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.45
	# 	if prob.index(max(prob)) == 5:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.90
	# 	if prob.index(max(prob)) == 6:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.55
	# 	if prob.index(max(prob)) == 7:
	# 		colormap[gridmap[c][0]][gridmap[c][1]] = 0.35
	# 	c += 1
	# import matplotlib.pyplot as plt
	# import numpy as np
	# (X, Y), C = np.meshgrid(np.arange(rangex+1), np.arange(rangey+1)), np.array(colormap)
	# plt.subplot(111)
	# plt.pcolormesh(X,Y,C.T)
	# plt.axis('off')
	# plt.show()
	# y0list, y1list, y2list, y3list = [], [], [], []
	# for line in fileinput.input("GibbsLDA++/model-final.phi"):
	# 	prob = [float(i) for i in line.strip().split(" ")]
	# 	y0, y1, y2, y3 = prob[0:24], prob[24:48], prob[48:72], prob[72:96]
	# 	y0list.append(y0)
	# 	y1list.append(y1)
	# 	y2list.append(y2)
	# 	y3list.append(y3)
	# fig = plt.figure()
	# ax1 = fig.add_subplot(241)
	# ax1.plot([i for i in xrange(24)], y0list[1], c="red")
	# ax1.plot([i for i in xrange(24)], y1list[1], c="yellow")
	# ax1.plot([i for i in xrange(24)], y2list[1], c="green")
	# ax1.plot([i for i in xrange(24)], y3list[1], c="blue")
	# ax1.set_xlim(0,23)
	# ax1.set_ylim(0,0.15)
	# ax2 = fig.add_subplot(242)
	# ax2.plot([i for i in xrange(24)], y0list[5], c="red")
	# ax2.plot([i for i in xrange(24)], y1list[5], c="yellow")
	# ax2.plot([i for i in xrange(24)], y2list[5], c="green")
	# ax2.plot([i for i in xrange(24)], y3list[5], c="blue")
	# ax2.set_xlim(0,23)
	# ax2.set_ylim(0,0.15)
	# ax3 = fig.add_subplot(243)
	# ax3.plot([i for i in xrange(24)], y0list[3], c="red")
	# ax3.plot([i for i in xrange(24)], y1list[3], c="yellow")
	# ax3.plot([i for i in xrange(24)], y2list[3], c="green")
	# ax3.plot([i for i in xrange(24)], y3list[3], c="blue")
	# ax3.set_xlim(0,23)
	# ax3.set_ylim(0,0.15)
	# ax4 = fig.add_subplot(244)
	# ax4.plot([i for i in xrange(24)], y0list[0], c="red")
	# ax4.plot([i for i in xrange(24)], y1list[0], c="yellow")
	# ax4.plot([i for i in xrange(24)], y2list[0], c="green")
	# ax4.plot([i for i in xrange(24)], y3list[0], c="blue")
	# ax4.set_xlim(0,23)
	# ax4.set_ylim(0,0.15)
	# ax5 = fig.add_subplot(245)
	# ax5.plot([i for i in xrange(24)], y0list[6], c="red")
	# ax5.plot([i for i in xrange(24)], y1list[6], c="yellow")
	# ax5.plot([i for i in xrange(24)], y2list[6], c="green")
	# ax5.plot([i for i in xrange(24)], y3list[6], c="blue")
	# ax5.set_xlim(0,23)
	# ax5.set_ylim(0,0.15)
	# ax6 = fig.add_subplot(246)
	# ax6.plot([i for i in xrange(24)], y0list[4], c="red")
	# ax6.plot([i for i in xrange(24)], y1list[4], c="yellow")
	# ax6.plot([i for i in xrange(24)], y2list[4], c="green")
	# ax6.plot([i for i in xrange(24)], y3list[4], c="blue")
	# ax6.set_xlim(0,23)
	# ax6.set_ylim(0,0.15)
	# ax7 = fig.add_subplot(247)
	# ax7.plot([i for i in xrange(24)], y0list[7], c="red")
	# ax7.plot([i for i in xrange(24)], y1list[7], c="yellow")
	# ax7.plot([i for i in xrange(24)], y2list[7], c="green")
	# ax7.plot([i for i in xrange(24)], y3list[7], c="blue")
	# ax7.set_xlim(0,23)
	# ax7.set_ylim(0,0.15)
	# ax8 = fig.add_subplot(248)
	# ax8.plot([i for i in xrange(24)], y0list[2], c="red")
	# ax8.plot([i for i in xrange(24)], y1list[2], c="yellow")
	# ax8.plot([i for i in xrange(24)], y2list[2], c="green")
	# ax8.plot([i for i in xrange(24)], y3list[2], c="blue")
	# ax8.set_xlim(0,23)
	# ax8.set_ylim(0,0.15)
	# plt.show()

	# movement func 2
	# from pylab import *
	# gridmap = {}
	# c = 0
	# for line in fileinput.input("statistic_move.txt"):
	# 	grid = line.strip().split("\t")[0]
	# 	lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
	# 	gridmap[c] = (lng, lat)
	# 	c += 1
	# colormap = [[0 for j in xrange(rangey)] for i in xrange(rangex)]
	# c = 0
	# for line in fileinput.input("GibbsLDA++/model-final.theta"):
	# 	prob = [float(i) for i in line.strip().split(" ")]
	# 	colormap[gridmap[c][0]][gridmap[c][1]] = prob[0]
	# 	c += 1
	# (X, Y), C = meshgrid(np.arange(rangex), np.arange(rangey)), np.array(colormap)
	# levels = arange(0, 1.1, 0.1) 
	# cmap, norm = cm.PRGn, cm.colors.Normalize(vmax=1.1, vmin=0)
	# figure()
	# subplot(1,1,1)
	# cset1 = contourf(X, Y, C.T, levels, cmap=cm.get_cmap("Oranges", len(levels)), norm=norm)
	# colorbar(cset1)
	# axis('off')
	# show()

	# intensity1
	# from pylab import *
	# import numpy as np
	# slist = []
	# for line in fileinput.input("statistic_move.txt"):
	# 	part = line.strip().split("\t")
	# 	grid, feature = part[0], [int(i) for i in part[2:]]
	# 	s1, s2 = sum(feature[0:48]), sum(feature[48:96])
	# 	lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
	# 	slist.append({"s":s1+s2,"r":float(s1)/float(s2) if s2!=0 else 0,"g":(lng,lat)})
	# slist = sorted(slist, key=lambda x:x["s"])
	# colormap = [[0 for j in xrange(150)] for i in xrange(225)]
	# for item in slist:
	# 	colormap[item["g"][0]][item["g"][1]] = min(1,item["s"]*1.0/(slist[-1]["s"]/4))
	# (X, Y), C = meshgrid(np.arange(rangex), np.arange(rangey)), np.array(colormap)
	# levels = arange(0, 1.1, 0.1)
	# cmap, norm = cm.PRGn, cm.colors.Normalize(vmax=1.1, vmin=0)
	# figure()
	# subplot(1,1,1)
	# cset1 = contourf(X, Y, C.T, levels, cmap=cm.get_cmap("Oranges", len(levels)), norm=norm)
	# colorbar(cset1)
	# axis('off')
	# show()

	# intensity2
	from pylab import *
	import numpy as np
	slist = []
	for line in fileinput.input("statistic_move.txt"):
		part = line.strip().split("\t")
		grid, feature = part[0], [int(i) for i in part[2:]]
		s1, s2 = sum(feature[0:48]), sum(feature[48:96])
		lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
		slist.append({"s":s1+s2,"r":float(s2)-float(s1) if s2!=0 else 0,"g":(lng,lat)})
	slist = sorted(slist, key=lambda x:x["s"])
	smin, smax = abs(min([slist[i]["r"] for i in xrange(len(slist))]))/4, abs(max([slist[i]["r"] for i in xrange(len(slist))]))/8
	# slist = [{"s":slist[i]["s"],"r":(slist[i]["r"]-smin)*1.0/(smax-smin),"g":slist[i]["g"]} for i in xrange(len(slist))]
	slist = [{"s":slist[i]["s"],"r":min(slist[i]["r"]*1.0/smax+0.05,1) if slist[i]["r"]>0 else max(slist[i]["r"]*1.0/smin+0.05,-0.95) if slist[i]["r"]<0 else 0,"g":slist[i]["g"]} for i in xrange(len(slist))]
	colormap = [[0 for j in xrange(150)] for i in xrange(225)]
	for item in slist:
		colormap[item["g"][0]][item["g"][1]] = item["r"]
	(X, Y), C = meshgrid(np.arange(rangex), np.arange(rangey)), np.array(colormap)
	levels = arange(-1, 1.1, 0.1) 
	cmap, norm = cm.PRGn, cm.colors.Normalize(vmax=1.1, vmin=-1)
	figure()
	subplot(1,1,1)
	cset1 = contourf(X, Y, C.T, levels, cmap=cm.get_cmap("RdBu", len(levels)), norm=norm)
	colorbar(cset1)
	axis('off')
	show()

	# poi func1
	# c = 0
	# gridmap = {}
	# for line in fileinput.input("statistic_move.txt"):
	# 	grid = line.strip().split("\t")[0]
	# 	lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
	# 	gridmap[str(lng)+","+str(lat)] = True
	# 	c += 1
	# 	if c == 1000:
	# 		break
	# fileinput.close()
	# tagmap = {}
	# for line in fileinput.input("poi.txt"):
	# 	part = line.strip().split("\t")
	# 	tag, lng, lat = part[0], float(part[1]), float(part[2])
	# 	if 120.02<=lng<=120.48 and 30.15<=lat<=30.42:
	# 		tagmap[tag] = 1 if not tagmap.has_key(tag) else tagmap[tag]+1
	# fileinput.close()
	# taglist = []
	# for k,v in tagmap.iteritems():
	# 	taglist.append({"k":k,"v":v})
	# taglist = sorted(taglist, key=lambda x:x["v"])
	# tag, count = [], []
	# for item in taglist:
	# 	if item["k"] in ["公司","购物","美食","房产","休闲","政府","丽人","金融","医疗","宾馆","汽车","教育","培训","旅游","运动"]:
	# 		item["k"] = "company" if item["k"] == "公司"\
	# 		else "shopping" if item["k"] == "购物"\
	# 		else "food" if item["k"] == "美食"\
	# 		else "housing" if item["k"] == "房产"\
	# 		else "leisure" if item["k"] == "休闲"\
	# 		else "government" if item["k"] == "政府"\
	# 		else "beauty" if item["k"] == "丽人"\
	# 		else "finance" if item["k"] == "金融"\
	# 		else "medical" if item["k"] == "医疗"\
	# 		else "hotel" if item["k"] == "宾馆"\
	# 		else "car" if item["k"] == "汽车"\
	# 		else "education" if item["k"] == "教育"\
	# 		else "training" if item["k"] == "培训"\
	# 		else "traveling" if item["k"] == "旅游"\
	# 		else "physical" if item["k"] == "运动"\
	# 		else ""
	# 		tag.append(unicode(item["k"],"utf-8"))
	# 		count.append(item["v"])
	# import matplotlib.pyplot as plt
	# import numpy as np
	# y_pos = np.arange(len(tag))
	# plt.barh(y_pos, count, align='center', alpha=0.4)
	# plt.yticks(y_pos, tag)
	# plt.xlabel('count')
	# plt.title('POI statistics')
	# plt.show()

	# poi func2
	# poistat = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for j in xrange(rangey)] for i in xrange(rangex)]
	# for line in fileinput.input("poi.txt"):
	# 	part = line.strip().split("\t")
	# 	tag, lng, lat = part[0], float(part[1]), float(part[2])
	# 	if tag in ["公司","购物","美食","房产","休闲","政府","丽人","金融","医疗","宾馆","汽车","教育","培训","旅游","运动"] and 120.05<=lng<120.25 and 30.15<=lat<30.35:
	# 		lng, lat = int((lng-120.02)/(120.48-120.02)*225), int((lat-30.15)/(30.42-30.15)*150)
	# 		tag = 0 if tag == "公司"\
	# 		else  1 if tag == "购物"\
	# 		else  2 if tag == "美食"\
	# 		else  3 if tag == "房产"\
	# 		else  4 if tag == "休闲"\
	# 		else  5 if tag == "政府"\
	# 		else  6 if tag == "丽人"\
	# 		else  7 if tag == "金融"\
	# 		else  8 if tag == "医疗"\
	# 		else  9 if tag == "宾馆"\
	# 		else 10 if tag == "汽车"\
	# 		else 11 if tag == "教育"\
	# 		else 12 if tag == "培训"\
	# 		else 13 if tag == "旅游"\
	# 		else 14 if tag == "运动"\
	# 		else -1
	# 		poistat[lng][lat][tag] += 1
	# # poistat = [[[float(poistat[i][j][k])/sum(poistat[i][j]) if sum(poistat[i][j])!=0 else 0 for k in xrange(15)] for j in xrange(50)] for i in xrange(50)]
	# gridmap = {}
	# c = 0
	# for line in fileinput.input("statistic_move.txt"):
	# 	grid = line.strip().split("\t")[0]
	# 	lng, lat = int(grid.split(",")[0]), int(grid.split(",")[1])
	# 	gridmap[c] = (lng, lat)
	# 	c += 1
	# classlist = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in xrange(8)]
	# c = 0
	# for line in fileinput.input("GibbsLDA++/model-final.theta"):
	# 	prob = [float(i) for i in line.strip().split(" ")]
	# 	for t in xrange(8):
	# 		classlist[t] = [i+j for i,j in zip(classlist[t], [k*prob[t] for k in poistat[gridmap[c][0]][gridmap[c][1]]])]
	# 	c += 1
	# classlist = [[float(classlist[i][j])/sum(classlist[i]) for j in xrange(15)] for i in xrange(8)]
	# avg = [sum([classlist[j][i] for j in xrange(8)])/8 for i in xrange(15)]
	# # classlist = [[classlist[i][j]-avg[j] for j in xrange(15)] for i in xrange(8)]
	# classlist = [[(classlist[i][j]-avg[j])*(1.0/8)/avg[j] for j in xrange(15)] for i in xrange(8)]
	# import matplotlib.pyplot as plt
	# import numpy as np
	# fig = plt.figure()
	# ax1 = fig.add_subplot(241)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[1], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax1.set_ylim(-0.1,0.1)
	# ax2 = fig.add_subplot(242)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[5], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax2.set_ylim(-0.1,0.1)
	# ax3 = fig.add_subplot(243)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[3], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax3.set_ylim(-0.1,0.1)
	# ax4 = fig.add_subplot(244)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[0], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax4.set_ylim(-0.1,0.1)
	# ax5 = fig.add_subplot(245)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[6], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax5.set_ylim(-0.1,0.1)
	# ax6 = fig.add_subplot(246)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[4], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax6.set_ylim(-0.1,0.1)
	# ax7 = fig.add_subplot(247)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[7], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax7.set_ylim(-0.1,0.1)
	# ax8 = fig.add_subplot(248)
	# tag = [str(i) for i in xrange(15)]
	# y_pos = np.arange(len(tag))
	# plt.bar(y_pos, classlist[2], align='center', alpha=0.4)
	# plt.xticks(y_pos, tag)
	# ax8.set_ylim(-0.1,0.1)
	# plt.show()

test()

