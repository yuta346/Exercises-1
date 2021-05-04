
def sum_imaginary(ilst):
    real_sum = 0
    imag_sum = 0
    for i,j in ilst:
        real_sum+=i
        imag_sum+=j
    return real_sum,imag_sum
       

ilst = [(1,2), (4,-1), (0, 0), (-2, -2)]
sum_imaginary(ilst)