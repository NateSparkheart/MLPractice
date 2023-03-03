from sklearn.datasets import load_digits
import pylab as pl

digits = load_digits()


pl.gray()
pl.matshow(digits.images[4])
pl.show()
print(digits.images[4])


