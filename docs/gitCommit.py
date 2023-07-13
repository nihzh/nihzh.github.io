import sys
import os

if __name__ == '__main__':
    try:
        comment = sys.argv[1]
        # os.system("git remote add origin git@github.com:nihzh.github.com.git")
        os.system("git add .")
        os.system(f"git commit -m {comment}")
        os.system("git push -u origin main")
    except Exception as e:
        print("usage: python gitCommit.py [comment_to_commit]")
    print("Commit finished")
