import functions as f
from variables import varis
from web3 import Web3
def globulars():
    global w3,main,mains,ch_id,net,account_1,private_key1,account_2,a,maxxi,p
    account_1 = ''
    maxxi = 0
    private_key1 = ''
    account_2 = ''
    chain = 'kovan-optimism'
    mains = varis["specs"][chain]
    a,p,n = f.get_walls()
    w3 = Web3(Web3.HTTPProvider(mains['net']))
    print(w3)
    glob_str = 'w3,mains,account_1,private_key1,account_2,a,p'
    glob_strs = glob_str.split(',')
    glob_vars = w3,mains,account_1,private_key1,account_2,a,p
    print(a,p,n)
    for i in range(0,len(glob_strs)):
        f.change_glob(glob_strs[i],glob_vars[i])

f.globulars()

globulars()

def create():
    js = f.wall_check()
    ls = f.new_wall()
    f.add_wall(ls)
    return ls
ls = []
for i in range(0,50):
    ls.append(create())
    print(ls)
f.pen(ls,'Wallets.txt')
print(a,p)
