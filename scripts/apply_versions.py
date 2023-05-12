import sys
import os

os.chdir(f"{os.path.dirname(__file__)}/..")

try:

    sys.path.append("wingetui")

    from versions import *


    def fileReplaceLinesWith(filename: str, list: dict[str, str], encoding="utf-8"):
        with open(filename, "r+", encoding=encoding, errors="ignore") as f:
            data = ""
            for line in f:
                match = False
                for key, value in list.items():
                    if (line.startswith(key)):
                        data += f"{key}{value}"
                        match = True
                if (not match):
                    data += line
            f.seek(0)
            f.write(data)
            f.truncate()


    fileReplaceLinesWith("WingetUI.iss", {
        "#define MyAppVersion": f" \"{versionName}\"\n",
        "VersionInfoVersion=": f"{versionISS}\n",
    }, encoding = "utf-8-sig")

    fileReplaceLinesWith("wingetui-version-file", {
        "      StringStruct(u'FileVersion'": f", u'{versionName}'),\n",
        "      StringStruct(u'ProductVersion'": f", u'{versionName}'),\n",
    })
    print("done!")
except Exception as e:
    print(e)