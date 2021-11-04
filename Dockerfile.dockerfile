FROM python

WORKDIR /Webpage

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["python","/Webpage/SeeTree-task.py"]