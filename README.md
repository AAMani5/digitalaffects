![alt text](/images/da_logo_small.png "digitalAffect logo")

## One Line Description

An app that assesses the mood of the country based on digital data.

## Deployment

* git clone this repo
* run a virtualenv
* pip3 install -r requirements.txt
* get Twitter dev access and generate app keys
* add them as environment variables (ckey, csecret, atoken, asecret)
* run python3 app.py in command line
* open localhost:5000

## Synopsis

DigitalAffect is at the confluence of sentiment analysis, social media proliferation, and machine learning.

We felt machine learning would be the most efficient way to analyse public opinion en masse by automating the sentiment analysis process. We arrived at this conclusion by researching popular tools in this field. The majority of the researchers chose the Python-based NLTK platform for its relatively extensive corpus collection and built-in features for tailoring machine learning.

We chose Chart.js for its sleek display interface and its comprehensive functionality.

We chose Twitter for its convenient character limitation which was ideal for working with our classifier to demonstrate public opinion.

## User Stories
```
As a User,
So that the UK's mood can be assessed,
I want to be able to enter a sentence on the page.
```
```
As a User,
So that the UK's mood can be classified as positive or negative,
I want to see the word 'positive' or 'negative'.
```
```
As a User,
So that I can get an idea about what people in the UK are thinking about a topic,
I want to be able to see the percentage of people who are positive or negative about it.
```
```
As a User,
So that I have confidence I am seeing the UK public's unbiased opinion,
I want the data to come from UK-based Twitter Users via their tweets.
```
```
As a User,
So that it's easy to use the site,
I want it to have a simple interface.
```
```
As a User,
So that I can enjoy using the site,
I want the site to look nice.
```
```
As a User,
So that I can have a visual representation of the output,
I would like to see the percentages of positive and negative views represented as a pie chart.
```
```
As a User,
So I can see people's opinions,
I want to be able to see the tweets from my search results.
```
```
As a User,
So I can make another search,
I want to be able to click back to the homepage.
```

## MVP

![alt text](/images/DifferentVersions.JPG "MVP diagram")

We planned out how hopes for our first 3 MVPs. The first was a simple text input with a positive or negative string output displayed. We reached this on the second day:

![alt text](/images/negMVP.png "Trump Negative")

The MVP2 was a pie chart generated from the data given that showed multiple moods. In reality we had to scale this back to just positive and negative moods due to the challenge presented by the refinement of our classifier.

![alt text](/images/pie-1.png "MVP2 Pie chart")

MVP3 was the shiny version of our efforts with a scrolling tweet bar so you can see UK Twitter's opinions for yourself. We coupled this with added classifier refinement, though we recognise in 2 weeks it's unlikely to be perfect.

![alt text](/images/mvp3.png "MVP3 results page")

## Naive Bayes

We looked at various classifiers available to use with the NLTK Python platform for human language processing. After testing each one for accuracy we chose Naive Bayes as it gave the most consistently high accuracy ratings when tested:

![alt text](/images/naive_bayes_accuracy.png "Naive Bayes accuracy rate")

## Refining our classifier

We began refining our classifier to increase the overall accuracy category matching. This involved tailoring stopwords for our purposes, and filtering out extreme frequency values from our features. This works by removing the most common useless words from our classifiers vocabulary, and then removing features that will skew the overall accuracy of the classifiers matching process by preventing 0% or 100% feature values.

Before:

![alt text](/images/OurTrainedAccuracyBeforeRefinement.png "Before refinement")

After:

![alt text](/images/classifier_accuracy_after_refinement.png "After refinement")

## Successes

* Reached MVP on day two!
* Identified the most relevant technologies for our project and learned to use them in less than a week
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

* Communication due to group size but resolved through better feedback and regular standups
* Task implementation through fair allocation via pairing and code reviews
* Using Python with no prior knowledge
* Using machine learning algorithms and understanding them
* Getting the right datasets to train our classifier
* Refining the classifier
* Implementing a dynamic front-end interface with Flask, Javascript and JQuery
* Figuring out how to pinpoint and process the right data from external APIs
* Maintaining energy levels and work output at a steady rate
* Cutting features to keep the end goal realistic

## Contributing Code

* Ashwini Mani - https://github.com/AAMani5/NBclassifier
* Bernard Malhame - https://github.com/evebalog/playing_with_classifiers
* Eva Balog - https://github.com/evebalog/playing_with_classifiers
* Imogen Kutz - https://github.com/allthatilk/judge-twitter-people, https://github.com/allthatilk/REST-and-Streaming-Twitter-grab
* John Chang - https://github.com/JohnChangUK/NaiveBayes-streaming, https://github.com/JohnChangUK/website-backend
* Katie Koschland - https://github.com/allthatilk/judge-twitter-people, https://github.com/JohnChangUK/NaiveBayes-streaming
