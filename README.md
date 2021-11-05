# Seetree Junior SW engineer task

Hello , and welcome to my Webserver that handles calculation of image statistics.
In this assignment we implemented a Flask webserver that handles calculation of image statistics. For a given image we calculate the : min,max,mean,median and percentile values.

## Before starting Please make sure that you have
* python
* Docker
* Git


## Installatin and Setup
Open the Command Prompt and Clone the reposotory using the following command 
```bash
https://github.com/noorkhamaisi/SeeTree_Task.git
```

## Running localy using Flask
Open the Command Prompt and make sure that you are in the SeeTree_Task folder .
To start the webserver, run the following commands :
```bash
py -m pip install -r requirements.txt
```
```bash
set FLASK_APP=main_seetree.py
```
```bash
python -m flask run 
```

Finally go to  https://127.0.0.1:5000 on your browser and strat your navigation . 

## Running localy using Dockerfile

Open the Command Prompt and make sure that you are in the SeeTree_Task folder .
 To start the webserver,Please run the following commands :
  

`
Bulding the image from the Dockerfile
`
```bash
docker build -t imagestatistics .
```


`
Running the conatiner and on port:5000
`
```bash
docker run -d -p 5000:5000 imagestatistics
```
Finally go to  https://127.0.0.1:5000 on your browser and strat your navigation . 

## pulling the conatiner from dockerhub and running localy

Open the Command Prompt , run the following commands :

`
Pulling the image from dockerhub`
```bash
docker pull noorkhamaisi/imagestatistics:V0.1
```

`
running the image 
`
```bash
docker run -d -p 5000:5000 noorkhamaisi/imagestatistics:V0.1
```

Finally go to  https://127.0.0.1:5000 on your browser and strat your navigation .

## Supported URLs
you can use those urls:
* http://127.0.0.1:5000
  is the home page of the Webserver
* http://127.0.0.1:5000/health
   returns OK to any request.
* http://127.0.0.1:5000/stats/IMAGE_FILE_NAME/FUNC_NAME
  while IMAGE_FILE_NAME is the Image name and FUNC_NAME is the required function. 

## Explanation
My Webserver calculates FUNC_NAME on the pixels of given IMAGE_FILE_NAME and return the result.
 Supported FUNC_NAMES are:
1. min:                                                                                                      
returns the Minimum value of the image pixles.                                                                      
This relies on the histogram() method, and simply returns the low and high bins used.                          
2. max:                                                                                                        
returns Maximum value of the image  pixels.                                                                     
This relies on the histogram() method, and simply returns the low and high bins used.                         
3. mean:                                                                                                       
returns Average (arithmetic mean) pixel level for each band in the image.                                                  
4. median:                                                                                                     
returns Median pixel level in the image.                                                                       
5.  pXXX where XXX is a percentile between 0...100 :                                                           
For example p10 is the 10th percentile of the image, p99 is the 99th percentile
returns a value that a certain percentage of a set of values (p%) is lower than it.     




## Implementation
* Because our images are in RGB format, so each image compose of three chanels - red ,green,blue .
therefore , i calculate every function from the supported , on the given grayscale image (the RGB image converted to grayscale) and not on the RGB image itself.
the mean function for example calculates the Average (arithmetic mean) pixel level for each chanel in the image. so i deciced to compute the mean of the grayscale image to get the mean value for the whole image . 
the supported functions is calculated using pillow library in python 
https://pillow.readthedocs.io/en/stable/reference/ImageStat.html 
 while the percntile function is computed by the percntile function in numpy library 


* For each function from the supported i return html file with the  matching result , for example : 
![C:\Users\get-a\Desktop\DevOpsCourse\SeeTree_Task\images\result.PNG](C:\Users\get-a\Desktop\DevOpsCourse\SeeTree_Task\images\result.PNG)

* If the function name is wrong - i have implemented a special 404 error handler , for example "
![functionerror](..\images\functionerror.PNG)

* If the image name is wrong - i have implemented a special 404 error handler , for example : 
![imageerror.PNG](..\images\imageerror.PNG)

* If the path is wrong and we have unspported URL we have 404 error unfound page      
![pagenotfound](..\images\404error.PNG)                                                                                                                                                       

## Examples
1. Requests to /stats/IMG_1.jpg/min responds with the correct min value in the
   image.

2. Requests to /stats/IMG_5.jpg/average responds with 404 error code.

3. Requests to /stats/IMG_100.jpg/min responds with 404 error code
(assuming such image was not added to the bucket).


   

##  Multiple identical requests
If we have a multiple identical requests (same image and same function) I can make it more efficient,
by saving a Dictionary that stores all the previous supported requests . so 
when the user request a supported service (after checking IMG_FILE_NAME  and FUNC_NAMES ) I check first if the specific image and function are stored in my Dictionary ; if so I return the stored data without the need to calculate it  again. 




