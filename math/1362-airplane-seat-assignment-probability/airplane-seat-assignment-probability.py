class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n ==1:
            return 1

        return 0.5

        # Key invariant / mental model:
        # After passenger 1 picks randomly, the only seats that determine the final outcome are:
        #   - seat 1 (original seat of passenger 1)
        #   - seat n (original seat of passenger n)
        #
        # The process becomes a "hot potato" chain:
        # - passengers take their own seat if free
        # - otherwise they pick a random remaining seat
        #
        # The chain ends exactly when someone randomly picks seat 1 or seat n:
        # - pick seat 1 => everyone else becomes deterministic => passenger n gets seat n  (win)
        # - pick seat n => seat n is gone => passenger n loses                 (lose)
        #
        # While the chain is alive, seat 1 and seat n are both still unpicked,
        # and any displaced passenger picks uniformly among remaining seats.
        # So seat 1 and seat n are symmetric => win prob = 1/2.
        




