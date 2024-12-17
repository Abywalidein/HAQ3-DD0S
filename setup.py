import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("pip install wheel==0.36.2 --force-reinstall")
    os.system("pip uninstall comtypes")
    os.system("pip install --no-cache-dir comtypes")
     undetected_chromedriver")
elif c == "1":
os.system("pip install wheel==0.36.2 --force-reinstall")
    os.system("pip uninstall comtypes")
    os.system("pip install --no-cache-dir comtypes")
     undetected_chromedriver")
print("Done.")
