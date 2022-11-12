# Autocorrection using NLP

Find out if a word is right spelled through Natural Language Processing algorithm

## Getting Started

In this model, we are going to consider **edit distance** between every pair of words in a list containing the vocabulary. Basically, edit distance is a **measure of minimum edits required to convert one word to another**.  
This process of conversion includes steps like **Delete**,**Replace**,**Switch** and **Insert** on a pair of words. 

In order to do tests the book [Alice in the Wonderland](alice_in_wonderland.txt) was used to provide the vocabulary and word to train the model.

In this project, to reduce complexity, we would go for words that are **1 or 2 edit distance away**.  
The goal of our model to produce the right output is to compute the **probability of a word being correct, _P(c/w)_ ,is probability of certain word _w_ given that is is correct, _P(w/c)_ , multiplied to probability of being correct in general, _P(c)_ , divided by probability of that word appearing, _P(w)_ .**

Formula : **𝑃(𝑐|𝑤)=𝑃(𝑤|𝑐)×𝑃(𝑐)/𝑃(𝑤)**

The method used above is called **Bayes Theorem**.

### Prerequisites

In order to use this porject you will need Python 3 and some libraries described bellow

```
re
numpy
pandas
```

### Running
To run the project on your machine you will need to clone this repository and execute the python3 command on the main.py file, as described bellow step-by-step:

```bash
git clone <project repository>
cd <project-name>
python3 main.py
```


## Built With

* [Python 3.7.3](https://www.python.org/) - One of the most high level programming languages used
* [Pandas](https://pandas.pydata.org/) - Library of data manipulation and organization
* [NumPy](https://numpy.org/) - Library to mathematical calculus on python algorithms

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/Wanghley/8d237a5e568b4e3149c0166dd010e375) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Wanghley/Word-Autocorrection-NLP/tags). 

## Authors

* **Wanghley Martins** - *Initial work* - [wanghley](https://github.com/wanghley)

See also the list of [contributors](https://github.com/Wanghley/Word-Autocorrection-NLP/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* You can use this code to integrate in your solutions to correct user's misspelled words.
* Feel free to use the code whenever you want and how you want to
* Just remember to reference me and follow the [LICENSE.md](LICENSE.md) rules
