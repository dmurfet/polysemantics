# polysemantics
The polynomial semantics of linear logic interprets linear logic programs as matrices of polynomials. We compute these matrices using Singular and do machine learning on them with Python and TensorFlow. If you have any questions, please don't hesitate to [get in touch](mailto:d.murfet@unimelb.edu.au).

# Installation & Usage

First you need a working installation of the commutative algebra package [Singular](https://www.singular.uni-kl.de/). Singular is available for Linux, Windows and Mac OS X and is [easy to install](https://www.singular.uni-kl.de/index.php/singular-download.html). You will also need to have installed Python and [TensorFlow](https://www.tensorflow.org/). Probably the easiest way to do this is by installing the [Anaconda](https://www.continuum.io/downloads) distribution of Python 2.7 and then installing TensorFlow by running (with the Anaconda binaries in your PATH)

```
conda install -c jjhelmus tensorflow=0.9.0
```

An alternative way to get TensorFlow working is to use an AMI with everything [already set up](http://erikbern.com/2015/11/12/installing-tensorflow-on-aws/) (you can test that things are working using the instructions at the end of [this page](http://ramhiser.com/2016/01/05/installing-tensorflow-on-an-aws-ec2-instance-with-gpu-support/)). Good examples of using TensorFlow can be found [here](https://bcomposes.wordpress.com/2015/11/26/simple-end-to-end-tensorflow-examples/) (which is a blog about [this](https://github.com/jasonbaldridge/try-tf.git) GitHub repo, on which our `hidden.py` is heavily based). There is documentation for [TensorFlow slim](https://github.com/tensorflow/models/blob/master/inception/inception/slim/README.md).

For an explanation of the mathematics behind this code, see [Murfet](http://arxiv.org/abs/1407.2650).

## Specific Jupyter instructions

On an AWS machine install Anaconda simply by `wget` and then follow [these instructions](http://blog.impiyush.me/2015/02/running-ipython-notebook-server-on-aws.html) to get Jupyter notebook serving off that machine. See the [official instructions](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html) if anything goes wrong. Hopefully all you need to do is run

```
cd ~/Notebooks
jupyter notebook
```

Managing EBS volumes can get confusing, see [this](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html). Regarding running Jupyter Notebook on startup, see [these instructions](http://stackoverflow.com/questions/14297741/how-to-start-ipython-notebook-server-at-boot-as-daemon/14298766#14298766).

# Logbook - learning second digit

A binary sequence S (for example 001) can be encoded in linear logic by a proof, and the interpreted by the polynomial semantics as a matrix of polynomials. This matrix of polynomials can in turn be viewed as a vector with integer coefficients, by reading off in some principled way all the coefficients of the monomials in each entry of the matrix. Call this vector V(S). The initial test is to use a deep net classifier to learn the second digit of S from the vector V(S).

The vectors V(S) are computed by the Singular code in `binaryseq.txt`. Running this code outputs all vectors for sequences S of length L (where L is a variable set in the file) randomly putting half of the vectors in a file `data/outfile-lengthL-train.csv` and half in `data/outfile-lengthL-eval.csv`. The format of these files is that there is one row per sequence S, with the first entry being the second digit of S and the remaining entries making up the vector V(S).

The network is trained with, e.g. for `L = 7`

```
python hidden.py --train data/outfile-length7-train-second_digit.csv --test data/outfile-length7-eval-second_digit.csv --num_epochs 10 --num_hidden 5 --verbose True
```

The results we get for various values of `num_epochs` and `num_hidden` are

```
with num_epochs 100 and num_hidden 2 we get 0.7, 0.63, 0.68
with num_epochs 500 and num_hidden 2 we get 0.7, 0.54
with num_epochs 100 and num_hidden 5 we get 0.72, 0.67
with num_epochs 100 and num_hidden 10 we get 0.72
```

Obviously this is not very good; probably we need more hidden layers.

Next we tried with a different initialisation, with weights to zero rather than randomly distributed. This was way worse

```
with num_epochs 100 and num_hidden 2 we get 0.49
with num_epochs 100 and num_hidden 10 we get 0.49, 0.49
```

Ok, so we stick with `xavier` then. The above are both using `tanh` nonlinearities, using `relu` the results are

```
with num_epochs 100 and num_hidden 2 we get 0.49, 0.49
with num_epochs 100 and num_hidden 10 (xavier init) we get 0.77
with num_epochs 100 and num_hidden 10 (uniform init) we get 0.70, 0.72
```

# Logbook - learning binary sum

Next we classify on the binary sum of the digits of S. With sequence length 6, `tanh` nonlinearity and `xavier` initialisation we use a command like

```
python hidden.py --train data/outfile-length6-train-sum_of_digits.csv --test data/outfile-length6-eval-sum_of_digits.csv --num_epochs 10 --num_hidden 5 --verbose True
```

The results are:

```
with num_epochs 10 and num_hidden 5 we get 0.95, 0.975
```

So, pretty good. Now we do the same thing with sequences of length 7, `tanh` and `xavier` again.

```
with num_epochs 10 and num_hidden 5 we get 0.974, 1.0
```

Probably we should choose a vector encoding with less zeros, so we can do longer sequences. OK, we did that, and things still work: now we get `0.98, 0.98` on length 7, and it is significantly faster. Finally, on sequences of length 8 we get

```
with num_epochs 10 and num_hidden 5 we get 0.99, 1.0, 1.0
```

# Logbook - learning majority ones

Classify a binary sequence S of length L as `1` if the number of ones occurring in S is greater than or equal to L/2, and as `0` otherwise. 

```
python hidden.py --train data/outfile-length7-train-half_ones.csv --test data/outfile-length7-eval-half_ones.csv --num_epochs 10 --num_hidden 5 --verbose True
```

The results of learning this classification are:

```
length 5: with num_epochs 10 and num_hidden 5 we get 1.0, 0.82, 0.86
length 6: with num_epochs 10 and num_hidden 5 we get 0.94, 0.86, 0.77
length 7: with num_epochs 10 and num_hidden 5 we get 1.0, 0.96, 0.98
```

Next we try to visualise this with [TensorBoard](https://www.tensorflow.org/versions/r0.7/how_tos/summaries_and_tensorboard/index.html) (sample code [here](https://github.com/tensorflow/tensorflow/blob/r0.7/tensorflow/examples/tutorials/mnist/mnist_with_summaries.py)). Note that you probably have to [install other stuff](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tensorboard/README.md). To open a port for the python webserver on an EC2 machine, see [these instructions](http://stackoverflow.com/questions/5004159/opening-port-80-ec2-amazon-web-services/10454688#10454688).

```
tensorboard --logdir=/home/ubuntu/polysemantics/mnist_logs
```

# Logbook - change in input format

Now we run `hidden.py` as follows, to train on length 7 sequences the `half_ones` type classifier, with log file written to `/home/ubuntu/polysemantis/logs/half_ones`:

```
python hidden.py --name second_digit --length 6 --num_epochs 10 --num_hidden 5
python hidden.py --name second_digit --length 8 --num_epochs 10 --num_hidden 5
python hidden.py --name half_ones --length 6 --num_epochs 10 --num_hidden 5
python hidden.py --name half_ones --length 7 --num_epochs 10 --num_hidden 5
python hidden.py --name sum_of_digits --length 7 --num_epochs 10 --num_hidden 5
python hidden.py --name sum_of_digits --length 8 --num_epochs 10 --num_hidden 5
tensorboard --logdir=/home/ubuntu/polysemantics/logs
```