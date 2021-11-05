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
* For each function i chose to return html rather than Json for user comfort so he can have much more fun! 

* I calculated each function on the given image grayscale and not on the image itself, and that due to the     RGB image Composition; each RGB image has three channels: red, green, and blue . the function (min for example) relies on the histogram for each channel and computes the min value for each channel; but in the
assignment we asked to return the min value of the whole image, therefore i chose to work on the grayscale image.
also for the percentile function i didn't see meaning of working on the RGB image because the function returns 
the percntile according to comparition with other pixles values in one channel so it needs to be grayscale image!

* I have implemented my own error 404 handler,each for different purpose:                                     
1- if the image name is not exists on the server.                                                              
2- if the function name is wrong.                                                                            
3- if the url is not supported.                                                                               

* I wrapped everything in Class.

## Examples
1. Requests to /stats/IMG_1.jpg/min responds with the correct min value in the
   image.

2. Requests to /stats/IMG_5.jpg/average responds with 404 error code.

3. Requests to /stats/IMG_100.jpg/min responds with 404 error code
(assuming such image was not added to the bucket).


   

## multiple identical requests
in case of multiple identical requests (same image and same function) we can make it more efficient
by providing a Hash table (or DB) that stores each legal request by the user in it. so whenever the user request some request from the server we check first if the specific image and function are stored in the hash table; if so we return the stored data without the need to calculate it all over again. (in other words- caching like) 




