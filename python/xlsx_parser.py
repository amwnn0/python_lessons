import requests, zipfile, io, openpyxl
from pathlib import Path

# download zip and extract to folder
zip_file_url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("C:\\Users\\amwnn\\Documents\\MyPythonProjects\\zip")

# parse files in folder, create list with lists [name, salary]
lst = []
p = Path("C:\\Users\\amwnn\\Documents\\MyPythonProjects\\zip")
for x in p.rglob("*"):
    wb = openpyxl.load_workbook(x)
    ws = wb.active
    lst.append([ws["B2"].value, int(ws["D2"].value)])

# create sorted list of employees in output .txt file
with open("employees.txt", "wt") as out:
    for employee in sorted(lst):
        print(*employee, file=out)
