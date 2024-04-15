from ddt import ddt, data, unpack
data = (("name","pass"),("sdd","sd"))

class test:
    @data(("name","pass"),("sdd","sd"))
    @unpack
    def func1(self,user,pass_):
        print(user, pass_)


ss = test()
ss.func1