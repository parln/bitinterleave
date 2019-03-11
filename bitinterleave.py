def bit_interleave64(x32,y32):
    x32 = x32 & 0xffffffff
    y32 = y32 & 0xffffffff
    result = 0x0000000000000000
    onebit = 0x0000000000000001
    for i in range(31,-1,-1):
        tmask = onebit << i
        xbit = x32 & tmask
        result = result | xbit << (i+1)
        ybit = y32 & tmask
        result = result | ybit << (i)
    return result

def uninterleave64(i64):
    mask1 = 0xaaaaaaaaaaaaaaaa
    mask2 = ~mask1
    xwide = i64 & mask1
    ywide = i64 & mask2
    xresult = yresult = 0
    for i in range(31,-1,-1):
        tmask = 0x1 << (2*i+1)
        xresult += (xwide & tmask) >> i+1
        tmask = tmask >> 1
        yresult += (ywide & tmask) >> i
    return (xresult, yresult)

def get_quadrant64(i64):
    quad = (i64 & 0xc00000000000) >> 62
    return quad
