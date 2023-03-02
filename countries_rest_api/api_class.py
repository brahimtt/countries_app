import requests


class GetCountry:
    def __init__(self):
        self.my_api = "https://restcountries.com/v3.1/region/"
        self.country_api = "https://restcountries.com/v3.1/name/"
        

    def get_data(self, region):
        respond = requests.get(url=f"{self.my_api}{region.lower()}")
        data = respond.json()
        resulte = []
        for country in data:
            try:
                answer = {
                    "name": country["name"]["common"],
                    "population": country["population"],
                    "region": country["region"],
                    "capital": country["capital"][0],
                    "flag": country["flags"]["png"]
                }
                resulte.append(answer)
            except KeyError:
                pass

            
                
        return resulte

    def each_country(self, country):
        respond = requests.get(url=f"{self.country_api}{country.lower()}")
        
        data = respond.json()
        result=[]
        for country in data :
            answer = {
            "name": country["name"]["common"],
            "population": country["population"],
            "region": country["region"],
            "sub_region": country["subregion"],
            "capital": country["capital"][0],
            "flag": country["flags"]["png"]

        }
            result.append(answer)
        
        return result
           
            
        
        
