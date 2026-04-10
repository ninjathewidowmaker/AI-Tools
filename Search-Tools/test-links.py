import subprocess

#This works only on linux. Use wsl or dual boot or shift entirely to linux


#Day 3 converted it into a function so that it can be used in other projects.
def web_scrape(url):
  command = ["links","-dump", url]
  result = subprocess.run(command, capture_output=True,check=True, text=True)  
  return result.stdout

   
#Day 3 And made this into a function.    
balla = web_scrape('https://wired.com')         
print(balla)