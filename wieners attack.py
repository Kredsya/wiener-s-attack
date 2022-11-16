def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

_print = lambda s, flag : print(">> " + s) if flag else 0

key_flag = True;

p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
q = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084241
N = p * q
e = 1000001
phi_N = (p-1)*(q-1)
_print("gcd(N, e) = {0}".format(gcd(phi_N, e)), key_flag)

if True:
    p = 379
    q = 239
    e = 5
    N = p*q
    phi_N = (p-1)*(q-1)

t1, t2, r1, r2, Q = 0, 1, phi_N, e, 0
while r1%r2:
    Q = r1//r2
    t1, t2 = (t2, t1)
    r1, r2 = (r2, r1)
    t2 -= Q*t1
    r2 %= r1
while t2 < 0:
    t2 += phi_N
d = t2
e, d = d, e

_print("e = {0}, d = {1}".format(e, d), key_flag)
_print("test(1) : {0}".format(e*d % phi_N), key_flag)

'''============================================'''

attack_flag = True

ingredient = list()
a, b = e, N
while b > 0:
    ingredient.append(a//b)
    a, b = (b, a%b)
ingredient = ingredient[1:]
_print("ingredient = "+str(ingredient), attack_flag)
candidate = list()
for i in range(len(ingredient)):
    son, mom = 1, ingredient[i]
    for j in reversed(range(i)):
        son, mom = mom, mom*ingredient[j]+son
    candidate.append([son, mom])
_print("candidate = "+str(candidate), attack_flag)

print(N, p, q)
lim_N = (p**0.25) * (q**0.25) / 3
_print("limit of N = {0}".format(lim_N), attack_flag)

for pred_k, pred_d in candidate:
    if pred_d > lim_N:
        break
    
    pred_phi_N = (e*pred_d - 1) // pred_k
    a, b, c = 1, -(N - pred_phi_N + 1), N
    pred_p, pred_q = (-b+(b**2-4*a*c)**0.5)/(2*a), (-b-(b**2-4*a*c)**0.5)/(2*a)
    pred_N = pred_p * pred_q
    if pred_N == N:
        _print("d is found! d = {0}".format(pred_d), True)
