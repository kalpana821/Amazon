from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib .request import urlopen as urReq
import logging
import requests
from selenium import webdriver
import pandas as pd

from datetime import datetime
# filename=datetime.now().strftime('main7_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(filename='main2.log', level = logging.INFO, format=" %(asctime)s %(levelname)s %(name)s %(message)s")
app = Flask(__name__)  
@app.route('/', methods=['POST','GET'])  
def index():  
      return render_template("ama.html")  




@app.route("/review", methods=['POST','GET'])
def results():
      if request.method == "POST":
        try:
            
            
                    searchString = request.form['content'].replace(" ","")
                    # print(searchString)
                    amazon_url= "https://www.amazon.in/s?k=" + searchString
                    # logging.info(amazon_url)

                    driver=webdriver.Chrome(r"C:\Users\KALPANA\OneDrive\Desktop\chromedriver.exe")
                    driver.get(amazon_url)
                    L=bs(driver.page_source,'html.parser')
                    # logging.info(L)

                    lap_all=L.find_all('div',{'class':'s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'})
                    ama=lap_all[0].find_all('div',{'class':'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right'})
                    # logging.info(ama)

                    
                    c=lap_all[0].find_all('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})[0].a['href']
                    # logging.info(c)
                    
                    s='https://www.amazon.in/ASUS-Vivobook-16-0-inch-40-64-M1603QA-MB501WS/dp/B0B8ZT96HS/ref=sr_1_1_sspa?keywords=asus+laptop&qid=1676709247&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
                    # logging.info(s)

                    driver.get(s)
                    L1=bs(driver.page_source,'html.parser')
                    # logging.info(L1)

                    # a=bs(s,'html.parser')
                    # logging.info(a)
                    reviews=[]
                    try:
                        price=L.find_all('span',{'class':'a-price-whole'})
                        
                        # logging.info(pri)
                    except:
                          ("prive not found")
                    # logging.info(price)
                    try:
                        
                        comments=L1.find_all('div',{'class':'a-expander-content reviewText review-text-content a-expander-partial-collapse-content'})
                        
                        # print(comm)
                    except:
                      ("comments not found")
                    # logging.info(comments)
                    try:
                        name=L1.find_all('div',{'class':'a-profile-content'})
                        
                    except:
                      print("name not found")
                    # logging.info(name)

                    mydict = {"price":price,'comments':comments,"name":name}
                    reviews.append(mydict)
                    # print(reviews)

                    return render_template('amazon.html', reviews=reviews[0:len(reviews)]) 
        except:
            pass
            return render_template("amazon.html")
      else:
            return render_template("ama.html")
     
if __name__ == '__main__':  
   app.run(debug=True) 