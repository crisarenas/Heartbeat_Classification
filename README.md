# Heartbeat Classification

As seen in the ggraph below, heart sound frequencies oscillate between 10Hz and 300Hz. 

However, in the case of aortic regurgitacion the frequency can be higher than 400Hz. 

![](images/heart_freq.jpg)

The dataset is divided into two sets. Set_a comes from iSthethoscope app; set_b comes from DigiScope. 
After getting these sounds we can preprocess (filter) then to remove the frequencies that are not in a (1,500)Hz interval since those kind of noises are not produced by the heart. 


![](images/transcription_diagram.jpg)



# References:
* [Agricultural and biological sciences heart sounds.](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/heart-sounds#:~:text=Although%20the%20human%20ear%20can,from%2020%20to%20500%20Hz)

* Article: [the frequency of heart.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3396354/#:~:text=Moreover%2C%20the%20frequency%20of%20heart,of%20a%20normal%20heart%20sound.)