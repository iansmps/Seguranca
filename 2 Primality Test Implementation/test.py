import time

def normal(p):
    if p%2 ==0:
        return 2
    res = (2**p)%p
    return res - 2

def normald(p):
    i = 1000000
    div = p//i
    res = (2**int(div))%p

    res = (res**i)*(2**(p%i))%p

    return res - 2  

def pot(q,p):
    b = 2
    listpot = [q]
    a = q
    #start_time = time.time()
    while b <= p/2:
        b = b*2
        a = a * a
        listpot.append(a)
    #print(listpot)
    #print("1--- %s seconds ---" % (time.time() - start_time))
    #start_time = time.time()
    primo = p
    res = 1
    #p = p-b
    while p != 0:
        b = b//2
        #tam = len(listpot)
        fat = listpot.pop()
        #print(fat)

        while p >= b:
            res = res*fat
            p = p - b
    #print("2--- %s seconds ---" % (time.time() - start_time))
    
    return res

def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0
    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """
    result = 1
    while power > 0:
        # If power is even
        if power % 2 == 0:
            # Divide the power by 2
            power = power / 2
            # Multiply base to itself
            base = base * base
        else:
            # Decrement the power by 1 and make it even
            power = power - 1
            # Take care of the extra value that we took out
            # We will store it directly in result
            result = result * base

            # Now power is even, so we can follow our previous procedure
            power = power / 2
            base = base * base

    return result

def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def binomial(n, k):
    if 0 <= k <= n:
        naux = 1
        kaux = 1
        for t in range(1, min(k, n - k) + 1):
            naux *= n
            kaux *= t
            n -= 1
        return naux // kaux
    else:
        return 0

def primetest(n):
    head = 3
    limit = 1000
    #print(limit)

    while(head!=limit and head!=(n//2)+1):
        a = binomial(n,head)
        #print(a)
        if a % n != 0:
            return 1
        else:
            head = head + 1
    return 0
    
a = 2
b = 100033000330001 

'''start_time = time.time()
c =fast_power(a,b)
print("FastP--- %s seconds ---" % (time.time() - start_time))
#print(c)

start_time = time.time()
c=pot(a,b)
print("Pot--- %s seconds ---" % (time.time() - start_time))
#print(c)'''
randp =[32416187567,32416188223,	32416188809	,32416189391,32416187627	,32416188227	,32416188839	,32416189459,32416187651	,32416188241	,32416188859	,32416189469, 32416187659	,32416188257	,32416188877	,32416189493,32416187701	,32416188269	,32416188887	,32416189499,32416187719	,32416188271	,32416188899	,32416189511,32416187737	,32416188331	,32416188949	,32416189573,32416187747	,32416188349	,32416189019	,32416189633,32416187761	,32416188367	,32416189031	,32416189657,32416187773	,32416188397	,32416189049	,32416189669,32416187827	,32416188449	,32416189061	,32416189681,32416187863	,32416188451	,32416189063	,32416189717,32416187893	,32416188491	,32416189079	,32416189721,32416187899	,32416188499	,32416189081	,32416189733,32416187927	,32416188517	,32416189163	,32416189753,32416187929	,32416188527	,32416189181	,32416189777,32416187933	,32416188583	,32416189193	,32416189853,32416187953	,32416188589	,32416189231	,32416189859,32416187977	,32416188601	,32416189261	,32416189867,32416187987	,32416188647	,32416189277	,32416189877,32416188011	,32416188689	,32416189291	,32416189909,32416188037	,32416188691	,32416189321	,32416189919,32416188113	,32416188697	,32416189349	,32416189987,32416188127	,32416188767	,32416189361	,32416190039,32416188191	,32416188793	,32416189381	,32416190071]
rand2=[1000000000,1000000007,1000000009,1000000861,1000004329,1000025261,1000075057,1000099999,1000273817,1007050321,1009101133,1023456798,1023456897,1023465798,1023479856,1023567948,1024243321,1024383257,1031223317,1053594241,1057438801,1063254978,1073676287,1088888881,1095912793,1097393351,1097393447,1097393663,1097393683,1111211111,1113251719,1113443017,1117175145,1117315319,1118869091,1119416189,1122547711,1122871751,1123456987,1123465789,1123564987,1123586479,1124396857,1124638579,1124685973,1133575799,1136972771,1153723573,1154454311,1170136777,1174638529,1175203278,1198754321,1202056903,1210864201,1227182861,1230507001,1231491827,1234457689,1234563037,1234567890,1234567891,1234798321,1245375689,1258925411,1265011073,1278491536,1290735486,1299963601,1301476963,1304119699,1317313771,1317317371,1331133113,1331177147,1335557777,1360499117,1364103977,1458765431,1464183521,1477271183,1480028171,1480028201,1481481481,1500000001,1516171819,1531415939,1608906624,1613902553,1617924853,1636616323,1654792830,1688816681,1694343422,1698118691,1716231163,1716336911,1719898171,1836660096,1870585220,1882341361,1914032047,1966640443,1979339339,1991096119,1997333137,2050918644,2106945901,2111011129,2111511013,2113733797,2131131137,2147483647,2148736590,2232232273,2233777723,2236133941,2282113373,2319131071,2327138083,2337537353,2391951273,2412134003,2432582681,2462372461,2481129210,2486784401,2527293133,2547863419,2599291451,2627282963,2754425310,2763087059,2819116381,2836536629,2853044003,2971215073,2981997480,2999999929,3086358019,3113510401,3133183103,3211891519,3215031751,3217924201,3235328807,3262811042,3322255777,3323333323,3333323333,3333555227,3444224222,3578962147,3592007533,3696741031,3708797237,3713821637,3731292319,3738668363,3743895347,3778888999,3781378039,3791085426,3799666951,4076863487,4180566390,4263918750,4276008809,4294967295,4295032837,4295145556,4332221111,4575242147,4712020471,4734234247,4771212547,4868747809,4916253649,4922894533,4938256511,4938271579,5363222357,5452515049,5513600773,5624281299,5748693121,5838052333,5897230146,5926535897,5949670231,6058655748,6102977801,6398410752,6554443333,6607882123,6650672641,6650672647,6666666666,6771737983,6801788249,6829547103,6913548721,6999999989,7313711101,7337737777,7373533723,7408868921,7427466391,7758337633,7777777777,7784383937,8000000008,8000000018,8018018851,8192454631,8437304723,8439563243,8565705523,8589935681,8660254037,8753196421,8757193191,8776320587,8803424081,8888888888,8890919293,8970134652,8990919293,9000000001,9152992349,9199999999,9387802769,9471413089,9487215360,9512368741,9592993410,9643187251,9731236789,9753236789,9761236789,9848868889,9876534120,9876543211,9999959999,9999999929]





f = 0
prime10 = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, 8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, 8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, 8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, 8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, 8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, 8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, 8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, 8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, 8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, 8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, 8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, 9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, 9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, 9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, 9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, 9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, 9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, 9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, 9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, 9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, 9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]

lista = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
lista2 =[503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] 
lista3 = [101,1013,10007,100019,1000033,10000079,100030001,1500450271,10000000019,100123456789,1000000000039,10000000000283,100033000330001]#
lista4=[101,1013,10007,100019,1000033,10000079,100030001,1500450271,10000000019,100123456789,1000000000039,10000000000283,100033000330001,1000000000100011,100055128505716009,12764787846358441471]
listacomp=[1000000000100015]#,100033000330005,1000000000100015,100055128505716005,12764787846358441473
lista5=[1451730470513778492236629598992166035067,15452417011775787851951047309563159388840946309807,14759984361802021245410475928101669395348791811705709117374129427051861355011151,1814159566819970307982681716822107016038920170504391457462563485198126916735167260215619523429714031]
listac2=[1451730470513778492236629598992166035065,15452417011775787851951047309563159388840946309805,14759984361802021245410475928101669395348791811705709117374129427051861355011153,1814159566819970307982681716822107016038920170504391457462563485198126916735167260215619523429714035]

'''for i in (prime10): 
    start_time = time.time()
    c = normald(i)
   # print("%.7s  %s" % (time.time() - start_time,i))
    if c == 0:
        #print(i)
        f = f+1
print(f)'''
count = 0
i=2

for i in (lista4): 
    start_time = time.time()
    #print(i)
    c = primetest(i)
    print("%.7s  %s" % ((time.time() - start_time),i))
    count = count +1
    if c == 1:
        #print(i)
        f = f+1

print("%s " % (time.time() - start_time))
print(f,count)