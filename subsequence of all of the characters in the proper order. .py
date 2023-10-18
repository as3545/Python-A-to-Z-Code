def hackerrankInString(s):
    # Write your code here  
    count=0
    h="hackerrank"
    for c in s:
        if c==h[count]:
            count+=1
            if count==len(h):
                return "YES"
    return "NO"
            
 
