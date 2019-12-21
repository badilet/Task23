# Напишите функцию котрый будет определять введенный год, високосный или нет.

year = int(input("Enter a year:"))

def year_type():
    if year % 4 == 0:
        print("This is a leap year!")
    else:
        print("This is not a leap year!")
year_type()
