import csv
import matplotlib.pyplot as plt

with open('Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))

def dataTypeConversion(rawList, dataType):
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            convertedList.append(previousValue) # replacing missing value with previous value
    return convertedList

def typeConversion(rawList, dataType):
  	mylist = []
  	for x in range(len(rawList)):
  		mylist.append(dataType(rawList[x]))
  	return mylist



  ##This function recives 3 things
  # 1) Whole_Data_List  2)Required_Data_Column 3) Required_Item(data)
  # At the end it return a list having all the indices of required_data

def fetchIndices(data, columnIndex, searchItem):
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)
    return listRowIndices



def fetchColumnData(data, columnIndex, hasHeader):
    listData = []
    for i in range(len(data)):
        listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData


def rankThisCountry(targetCountry):
    for indicatorName in indicators:
        if indicatorName in maxStateFactList:
            rankThisIndicator_max(targetCountry, indicatorName)
        elif indicatorName in minStateFactList:
            rankThisIndicator_min(targetCountry, indicatorName)

def rankThisIndicator_max(targetCountry, targetIndicator):
    temp = avgDictOfIndicators[(targetCountry, targetIndicator)] 
    avg = avgDictForAllIndicators[targetIndicator]

    if temp < avg/2: #If the indicator is in low state (BAD STATE)
        rankDict[(targetCountry, targetIndicator)] = 25
          # FAIR STATE (NEED IMPROMENT)
    elif temp >= avg/2 and temp <= avg:
        rankDict[(targetCountry, targetIndicator)] = 45
        # GOOD STATE (Above the average)        
    elif temp > avg and temp < (avg*2):   
        rankDict[(targetCountry, targetIndicator)] = 65.4
           #INDICATOR IS IN MAX(best) STATE
    elif temp > (avg*2):
        rankDict[(targetCountry, targetIndicator)] = 90

def rankThisIndicator_min(targetCountry, targetIndicator):
    temp = avgDictOfIndicators[(targetCountry, targetIndicator)] 
    avg = avgDictForAllIndicators[targetIndicator]

        #INDICATOR IS IN DANGER STATE "i.e. Co2 Emmission is HIGH"
    if temp < avg/2: 
        rankDict[(targetCountry, targetIndicator)] = 85
        #FAIR STATE  (NOT GOOD)
    elif temp >= avg/2 and temp <= avg: 
        rankDict[(targetCountry, targetIndicator)] = 60.4
        # ABOVE AVERAGE (GOOD)
    elif temp > avg and temp < (avg*2):
        rankDict[(targetCountry, targetIndicator)] = 45
        #WE CAN SAY BEST STATE "i.e. Very low Co2 EMMISSION"
    elif temp > (avg*2): 
        rankDict[(targetCountry, targetIndicator)] = 20





## This function recives 3 values
# 1)Whole_data_list   2)required_data_column 3)List_of_all indices(row)[returned by fetchIndecies Function]
# At result it return list contains all the DATA of recived country indices and indicator

def fetchDataYears(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
    return listDataValues

paksitanIndices = fetchIndices(data,0,'Pakistan')
#print(paksitanIndices)

years = dataTypeConversion(fetchDataYears(data,4,paksitanIndices),int)

countries = set(fetchColumnData(data,0,True))


#This list contains all the indicators names
#Indicators starts from 6 to onwards 55
indicators = data[0][6:]

#This is the countries dictionary
countriesDict = {}

#This first for loop will goes upto the last country in the country list

for countryName in countries:
    countryIndices = fetchIndices(data,0,countryName) #This will return a list that contains all the index of the countryName
    for indicatorName in indicators:
    	#In the 2nd for loop, we fetch DataYears list of each Indicator and convert it into float
    	#We are giving a tupple as a key to dictionary, and each value against evry contains 16 entries (a list)
        countriesDict[(countryName,indicatorName)] = dataTypeConversion(fetchDataYears(data,data[0].index(indicatorName),countryIndices),float)
#We feed all the data into Dictionary that key is a tupple of two values [countryName, IndicatorName] and each Value contains
# 16 records(a list)



#Below 2 for loops will help to undertsand the structure of dictionary very very easily :)

#for countryName in countries:
#	print(" ")
#	print(" ")
#	print("Country Name : " + countryName)
#	print(" ")
#	print(" ")
#	for indicatorName in indicators:
#		print("indicatorName : " + indicatorName)
#		print(countriesDict[(countryName, indicatorName)])


#print(sum(countriesDict[('Norway','DemocracyScore')])/len(years))
#print(sum(countriesDict[('Norway','EnergyUsePerPerson')])/len(years))
#print(sum(countriesDict[('Norway','Exports')])/len(years))
#print(sum(countriesDict[('Norway','Femalesaged25to54labourforceparticipationrate')])/len(years))
#print(sum(countriesDict[('Norway','Imports')])/len(years))
#print(sum(countriesDict[('Norway','Taxrevenue')])/len(years))
#print(sum(countriesDict[('Norway','YearlyCO2emission')])/len(years))


# This Dictionary will contain all the avrages of INDICATorS
avgDictOfIndicators = { }
rankDict = { }
for countryName in countries:
    for indicatorName in indicators:
		avgDictOfIndicators[(countryName,indicatorName)]= sum(countriesDict[(countryName, indicatorName)])/len(years)
    #rankThisCountry(countryName, avgDictOfIndicators)
    #Here we get the AVERAGE of all INDICAORS IN A SINGLE DICTIONARY
    #Now we would rank that country according to these indicators

avgDictForAllIndicators = { }
for indicatorName in indicators:
    avg = 0
    for countryName in countries:
        avg = avg + avgDictOfIndicators[(countryName, indicatorName)]
    avgDictForAllIndicators[indicatorName] = (avg/len(countries))

##################################################################################################
##################################################################################################
#Now Some inddicators should be in MAX state for the better future of country as well as the world
#Like incomePerPerson, TotalGDP, Exports, DemocracyScore, ForestArea, Agricultural Land and so many others.
##################################################################################################
#While some indicators should be in MIN state for good future
#Like Co2 Emission, GrowthRate, EnergyUsage and many other factors.

#Now we are dividing the whole indicators list into two categories
# 1) That should be in MAX state (for bright future of country)
# 2) That should be in MIN state (for bright future of country)

minStateFactList = []
maxStateFactList = []

for indicatorName in indicators:
    if indicatorName in ("YearlyCO2emission", "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity", "Populationtotal", "Populationgrowth", "  Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Longtermunemploymentrate", "Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
        minStateFactList.append(indicatorName)
    else:
        maxStateFactList.append(indicatorName)
#maxStateFactList.pop(-1)

#Here we divide both the indicators in two categoreis////
#Now we are ranking the countires

for countryName in countries:
    rankThisCountry(countryName)



#c=0 #checking for below average countries
#for countryName in countries:
#    for indicatorName in indicators:
#        if indicatorName == "IncomePerPerson":
#            if avgDictOfIndicators[(countryName, indicatorName)] < avgDictForAllIndicators["IncomePerPerson"]:
#                print(countryName)
#                c+=1


########################################################################################
print("")
print(" ___________________________________________________________________________________________________")
print("|                                       PROJECT OVERVIEW                                            |")
print("|___________________________________________________________________________________________________|")
print("|  In this dataScience project, we are given a large data set, containing records of 65 years. The  |")
print("|  Data set contains 50 different FACTORS that gives information about the status of country. This  |")
print("|  Program Rank all the countires according to the factors score/value. Remember, We Divide the     |")
print("|  Factors into two main categories having different ranges. Some factors should be at MAX state    |")
print("|  for the bright future of country while some should be at MIN state(HAZARDIOUS).                  |")
print("|___________________________________________________________________________________________________|")
print("\n")

print(" ___________________________________________________________________________________________________")
print("|                                       FINAL RESULTS                                               |")
print("|___________________________________________________________________________________________________|")
print("\n\n")
#Final Ranking
pointsTotal  =  5000
for countryName in countries:
    pointsGained = 0
    for indicatorName in indicators:
        pointsGained+=rankDict[(countryName, indicatorName)]
        pointsTotal+=100
    rankDict[countryName]=(float(pointsGained)/ 5000)*100

avg_score = 0
max_score = 0
min_score = 1000000
for countryName in countries:
  #  print(countryName + "  "+ str(rankDict[countryName]))
    avg_score+=rankDict[countryName]
    if min_score > rankDict[countryName]:
        min_score = rankDict[countryName]
    if rankDict[countryName] > max_score:
        max_score = rankDict[countryName]
avg_score = avg_score / len(countries)
print("After whole calculations, Countries score statistics")
print("\nAVG SOCRE : " + str(avg_score))
print("MAX SCORE : " + str(max_score) + "                [Out of 100]")
print("MIN SCORE : " + str(min_score) + " \n")

Grade_A = []
Grade_B = []
Grade_C = []
Grade_D = []
for countryName in countries:
    if rankDict[countryName] > float((max_score - avg_score)/2)+avg_score:
        Grade_A.append(countryName)
    if rankDict[countryName] > avg_score and rankDict[countryName] < float((max_score - avg_score)/2) + avg_score:
        Grade_B.append(countryName)
    if rankDict[countryName] > ((avg_score - min_score)/2)+min_score and rankDict[countryName] < avg_score:
        Grade_C.append(countryName)
    if rankDict[countryName] < ((avg_score - min_score)/2)+min_score:
        Grade_D.append(countryName)

print("Countries in Grade A : " + str(len(Grade_A)) + " (Top Countries)")
print("Countries in Grade B : " + str(len(Grade_B))) + " (above the average)"
print("Countries in Grade C : " + str(len(Grade_C)) + " (Below average But good enough, majority lies there)")
print("Countries in Grade D : " + str(len(Grade_D)) + " (Bottom level)\n\n")
#print("Total Countries : " + str(len(Grade_A) + len(Grade_B) + len(Grade_C) + len(Grade_D)))

# Top 10 countries

#You can change the LIST NAME AND NO OF COUNTRIES TO BE PRINTED
ShowGrade = Grade_A
listName = "Grade_A"
countryCount = 10




temp = []
for countryName in ShowGrade:
    temp.append(rankDict[countryName])


#No of countries you want to print

topTenCountries = []
topTenCountriesName = []
count = 0
for countryName in ShowGrade:
    if count == countryCount+1:
        break
    mx = max(temp)
    topTenCountries.append(mx)
    temp.remove(mx)
    count+=1

i=0
for countryName in ShowGrade:
    if i==(countryCount):
        break
    for countryName in ShowGrade:
        if rankDict[countryName] == topTenCountries[i]:
            topTenCountriesName.append(countryName)
            i+=1
            break



lab = " "
if listName=="Grade_A":
    lab = "TOP" 
else:
    lab = "BelowTop"

if lab=="TOP":
    print("\n __________________________________________________________________________________________________")
    print("|        |        |          |      TOP "+str(countryCount)+" COUNTRIES LIST        |           |           |         |")
    print("|________|________|__________|___________________________________|___________|___________|_________|")
else:
    print("\n __________________________________________________________________________________________________")
    print("|        |        |          | "+lab+" "+str(countryCount)+" COUNTRIES LIST        |           |           |         |")
    print("|________|________|__________|___________________________________|___________|___________|_________|")


print("\n")
plist = []
for i in topTenCountries:
    if i not in plist:
        plist.append(i)

plist2 = []
for i in topTenCountriesName:
    if i not in plist2:
        plist2.append(i)

index=0
for i in plist2:
    print( ":-->   " + i +"            \t     (score: "+ str(plist[index])+ ")")
    index+=1
print("\n ____________________________________________________________________________")
print("|      Project Parthners: |       Saif & Wisha                               |")
print("|_________________________|__________________________________________________|")
#for indicatorName in indicators:
#    plt.figure()
#    plt.plot(years, countriesDict[('Pakistan',indicatorName)], 'green', label="Pakistan")
#    plt.plot(years, countriesDict[('India',indicatorName)], 'red', label="India")
#    plt.plot(years, countriesDict[('United States of America',indicatorName)], 'blue', label="USA")
#    plt.plot(years, countriesDict[('China',indicatorName)], 'black', label="China")
#    plt.plot(years, countriesDict[('Somalia',indicatorName)], 'orange', label="Somalia")
#    plt.plot(years, countriesDict[('Bangladesh',indicatorName)], 'yellow', label="Bangladesh")
#    plt.plot(years, countriesDict[('United Kingdom',indicatorName)], 'cyan', label="UK")
#    plt.plot(years, countriesDict[('Norway',indicatorName)], 'magenta', label="Norway")
#    plt.title(indicatorName)
#    plt.legend(loc="best")

#plt.show()
