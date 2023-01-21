# Calculate Depreciation of Value


cost_of_asset = int(input('Ammount of cost ofasset '))
salvage_value = int(input("salvage_value"))
useful_life = int(input("useful_life"))

depreciation = (cost_of_asset - salvage_value) / useful_life
print(depreciation)