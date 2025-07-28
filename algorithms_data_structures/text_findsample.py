# import random
# import string

import time


class Text:
    def __init__(self, sample, text):
        x = 59
        self.p = 67
        self.txt = text
        self.sample = sample
        self.len_txt = len(text)
        self.len_sample = len(sample)
        self.indices = []
        self.x_powers = [pow(x, i, self.p) for i in range(self.len_sample + 1)]
        self.hash_sample = self.hash(sample, 0)
        self.hash_txt = self.hash(self.txt, self.len_txt - self.len_sample)

    def findall(self):
        for i in range(self.len_txt - self.len_sample, -1, -1):
            if self.hash_txt == self.hash_sample:
                if self.txt[i : i + self.len_sample] == self.sample:
                    self.indices.append(i)
            self.hash_txt = self.hash_next(i - 1)

    def hash(self, text, ind_left):
        hash = 0
        for i in range(self.len_sample):
            hash = (hash + ord(text[ind_left + i]) * self.x_powers[i]) % self.p
        return hash

    def hash_next(self, ind_left):
        if ind_left < 0:
            pass
        else:
            hash = (
                (
                    self.hash_txt
                    - ord(self.txt[ind_left + self.len_sample])
                    * self.x_powers[self.len_sample - 1]
                )
                * self.x_powers[1]
                + ord(self.txt[ind_left])
            ) % self.p
            return hash


def timed(func):
    t1 = time.time()
    func()
    t2 = time.time()
    print(f"Elapsed time = {t2-t1}\n")


def main():
    p = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    text = Text(p, s)
    # text = Text(input(), input())

    text.findall()
    print(*reversed(text.indices))


def main1():
    p = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # p, s = input(), input()
    n, m = len(p), 0xFFFFFFF
    t = pow(127, n, m + 1)
    d = {chr(i): i * t & m for i in range(128)}
    t = x = 0
    for a, b in zip(p, s):
        t = t * 127 + ord(a) & m
        x = x * 127 + ord(b) & m
    for i, a, b in zip(range(m), s[n:] + "!", s):
        if x == t:
            print(i, end=" ")
        x = x * 127 + ord(a) - d[b] & m


timed(main)
timed(main1)

# lst = []
# for i in range(1000):
#     lst.append(random.choice(string.ascii_letters))
# print("".join(lst))

# string = "KSWWgfZqeeZVZEJCIgyOYztOHftpYUzlugogKnyZKtztYtukxvXFcbUZyWPnYkBDhiBjuewFJfonREFeGJZRTkWzqisdjZrYnVEyvHsNvRVXiBdeUSUmowYIvYiBdgOFfwGbcdudNneAhpUcDFgZDVWvcZUMBpXozsavvHDVKSyyPdmErgZiCFNnGdaEQUnjIUiMhmMRCsCrzwAHRrCDEfgODeMujGrflewlWjwmkSfkkPaZJyDjrUkFeWFhQlKxKLUAAhlSEPejArLSVoHwfpgOOKDJNIwvFWyyHAZRNJCTZFsYVnsLJagneklUImTuhJKRFZmObNVosNKeLWhSDElreqVKnnHtyiPDmmWxWdUtkMsXoPcUZWVOVCjDumondmyCcLyTVuLKFspFSzUTUQxuNUPhlMtyJLmrXxuOypiHGKySCbQWbtnhHoEQniQTwZSRvLITugabvtaaUMNaVcXkmIMLdCiOvhWdoUXMudZNhIBYFTHejYMBUCOvAMQIhomiIhyxTRDIsfTpRmRxOCwcKKuwRJwJhBdsuAztkeNfMyMtXgyGoVcyQKtxcRhluFDwBqJTdKOikQRjOEJrnpaUIhzuLQLNAltDIFjrvhylLJlBhLHqqaTAfXjdKCEjMZlWDOsONPVLPQZpBhIgfMdNKaIbxirRvKAKQkLOYQxWsebDYxsQubVsbBLEcXMvjIJcjYzwZjIiBteRQTNUEjpPrBplMpfQmDygpNbuaEhqsfXQfqxiPiPHGTjKTPojAsXYLSPGqyLpvBFQoqjOWzTEVYEPNgGoRQExftFlwPMdSrkOzJLMjIKgILJNufHUkpjpmhAjuVLVewIqmDSEKLfKZhsCwOmwidozSkvUHfwQvYdenIgZsKnxvzjDqVuJBgmklCeawYcaIZVJmmJLMvHlNxQvAOqnzHWngNQXrtxeWIdXcPvREMbAcexcuhDmmbFlGmxsgmkZUJMehGLeRbfwvkWuceZWBOzbQbio"
# print(string.count("Wd"))
