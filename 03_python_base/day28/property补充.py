class Foo:

    @property
    def A(self):
        print("===> get A")

    @A.setter
    def A(self, val):
        print("===> set A, val = {}".format(val))

    @A.deleter
    def A(self):
        print("===> del A")


f = Foo()
f.A         # ===> get A
f.A = "a"   # ===> set A, val = a
del f.A     # ===> del A



class Foo:

    def get_A(self):
        print("===> get_A")

    def set_A(self, val):
        print("===> set_A, val = {}".format(val))

    def del_A(self):
        print("===> del_A")

    A = property(get_A, set_A, del_A)


f = Foo()
f.A         # ===> get_A
f.A = "a"   # ===> set_A, val = a
del f.A     # ===> del_A
