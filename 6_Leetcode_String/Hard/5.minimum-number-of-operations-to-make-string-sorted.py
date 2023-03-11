# 5. [Minimum Number of Operations to Make String Sorted](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/)


def makeStringSorted(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        inverses = [1] * (len(s) + 1)
        for a in range(2, len(s) + 1):
            inverses[a] = MOD - ((MOD // a) * inverses[MOD % a]) % MOD

        ans, tot, comb_tot = 0, 0, 1
        cnt = [0] * 26
        for cur in map(ord, reversed(s)):
            num = cur - 97
            cnt[num] += 1
            tot += 1
            comb_tot = (comb_tot * tot * inverses[cnt[num]]) % MOD
            ans += comb_tot * sum(cnt[:num]) * inverses[tot]
        return ans % MOD