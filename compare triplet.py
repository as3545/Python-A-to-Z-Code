//Code
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return [alice_score, bob_score]

# Example usage:
alice_ratings = [5, 6, 7]
bob_ratings = [3, 6, 10]
result = compareTriplets(alice_ratings, bob_ratings)
print(result)
