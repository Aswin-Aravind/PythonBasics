# def greet(name):
#     return "hello "+name
# student={"name":"Aswin"}


# def number_sum(*args):
#     return sum(args)
# k=number_sum(1,2,3,5,1)


def unique_elements(lst):
    t=[]
    for i in lst:
        if i not in t:
            t.append(i)
    return t
k=unique_elements([1,2,2,3,3,4,5,1])
print(k)