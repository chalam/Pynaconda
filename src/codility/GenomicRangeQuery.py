import sys
def genomic_range_query(s, p, q):
    weights = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    n = len(p)
    impacts = []
    for i in range(n):
        impact = sys.maxsize
        print(s[p[i]:q[i]+1])
        # for slice in s[p[i]:q[i]+1]:
        #     print(slice, weights[slice])
        #     impact = min(impact, weights[slice])
        for k, v in weights.items():
            if k in s[p[i]:q[i]+1]:
                impact = min(v, impact)
                break
        print('impact', impact)
        impacts.append(impact)
    return impacts

if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]
    impacts = genomic_range_query(S, P, Q)
    assert impacts == [2, 4, 1], impacts