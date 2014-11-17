__author__ = 'vvu'
import urllib
from lxml.html import fromstring
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

oX = []
oY = []
oZ = []

for year in range(2007, 2015):
    for i in range(5):
        oX.append(year)

    #oZ.append("USA")
    #oZ.append("UK")
    #oZ.append("Germany")
    #oZ.append("France")
    #oZ.append("Switzerland")  

    oZ.append(0)
    oZ.append(1)
    oZ.append(2)
    oZ.append(3)
    oZ.append(4)  
    temp_col = [0] * 5
    nr_uni = [0] * 5

    f = open('dataEng/' + str(year) + '.csv', 'w')
    url = 'http://www.shanghairanking.com/FieldENG' + str(year) + '.html'
    content = urllib.urlopen(url).read()
    doc = fromstring(content)
    doc.make_links_absolute(url)

    tableHdr = ["World Rank", "Institution", "Country", "National Rank", "Total Score", "Additional Score"]
    f.write(",".join(tableHdr))
    f.write('\n')
    table = doc.get_element_by_id('UniversityRanking')
    skip = True
    for tr in table:
        if skip:
            skip = False
            continue
        index = tr[0].text
        uni_name = ""
        uni_country = ""
        uni_rank = ""
        uni_total_score = ""
        uni_alumni_score = ""

        name_children = tr[1].getchildren()
        for name in name_children:
            #if year == 2011:
            #    uni_name = name.getchildren()[0].text.rstrip().replace(',', '')
            #else:
                uni_name = name.text.rstrip().replace(',', '')

        country_children = tr[2].getchildren()
        for country in country_children:
            if country.attrib:
                tmp_name = country.attrib['src'].split('/')
                uni_country = tmp_name[len(tmp_name)-1].split('.')[0]

        if year == 2008:
            uni_rank = tr[3].text
        else:
            rank_children = tr[3].getchildren()
            for rank in rank_children:
                if (rank.text):
                    uni_rank = rank.text.rstrip()
                else:
                    uni_rank = ""

        if year == 2008:
            uni_total_score = tr[4].text
        else:
            score_children = tr[4].getchildren()
            for score in score_children:
                if year == 2011:
                    uni_total_score = score.text.rstrip()
                else:
                    uni_total_score = score.text

        if year == 2008:
            uni_alumni_score = tr[5].text
        else:
            additional_score = tr[5].getchildren()
            for score in additional_score:
                uni_alumni_score = score.text.rstrip()

        if index == "51-75" or index == "52-76" or index == "51-77" or index == "52-75":
            index = 437
        elif index == "76-110" or index == "76-100" or index == "77-107" or index == "78-100" or index == "77-106" or index == "76-107":
            index = 408
        elif index == "101-150" or index == "101-152" or index == "102-150" or index == "101-151":
            index = 376
        elif index == "151-200" or index == "153-202" or index == "151-202" or index == "152-200":
            index = 326
        elif index == "201-300" or index == "203-300" or index == "203-304" or index == "201-302":
            index = 251
        elif index == "301-400" or index == "305-402" or index == "303-401":
            index = 151
        elif index == "401-500" or index == "403-510" or index == "402-503" or index == "402-501":
            index = 51
        elif index != "World ":
            index = 501-int(index)
        if uni_total_score is None:
            uni_total_score = "0"
        if (uni_rank is None):
            uni_rank = "0" 
        lst = [str(index), uni_name, uni_country, uni_rank, uni_total_score, uni_alumni_score]
        if (uni_country == "USA" or uni_country == "UnitedStates" or uni_country == "US"):
            temp_col[0] += index
            nr_uni[0]+=1
        elif (uni_country == "UK" or uni_country == "UnitedKingdom"):
            temp_col[1] += index
            nr_uni[1]+=1
        elif (uni_country == "Germany"):
            temp_col[2] += index
            nr_uni[2]+=1
        elif (uni_country == "France"):
            temp_col[3] += index
            nr_uni[3]+=1
        elif (uni_country == "Switzerland"):
            temp_col[4] += index
            nr_uni[4]+=1
        

        f.write(",".join(lst))
        f.write('\n')
    f.close()
    for i in range(5):
        temp_col[i] /= float(nr_uni[i])

    oY += temp_col




c = []
c.append('red')
c.append('blue')
c.append('yellow')
c.append('green')
c.append('orange')

colours = [c[item] for item in oZ]

ax.scatter(oX, oY, oZ)


# labels = [item.get_text() for item in ax.get_zticklabels()]
# labels[1] = "USA"
# labels[2] = "UK"
# labels[3] = "Germany"
# labels[4] = "France"
# labels[5] = "Switzerland"
# ax.set_zticklabels(labels)


# labels = [item.get_text() for item in ax.get_xticklabels()]
# labels[1] = 2007
# labels[2] = 2008
# labels[3] = 2009
# labels[4] = 2010
# labels[5] = 2011
# labels[6] = 2012
# labels[7] = 2013
# labels[8] = 2014
# ax.set_xticklabels(labels)

for n in range(5):
    x = []
    y = []
    for i in range(8):
        y.append(oY[i*5+n])
        x.append(i)
    a, b = np.polyfit(x,y,1)
    print [b,a*8+b]
    ax.plot([0,8],[b,a*8+b],[n,n])

plt.show()