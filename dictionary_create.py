with open ('D:\python\quizbot\capitals.txt') as p:
    lines = [line.rstrip().split(' 	') for line in p]

country_capitals_dict = {}
countries = []
capitals = []
for i in lines:
    country_capitals_dict[i[0].rstrip()] = i[1].rstrip()
    countries.append(i[0])
    capitals.append(i[1])

