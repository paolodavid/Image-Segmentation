# -*- coding: utf-8 -*-

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

import pixellib
from pixellib.semantic import semantic_segmentation
from pixellib.instance import instance_segmentation

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def imgg(immg):
  segment_image = semantic_segmentation()
  segment_image.load_pascalvoc_model("./deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 
  segment_image.segmentAsPascalvoc("./"+immg, output_image_name = "static/"+immg, overlay = True)

def pimgg(immg):
  segment_image = instance_segmentation()
  segment_image.load_model("./mask_rcnn_coco.h5") 
  segment_image.segmentImage("./"+immg, output_image_name = "static/2"+immg)
