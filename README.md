# Digital Affect

## One Line Description

An app that assesses the mood of the country based on digital data.

## User Stories
```
As a User,
So that my mood can be assessed,
I want to be able to enter a sentence.
```
```
As a User,
So that my mood can be classified as positive or negative,
I want to see the word 'positive' or 'negative'.
```
More TBA

## MVP

![alt text](https://github.com/AAMani5/digitalaffect/blob/master/images/DifferentVersions.JPG "MVP diagram")

We planned out how hopes for our first 3 MVPs. The first was a simple text input with a positive or negative string output displayed. We reached this on the second day:

![alt text](https://github.com/AAMani5/digitalaffect/blob/master/images/negMVP.png "Trump Negative")

The MVP2 was a pie chart generated from the data given that showed multiple moods. In reality we had to scale this back to just positive and negative moods due to the challenge presented by the refinement of our classifier.

Reminder: pie chart screenshot

MVP3 TBA

## Naive Bayes

We looked at various classifiers available to use with the NLTK Python platform for human language processing. After testing each one for accuracy we chose Naive Bayes as it gave the most consistently high accuracy ratings when tested:

![alt text](https://github.com/AAMani5/digitalaffect/blob/master/images/Screen%20Shot%202017-04-27%20at%2016.38.56.png "Naive Bayes accuracy rate")

## Refining our classifier

We began refining our classifier to increase the overall accuracy category matching. This involved tailoring stopwords for our purposes, and filtering out extreme frequency values from our features. This works by removing the most common useless words from our classifiers vocabulary, and then removing features that will skew the overall accuracy of the classifiers matching process by preventing 0% or 100% feature values.

Before:

![alt text](https://github.com/AAMani5/digitalaffect/blob/master/images/OurTrainedAccuracyBeforeRefinement.png "Before refinement")

After:

## Successes

* Reached MVP on day two!
* Identified the most relevant technologies for our project and learned to use them in less than a week.
* Reached MVP2 on day four which required the following to be integrated:
  * Python classifier
  * Flask web framework MVC
  * Javascript pie-chart interface
  * Twitter API tweet generation
* Regular code reviews
* Effective pairing practices
* Regular feedback
* Chocolate helps you learn!!

## Struggles

## Contributing Code

* Ashwini Mani - https://github.com/AAMani5/NBclassifier
* Bernard Malhame - https://github.com/evebalog/playing_with_classifiers
* Eva Balog - https://github.com/evebalog/playing_with_classifiers
* Imogen Kutz - https://github.com/allthatilk/judge-twitter-people, https://github.com/allthatilk/REST-and-Streaming-Twitter-grab
* John Chang - https://github.com/JohnChangUK/NaiveBayes-streaming, https://github.com/JohnChangUK/website-backend
* Katie Koschland - https://github.com/allthatilk/judge-twitter-people, https://github.com/JohnChangUK/NaiveBayes-streaming
