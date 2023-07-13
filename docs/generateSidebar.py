import os
import re

ptnBlankFilter = r"([|]?[ ]{2,})|(\n)"
ptnFolderFilter = r"[\+\\]-+"
folderFilter = ("img", "themes", "snippets")
extentFilter = (".png", ".json", ".css")
lastFolder = "计算机基础"

treeFile = os.popen("tree /f /a d:\\文档\\nihzh.github.io\\docs")
dirDict = dict()
folderName = ""
subFolderName = ""
flag = False

def readDictFile(dirItem, dirList):
    if isinstance(dirItem, dict):
        if (listNotEmpty:=len(dirList)) > 0:
            toWritef = ""
            for i in range(len(dirList)-1):
                toWritef += "  "
            toWritef += f"* **{str(dirList[-1])}**\n"
            f.write(toWritef)
        for keys in dirItem.keys():
            dirList.append(keys)
            readDictFile(dirItem[keys], dirList)
        if listNotEmpty:
            dirList.pop()
    elif isinstance(dirItem, list):
        fileName = dirList.pop().replace(" ", "_")
        toWrite = ""
        for i in range(len(dirList)):
            toWrite += "  "
        toWrite += f"* [{str(fileName)}]({dirList[0]}"
        for i in dirList[1:]:
            toWrite += f"/{i}"
        toWrite += f"/{str(fileName)})\n"
        #print(toWrite)
        f.write(toWrite)
        return


if __name__=='__main__':
    for row in treeFile:
        trimRow = re.sub(ptnBlankFilter, "", row)
        if trimRow.startswith("+---") or (isLast:=trimRow.startswith("\\---")) :
            folder = re.sub(ptnFolderFilter, "", trimRow)
            if folder in folderFilter or folder.startswith("."):
                continue
            if flag or row.startswith("+---"):
                folderName = ""
                subFolderName = ""
                flag = False
            if folderName == "":
                folderName = folder
                subFolderName = ""
                dirDict[folderName] = dict()
            else:
                subFolderName = folder
                dirDict[folderName][subFolderName] = dict()
            if trimRow.startswith("\\---") and folder != lastFolder:
                flag = True
        elif folderName != "" and not folderName.endswith(extentFilter):
            fileName = trimRow.replace(".md", "")
            if fileName == "":
                continue
            if subFolderName == "":
                dirDict[folderName][fileName] = []
            else:
                dirDict[folderName][subFolderName][fileName] = []
    print(dirDict)

    # os.popen("rename d:\\文档\\nihzh.github.io\\docs\\_sidebar.md _sidebar.md.old")
    with open("_sidebar.md", "w") as f:
        readDictFile(dirDict, [])
        f.close()