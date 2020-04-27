import subprocess as cmd

cp = cmd.run("git add .", check=True, shell=True)
#print(cp)

message = "update the repository"

cp = cmd.run("git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push -u origin master -f", check=True, shell=True)
