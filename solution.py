class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        sl1 = s1.split()
        sl2 = s2.split()
        slcount= sl1+sl2
        wc= {}

        for s in slcount:
            if s in wc:
                wc[s] +=1
            else:
                wc[s]=1
        ret = []

        for w in wc:
            if wc[w] ==1:
                ret.append(w)
        return ret
