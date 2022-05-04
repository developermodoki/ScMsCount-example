import subprocess
from subprocess import PIPE
import json

username = input("Enter the username: ")
denoEval = "deno eval 'const res=await fetch(`https://api.scratch.mit.edu/users/{}/messages/count`);console.log(JSON.stringify((await res.json())))'".format(username)
proc = subprocess.run(denoEval,shell=True,text=True,stdout=PIPE)
print(json.loads(proc.stdout))
