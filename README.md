## Link download weight VGG-M
vggm.pth weight (https://data.lip6.fr/cadene/pretrainedmodels/vggm-786f2434.pth)
## Link download datasets VOT, OTB
https://www.votchallenge.net/challenges.html

http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html
## Structure
```
├── datasets 
        ├── data
                ├── otb   
                        ├── Basketball
                                ├── img
                                        ├── ....jpg
                                ├── groundtruth_rect.txt
                        ├── Biker
                                ├── img
                                        ├── ....jpg
                                ├── groundtruth_rect.txt
                        ├── (continue till last class)
                                
                ├── vot13
                        ├── bicycle
                                ├── ....jpg
                                ├── camera_motion.label
                                ├── groundtruth.txt
                                ├── (and other files)
                        ├── bolt    
                                ├── (similar structure with bicycle)
                        ├── (continue till last class)
                ├── vot14
                        ├── (similar structure with vot13)
                ├── vot15
                        ├── (similar structure with vot13)
├── utils
        (toolbox for drawing and scheduling)
        ├── videolist
                ├── vot13-otb.txt
                ├── vot14-otb.txt
                ├── vot15-otb.txt
├── vggm.pth
        (the vggm weights for the base network)
```

## Usage examples
*  ADNet - train 
    ```bash
    python mains_ADNet.py --visualize True
    ```
    
-------------------------------------------

*  ADNet_test
    ```bash
    python mains_ADNet_test.py --save_result_images results_on_test_images --display_images False
    ```

-------------------------------------------
*  Examples on creating plot
    ```bash
    python create_plots.py --bboxes_folder results_on_test_images/ADNet_RL_-0.5 --show_plot False --save_plot_folder results_on_test_images/ADNet_RL_-0.5
    ```
    
