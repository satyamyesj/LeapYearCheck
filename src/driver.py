from leap_year import is_leap_year

def main():
    print("Enter year: ")
    input_year=int(input())
    if is_leap_year(input_year):
        print("Entered year is leap year.")
    else:
        print("Entered year is not leap year.")

if __name__=="__main__":
    main()