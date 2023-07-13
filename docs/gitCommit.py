import sys
import os
import datetime

if __name__ == '__main__':
    comment = ""
    try:
        comment = sys.argv[1]
    except Exception as e:
        comment = str(datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'))
        print(f'No argument, the comment will be "{comment}"')
    # os.system("git remote add origin git@github.com:nihzh.github.com.git")
    os.system("git add .")
    os.system(f"git commit -m {comment}")
    os.system("git push -u origin main")
    print("Commit finished")
