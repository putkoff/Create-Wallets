from glob import globulars
import functions as f

f.globulars()
globulars()
js = f.exists_js('adds.txt')
a = js['adds']
p = js['priv']
f.get_new_gas()
q = input('send a txn??')
if q == 'y':
    account_1,private_key1 = f.pic_walls()
    account_2 = f.change_main()
    a,p = f.get_walls()
    glob_str  = 'account_1,private_key1,account_2,a,p'
    glob_strs = glob_str.split(',')
    glob_vars = account_1,private_key1,account_2,a,p
    for i in range(0,len(glob_strs)):
        f.change_glob(glob_strs[i],glob_vars[i])
    f.send()
q = input('did you want to send all to one wallet?')
if q == 'y':
    a = input('what is the beginning range of wallets?')
    z = input('what is the end range of wallets?')
    add,pr = f.pic_walls()
    f.send_all(str(add),int(a),int(z))
    

