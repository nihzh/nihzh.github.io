import sys
import os
import datetime

if __name__ == '__main__':
    comment = ""
    for i in sys.argv[1:]:
        comment += i + " "
    # comment = str(datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'))
    # os.system("git remote add origin git@github.com:nihzh.github.com.git")
    os.system("git add .")
    os.system(f'git commit -m "{comment}"')
    os.system("git push -u origin main")
    print("Commit finished")
