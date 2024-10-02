class net_worth:
    def __init__(self, assets=0, liabilities=0):
        self.assets = assets
        self.liabilities = liabilities

    def calculate_net_worth(self):
        self.net_worth = self.assets - self.liabilities
        print(f"\nCurrent net worth: {self.net_worth:.2f}")

    def get_assets(self, asset):
        while True:
            try:
                total_value = 0
                assets = int(input(f"\nHow many {asset} do you have?: "))
                if assets < 1:
                    return 0
                else:
                    print(f"\nEnter the value of each asset.")
                    for i in range(assets):                        
                        self.asset_value = input(f"\n{i + 1}: $")
                        total_value += self.validate_currency(self.asset_value)
                self.assets += total_value
                print(f"\nTotal {asset} value: ${total_value:.2f}")
            except ValueError as error:
                print("\nYour entry must be a whole number!")
                continue
            break
    
    def get_liabilities(self, liability):
        while True:
            try:
                total_value = 0
                liabilities = int(input(f"\nHow many {liability} do you have?: "))
                if liabilities < 1:
                    return 0
                else:
                    print(f"\nEnter the value of each debt.")
                    for i in range(liabilities):                        
                        self.liability_value = input(f"\n{i + 1}: $")
                        total_value += self.validate_currency(self.liability_value)
                self.liabilities += total_value
                print(f"\nTotal {liability} value: ${total_value:.2f}")
            except ValueError as error:
                print("\nYour entry must be a whole number!")
                continue
            break
        
    def validate_currency(self, value):
        while True:
            try:
                value = float(value)
                return value
            except ValueError:
                value = input("\nYour entry must be a dollar ammount! $")
                continue