#!/usr/bin/env python
def prismatic_coef(V, S, L):
    """Returns the prismatic coeficient, given (V)olume,
       the (L)ength overall and the cross-(S)ectional area
       distribution

    Args:
       V - (float): Volume
       L - (float): Length, in meters
       S - (float): Cross-sectional area distribution.
    """
    return V / float(S * L)


