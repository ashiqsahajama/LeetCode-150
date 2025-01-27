class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        items = path.split("/")
        print(items)

        for i in items:
            if i=="..":
                if stack:
                    stack.pop()
            elif i!="" and i!=".":
                stack.append(i)
        return "/"+"/".join(stack)
