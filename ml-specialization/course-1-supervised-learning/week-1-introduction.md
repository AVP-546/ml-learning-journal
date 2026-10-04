# Course 1, Week 1 — Introduction to Machine Learning

Notes taken while following the Machine Learning Specialization (Coursera).

## What is Machine Learning?

Machine learning definition: "Field of study that gives computers the ability to learn without being explicitly programmed" (Arthur Samuel, 1959). For example, the definition given by Arthur Samuel came from creating a program that after playing tens of thousands of checkers games understood what positions lead to good results, when compared to the opponent's position, and what gave bad results. After all of these games it understood how to play checkers, alone.

**AGI**: Artificial General Intelligence. Human capacity of adaptation to different environments, with expert-level performance in each of them.

### Types of ML algorithms

1. Supervised Learning (most used in real-world applications + the one with most rapid advancements) -> Courses 1 and 2
2. Unsupervised Learning -> Course 3
3. Recommender Systems
4. Reinforcement Learning

All the ML algorithms try to mimic what exactly goes on inside the brain, when a human is learning.

## Supervised Learning

Supervised Learning or Supervised Machine Learning: maps an x (input) to a y (output label). The key characteristic of Supervised Machine Learning is that the program learns with examples given, where it can learn what are the right answers for each input. Therefore, it posteriorly learns the logic of this process and is able to, with only the input, predict what the output will be, with a specific confidence.

Some input/output pairs and the respective applications (3:32, "Supervised learning part 1" video):

| Input (x) | Output (y) | Application |
| --- | --- | --- |
| email | spam? (0/1) | spam filtering |
| audio | text transcripts | speech recognition |
| English | Spanish | machine translation |
| image or radar info | position of other cars | self-driving car |
| ad + user info | click? (0/1) | online advertising |
| image of product | defect? (0/1) | visual inspection, for manufacturing, for instance |

If we have a dataset that maps housing price by m^2 and the corresponding price in a specific area, we can plot this dataset in a graph. Then, if we find the best curve that fits the multiple data pairs, we can create a relatively accurate prediction of, given the area, what will be the housing price, and given the price, what will be the area of the house (this second one is less relevant, since we normally have a house we have to price and not a price we have "to house").
This is what is called a regression.

**Regression**: predict a specific number, from infinitely many possible outputs. This is also a type of Supervised Learning.

**Question**: What allows a system to learn x to y mappings? Exposure to labeled examples.

## Classification vs Regression

- Regression tries to predict a number from an infinite amount of possible outputs/y labels.
- Classification is when we have a measurable amount of possible y's. For instance, mapping tumor size in x, and benign/malignant in y as 0/1. We will have only two possible outputs for infinite possible x's. Each x can only lead to 1 or 0.

In this case, as we only have 2 possible categories, benign (0) or malignant (1), we can plot the data using only the x axis for the cm, and each point will correspond to an 'O' (benign) or an 'X' (malignant).

This would also be possible for n categories or classes, it does not have a fixed number.

Terminologically, in "Classification" Supervised Learning, we talk about classes of outputs or categories of outputs. We say that the algorithm can predict categories, such as "cat" or "dog". The difference between classification and regression, in terms of analyzing the data: classification manages a finite, small group of outputs, whereas regression refers to an infinite number of outputs. Also, usually, in SL Regression the result is a raw number; in classification, it is most of the time related to a term or range of output ("cat", "malignant", "satisfied", etc).

We can also have more than 1 input. For instance, we can plot this data by tumor size (cm) on the x axis, and patient age on the y axis. Then, each point in the 2D graph will be a round O or an X. Usually, in these cases, what the ML algorithm does is it tries to find some sort of boundary or boundaries that separate "malignant" areas from "benign" areas; therefore, when a tumor dot falls into that area, it is benign/malignant, with a relatively high confidence parameter (sometimes).

## Unsupervised Learning

If in SL we tracked inputs to labeled outputs ("right answers"), in Unsupervised Learning we plot/give the data with no label attached. Our objective is not properly to "predict" something right inside a category or range, but to find patterns in unlabeled data; basically the machine has freedom to analyze the data as it wants, and try to find out what patterns emerge, or other interesting things.

**Clustering algorithms**: grouping data together (placing unlabeled data into different clusters), in UL. For instance, the algorithm parts the whole data into different groups, needed to be analyzed separately, for different, more relevant patterns. What Google News does, for example: in the whole entirety of news on the internet, it may sort them by theme or related key-words.
Here, for example, finding all the titles with "Panda" + "zoo" + "twins" and grouping them together is a type of clustering algorithm. It is called UNSUPERVISED learning because there is no one telling the algorithm, "Okay, you have to sort these news by panda+zoo+twin". It finds out on its own. It does not have supervision and also it does not have "the right answers" (labeled data), therefore, it is unsupervised.

Example: surveying clients of a company on why they buy and where they buy from, what products they enjoy the most, etc. Then, giving this algorithm all of the data, it tries to find STRUCTURE in the data, clustering people into different groups. Therefore, by finding our major groups, our company might be able to better cater in advertising or new product launches, etc.

Summarizing: in UL, the algorithm has to find structure or categories in the data.

### Types of UL algorithms

1. Clustering: groups similar datapoints together
2. Anomaly Detection: find unusual data points
3. Dimensionality reduction: compressing datasets using fewer numbers

## Summary

- **Supervised learning**: data comes with inputs x, with labels y
- **Unsupervised learning**: data comes with inputs x, but with no labels y
- **Clustering**: groups similar datapoints together
