from json import load
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)
#print no of countries

#print(len(data))

#print all country name

all_country_names=[country.get("name") for country in data]

#print(all_country_names)

#print allregions

all_regions=[country.get("region") for country in data]

#print(set(all_regions))
region_count={region:all_regions.count(region) for region in all_regions}
#print(region_count)

#print maximum region count 

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))

#capital of aspecific country

#capital of india

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

#print(country_capital)

#countries with most number of boarders

country_borders={country.get("name"):len(country.get("borders",[]))for country in data}

#print(country_borders)

#max_border_country

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_border_country)

max_border_count=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
#print(max_border_count)

#most populated country

most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")

#print(most_populated_country)

alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="afghanisthan"]

for code in alpha_three_codes:
    for country in data:
        if country.get("alpha3code")==code:
            print(country.get("name"))

