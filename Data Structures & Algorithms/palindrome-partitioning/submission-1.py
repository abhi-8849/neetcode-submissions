class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def split(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                sub = s[start:end+1]

                if sub == sub[::-1]:
                    path.append(sub)
                    split(end+1)
                    path.pop()

        split(0)
        return res