import math



def conv_1D(signal1, signal2):
   len1 = len(signal1)
   len2 = len(signal2)
   size = len1 + len2 - 1
   pad = abs(len2 * (len1 - len2))
   signal2 += [0] * pad

   y = [0] * size
   for i in range(size):
      for j in range(len1):
         if i - j >= 0:
            y[i] += signal1[j] * signal2[i-j]
   return y

def plot_term(array):
   import time
   Y = round(max(array)) + 1
   X = len(array)
   L = 1
   for y in reversed(range(-Y, Y)):
      if y == -Y: 
         L = 0
      print(f"{y:>3} | ", end="")
      for x in range(X):
         if(L == 1):
            val = round(array[x])
            if val - y == 0:
               print("--*--", end="", flush=True)
            elif abs(val) - abs(y) > 0 and ((val >= 0 and y >= 0) or (val < 0 and y <= 0)):
               print("--|--", end="", flush=True)
            else:
               print("-----", end="", flush=True)
            #time.sleep(0.01)
         else:
            print(f"[{x:>3}]", end="")
      print()

if __name__ == "__main__":
   N = 15
   f = 1
   sin = [0] * N
   for i in range(len(sin)):
      sin[i] = math.sin(2 * f * math.pi * i / N)
   sig1 = [1]
   sig2 = [1,2,3,1,1,4,1,1]
   output = conv_1D(sin, sig2)
   print(output)
   plot_term(output)

