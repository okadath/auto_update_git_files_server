import subprocess as cmd

cp = cmd.run("git add db.sqlite", check=True, shell=True)
#print(cp)

#response = input("Do you want to use the default message for this commit?([y]/n)\n")
message = "update db.sqlite server"

#if response.startswith('n'):
#    message = input("What message you want?\n")

cp = cmd.run("git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push -f origin master ", check=True, shell=True)
