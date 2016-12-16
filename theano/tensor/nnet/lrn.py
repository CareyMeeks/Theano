from __future__ import absolute_import, print_function, division

import theano
from theano.sandbox.mkl.mkl_lrn import AbstractLRN

# Move AbstractLRN and AbstractLRNGrad to theano/sandbox/mkl/mkl_lrn.py


def lrn(x, slope=1, alpha=1e-4, beta=0.75, k=2, n=5):
    if theano.sandbox.mkl.mkl_available.avail is None:
        theano.sandbox.mkl.mkl_available()

    if (theano.sandbox.mkl.mkl_available.avail is True) and (x.type.ndim == 4):
        return AbstractLRN(slope, alpha, beta, k, n)(x)
    else:
        # TODO: need a numpy implement
        raise NotImplementedError('LRN: MKL not available or dimension is wrong.')
