from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
search = input("search for : ")
# search = "orange"
params = {"q":search}
r = requests.get("http://www.bing.com/images/search" , params=params)

soup = BeautifulSoup(r.text , "html.parser")

links = soup.findAll("a", {"class":"iusc"})
print("number of found images is: " , len(links))
string = " "
try:
  dir = str(search)
  parent_dir = "./image/"
  path = os.path.join(parent_dir, dir)
  os.mkdir(path)
  print("Directory '% s' created" % dir)
except IOError:
  print("file exist ...")
  pass
progress = ""
for link in links:
  try:
    image_url = link.attrs['m'].split(",")[2].split('"')[3]
    filename =image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    progress+="-"
    print(f"progress bar: {progreaa}")
    # image = requests.get(r.url, stream = True)
    img = Image.open(BytesIO(r.content))

    img.save(path +"/" + filename , img.format)
  except IOError:
    print("Ooops there is an error")