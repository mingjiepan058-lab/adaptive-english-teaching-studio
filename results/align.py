import json,sys
W=[.30,.25,.15,.15,.15]; D=["D1","D2","D3","D4","D5"]
H=[([5,4,5,5,4],[5,5,4,5,5],"B",(4.60,4.85)),([4,4,5,5,4],[5,5,5,5,5],"B",(4.3,5.0)),
([3,4,1,4,4],[3,3,4,4,3],"B",(3.23,3.3)),([5,5,5,5,5],[4,4,3,5,5],"A",(5,4.15)),
([5,3,4,4,3],[5,4,4,4,4],"B",(3.9,4.3)),([5,4,5,5,5],[5,4,5,4,5],"A",(4.75,4.30)),
([5,4,5,5,4],[5,5,5,4,5],"B",(4.60,4.85)),([5,5,5,5,5],[5,4,3,4,5],"A",(4.90,4.3)),
([5,4,4,5,5],[5,5,3,4,5],"A",(4.85,4.55)),([5,5,5,5,5],[4,3,5,5,5],"A",(5,4.2))]
M=[json.loads(l) for l in open(sys.argv[1])]
ex=adj=n=0; dim={d:[0,0,0] for d in D}; rows=[]
for i,(m,(ha,hb,hw,ht)) in enumerate(zip(M,H),1):
    for side,hs in (("A",ha),("B",hb)):
        for d,h in zip(D,hs):
            c=m["scores"][side][d]["score"]; n+=1
            ex+=c==h; adj+=abs(c-h)<=1; dim[d][0]+=c==h; dim[d][1]+=abs(c-h)<=1; dim[d][2]+=abs(c-h)
            if c!=h: rows.append(f"  #{i} {side} {d}: model {c} vs human {h}")
    calc=tuple(round(sum(s*w for s,w in zip(x,W)),2) for x in (ha,hb))
    print(f"#{i} winner model={m['winner']} human={hw} {'✓' if m['winner']==hw else '✗'} | model {m['weighted_total']['A']}/{m['weighted_total']['B']} human {ht[0]}/{ht[1]} (recomputed {calc[0]}/{calc[1]})")
print("exact",ex,n,ex/n,"adj",adj,adj/n)
for d in D: print(d,dim[d][0],"/20 exact",dim[d][1],"/20 ±1  MAE",dim[d][2]/20)
print("\n".join(rows))
