from typing import List ,Optional,Set
from collections import deque
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        lenWords=len(words)
        lenS=len(s)
        lenWord=len(words[0]) if lenWords>0 else 0
        totalWordsLen=len(words)* lenWord
        res=[]
        wordMap={key:0 for key in words}
        for i in range(lenWords):
            wordMap[words[i]]+=1
        tempWordMap={key:0 for key in words}
        for i in range(lenWord):
            k=i
            while k <=lenS-totalWordsLen:
                print(k)
                length=0
                j=k
                while j < lenS:
                    word=s[j:j+lenWord]
                    if word in wordMap.keys():
                        if tempWordMap[word]<wordMap[word]:
                            tempWordMap[word]+=1
                            length+=1
                            if length==lenWords:
                                res.append(k)
                                print(s[j-length*lenWord+lenWord:j-length*lenWord+2*lenWord],j)
                                tempWordMap[s[j-length*lenWord+lenWord:j-length*lenWord+2*lenWord]]-=1
                                k=j
                        else:
                            tempWordMap={key:0 for key in words}
                            break
                        j+=lenWord
                    else:
                        tempWordMap={key:0 for key in words}
                        k=j+lenWord
                        break
                k+=lenWord
            print()
            print()
        return res
print(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
