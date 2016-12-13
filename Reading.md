# Background reading

This is a list of background reading for the paper "Linear logic and recurrent neural networks" and program induction by neural methods, in general. For the papers, see `DPsurvey.md`. In this file we concentrate on more basic background material.

* For general background on neural networks see [Goodfellow-Bengio-Courville](http://www.deeplearningbook.org/). At a minimum, try to understand the deep feedforward network (II.6) and backpropagation for it, plus ordinary RNNs and their backpropagation (II.10). 

* Grefenstette has a nice [talk on augmented RNNs](http://videolectures.net/deeplearning2016_grefenstette_augmented_rnn/).

* The particular package we are using for training neural networks is Google's [TensorFlow](https://www.tensorflow.org/). For a clear exposition of the underlying concepts, see the [official paper](https://arxiv.org/abs/1603.04467).

* For RNNs in TensorFlow see [this](http://r2rt.com/recurrent-neural-networks-in-tensorflow-i.html) and [this](http://r2rt.com/recurrent-neural-networks-in-tensorflow-ii.html).

* The theory behind our approach is differential linear logic, which is a fancy version of automatic differentiation. For the role of automatic differentiation in machine learning and backpropagation specifically, see [these lecture notes](http://users.cecs.anu.edu.au/~jdomke/courses/sml/09autodiff_nnets.pdf) and the INRIA guide [What is automatic differentiation?](https://www-sop.inria.fr/tropics/ad/whatisad.html)
