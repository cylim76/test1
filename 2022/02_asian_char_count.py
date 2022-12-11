title = "레지나레나 - 용서받지 못한 그대에게"
# 한글 개수 세는 함수
def title_length(title):
    
    # slice the title to a list
    tlist =[]
    for t in range(0,len(title)):
        tlist.append(title[t])

    # count number of alpha charaters in the tlist
    title_length =0
    for t in tlist:
        if t.isalpha() :
            title_length+=1

    return title_length



print(title_length(title))
