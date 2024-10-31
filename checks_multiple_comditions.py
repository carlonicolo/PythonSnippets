filenames = ["car.xlsx", "trains.xls",
             "cities.py"]

xls_filenames = [
    file
    for file in filenames
    if file.lower().endswith((".xlsx",".xls",".xlsm"))
    ]

print(xls_filenames)