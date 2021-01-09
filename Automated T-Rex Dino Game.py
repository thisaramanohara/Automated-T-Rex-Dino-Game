#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the necessary modules
from PIL import ImageGrab
import numpy as np
from matplotlib import pyplot as plt
import cv2
import win32com.client as comctl


# In[ ]:


wsh=comctl.Dispatch('WScript.Shell')
wsh.AppActivate('chromedino.com')    #allow to chromedino.com


# In[ ]:


#defining the size of the tree (a box infront of the dinosaur)
#NOTE : Positions may be different in your screen. So be careful to change the positions if needed
tree_x,tree_y,tree_w,tree_h=(80,65,60,50)


# In[ ]:


while(True):
    #getting the part of the screen where the game is happening
    #NOTE : Positions may be different in your screen. So be careful to change the positions if needed
    screen=np.array(ImageGrab.grab(bbox=(220,200,1300,350)))
    
    #converting color the grabbed image
    screen=cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
    
    #getting the box from the image which is infront of the dinosaur 
    tree_window=screen[tree_y:tree_y+tree_h,tree_x:tree_x+tree_w]
    
    #getting the thresholded image of the box
    ret,tree_window_thresh=cv2.threshold(tree_window,127,255,cv2.THRESH_BINARY)
    
    #counting the number of the black pixels
    num_of_black_pixels=np.count_nonzero(tree_window_thresh==0)
    
    #counting the number of all pixels
    num_of_all_pixels=np.size(tree_window_thresh)
    
    #getting a ratio between black pixels and all pixels
    tree_ratio=num_of_black_pixels/num_of_all_pixels
    
    #if there is a tree or a bird caught into the box
    if(tree_ratio>0.05):
        #to draw a red rectangle
        cv2.rectangle(screen,(tree_x,tree_y,tree_w,tree_h),(0,0,255),-1)
        
        #to display a text
        cv2.putText(screen,'UP',(tree_x,tree_y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        
        #press UP button
        wsh.SendKeys('{UP}')
    
    #display the image
    cv2.imshow('printscreen',screen)
    
    #if you pressed ESC button , programe will quit
    if(cv2.waitKey(1)==27):
        cv2.destroyAllWindows()
        break

