class Codec:
    def __init__(self):
        self.result={}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def randStr(chars = string.ascii_uppercase + string.ascii_lowercase + string.digits, N=10):
	        return ''.join(random.choices(chars,k=N) )
        temp=randStr()
        while temp in self.result.keys():
            temp=randStr()
        self.result[temp]=longUrl
        return 'http://tinyurl.com/'+temp

            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        lst=shortUrl.split('/')
        return self.result[lst[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))