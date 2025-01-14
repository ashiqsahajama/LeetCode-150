class Solution:
    def findSubstring(self, s, words):
        main_dict = {}
        for i in words:
            if i in main_dict:
                main_dict[i]+=1
            else:
                main_dict[i]=1
        res = []
        l = len(s)
        ite = len(words[0])*len(words)

        for i in range(l-ite+1):
            dict2 = defaultdict(int)
            for j in range(i,i+ite,len(words[0])):
                dict2[s[j:j+len(words[0])]] += 1 
            if main_dict == dict2:
                res.append(i)

        return res 
