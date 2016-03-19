# polysemantics
The polynomial semantics of linear logic interprets linear logic programs as matrices of polynomials. We compute these matrices using Singular and Python. If you have any questions, please don't hesitate to [get in touch](mailto:d.murfet@unimelb.edu.au).

# Installation & Usage

First you need a working installation of the commutative algebra package [Singular](https://www.singular.uni-kl.de/). Singular is available for Linux, Windows and Mac OS X and is [easy to install](https://www.singular.uni-kl.de/index.php/singular-download.html). You will also need to have installed Python and [TensorFlow](https://www.tensorflow.org/). Probably the easiest way is to use an AMI with everything [already set up](http://erikbern.com/2015/11/12/installing-tensorflow-on-aws/) (you can test that things are working using the instructions at the end of [this page](http://ramhiser.com/2016/01/05/installing-tensorflow-on-an-aws-ec2-instance-with-gpu-support/)). Good examples of using TensorFlow can be found [here](https://bcomposes.wordpress.com/2015/11/26/simple-end-to-end-tensorflow-examples/) (which is a blog about [this](https://github.com/jasonbaldridge/try-tf.git) GitHub repo).

For an explanation of the mathematics behind this code, see [Murfet](http://arxiv.org/abs/1407.2650).