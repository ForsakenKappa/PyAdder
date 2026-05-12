import subprocess
import sys
import urllib.request
import os

print(f"Accesing as module {__name__}")

def connect(host="https://pypi.org"):
    try:
        urllib.request.urlopen(host, timeout=5)
        return True
    except:
        return False

def install_module(module_name):

    if not connect():
        print("Internet connection is not available")
        return

    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", module_name],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{module_name} installed successfully")
    else:
        print("Error occurred while installing module")
        print(result.stderr)

def prepare_directories():
    if not os.path.exists("./resources"):
        os.mkdir("./resources")

def prepare_knowledge_base():
    if os.path.isfile("./resources/knowledgeBase.xlsx"):
        print("Knowledge base found")
        return

    print("Knowledge base not found, creating...")
    wb = Workbook()
    wb.save("./resources/knowledgeBase.xlsx")
    print("Knowledge base created")

def prepare_data_base():
    if os.path.isfile("./resources/dataBase.xlsx"):
        print("Database found")
        return
    print("Database not found, creating...")
    wb = Workbook()
    wb.save("./resources/dataBase.xlsx")
    print("Database created")



if __name__ == "__main__":
    print("This script isn't suppoused to be executed seperatly!")

if __name__ == "install":

    try:
        import pyforms
    except ImportError:
        install_module("pyforms")
    
    try:
        import openpyxl
    except ImportError:
        install_module("openpyxl")

    from openpyxl import Workbook
    prepare_directories()
    prepare_knowledge_base()
    prepare_data_base()
    print("Installation is complete")

