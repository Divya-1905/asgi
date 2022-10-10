
def minJumps(arr, n):
    moves=arr[0]
    steps=0
    for i in range(moves,n):
        print(moves)
        if moves >=n :
            moves+=arr[i]
            break
        else:
            moves+=arr[moves]
            steps+=1
    return steps,'hi'  
arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr=[1, 4, 3, 2, 6, 7]
n=len(arr)
print(minJumps(arr,n))