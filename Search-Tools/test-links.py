import subprocess

# Define the command as a list for better security and reliability
url = "" #Enter the url
command = ["links", url]  


result = subprocess.run(command, check=True, text=True)
    
    
#Alright this is day 2 of my expirement with the GitHub contributions.    