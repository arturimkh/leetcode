        prefix=strs[0]
        plen=len(prefix)
        
        for s in strs[1:]:
            while(prefix!=s[0:plen]):
                prefix=prefix[0:plen-1]
                plen-=1
                if plen==0:
                    return ""
        return prefix
        
