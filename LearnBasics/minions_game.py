def minion_game(string):
    # your code goes here
    
    # kevin --> start with vowels
    # stuart --> start with consonants
    # dictionary 
    #  --> word, count
    
    freq1 = {}
    freq2 = {}
    
    length = len(string)
    
    for i in range(length):
        char = string[i]

        print("char : ", char)
        
        # VOWELS
        if char in "AEIOU":
            # kevin
            for j in range(i+1,length + 1):
                sub = string[i:j]
                print(sub)
                
                if sub not in freq1:
                    freq1[sub]=1
                else:
                    freq1[sub] = freq1[sub] + 1
        else:
            # stuart
            for j in range(i+1, length + 1):
                sub = string[i:j]
                print(sub)
                
                if sub not in freq2:
                    freq2[sub]=1
                else:
                    freq2[sub] = freq2[sub] + 1
    
    print(freq1)
    print(freq2)

    sum1 = 0
    sum2 = 0
    
    for k,v in freq1.items():
        sum1 = sum1 + v
        
    for k,v in freq2.items():
        sum2 = sum2 + v
        
    print(sum1)
    print(sum2)
            
            
            

if __name__ == '__main__':
    # s = input()
    s = "BANANA"
    minion_game(s)