# Installation Requirements
```
pip install zeus
```

# How to use


```
from zeus import ZYS

x = ZYS()

zys = x.get_info(user.id)
print(x)
print(x.reason)

```


# How to add Auto ban Code?

Add This Code on Your Gban Module check_and_ban

```
    x = ZYS()
    zys = x.get_info(int(user.id))
    
    if not zys['blacklisted']:
            return        
    else:
                chat.kick_member(user_id)
                reason , enf , user = zys['reason'] , zys['enforcer'] , zys['user']
                print(reason)
 ```
 
 #Show User is Banned or not in user information
 
 ```
 try:
        x = ZYS()
        zys = x.get_info(int(user.id))
        if not zys['blacklisted']:
                pass
        else:
                 
                if zys:
                    print(zys.reason)
        
    except:
        pass  # don't crash if api is down :)          

```
