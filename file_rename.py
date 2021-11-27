import os
 
print(os.getcwd())
 
for a in enumerate(os.listdir("data/twitter")):
    
     print(a[1])
     path1 = "data/twitter/" + a[1]
     
     for b in enumerate(os.listdir(path1)):
         
        print (b[1])
        path2 = "data/twitter/" + a[1] + "/" + b[1]
        
        for c in enumerate(os.listdir(path2)):
            
            string = c[1]
            new = string.replace(":", "_")

            path3old = "data/twitter/" + a[1] + "/" + b[1] + "/" + c[1]
            path3new = "data/twitter/" + a[1] + "/" + b[1] + "/" + new
            
            os.rename(path3old, path3new)
            
            
            
