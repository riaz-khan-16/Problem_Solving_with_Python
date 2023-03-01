# 15. [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)
# Google Coding Question

name = "alex"
typed = "xale"

name ="rick"
typed ="kric"


#   help: https://www.youtube.com/watch?v=0OrGZpjAwI8&t=15s
def isLongPressedName(name, typed):
        # j and i - 1 the previous iteration on the anme not typed
        i = 0 # pointer for 'name'
        j = 0 # pointer for 'typed'
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j != 0 and typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False
        
        return i == len(name) and j == len(typed)
