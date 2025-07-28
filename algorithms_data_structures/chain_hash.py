from collections import deque


class PhoneBook:
    def __init__(self, m):
        self.x = 263
        self.p = 1000000007
        self.m = m
        self.phones = [deque() for _ in range(self.m)]
        self.dct = {
            "add": self.add_str,
            "check": self.check_i,
            "find": self.find_str,
            "del": self.del_str,
        }

    def hash_str(self, str):
        return (
            sum([(ord(str[i]) * (self.x**i)) for i in range(len(str))])
            % self.p
            % self.m
        )

    def add_str(self, str):
        hsh = self.hash_str(str)
        if not self.phones[hsh] or str not in self.phones[hsh]:
            self.phones[hsh].appendleft(str)

    def find_str(self, str):
        hsh = self.hash_str(str)
        if not self.phones[hsh]:
            print("no")
        else:
            if str in self.phones[hsh]:
                print("yes")
            else:
                print("no")

    def del_str(self, str):
        hsh = self.hash_str(str)
        if self.phones[hsh]:
            try:
                self.phones[hsh].remove(str)
            except:
                pass

    def check_i(self, i):
        print(*self.phones[int(i)])

    def execute(self, func, arg):
        self.dct[func](arg)


def main():
    m = int(input())
    pb = PhoneBook(m)
    for _ in range(int(input())):
        func, arg = input().split()
        pb.execute(func, arg)


if __name__ == "__main__":
    main()
