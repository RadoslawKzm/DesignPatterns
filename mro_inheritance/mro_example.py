"""Method Resolution Order example (MRO)"""

class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D:
    pass


class E:
    pass


class F(D, E):
    pass


class G(C, F):
    pass


def test_case():
    """Test case displaying zen of python principle: No error should go through silently"""

    class H(F, C):
        pass

    class J(G, H):
        pass


print(f"{G.mro()=}")
# test_case()
