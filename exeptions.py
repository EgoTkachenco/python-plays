# Return age 

def getUserAge():
    try :
        age = int(input("Your Age:"))
    except:
        print("Invalid age...")
        return getUserAge()
    return age


print(getUserAge())