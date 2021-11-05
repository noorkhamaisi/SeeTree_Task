# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:26:55 2021

@author: get-a
"""


import STATISTICS_FUNCTION as imgstatistics
from flask import Flask,render_template
from PIL import Image,ImageOps
import requests
#import time



app = Flask(__name__)

multipleRequestsDict={}




#### https://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python
#check if a URL of an image is up and exists in the bucket
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


## making multiple identical requests (same image and same function) more efficient
def FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,value,describtion):  
    global multipleRequestsDict
    multipleRequestsDict[IMAGE_FILE_NAME]={}
    multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]={}
    multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=URL
    multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["value"]=value
    multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]=describtion


@app.errorhandler(404)   
# inbuilt function which takes error as parameter to handle paths error
def not_found(e):  
  return render_template("404.html")


@app.route('/', methods=['GET'])
def HomePage():
    return render_template('home.html')


@app.route('/health',methods=['GET'])
def health():
    return render_template('health.html')




@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>',methods=['GET'])
def get_Statics(IMAGE_FILE_NAME,FUNC_NAME):
    
  #  start_time = time.time()

    if IMAGE_FILE_NAME in multipleRequestsDict.keys():
        if FUNC_NAME in multipleRequestsDict[IMAGE_FILE_NAME].keys():
         #   elapsed_time = time.time() - start_time
          #  print("multuply request: "+str(elapsed_time))
            return render_template('statistics_result.html',func=FUNC_NAME,img_url=multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["img_url"],img_name=IMAGE_FILE_NAME, value=multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["value"],describtion=multipleRequestsDict[IMAGE_FILE_NAME][FUNC_NAME]["describtion"])



   
    URL = 'https://storage.googleapis.com/seetree-demo-open/{}'.format(IMAGE_FILE_NAME) 
    #Chicking if the image exists 
    if not is_url_image(URL):          
        return render_template('imgerror_404.html')

    #### https://stackoverflow.com/questions/12020657/how-do-i-open-an-image-from-the-internet-in-pil
    myimage=Image.open(requests.get(URL, stream=True).raw)
    #Converting RGB Image to Grayscale image
    gray_image = ImageOps.grayscale(myimage) 

    
    if FUNC_NAME =='min': 
        func_describtion ="This function calculates the Min value of the pixels in the image."
        min_value=imgstatistics.Min_value(gray_image) 
       # elapsed_time = time.time() - start_time
      #  print("elapsed time: "+str(elapsed_time))
        FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,min_value,func_describtion)

        return render_template('statistics_result.html',func=FUNC_NAME,img_url=URL,img_name=IMAGE_FILE_NAME, value=min_value,describtion=func_describtion)
    
    
    elif FUNC_NAME =='max':
        func_describtion = "This function calculates the Max value of the pixels in the image."
        max_value=imgstatistics.Max_value(gray_image)
       # elapsed_time = time.time() - start_time
      #  print("elapsed time: "+str(elapsed_time))
        FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,max_value,func_describtion)
        
        return render_template('statistics_result.html',func=FUNC_NAME ,img_url=URL,img_name=IMAGE_FILE_NAME, value=max_value,describtion=func_describtion)

    elif FUNC_NAME =='mean':
        func_describtion = "This function calculates the Mean of the pixels level in the image."
        Mean_value=imgstatistics.Mean_value(gray_image)
      #  elapsed_time = time.time() - start_time
      #  print("elapsed time: "+str(elapsed_time))
        FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,Mean_value,func_describtion)

       
        return render_template('statistics_result.html',func=FUNC_NAME ,img_url=URL,img_name=IMAGE_FILE_NAME, value=Mean_value,describtion=func_describtion)

    elif FUNC_NAME =='median':
        func_describtion = "This function calculates the Median pixel level in the image."
        Median_value=imgstatistics.Median_value(gray_image)
       # elapsed_time = time.time() - start_time
       # print("elapsed time: "+str(elapsed_time))
        FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,Median_value,func_describtion)

        
        return render_template('statistics_result.html',func=FUNC_NAME ,img_url=URL,img_name=IMAGE_FILE_NAME, value=Median_value,describtion=func_describtion)

    elif FUNC_NAME[0]=='p' and FUNC_NAME[1:].isnumeric():
        if int(FUNC_NAME[1:])>=0 and int(FUNC_NAME[1:])<=100:
            func_describtion = "This function calculates the n'th Percentile of the image."
            percentile=imgstatistics.percentile_value(gray_image,int(FUNC_NAME[1:]))
        #    elapsed_time = time.time() - start_time
         #   print("elapsed time: "+str(elapsed_time))
            
            FillingDict(IMAGE_FILE_NAME,FUNC_NAME,URL,percentile,func_describtion)

            return render_template('statistics_result.html',func=FUNC_NAME ,img_url=URL,img_name=IMAGE_FILE_NAME, value=percentile,describtion=func_describtion)

        # The percentile must be between 0..100 
        else:                                                
            return render_template('funcerror_404.html')     

    else:  # The Function doesn't exists
         return render_template('funcerror_404.html')

    

        
        

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)
