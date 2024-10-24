import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: Este código sirve para modular una señal binaria en OOK versión RF, se le definen 2 entradas que son la señal binaria a modular A y el desfase Q, además se define la frecuencia del carry y la tasa de muestreo. Por último se realiza la modulación teniendo en cuenta el desfase, la frecuencia del carry, la tasa de muestreo, la amplitud y se retorna la longitud del array de salida.  """

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


