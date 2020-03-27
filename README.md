# Text_Detection_Synthetic_DataGenerator

This project is aimed at generating synthetic data for training text localization/detection methods especially for OCR solutions. 

## Intuition behind the project
All most, all of the open source datasets for text localizations([ICDAR](https://rrc.cvc.uab.es/), [SynthText](https://github.com/ankush-me/SynthText),[COCO](https://vision.cornell.edu/se3/coco-text-2/#download), etc) are made of natural images. for instance, text inside an advertisement board, etc. But, most of the OCR problems involve, getting texts extracted from pdf documents/scanned images which, mostly contain texts with in white backgrounds. We dont actually need to train a localiser model with a lot of natural images in such a usecase, instead if we can train on data, in which texts are embedded in white background, it makes more sense.

Since scanned documents contain noise, i tried to generate data with multiple noise types also. Right now, the project support gaussian, salt&pepper, poisson and speckle noise types.

## Requirements
1. Python (any version would do)
2. numpy
3. opencv
4. PIL
5. tqdm

## How to run

The synthetic data generator generates random texts from a specidfied text corpus, by sampling from hundreds of font types and font sizes. specify all the requirements as arguments inside the run.py file and run the script.

``` python run.py      ```

Note: Here, i have added a separate corpus for dates, since in my usecase, i had to detect a lot of dates within the images.

## Output

The generator will generate syntetic data and save inside the output folder mentons as the argument. It also saves a ground truth file with same name as the image. Groundtruth file format is mainteained similar to ICDAR format

``` x0,y0,x1,y1,x2,y2,x3,y3,<text>```

## samples
**Sample1 (with noise)**
<img src="https://github.com/vinayakkailas/Text_Detection_Synthetic_DataGenerator/blob/master/samples/img_1.jpg" />
**Sample2 (without noise)**
<img src="https://github.com/vinayakkailas/Text_Detection_Synthetic_DataGenerator/blob/master/samples/img_4.jpg" />

## TODO

Right now this is in very naive shape. There are lot of additions we can do to create more useful data.

- [x] sampling from font styles
- [x] sampling from font sizes
- [x] sampling text from corpus
- [ ] sampling text from wikipedia
- [ ] adding more noise types
- [ ] option to choose background image



