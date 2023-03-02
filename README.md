# CAKe_analysis
These scripts conduct the behavioral analyses and create the figures reported in:

[Fritch, H. A., Moo, L. R., Sullivan, M. A., Thakral, P. P., & Slotnick, S. D. (2023). Impaired cognitive performance in older adults is associated with deficits in item memory and memory for object features. Brain and Cognition, 166, 105957.](https://www.sciencedirect.com/science/article/pii/S0278262623000143#f0015) 

## Background
Amnestic mild cognitive impairment (aMCI) is associated with disproportionate damage to the perirhinal cortex and lateral entorhinal cortex (with relative sparing of the other MTL regions). Consequently, individuals with aMCI exhibit deficits in item/object memory. 

Because most cognitive assessments used to screen for aMCI require a clinician to be present, we created the Cognitive Assessment via Keyboard (CAKe), which can be self-administered remotely. It tests the same cognitive domains as the Montreal Cognitive Assessment (MoCA), which is the most commonly employed assessment to screen for mild cognitive impairement. 

To assess the relationship between CAKe performance and perirhinal/entorhinal cortex-dependent memory function, participants (age 55 or older) completed the CAKe, a feature source memory task, and a context memory task. 
* During the context memory task, participants studied line drawings presented on either an **orange or green background** with a gray internal color. 
* During the feature memory task, participants studied line drawings presented on a gray background with either an **orange or green internal color**. 
* During the memory phase of both tasks, line drawings were presented in the center of the screen and participants identified each item as previously “orange”, previously “green”, or “new”

![image illustrating the memory tasks](https://ars.els-cdn.com/content/image/1-s2.0-S0278262623000143-gr1.jpg)

      
      
Given the relationship between perirhinal cortext damage and deficits in memory for objects and object features, we predicted that individuals at-risk for MCI (those with 'impaired' performance on the CAKe) would have preferential deficits in item memory during both tasks and source memory during the feature memory task, with relatively unimpaired performance in source memory during the context memory task.

For the analysis of CAKe scores and memory accuracies, participants were split into 'normal' (CAKe scores between 21 and 24) and 'impaired' (CAKe scores below 21) groups based on the threshold for 'impaired' performance on the MoCA. 


## Description of the scripts
* run_CAKe_ANOVA.py conducts a repeated measures ANOVA and produces the following bar graph of memory accuracies for participants with 'normal' and 'imapired' scores on the CAKe (similar to Fig. 2 in Fritch et al., 2023)  
  * The function rm22_bar_graph makes a bar graph with significance indicators for a 2x2 repeated measures design (two groups, two conditions)
![Figure_2](https://user-images.githubusercontent.com/126597042/222548529-79522b80-d3df-4009-99db-b4ddcf2a5c59.png)
* run_CAKe_corrs.py calculates the correlations between participants' CAKe scores and memory accuracies and displays these relationships as line graphs (i.e., recreates Figs. 4 and 5 in Fritch et al., 2023)
  * The function add_corr_line calculates the correlation between two variables and plots the line of best fit 
![Figure_5](https://user-images.githubusercontent.com/126597042/222549001-c5e2190d-966e-4433-ac2b-246747f80657.png)

## Description of the data
The file older_adult_data.csv contains the following variables:
* Age: participant ages
* Sex: participants' sex
* CAKe score: participants' scores on the CAKe (ranging from 6 to 24)
* context source accuracy: participants' source memory accuracies on the context memory task (i.e., accuracy in remembering the previous background color of objects)
* feature source accuracy: participants' source memory accuracies on the feature memory task (i.e., accuracy in remembering the previous internal color of objects)
* context item accuracy: participants' recogntion memory accuracies on the context memory task (i.e., accuracy in regocnizing objects as "old" or "new")
* feature item accuracy: participants' recogntion memory accuracies on the feature memory task (i.e., accuracy in regocnizing objects as "old" or "new")

