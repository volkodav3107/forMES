FILE_NAME = '/home/vlad/PycharmProjects/untitled/asd'
f = open(FILE_NAME)
l = [line.strip() for line in f]
print(l)
d = {}
d.update({1: 2})
my_L = map(len, [l, 'asd'])
print(my_L)
print(d)
f.close()


def get_dict_to_show():
    my_dict = {1: 23, 'asd': 123123}
    return my_dict
