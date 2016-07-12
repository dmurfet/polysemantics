# Survey of differential programming

This is a preliminary survey of the literature on differential programming, by which we mean a system which couples together some kind of deep neural network controller with a differentiable memory module. Some of the papers below are not directly about differential programming in this sense, but they are relevant to our approach to the subject. Our purpose here is to list the *models* used and the *benchmark problems* or tasks considered.

## The papers

1. Alex Graves, Greg Wayne, Ivo Danihelka "Neural Turing machines" 2014 [link](https://arxiv.org/abs/1410.5401).
2. Armand Joulin, Tomas Mikolov "Inferring Algorithmic Patterns with Stack-Augmented Recurrent Nets" 2015 [link](https://arxiv.org/abs/1503.01007).
3. Edward Grefenstette, Karl Moritz Hermann, Mustafa Suleyman, Phil Blunsom "Learning to Transduce with Unbounded Memory" 2015 [link](https://arxiv.org/abs/1506.02516).
4. Jason Weston, Sumit Chopra, Antoine Bordes "Memory Networks" 2014 [link](http://arxiv.org/abs/1410.3916).
5. Scott Reed, Nando de Freitas "Neural Programmer-Interpreters" 2015 [link](https://arxiv.org/abs/1511.06279), [video](https://www.youtube.com/watch?v=B70tT4WMyJk).
6. Wojciech Zaremba, Tomas Mikolov, Armand Joulin, Rob Fergus "Learning simple algorithms from examples" 2015 [link](http://arxiv.org/abs/1511.07275), [video](https://www.youtube.com/watch?v=GVe6kfJnRAw).
7. Arvind Neelakantan, Quoc V. Le, Ilya Sutskever "Neural Programmer: Inducing Latent Programs with Gradient Descent" 2015 [link](http://arxiv.org/abs/1511.04834).
8. Wojciech Zaremba, Ilya Sutskever "Learning to Execute" 2014 [link](https://arxiv.org/abs/1410.4615)
9. Wojciech Zaremba, Ilya Sutskever "Reinforcement Learning Neural Turing Machines - Revised" 2015 [link](https://arxiv.org/abs/1505.00521).
10. Rudy Bunel, Alban Desmaison, Pushmeet Kohli, Philip H.S. Torr, M. Pawan Kumar "Adaptive Neural Compilation" 2016 [link](https://arxiv.org/abs/1605.07969), [GitHub](https://github.com/albanD/adaptive-neural-compilation), [supplementary materials](http://www.robots.ox.ac.uk/~rudy/assets/anc-supplementary.pdf) (includes task details).
11. Caglar Gulcehre, Sarath Chandar, Kyunghyun Cho, Yoshua Bengio "Dynamic Neural Turing Machine with Soft and Hard Addressing Schemes" 2016 [link](https://arxiv.org/abs/1607.00036).
12. Łukasz Kaiser, Ilya Sutskever "Neural GPUs Learn Algorithms" 2015 [link](http://arxiv.org/abs/1511.08228), [video](https://www.youtube.com/watch?v=LzC8NkTZAF4).
13. Nal Kalchbrenner, Ivo Danihelka, Alex Graves "Grid Long Short-Term Memory" [link](https://arxiv.org/abs/1507.01526).
14. Karol Kurach, Marcin Andrychowicz, Ilya Sutskever "Neural Random-Access Machines" 2015 [link](http://arxiv.org/abs/1511.06392).
15. Sebastian Riedel, Matko Bošnjak, Tim Rocktäschel "Programming with a Differentiable Forth Interpreter" 2016 [link](https://arxiv.org/abs/1605.06640).
16. Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, Timothy Lillicrap "One-shot Learning with Memory-Augmented Neural Networks" 2016 [link](https://arxiv.org/abs/1605.06065).
17. Yuhuai Wu, Saizheng Zhang, Ying Zhang, Yoshua Bengio, Ruslan Salakhutdinov "On Multiplicative Integration with Recurrent Neural Networks" 2016 [link](https://arxiv.org/abs/1606.06630).
18. Ozan İrsoy, Claire Cardie "Modeling Compositionality with Multiplicative Recurrent Neural Networks" 2014 [link](https://arxiv.org/abs/1412.6577).
19. Wojciech Zaremba's thesis "Learning algorithms from data" 2016 [link](http://www.cs.nyu.edu/media/publications/zaremba_wojciech.pdf).
20. Marcin Andrychowicz, Karol Kurach "Learning Efficient Algorithms with Hierarchical Attentive Memory" 2016 [link](http://arxiv.org/abs/1602.03218).

## The tasks

Generally the sequence tasks are run either on sequences of binary numbers, sequences of vectors of binary numbers, or sequences of integers 0-9.

* **Copy** (*given a sequence, return the same sequence*): [1], [3], [6], [9], [14].
* **Repeat copy** (*given a sequence S and integer N, return the sequence S repeated N times*): [1], [9].
* **Reverse** (*given a sequence, return the reversed sequence*): [3], [6], [9], [14], [20].
* **Addition** (*given a pair of sequences representing integers in some base, return the sequence representing their sum*): [2], [5], [6], [12], [20].
* **Multiplication** (*given a pair of sequences representing integers in some base, return the sequence representing their product*): [6], [12].
* **Search**: [14], [20]
* **Merge**: [14], [20]
* **Sort** (*given a sequence of integers, return it in ascending order*): [1], [5], [20].
* **Bigram flipping** (*given a sequence of even length, decompose it linearly into pairs and transpose each pair*): [3].
* **De-duplicate** (*given a sequence in which every symbol is repeated consecutively N times, return the sequence with all duplicates identified*): [9].
* **Array** (*given an index and a sequence, return the element of the sequence at that index*): [14].
* **Increment** (*given a sequence of integers, increment each element*): [14].
* **Swap** (*given a sequence and two indices, swap the symbols at those indices*): [14].
* **Permutation** (*given a sequence of integers representing a permutation, and an arbitrary sequence of the same length, permute the second sequence according to the first*): [14].