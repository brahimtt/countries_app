from flask import render_template,Flask,request,url_for
import requests
import json
from api_class import GetCountry
app=Flask(__name__)
my_skills=[('html',80),('css',75),('python',95)]


@app.route("/")
@app.route("/home", methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route("/result", methods=['POST','GET']) 
def result():
    if request.method=="POST" and request.form.get("format")=="fullname":
        country=request.form.get("countryInp")
        
        tool = GetCountry()
        chosen_country = tool.each_country(country=country)
    
        return render_template("index.html", country_list=chosen_country)
    elif request.method=="POST" and request.form.get("format")=="region":
        
        region = request.form.get("countryInp")
        print(region)

        tool = GetCountry()
        country_info = tool.get_data(region=region)
        return render_template("index.html", country_list=country_info) 

 
        




    

        
    


     
     



      

    
    
    
    


    


if  __name__  == '__main__':
    app.run(debug=True,port=5001)

