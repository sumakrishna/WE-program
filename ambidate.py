def isAmbiguous(date: str) -> bool:
    date_list = date.split("/")
    if int(date_list[0]) in range(1, 13) and int(date_list[1]) in range(1, 13):
        if date_list[0] == date_list[1]:
            return False
        else:
            return True
    else:
        return False

import sys
print(isAmbiguous(sys.argv[1]))
