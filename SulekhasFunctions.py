#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class SulekhasFunctions:

   def normalizeWithinRange(self, inputcolumn, outputrange = [1,5]):
       '''
       This is a function to normalize any array of numbers to fall between a particular range.
       
       inputcolumn - input array to be normalized
       
       outputrange - Range of the output [lowerbound,upperbound]
       
       Eg: list1 = [1,2,3,4,5,6,7,7,8,9,10,11,2222,445555,1133243,35354,13213]
       normalizeWithinRange(list1, [1,4])
       
       '''
       import numpy as np
       self.inputcolumn = inputcolumn
       inputcolumn = self.inputcolumn
       
       self.outputrange = outputrange
       outputrange = self.outputrange
        
          
       data = np.array(inputcolumn) 
       datamax = np.max(data)
       datamin = np.min(data)
       upperbound = outputrange[1]
       lowerbound = outputrange[0]
       coefficient = (upperbound - lowerbound) / (datamax - datamin)
       weight = (coefficient * (data - datamin)) + lowerbound
       return weight
    
    def effective_lookup(self, left, leftkey, right, keycol, valuecol):
        '''
        This is a function to lookup and join a right dataframe to a left dataframe while there are duplicate values for the key in left table.
        
        left - Left data frame
        
        leftkey - Key column of the left data frame
        
        right - Right data frame
        
        keycol - Key column of the right data frame
        
        valuecol - Column name of the value to be merged from right data frame into left data frame
        
        Eg:
        effective_lookup(df1, "df1keycol", df2, "df2keycol", "df2valuecol")
        
        '''
        self.left = left
        left = self.left
        
        self.leftkey = leftkey
        leftkey = self.leftkey
        
        self.right = right
        right = self.right
        
        self.keycol = keycol
        keycol = self.keycol
        
        self.valuecol = valuecol
        valuecol = self.valuecol
                
        dictionary = dict([(key,value) for key,value in zip(right[keycol], right[valuecol])])
        result = left[leftkey].map(dictionary)
        return result
         
        

