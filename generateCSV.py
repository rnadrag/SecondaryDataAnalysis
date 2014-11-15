__author__ = 'vvu'
import urllib
from lxml.html import fromstring
for year in range(2005, 2015):
    f = open('data/' + str(year) + '.csv', 'w')
    url = 'http://www.shanghairanking.com/ARWU' + str(year) + '.html'
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
            if year == 2011:
                uni_name = name.getchildren()[0].text.rstrip().replace(',', '')
            else:
                uni_name = name.text.rstrip().replace(',', '')

        country_children = tr[2].getchildren()
        for country in country_children:
            if country.attrib:
                tmp_name = country.attrib['href'][:-5]
                uni_country = tmp_name[62:]

        if year == 2008:
            uni_rank = tr[3].text
        else:
            rank_children = tr[3].getchildren()
            for rank in rank_children:
                uni_rank = rank.text.rstrip()

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

        if index == "101-150" or index == "101-152" or index == "102-150" or index == "101-151":
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
        lst = [str(index), uni_name, uni_country, uni_rank, uni_total_score, uni_alumni_score]
        f.write(",".join(lst))
        f.write('\n')
    f.close()