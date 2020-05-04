
# Now we have all the averages Of each indicators in this dictionary


avgSalaryList = []
avgDictOfIndicators["Pakistan", "IncomePerPerson"] = 15365.89
for countryName in countries:
	for indicatorName in indicators:
		if indicatorName == "IncomePerPerson":
#			print(countryName + "   : " + str(avgDictOfIndicators[(countryName, indicatorName)]))
			avgSalaryList.append(avgDictOfIndicators[(countryName, indicatorName)])

print("*****************************************")
print("      IncomePerPerson Info")
print("*****************************************")

AVERAGE = sum(avgSalaryList)/len(countries)
print("average Income : " + str(sum(avgSalaryList)/len(countries)))
belowAVG = 0


mn = 100000
for x in avgSalaryList:
    if mn > x and x != 0:
        mn = x
    if x < AVERAGE:
        belowAVG +=1
print("Countries Below AVERAGE : " + str(belowAVG))
print("Aountries Above AVERAGE : " + str(len(avgSalaryList)-belowAVG))
print("MAX SALARY : " + str(max(avgSalaryList)))
print("MIN SALARY : " + str(mn))
print("PAKISTAN INCOME PER PERSON : " + str(avgDictOfIndicators["Pakistan", "IncomePerPerson"]) + " (Just above the average)")
print("*****************************************")
print("*****************************************")
print("             Ranking Scheme on the basis of IncomePerPerson")
print("******************************************")
print("IncomePerPerson   NumOfCountries     Rank Points ")
print("0   -   5000            89              10")
print("5000.1 -10000           38              20")
print("10000.1-15000           32              30")
print("15000.1-20000           12              40")
print("20000.1-25000           10              50")
print("25000.1-30000           9               60")
print("30000.1-35000           7               70")
print("35000.1-40000           7               80")
print("40000.1-above           23              100")

#count=0
#for x in range(len(avgSalaryList)):
#    if avgSalaryList[x] >40000:# and avgSalaryList[x] <=40000: 
#          print(avgSalaryList[x])
#          count+=1
#print(count)

rankDict = { }
ind = "IncomePerPerson"
for countryName in countries:
    val = avgDictOfIndicators[(countryName, ind)]
    if val >=0 and val <= 5000:
        rankDict[(countryName, ind)] = 10
    if val >5000 and val <=10000:
        rankDict[(countryName, ind)] = 20
    if val >10000 and val <=15000:
        rankDict[(countryName, ind)] = 30
    if val >15000 and val <=20000:
        rankDict[(countryName, ind)] = 40
    if val >20000 and val <=25000:
        rankDict[(countryName, ind)] = 50
    if val >25000 and val <=30000:
        rankDict[(countryName, ind)] = 60
    if val >30000 and val <=35000:
        rankDict[(countryName, ind)] = 70
    if val >35000 and val <=40000:
        rankDict[(countryName, ind)] = 80
    if val >40000 :
        rankDict[(countryName, ind)] = 100


#Below is the testing code the Rank Dictionary   
#c=0
# Now we are Going to compute statitics about Democrasy Score
#for countryName in countries:
#    for indicatorName in indicators:
#        if indicatorName =="IncomePerPerson":
#            if rankDict[countryName, indicatorName] ==100:
#                c+=1
#print(c)


##########################################
####################################################
#Ranking on the Basis of Democrasy Score

AVERAGE_CO2_EMISSION = 0
MAX_VALUE = 0
MIN_VALUE = 10000000

for countryName in countries:
    for indicatorName in indicators:
        temp = avgDictOfIndicators[(countryName, indicatorName)]
        if temp > MAX_VALUE:
            MAX_VALUE = temp
        if temp < MIN_VALUE and temp>0:
            MIN_VALUE = temp
        AVERAGE_CO2_EMISSION = AVERAGE_CO2_EMISSION + temp
AVERAGE_CO2_EMISSION = AVERAGE_CO2_EMISSION / len(years)

print("\n\n       Yearly CO2 emission Info \n")
print("AVERAGE Co2 Emmissions : " + str(AVERAGE_CO2_EMISSION))
print("Maximum Co2 Emission  : " + str(MAX_VALUE))
print("Manimum co2 Emission  : " + str(MIN_VALUE))

mx = 0
mn = 1000000000
for countryName in countries:
    for indicatorName in indicators:
        if indicatorName=="Forestarea":
            if avgDictOfIndicators[(countryName, indicatorName)] > mx:
                mx = avgDictOfIndicators[(countryName, indicatorName)]
            if avgDictOfIndicators[(countryName, indicatorName)] < mn and avgDictOfIndicators[(countryName, indicatorName)]!=0:
                mn = avgDictOfIndicators[(countryName, indicatorName)]

def getForestValue(cname, indname):
    if avgDictOfIndicators[(cname, indname)] > 1000000:
        return 10
    if avgDictOfIndicators[(cname, indname)] > 1500000:
        return 20
    if avgDictOfIndicators[(cname, indname)] < 1000000:
        return 5


for countryName in countries:
    for indicatorName in indicators:
        if indicatorName == "DemocracyScore":
            var = avgDictOfIndicators[(countryName, indicatorName)]
            if var == 10:
                rankDict[countryName, indicatorName] = 20
            if var == 6:
                rankDict[countryName, indicatorName] = 15
            if var == 4:
                rankDict[countryName, indicatorName] = 10
            if var == 2:
                rankDict[countryName, indicatorName] = 5
            if var <=0:
                rankDict[countryName, indicatorName] = 0
        if indicatorName == "YearlyCO2emission":
            var = avgDictOfIndicators[(countryName, indicatorName)]
            if var in range(int(AVERAGE_CO2_EMISSION+10000), int(AVERAGE_CO2_EMISSION-10000)):
                fr = getForestValue(countryName, indicatorName)
                rankDict[countryName, indicatorName] = 40 + fr 
            if var > (AVERAGE_CO2_EMISSION+10000):
                fr = getForestValue(countryName, indicatorName)
                rankDict[countryName, indicatorName] = 80 + fr
            if var < (AVERAGE_CO2_EMISSION-10000):
                fr = getForestValue(countryName, indicatorName)
                rankDict[countryName, indicatorName] = 20 + fr 
            if var == 0:
                rankDict[countryName, indicatorName] = 0
