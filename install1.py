import imp
import subprocess
import os
user=os.environ["USER"]
subprocess.run(["bash","-c","curl -SsL https://playit-cloud.github.io/ppa/key.gpg | sudo apt-key add - && sudo curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list && sudo apt update && sudo apt install playit"])