import math

def conv_1D(signal1, signal2):
   len1 = len(signal1)
   len2 = len(signal2)
   pad = len1 - 1
   size = len2 + pad
   signal2 += [0] * pad

   y = [0] * size
   for i in range(size):
      for j in range(len1):
         if i - j >= 0:
            y[i] += signal1[j] * signal2[i-j]
   return y

def plot_term(signal):
   import time
   Y_SCALE = 20
   Y = round(max(signal)) + 1
   X = len(signal)
   L = 1
   yaxis = [(Y - i * (2 * Y / Y_SCALE)) for i in range(Y_SCALE + 1)]
   for y in yaxis:
      if y == -Y: 
         L = 0
      print(f"{y:> 5.1f} | ", end="")
      for x in range(X):
         if(L == 1):
            val = signal[x]
            if abs(val - y) <= float(Y) / float(Y_SCALE):
               print("-◈-", end="", flush=True)
            elif abs(val) - abs(y) > 0 and ((val >= 0 and y >= 0) or (val < 0 and y <= 0)):
               print("-┃-", end="", flush=True)
            else:
               print("---", end="", flush=True)
            time.sleep(0.0010)
         else:
            print(f"{x:>2}|", end="")
      print()

if __name__ == "__main__":
   N = 20
   f = 1
   sin = [0] * N
   for i in range(len(sin)):
      sin[i] = math.sin(2 * f * math.pi * i / N)
   sig1 = [-4, 3, 7, 0]
   sig2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
   output = conv_1D(sin, sig2)
   print(output)
   plot_term(output)

