def countingValleys(path):
    lowwer_path = path.lower()
    listPath = []
    count = 0
    valley = 0
    for i in lowwer_path:
        listPath.append(str(i))
    for i in listPath:
        if i == "u":
            count = count + 1
            
            if count == 0:
                valley = valley + 1
        elif(i == "d"):
            count -= 1
    return valley