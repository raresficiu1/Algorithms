#https://leetcode.com/contest/biweekly-contest-44/problems/find-the-highest-altitude/


class Solution:
    def largestAltitude(self, gain) -> int:
        alt = 0
        maxim = 0
        for i in gain:
            alt += int(i)
            if (alt > maxim):
                maxim = alt

        return (maxim)

