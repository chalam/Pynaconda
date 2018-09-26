"""
Multiplication of big-digit values with Toom-Cook 3-way method
https://gist.github.com/komasaru/c7306412ed3e76442f9ced2bc3090a64
Θ(N^(log(5)/log(3)))
https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication
"""
import random
import sys
import traceback


class MultiplyToomCook3:
    D_MAX = 729  # Maximum number of digits (power of 3)
    D     = 729  # Digits of computation (<= D_MAX)

    def __init__(self, a=None, b=None):
        if a is None and b is None:
            self.a = [random.randrange(10) for _ in range(self.D)]
            self.b = [random.randrange(10) for _ in range(self.D)]
        else:
            self.a = [i for i in range(len(str(a)))]
            self.b = [i for i in range(len(str(b)))]
            D_MAX  = len(self.a)  # Maximum number of digits (power of 3)
            D      = D_MAX        # Digits of computation (<= D_MAX)

    def compute(self):
        """ Computation of multiplication """
        try:
            for i in range(self.D_MAX - len(self.a)):
                self.a.append(0)
            for i in range(self.D_MAX - len(self.b)):
                self.b.append(0)
            z = self.__multiply_toom_cook_3(self.a, self.b)
            z = self.__do_carry(z)
            self.__display(self.a, self.b, z)
        except Exception as e:
            raise

    def __multiply_normal(self, a, b):
        """ Normal multiplication
        :param  list a
        :param  list b
        :return list z
        """
        try:
            a_len, b_len = len(a), len(b)
            z = [0 for _ in range(a_len + b_len)]
            for j in range(b_len):
                for i in range(a_len):
                    z[j + i] += a[i] * b[j]
            return z
        except Exception as e:
            raise

    def __multiply_toom_cook_3(self, a, b):
        """ Toom-Cook 3-way multiplication
        :param  list a
        :param  list b
        :return list z
        """
        a_m1, a_m2, a_0, a_1, a_inf = [], [], [], [], []
        b_m1, b_m2, b_0, b_1, b_inf = [], [], [], [], []
        c_m1, c_m2, c_0, c_1, c_inf = [], [], [], [], []
        c0, c1, c2, c3, c4          = [], [], [], [], []
        try:
            t_len = len(a)
            # 9
            if t_len <= 9:
                return self.__multiply_normal(a, b)
            a0 = a[:(t_len // 3)]
            a1 = a[(t_len // 3):(t_len * 2 // 3)]
            a2 = a[(t_len * 2 // 3):]
            b0 = b[:(t_len // 3)]
            b1 = b[(t_len // 3):(t_len * 2 // 3)]
            b2 = b[(t_len * 2 // 3):]
            for i in range(t_len // 3):
                a_m2.append((a2[i] << 2) - (a1[i] << 1) + a0[i])
                b_m2.append((b2[i] << 2) - (b1[i] << 1) + b0[i])
            for i in range(t_len // 3):
                a_m1.append(a2[i] - a1[i] + a0[i])
                b_m1.append(b2[i] - b1[i] + b0[i])
            a_0, b_0 = a0, b0
            for i in range(t_len // 3):
                a_1.append(a2[i] + a1[i] + a0[i])
                b_1.append(b2[i] + b1[i] + b0[i])
            a_inf, b_inf= a2, b2
            c_m2  = self.__multiply_toom_cook_3(a_m2, b_m2)
            c_m1  = self.__multiply_toom_cook_3(a_m1, b_m1)
            c_0   = self.__multiply_toom_cook_3(a_0, b_0)
            c_1   = self.__multiply_toom_cook_3(a_1, b_1)
            c_inf = self.__multiply_toom_cook_3(a_inf, b_inf)
            c4 = c_inf
            for i in range((t_len // 3) * 2):
                c  = -c_m2[i]
                c += (c_m1[i] << 1) + c_m1[i]
                c -= (c_0[i] << 1) + c_0[i]
                c += c_1[i]
                c += (c_inf[i] << 3) + (c_inf[i] << 2)
                c  = c // 6
                c3.append(c)
            for i in range((t_len // 3) * 2):
                c  = (c_m1[i] << 1) + c_m1[i]
                c -= (c_0[i] << 2) + (c_0[i] << 1)
                c += (c_1[i] << 1) + c_1[i]
                c -= (c_inf[i] << 2) + (c_inf[i] << 1)
                c  = c // 6
                c2.append(c)
            for i in range((t_len // 3) * 2):
                c  = c_m2[i]
                c -= (c_m1[i] << 2) + (c_m1[i] << 1)
                c += (c_0[i] << 1) + c_0[i]
                c += (c_1[i] << 1)
                c -= (c_inf[i] << 3) + (c_inf[i] << 2)
                c  = c // 6
                c1.append(c)
            c0 = c_0
            z = c0 + c2 + c4
            for i in range((t_len // 3) * 2):
                z[i + t_len // 3] += c1[i]
            for i in range((t_len // 3) * 2):
                z[i + t_len] += c3[i]
            return z
        except Exception as e:
            raise

    def __do_carry(self, a):
        """ Process of carrying
        :param  list a
        :return list a
        """
        cr = 0

        try:
            for i in range(len(a)):
                a[i] += cr
                cr = a[i] // 10
                a[i] -= cr * 10
            if cr != 0:
                print("[ OVERFLOW!! ] ", cr)
            return a
        except Exception as e:
            raise

    def __display(self, a, b, z):
        """ Display
        :param list a
        :param list b
        :param list z
        """
        a_len = self.D_MAX
        b_len = self.D_MAX
        z_len = self.D_MAX * 2
        try:
            while a[a_len - 1] == 0:
                if a[a_len - 1] == 0:
                    a_len -= 1
            while b[b_len - 1] == 0:
                if b[b_len - 1] == 0:
                    b_len -= 1
            while z[z_len - 1] == 0:
                if z[z_len - 1] == 0:
                    z_len -= 1
            print("a =")
            for i in reversed(range(a_len)):
                print(a[i], end="")
                if (a_len - i) % 10 == 0:
                    print(" ", end="")
                if (a_len - i) % 50 == 0:
                    print()
            print()
            print("b =")
            for i in reversed(range(b_len)):
                print(b[i], end="")
                if (b_len - i) % 10 == 0:
                    print(" ", end="")
                if (b_len - i) % 50 == 0:
                    print()
            print()
            print("z =")
            for i in reversed(range(z_len)):
                print(z[i], end="")
                if (z_len - i) % 10 == 0:
                    print(" ", end="")
                if (z_len - i) % 50 == 0:
                    print()
            print()
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = MultiplyToomCook3()
        obj.compute()

        a = 5313969797022876007865453254137711291618937695170868966548357976313192691870262523766483684170857804
        b = 9783483294082441361180615595894143546512317591170502530626606255574218864396333893954928230682223373
        obj = MultiplyToomCook3(a, b)
        obj.compute()

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)