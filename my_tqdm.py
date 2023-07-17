from time import sleep
from faker import Faker

f = Faker("en-us")
alist = [f.name() for _ in range(50)]

# Importing tqdm modules
from tqdm import tqdm, trange

'''
# use tqdm
p = 1
for i in tqdm(range(50)):  
    sleep(0.05)
'''

'''
# Information in process
proc_bar = tqdm(range(50))
p = 1
for i in proc_bar:
    proc_bar.set_description(f"computing:{i=:02d}") # Setting the leading information
    sleep(0.05)
'''

# Display Information
proc_bar = tqdm(alist)
for name in proc_bar:
    proc_bar.set_postfix({"Processing":f"{name}"})
    sleep(0.05)