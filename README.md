[![Ceasefire Now](https://badge.techforpalestine.org/ceasefire-now)](https://techforpalestine.org/learn-more)

Tweet Pulse
===========
This tool utilizes Google's [Natural Language Processing API](https://cloud.google.com/natural-language/) to analyze the sentiment behind a piece of text.

Google's NLP library handles sentence tokenization already.

Manual Setup
------------
* Using a Gmail account, create a new [Google Cloud Platform project](https://cloud.google.com/natural-language/docs/quickstart#set_up_a_project)
* Install the [Cloud SDK](https://cloud.google.com/sdk/docs/) for the operating system of your choice. This example runs on a Linux machine.
* Create a [Service Account](https://cloud.google.com/docs/authentication/getting-started) as described in the link and update the path to **GOOGLE_APPLICATION_CREDENTIALS** in `start.sh.example` with yours.
* Create a *virtualenv* for this project e.g. 
```
$ virtualenv name_of_my_env --python=python2
```
* Activate the *virtualenv* and install the project requirements via 
```
$ source name_of_my_env && pip install -r requirements.txt
```
* Rename `start.sh.example` to `start.sh`, change permissions on `start.sh` to make it executable. e.g. on Linux 
```
$ mv start.sh.example start.sh
$ chmod +x start.sh
```
* Launch the app from within the *virtualenv* by executing the following: 
```
$ ./start.sh
```

Usage
-----
* Enter a piece of text in the box shown and click the **Get Sentiments** button to see results OR
* Enter a twitter handle in the box provided and click **Get Tweets and Sentiments** button to see results

Screenshots
-----------
*Form*:

![Enter one or more sentences](https://github.com/inspaya/tweet_pulse/blob/master/tweet_pulse_enter_sentence.png)

*Sample Results*:

![Sentiment analyzed](https://github.com/inspaya/tweet_pulse/blob/master/tweet_pulse_results.png)
 

Todo
----
* Add Unit Tests
* Add Mood Prediction based on the sentiments analyzed over a given time frame.
