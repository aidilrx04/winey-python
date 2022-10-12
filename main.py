

def main():

    daily_limit = float(input('Enter your daily limit amount: '))

    expend_amount = float(input('Enter your spending amount for today: '))
    # expend_type = str(
    # input("What did you spend your money for(e.g food/clothing): "))

    spending_val = daily_limit - expend_amount

    if spending_val < 0:
        print(":( You spent too much money today. Try again tomorrow")
    else:
        print("Good job! You spent your money wisely today :D")


if __name__ == '__main__':
    main()
