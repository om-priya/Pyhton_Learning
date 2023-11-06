import time
from lib.api_call import HandleApi

APIID = "1be0554af3864a54b01c3ed2db72aa5f"

my_obj = HandleApi(APIID)

start = time.time()
value_in_usd = int(input("Enter the value in USD: "))
value_in_gbp = my_obj.convert_value(value_in_usd)

print(value_in_gbp)
print(f"the function took {time.time() - start}")

# Another One
start = time.time()
value_in_usd = int(input("Enter the value in USD: "))
value_in_gbp = my_obj.convert_value(value_in_usd)

print(value_in_gbp)
print(f"the function took {time.time() - start}")

# Another One
start = time.time()
value_in_usd = int(input("Enter the value in USD: "))
value_in_gbp = my_obj.convert_value(value_in_usd)

print(value_in_gbp)
print(f"the function took {time.time() - start}")
