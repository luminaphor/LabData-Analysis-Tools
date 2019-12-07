def compute_y(x,m,b):
    return m*x+b

#sqare errors, add, divide

def compute_all_y(list_of_x,m,b):
    y_p=[]
    for x in list_of_x:
        y_p.append(compute_y(x,m,b))
    return y_p

def compute_mse(list_of_known,list_of_predictions):
    error=[]
    pIndex=0
    errorCount=0
    
    for num in list_of_known:
        error.append((num-list_of_predictions[pIndex])**2)
        errorCount+=1
        pIndex+=1
        
    MSE=(sum(error))/errorCount
    return MSE
    
def getMinError(x,y):
  y_p=[]
  error=[]
  m=0
  b=0
  pIndex=0
  errorCount=0
  step=0.01
  MSE=1.1
  minMSE=1

      if MSE>minMSE:
          for i in range(1000):
              m+=step
              b+=step
      elif MSE<0:
          for i in range(1000):
              m-=step
              b-=step    

      for num in x:
          y_p.append(m*num+b)

      for num in y:
          error.append((num-list_of_predictions[pIndex])**2)
          errorCount+=1
          pIndex+=1

      MSE=(sum(error))/errorCount
