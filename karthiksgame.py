import random
words=['impotent','imma','poojith']
w=list(words)
g='' 
turns=10
f=0
p=0
print("Guess the right word")
i=random.randint(0,1)  
print("_ "*len(w[i]))
while turns>0:
      a=input("enter letter:  ")
      
      if a in w[i]:
        g=g+a
    
        for c in w[i]:
                 
                 if c==a:
                     f+=1
            
                 if c in g:   
            
                   print(c,end=' ')
                   
                 else:
                   
                   print("_",end=' ')
             
      print("")  
 
      if f== len(w[i]):
          print("Wohoo you won!!!")
          break
      if a not in w[i]:
          
          turns-=1
          print("wrong")
          print("turns left",turns)
     
      if turns==0:
          print(" HAHA you lost")
          print("The right word is :",w[i])
          break
          
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
     

    
              
              
         

