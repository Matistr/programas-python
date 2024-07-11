from datetime import *
import time
from IPython.display import clear_output

inicio = time.time()
while True:
    clear_output(wait=True)
    print(datetime.now().strftime("%H:%M:%S") , time.time()-inicio )
    time.sleep(1)