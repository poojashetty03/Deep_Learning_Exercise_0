import os
import json
import itertools
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        #TODO: implement constructor
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        
        self.file_names = os.listdir(file_path)
        self.file_names.sort(key = lambda x : int(x.split(".")[0]))
        self.iterator_gen = itertools.cycle(self.file_names)
        self.next_request_count = 0


        with open(self.label_path, 'r') as j:
            self.label_json = json.loads(j.read())
        
    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        
        image_names = [next(self.iterator_gen) for _ in range(self.batch_size)]
        
        images = [np.load(self.file_path + i) for i in image_names]
        
        labels = [int(i.split(".")[0]) for i in image_names]
        
        self.next_request_count += 1

        return images, labels

    def augment(self,img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function

        return img

    def current_epoch(self):
        # return the current epoch number
        return self.next_request_count * self.batch_size // len(self.file_names)

    def class_name(self, x):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[self.label_json[x]]
    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        #TODO: implement show method
        
        images, labels = self.next()
        
        classes = [self.class_name(str(i)) for i in labels]
        
        return classes


file_path = '/home/shanur/SS22_Programs/exercise0_material/src_to_implement/exercise_data/'
label_path = '/home/shanur/SS22_Programs/exercise0_material/src_to_implement/Labels.json'
batch_size = 32
image_size = [20, 20, 3]
 
 
obj = ImageGenerator(file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False)

l1 = obj.next()
l2 = obj.next()
l3 = obj.next()
l4 = obj.next()

#l = [obj.next() for _ in range(3)]
print("Epochs")
print(obj.current_epoch())









