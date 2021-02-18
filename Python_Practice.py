counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registerd voters.")

voting_data = [{"county" : "Arapahoe", "registered voters" : 422829},
                {"county" : "Denver", "registered voters" : 463353},
                {"county" : "Jefferson", "registered voters" : 432438}]

for county_dict in voting_data:
        print(f"{county_dict['county']} has {county_dict['registered voters']:,} registered voters.")


   

