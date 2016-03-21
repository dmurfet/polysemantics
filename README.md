# polysemantics
The polynomial semantics of linear logic interprets linear logic programs as matrices of polynomials. We compute these matrices using Singular and Python. If you have any questions, please don't hesitate to [get in touch](mailto:d.murfet@unimelb.edu.au).

# Installation & Usage

First you need a working installation of the commutative algebra package [Singular](https://www.singular.uni-kl.de/). Singular is available for Linux, Windows and Mac OS X and is [easy to install](https://www.singular.uni-kl.de/index.php/singular-download.html). You will also need to have installed Python and [TensorFlow](https://www.tensorflow.org/). Probably the easiest way is to use an AMI with everything [already set up](http://erikbern.com/2015/11/12/installing-tensorflow-on-aws/) (you can test that things are working using the instructions at the end of [this page](http://ramhiser.com/2016/01/05/installing-tensorflow-on-an-aws-ec2-instance-with-gpu-support/)). Good examples of using TensorFlow can be found [here](https://bcomposes.wordpress.com/2015/11/26/simple-end-to-end-tensorflow-examples/) (which is a blog about [this](https://github.com/jasonbaldridge/try-tf.git) GitHub repo).

For an explanation of the mathematics behind this code, see [Murfet](http://arxiv.org/abs/1407.2650).

On a machine where TensorFlow is installed, you can run for example

```
python hidden.py --train data/outfile-length5-train.csv --test data/outfile-length5-eval.csv --num_epochs 10 --num_hidden 5 --verbose True
```

# Initial results

A binary sequence S (for example 001) can be encoded in linear logic by a proof, and the interpreted by the polynomial semantics as a matrix of polynomials. This matrix of polynomials can in turn be viewed as a vector with integer coefficients, by reading off in some principled way all the coefficients of the monomials in each entry of the matrix. Call this vector V(S). The initial test is to use a deep net classifier to learn the second digit of S from the vector V(S).

The vectors V(S) are computed by the Singular code in `binaryseq.txt`. Running this code outputs all vectors for sequences S of length 7, randomnly putting half of the vectors in a file `data/outfile-length7-train.csv` and half in `data/outfile-length7-eval.csv`. The format of these files is that each row represents a sequence S, with the first entry being the second digit of S and the remaining entries making up the vector V(S).

The network is trained with

```
python hidden.py --train data/outfile-length7-train.csv --test data/outfile-length7-eval.csv --num_epochs 10 --num_hidden 5 --verbose True
```

The results we get for various values of `num_epochs` and `num_hidden` are

```
with num_epochs 100 and num_hidden 2 we get 0.7, 0.63, 0.68
with num_epochs 500 and num_hidden 2 we get 0.7, 0.54
with num_epochs 100 and num_hidden 5 we get 0.72, 0.67
with num_epochs 100 and num_hidden 10 we get 0.72, 
```