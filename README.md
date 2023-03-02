# X or O:  A Very Exciting and Useful Machine Learning Web Application

Despite my poor penmanship, if I wrote down a list of all the digits, you'd have no problem identifying each one:

![digits1](./readme/handwritten1.png)

People are good at using a limited set of observations and extrapolating out to novel instances.  So if I now showed you my friend's list:

![digits2](./readme/handwritten2.png)

you are unlikely to be baffled by it, even though you've never seen a `7` with that _exact_ shape before.

A task which is so easy for humans that we don't even think about it, is extremely difficult to perform correctly using a computer.

But for the sake of the exercise, let's try and figure out how we might get a computer to correctly identify handwritten digits using what we already know about programming.

The first problem is representing our domain in a programming language (Python, from here on).  We can't simply write a function like this:

```python
def give_digit(image):
  return ???
```
The image has to be converted into a Python object of some sort.  We have a few options; you might be experiencing Sudoku flashbacks right about now.  What about this?

![breakdown](./readme/digits-breakdown.png)

At least conceptually, we can break the image down into smaller pieces with a grid.  And a grid can be fairly straightforwardly represented as a 2-dimensional array in Python.  What values might we use to fill up a 2D array?  

For the sake of simplicity, let's assume that a given coordinate is either filled or empty.  This `1` might be represented as:

```python
[
  [0,0,0,0,0],
  [0,0,0,1,0],
  [0,0,1,0,0],
  [0,1,0,0,0],
  [0,1,0,0,0]
]
```

Or something like that.  The level of precision necessary for our application is not obvious right now, but that's the idea.

As an aside, what letter do you think this is?

```python
a_letter = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
```

OK, now we've outsmarted the computer by translating some real-world object into a Python object.  We can go back and implement the `give_digit` function:

```python
def give_digit(image):
  if image == [
  [0,0,0,0,0],
  [0,0,0,1,0],
  [0,0,1,0,0],
  [0,1,0,0,0],
  [0,1,0,0,0]
]:
    return 1
  elif image == ...
```

Hmm, it looks like we can only identify a `1` if it's written exactly like the example.  No problem, we can just account for all the variations in our function:

```python
def give_digit(image):
  if image == [
  [0,0,0,0,0],
  [0,0,0,1,0],
  [0,0,1,0,0],
  [0,1,0,0,0],
  [0,1,0,0,0]
] or image == [
  [0,0,0,1,0],
  [0,0,0,1,0],
  [0,0,1,0,0],
  [0,1,0,0,0],
  [0,1,0,0,0]
] or image == [
  [0,0,0,1,0],
  [0,0,0,1,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,1,0,0,0]
]  or ...:
    return 1
```

If the tedium weren't enough, imagine trying to update this or find bugs in it.  What we'd really like to do is hand off the actual implementation of this function to something else, so we don't have to write and maintain it.  A nice shiny black box that just gives us the correct answer (at least most of the time).

[some black boxes](https://scikit-learn.org/stable/)

It turns out that the hardest part of developing a machine learning model is not the actual machine learning--it's figuring out what to give the model.

That scikit-learn documentation shows three different kinds of problems: classification, regression, and clustering.  

Our number interpreter is an example of a classification problem.  We have a finite and discrete set of possible answers: is it a 1, or a 2, or a 3...  Another typical example is a model that answers the question: is this email spam or not spam? 

We won't go into the other types right now, but the same basic principles are generally applicable.

We need 3 basic things 
1. Input
  - The thing we're answering a question about, transformed into (almost always) a list of numbers.  Example: an image of a digit -> a 2D array of 0s and 1s.
2. Output
  - The thing we want to know about the input.  In a classification problem, this is a set of possible answers.  There could be just 2 (spam, not spam), or many more.  You need to know the possible answers in advance (there is also "unsupervised learning," but that's another thing).
3. Model (a black box)
  - A model is basically a function that takes an input and returns an output. But models don't just exist, they have to be "trained" (customized) on data that you give them.

### Training a Model

If you want your digit guessing model to be reasonably accurate, you want to give it as much data as possible.  In the case of a supervised classification model, that training data should be labeled.  In Python, that might look like this:

```python

training_data = [
  [
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
  ],
  "1",
  [
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
  ],
  "1",
  ...
]
```


You might just happen to have a bunch of this data lying around, but more likely you'll have to get it from [somewhere else](https://www.kaggle.com/competitions/digit-recognizer/data).  And whereever you get it from, you'll have to do some thinking, cleaning and processing to get the original data into the shape you need it.  This is 90% of the work.

How do you know if you have enough data?  It's hard to say, but it's never enough.  The simpler the input/output, the less you need.


## An Mini Example
If you want to run this example, do the usual create and activate a virtual environment, and install the requirements.

Let's say that we want to create a model that will predict a customer's complaint based on the temperature inside a restaurant.  Let's also say that we have a bunch of records going back a few years that record both the temperature, and customer's complaints.  After looking through the data and doing some [Exploratory Data Analysis](https://chartio.com/learn/data-analytics/what-is-exploratory-data-analysis/), you decide that you'd like to consolidate customer's responses into three basic categories:

- Too hot
- Just right
- Too cold

You then want to be able to predict a given customer's response based on the current temperature.  After some initial data wrangling, you create a [.csv](./mini_example/raw_data.csv) file with a bunch of responses and temperatures (You can cheat and use the `generate_raw_data.py` script).

Now that we have our basic dataset, we need to do a little bit of [processing](./mini_example/process.py) to make things easier on our model (the poor thing really only understands numbers...).  Convert the responses to numbers.  This conversion is arbitrary as long as you remember how to convert (conveniently stored in `output_conversion_dict`).

At this point we have our cleaned and processed data (`prepared_data`).  We now need to do a couple things before we get to the model itself

#### Train/Test Split

We want to train our model, but we also want to have an easy way to test it out on data it hasn't seen.  There is a tension here in that we want to give our model as much data as possible so the model represents our problem domain as accurately as possible, but we also don't want some way to verify that our model actually extends to data that it hasn't seen yet.  For that reason we always split our data into a training set (usually 70-80%) and a test set (usually 20-30%).  This results in `train_samples` and `test_samples` . 

In addition to that split into training and testing data, we also want to split each division into the input data and the correct outcome.  Confusingly, the convention for input data is `X`, and the corresponding correct outcome is `Y`.  This results in `train_X`, `train_Y`, `test_x`, `test_y` where the "x" is the temperature and the "y" is the (encoded) customer's response.

Now that we have all our data ready to go, let's move on to the easy part.

#### Training the Model
There are many options for classification models.  You can, and should, play around with several when you are developing an app.  But for now we are going to use the [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/tree.html).  

Hopefully, looking at the example helps to justify everything we've just done:

```python
>>> from sklearn import tree
>>> X = [[0, 0], [1, 1]]
>>> Y = [0, 1]
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, Y)
```

In our case, `X` would be the temperatures:

```python
[[83], [65], [40], [89], [77], [82], [85], [44], [72], [66], [69], [57], [62], [81], [88], [89], [51], [55], [70], [52], [60], [81], [75], [42], [55], [91], [50], [80], [89], [76], [81], [53], [62], [79], [88], [77], [72], [69], [73], [47], [83], [83], [84], [85], [47], [44], [90], [45], [64], [44], [74], [66], [81], [88], [72], [43], [88], [76], [53], [93], [48], [91], [80], [65], [87], [42], [94], [74], [57], [67], [66], [47], [65], [85], [51], [76], [85], [86], [73], [84], [79], [47], [93], [80], [40], [44], [49], [91], [79], [55], [64], [73], [53], [61], [44], [50], [72], [83], [68], [57], [72], [64], [83], [85], [86], [62], [91], [99], [95], [46], [40], [96], [63], [93], [59], [84], [75], [77], [85], [85], [79], [60], [43], [60], [40], [47], [68], [83], [41], [61], [46], [57], [44], [72], [87], [84], [44], [76], [98], [73], [94], [44], [63], [98], [93], [55], [89], [40], [94], [59], [89], [63], [78], [66], [99], [43], [50], [98], [61], [47], [57], [91], [74], [67], [85], [64], [73], [50], [68], [83], [83], [71], [65], [44], [58], [74], [65], [99], [40], [45], [93], [81], [99], [98], [73], [46], [77], [89], [99], [40], [51], [65], [47], [50], [59], [41], [72], [71], [91], [58], [48], [61], [66], [59], [41], [70], [53], [62], [44], [47], [41], [99], [92], [72], [50], [56], [67], [92], [65], [66], [51], [60], [49], [49], [88], [40], [56], [49], [85], [69], [79], [92], [82], [66], [69], [78], [65], [74], [66], [50], [96], [61], [44], [67], [63], [62], [73], [64], [87], [72], [84], [63], [92], [65], [96], [69], [45], [86], [88], [91], [67], [99], [60], [88], [60], [99], [65], [46], [72], [40], [63], [61], [78], [65], [43], [91], [85], [52], [51], [61], [73], [79], [49], [42], [99], [98], [80], [81], [74], [48], [76], [62], [69], [67], [75], [90], [53], [42], [52], [50], [43], [87], [76], [50], [45], [68], [60], [57], [71], [97], [42], [73], [77], [56], [81], [86], [69], [91], [56], [89], [93], [97], [59], [66], [83], [99], [50], [50], [57], [74], [66], [56], [50], [45], [45], [88], [48], [91], [72], [98], [77], [60], [78], [59], [44], [50], [69], [66], [47], [91], [48], [42], [89], [55], [64], [82], [76], [70], [70], [46], [75], [47], [46], [69], [66], [52], [59], [47], [67], [83], [65], [47], [50], [67], [83], [67], [89], [43], [86], [65], [89], [98], [67], [97], [41], [97], [44], [42], [57], [86], [41], [64], [63], [95], [42], [73], [66], [96], [91], [47], [92], [40], [45], [92], [48], [48], [40], [53], [86], [89], [66], [86], [45], [64], [72], [55], [83], [77], [63], [97], [73], [68], [46], [87], [59], [94], [82], [58], [95], [98], [74], [99], [92], [90], [78], [52], [75], [58], [43], [91], [92], [54], [67], [57], [81], [65], [71], [90], [54], [98], [64], [47], [50], [71], [94], [74], [83], [54], [82], [77], [71], [95], [87], [48], [72], [53], [56], [72], [44], [91], [56], [90], [51], [40], [44], [66], [96], [50], [86], [88], [61], [93], [80], [77], [91], [67], [93], [91], [56], [95], [57], [90], [67], [78], [80], [92], [64], [65], [90], [66], [72], [86], [72], [46], [91], [74], [71], [42], [64], [43], [57], [78], [99], [82], [67], [72], [66], [89], [54], [88], [66], [43], [87], [84], [94], [79], [73], [99], [44], [59], [40], [85], [97], [78], [83], [54], [75], [75], [90], [90]]
```

and `Y` would be the encoded customer responses:

```python
[1, 1, 1, 2, 3, 3, 1, 3, 2, 1, 1, 1, 3, 1, 3, 3, 1, 1, 3, 1, 1, 1, 3, 3, 1, 3, 3, 1, 1, 2, 3, 3, 1, 1, 2, 1, 1, 3, 1, 2, 2, 1, 3, 3, 3, 1, 1, 1, 3, 2, 3, 1, 1, 2, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 1, 3, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 2, 3, 3, 1, 3, 1, 2, 3, 3, 1, 1, 3, 1, 3, 3, 3, 3, 1, 1, 1, 3, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1, 2, 1, 3, 3, 3, 1, 1, 1, 3, 2, 1, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 1, 1, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 1, 1, 2, 3, 2, 3, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 1, 3, 3, 1, 3, 3, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 1, 3, 2, 3, 1, 1, 3, 3, 3, 3, 1, 3, 3, 1, 2, 3, 1, 3, 1, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 2, 3, 2, 2, 3, 3, 2, 1, 3, 1, 1, 3, 1, 2, 1, 2, 3, 1, 2, 2, 3, 3, 1, 3, 1, 1, 3, 3, 1, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 1, 3, 3, 1, 3, 3, 1, 2, 3, 1, 2, 3, 3, 1, 1, 1, 3, 2, 2, 1, 3, 3, 3, 3, 2, 3, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 3, 3, 1, 1, 2, 3, 2, 3, 2, 1, 3, 3, 1, 3, 2, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 3, 1, 1, 3, 1, 3, 3, 3, 1, 2, 3, 1, 1, 3, 3, 3, 1, 1, 3, 1, 3, 1, 1, 1, 1, 3, 1, 1, 2, 2, 1, 1, 3, 1, 1, 3, 1, 1, 1, 3, 2, 1, 3, 1, 1, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 1, 3, 3, 1, 1, 1, 2, 3, 3, 1, 1, 2, 3, 3, 1, 3, 3, 2, 1, 3, 3, 3, 3, 1, 3, 1, 3, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 3, 1, 1, 2, 3, 1, 3, 3, 2, 3, 2, 1, 3, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 3, 1, 3, 3, 3, 2, 3, 1, 2, 1, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 1, 3, 1, 2, 1, 1, 2, 3, 3, 1, 3, 2, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 1, 2, 1, 2, 2, 1, 3, 1, 1, 3, 1, 3, 3, 3, 1, 2, 3, 3, 1, 3, 1, 3, 3, 3, 1]
```

Notice that the input needs to be a matrix, while the outcomes need to be a flat list.

Let's go ahead and train the model now.