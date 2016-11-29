# TensorFlow notes

*  [Tensor Ranks, Shapes and Types](https://www.tensorflow.org/versions/r0.10/resources/dims_types.html). The [None element in a shape](https://www.tensorflow.org/versions/r0.10/resources/faq.html) corresponds to a variable-sized dimension.

*  The API documentation for [Tensor ops](https://www.tensorflow.org/versions/r0.10/api_docs/python/array_ops.html#reshape) such as `tf.reshape`, `tf.transpose`, etc.

*  [RNN reference](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell.py): code for BasicRNNCell.

*  In generating data for an RNN or LSTM a common tensor shape is `(batch_size, n_steps, input_size)` so that for an input tensor `T`, the scalar `T[i,j,k]` is the `k`th coefficient of the vector which occurs as the `j`th time-step of the `i`th training sample in the batch. That is, the `i`th training sample is the sequence of vectors `T[i,0], T[i,1], ..., T[i, n_steps-1]`. See for example [here](http://mourafiq.com/2016/05/15/predicting-sequences-using-rnn-in-tensorflow.html) or [here](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/dynamic_rnn.py). *Confusion:* arrays are 0-indexed but it's not clear to me in TF shapes whether the shape [9] means that it has 9 entries, or indices 0,...,9.

* The foundational stuff in Oreilly "Hello, Tensorflow!" is quite good, on e.g. the graph

* The documentation `g3doc/get_started/basic_usage.md` is pretty clear

* ALso see `g3doc/api_docs/python/math_ops.md`



