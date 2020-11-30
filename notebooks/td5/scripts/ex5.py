## Q1.
def heure_to_sec(h, m, s):
    return h * 3600 + m * 60 + s
#print(heure_to_sec(10, 15, 20))
## Q2.
def sec_to_heure(s):
    m, s = s // 60, s % 60
    h, m = m // 60, m % 60
    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
#sec_to_heure(36920)
## Q3.
def duree(h1, m1, s1, h2, m2, s2):
    s = heure_to_sec(h2, m2, s2) - heure_to_sec(h1, m1, s1)
    sec_to_heure(s)
    
#duree(11, 30, 0, 12, 30, 0)