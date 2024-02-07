#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Jesus D.
# DATE CREATED:       22/01/2024                           
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    name_list = listdir(image_dir)
    new_list= []
    results_dic = {}
    
    # Clean names, if the name is like this: Boston_terrier_02259.jpg, or any other name with numbers and
    # in a list like this: ['Boston_terrier_02259.jpg', 'Boston_terrier_02303.jpg', 'Boston_terrier_02340.jpg'], remove the .jpg and the numbers, if ends with "_", remove it too, and replace "_" with "
    for name in name_list:
        name = name.lower()
        name = name.replace(".jpg", "")
        name = name.replace("0", "")
        name = name.replace("1", "")
        name = name.replace("2", "")
        name = name.replace("3", "")
        name = name.replace("4", "")
        name = name.replace("5", "")
        name = name.replace("6", "")
        name = name.replace("7", "")
        name = name.replace("8", "")
        name = name.replace("9", "")
        name = name.replace("_", " ")
        name = name.strip()
        new_list.append(name)
    
    for i in range(len(name_list)):
        results_dic[name_list[i]] = [new_list[i]]   
  
    return results_dic
