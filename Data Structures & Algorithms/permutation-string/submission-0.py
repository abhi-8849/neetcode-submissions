class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False


        target = [0]*26
        for char in s1:
            target[ord(char) - ord('a')] += 1

        window = [0]*26
        for right in range(len(s2)):
            window[ord(s2[right]) - ord('a')] += 1

            if right >= k:
                window[ord(s2[right - k]) - ord('a')] -= 1

            if right >= k-1:
                if target == window:
                    return True

        return False
                

            