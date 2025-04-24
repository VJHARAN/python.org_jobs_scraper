import requests as req
from bs4 import BeautifulSoup

url="https://www.python.org/jobs/"
page=req.get(url)

user_input=input("Enter job keyword to search:")

soup=BeautifulSoup(page.content,'html.parser')
main_content=soup.find('div',class_='row')
job_lists=main_content.find_all('a',string=lambda text: user_input in text.lower())
job_details=[anchor.parent.parent.parent for anchor in job_lists]

count=0
for job in job_details:
    count+=1
    title_element=job.find('span',class_='listing-company-name')
    print(f'#{count}>>\t\t{title_element.text.strip()}')
    link=job.find('a')['href']
    print(f'\t\tApply here:  https://www.python.org{link}\n')

  
