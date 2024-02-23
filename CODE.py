
#CODE OF WEBSCRPING WITH PYTHON:
import requests 
import csv
from bs4 import BeautifulSoup
def getdata(job):
 
  job_title=job.a.text.strip()
  job_url=job.a.get('href')
  posted_time=job.find('div',class_="job-age").text.strip()
  job_details=job.find('div',class_="row align-items-center mb-2")
  job_place=job.find('div',class_="col pe-0 job-locations text-truncate").text.strip()
  job_desc=job.find('div',class_="job-description")
#   print(job_title)
  #print(job_url)
  #print(posted_time)
  #print(job_desc)
  #print(job_place)
  information=[job_title,posted_time,job_desc.get_text(),job_place,"https://www.flexjobs.com"+job_url]

  return information

def main():

    total_information=[]
    url='https://www.flexjobs.com/search?search=work+from+home+part+time&location='  
    # print(len(jobs)) 
#   while True:
    r=requests.get(url)

    soup=BeautifulSoup(r.text,'html.parser')
    jobs=soup.find_all('div',class_="col-md-12 col-12")  
    for job in jobs:
        information=getdata(job)
        total_information.append(information)
    with open('results.csv','w',encoding='utf-8')as f:
        writer=csv.writer(f)
        writer.writerow(['job_title','posted_time','job_desc','job_place','job_url'])
        writer.writerows(total_information)
        
main()
