def solution(box, n):
    a,x=divmod(box[0],n)    
    b,x=divmod(box[1],n)
    c,x=divmod(box[2],n)
    return a*b*c