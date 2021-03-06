import sys
import pypgfplots
import numpy as np

np.random.seed( 10 )

mat = np.random.rand( 10, 10 )

pypgfplots.standalone( 
        matrix = mat
        , outfile = '%s.tex' % sys.argv[0] 
        , title = 'Measurement matrix'
        , xlabel = 'Index'
        , ylabel = 'Index'
        , label = r'\bf b.'
        )
