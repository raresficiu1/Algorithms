#https://codeforces.com/contest/799/problem/A
import math


nr_prajituri, t_set, nr_acelasi_timp, t_cuptor = input().split()
nr_prajituri=int(nr_prajituri)
t_set=int(t_set)
nr_acelasi_timp=int(nr_acelasi_timp)
t_cuptor=int(t_cuptor)
t1 = math.ceil(nr_prajituri/nr_acelasi_timp) * t_set

t2=2
if(t_set>t_cuptor):
    t2 = math.ceil(math.ceil(nr_prajituri/2)/nr_acelasi_timp) * t_set
if(t_set==t_cuptor):
    t2 = t_set + math.ceil((nr_prajituri - nr_acelasi_timp) / (nr_acelasi_timp * 2)) * t_set

if(t_set<t_cuptor):
    intretimp= t_cuptor / t_set * nr_acelasi_timp
    t2= t_cuptor + math.ceil(math.ceil((nr_prajituri-intretimp)/2)/nr_acelasi_timp) * t_set


if(t1<=t2):
    print("NO")
else:
    print("YES")