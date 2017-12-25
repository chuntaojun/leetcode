import random


class Codec:
    def __init__(self):
        self.__random_length = 6
        self.__tiny_url = "http://tinyurl.com/"
        self.__alaphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__lookup = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        def getRand():
            rand = []
            for _ in xrange(self.__random_length):
                rand += self.__alaphabet[random.randint(0, len(self.__alaphabet) - 1)]
            return "".join(rand)
        key = getRand()
        while key in self.__lookup:
            key = getRand()
        self.__lookup[key] = longUrl
        return self.__tiny_url + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.__lookup[shortUrl[len(self.__tiny_url):]]