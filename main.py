from net_worth import *

assets = ["bank accounts", "investment accounts", "crypto currency accounts", "properties", "vehicles", "other assets"]
liabilities = ["credit card debts", "car loans", "student loans", "mortgages", "other debts"]

def main():
    user = net_worth()
    print("\nEnter your assets and liabilities when prompted to calculate your net worth.")
    for asset in assets:
        user.get_assets(asset)
    for liability in liabilities:
        user.get_liabilities(liability)
    user.calculate_net_worth()
    

if __name__ == '__main__':
    main()