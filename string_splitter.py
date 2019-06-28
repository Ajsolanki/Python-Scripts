#%%

def str_spt(string):
        x= string.split(" ")
        temp_list =[]

        for i in x:
                if len(i)>= 4 and len(i)%2==0:                        
                        temp = spt(i)                
                        temp_list.append(temp[0])
                        temp_list.append(temp[1])
                        del(temp)
                else:
                        temp_list.append(i)
        return ' '.join(temp_list)

        
def spt(element):
        y = len(element)//2
        y1 = element[:y]        
        y2 = element[y:]        
        return y1,y2