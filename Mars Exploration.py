
def marsExploration(s):
    c=0
    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2:
            if s[i]!='S':
                c+=1
        else:
            if s[i]!='O':
                c+=1
    return c
                
if __name__ == '__main__':

    s = input()

    result = marsExploration(s)
    print(result)
