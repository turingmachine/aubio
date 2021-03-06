from aubio import filterbank, fvec

f = filterbank(9, 1024)
freq_list = [60, 80, 200, 400, 800, 1600, 3200, 6400, 12800, 15000, 24000]
freqs = fvec(freq_list)
f.set_triangle_bands(freq_list, 48000)
f.get_coeffs().T

from pylab import loglog, show
loglog(f.get_coeffs().T, '+-')
show()

