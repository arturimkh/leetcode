class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        prefix=strs[0];
        for i in range(len(prefix)):
            for s in strs:
                if(i==len(s))or(s[i]!=prefix[i]):#прошлись по всем i-ой букве массиве если поняли что 
                                                 #все i-ая буква совпадает во всех словах то в                                                        #результат записываем эту букву, если же когда брали i+1 букву и её нет хоть в одном слове то моментально return res;
                    return res
            res+=prefix[i]
        return res
            
            
