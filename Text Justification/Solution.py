class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        length = 0
        i = 0
        while(i<len(words)):
            if length+len(line)+len(words[i])>maxWidth:
                remain = maxWidth - length
                space  = remain // max(1,len(line)-1)
                remainder =  remain % max(1,len(line)-1)

                for j in range(max(1,len(line)-1)):
                    line[j]+=" "*space
                    if remainder:
                        line[j]+=" "
                        remainder-=1
                res.append("".join(line))
                line = []
                length = 0
            line.append(words[i])
            length += len(words[i])
            i+=1

        ll =" ".join(line)
        rr = maxWidth - len(ll)
        ll+=" "*rr
        res.append(ll)
        return res 
        

