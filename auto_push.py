import os
import time
from datetime import datetime

while True:
    os.system("git add .")
    os.system(f'git commit -m "Auto commit: {datetime.now()}"')
    os.system("git push origin master")  # ya 'master' agar repo ka branch master ho
    print("Code auto pushed! ✅")
    time.sleep(200)  # wait 5 minutes
