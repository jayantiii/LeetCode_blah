class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # 2 meeting end and start at same time is conflict
        #Parse time format to some integer interval first

        if max(event1[0], event2[0]) <= min(event1[1], event2[1]):
            return True
        return False
        