class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter='#'
        encode=''
        for ch in strs:
            ch_encoding=str(len(ch))+delimiter+ch
            encode+=ch_encoding
        return encode

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            len_ch=int(s[i:j])
            word=s[j+1: j+1+len_ch]
            res.append(word)
            i=j+1+len_ch
        return res
