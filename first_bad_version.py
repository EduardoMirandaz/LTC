# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1): return 1

        righter_good_version = 1

        lefter_bad_version = n

        while lefter_bad_version - righter_good_version > 1:

            middle_version = (righter_good_version + lefter_bad_version) // 2
            
            if isBadVersion(middle_version):
                lefter_bad_version = middle_version
            else:
                righter_good_version = middle_version

        else:
            return lefter_bad_version    


