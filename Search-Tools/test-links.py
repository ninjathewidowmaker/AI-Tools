import subprocess


#Day 3 converted it into a function so that it can be used in other projects.
def web_scrape(url):
  command = ["links", url]
  result = subprocess.run(command, check=True, text=True)  
  return result



    
    
#Day 3 And made this into a function.    
web_scrape('https://pokemon.com')