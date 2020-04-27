import subprocess as cmd
from  time import sleep
while True:
	try:
		sleep(30)
		cp = cmd.run("git add .", check=True, shell=True)
		message = "update the repository"
		cp = cmd.run("git commit -m '{message}'", check=True, shell=True)
		cp = cmd.run("git push -u origin master -f", check=True, shell=True)
	except Exception as e:
		pass
