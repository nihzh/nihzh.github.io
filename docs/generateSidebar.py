import os
import re

ptnBlankFilter = r"([|]?[ ]{2,})|(\n)"
ptnFolderFilter = r"[\+\\]-+"
folderFilter = ("img", "themes", "snippets", "蚁景网安夏令营")
extentFilter = (".png", ".json", ".css")
lastFolder = "计算机基础"


def readDictFile(dirItem, dirList, f):
    if isinstance(dirItem, dict):
        if (listNotEmpty:=len(dirList)) > 0:
            toWritef = ""
            for i in range(len(dirList)-1):
                toWritef += "  "
            toWritef += f"* **{str(dirList[-1])}**\n"
            f.write(toWritef)
        for keys in dirItem.keys():
            dirList.append(keys)
            readDictFile(dirItem[keys], dirList, f)
        if listNotEmpty:
            dirList.pop()
    elif isinstance(dirItem, list):
        file = dirList.pop()
        pathName = file.replace(" ", "%20")
        fileName = file.replace(" ", "_").replace("`", "\`")
        toWrite = ""
        for i in range(len(dirList)):
            toWrite += "  "
        toWrite += f"* [{str(fileName)}]({dirList[0]}"
        for i in dirList[1:]:
            toWrite += f"/{i}"
        toWrite += f"/{str(pathName)})\n"
        # print(toWrite)
        f.write(toWrite)
        return

def generateDictFile(dirDict):
    treeFile = os.popen("tree /f /a d:\\文档\\nihzh.github.io\\docs")
    folderName = ""
    subFolderName = ""
    # 是否最后一个文件夹
    flag = False
    # 当前文件夹是否要过滤
    isToFilt = False

    for row in treeFile:
        trimRow = re.sub(ptnBlankFilter, "", row)
        # 读到目录
        if trimRow.startswith("+---") or (isLast:=trimRow.startswith("\\---")) :
            folder = re.sub(ptnFolderFilter, "", trimRow)
            # 不是总最后一个文件夹（返回上一级）
            if flag or row.startswith("+---"):
                folderName = ""
                subFolderName = ""
                flag = False
            # 当前目录最后一个文件夹，且不是总目录最后一个，下次读到目录时返回上一级
            if trimRow.startswith("\\---") and folder != lastFolder:
                flag = True
            # 需要过滤的文件夹
            if folder in folderFilter or folder.startswith("."):
                isToFilt = True
                continue
            # 当前文件夹为空，填入当前文件夹
            if folderName == "":
                folderName = folder
                subFolderName = ""
                dirDict[folderName] = dict()
            # 有当前文件夹，填入子文件夹
            else:
                subFolderName = folder
                dirDict[folderName][subFolderName] = dict()
            # 读取过文件夹，即不需要过滤
            isToFilt = False
        # 读到文件
        elif folderName != "" and not folderName.endswith(extentFilter):
            if isToFilt:
                continue
            fileName = trimRow.replace(".md", "")
            if fileName == "":
                continue
            if subFolderName == "":
                dirDict[folderName][fileName] = []
            else:
                dirDict[folderName][subFolderName][fileName] = []
    print(dirDict)

if __name__=='__main__':
    dirDict = dict()
    generateDictFile(dirDict)
    # os.popen("rename d:\\文档\\nihzh.github.io\\docs\\_sidebar.md _sidebar.md.old")
    with open("_sidebar.md", "w", encoding="utf-8") as f:
        readDictFile(dirDict, [], f)
        f.close()
    print("Generate successfully.")