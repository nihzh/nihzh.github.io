import sys
import os
import datetime

if __name__ == '__main__':
    os.system("python3 d:\\文档\\nihzh.github.io\\docs\\generateSidebar.py")
    comment = ""
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            comment += i + " "
    else:
        comment = str(datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'))
    # os.system("git remote add origin git@github.com:nihzh.github.com.git")
    os.system("git add .")
    os.system(f'git commit -m "{comment}"')
    os.system("git push -u origin main")
    print("Commit finished")
