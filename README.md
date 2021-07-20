# LinkedIn-Scrapper
## Young professionals and graduates are often in the need of a job. As a result, they look out for opportunities in LinkedIn. However there are too many posts one has to go through to finally discover a job posting
### We saw this as an opportunity to deploy web scraping and machine learning skills to somehow boil down posts users have to go through
#### This project will scroll for few minutes and prepare a data file which can be surfed using find in page for potential hiring post.

## Approach
* Create a custom dataset using web scraper and get our LinkedIn feed
* Deploy NLP techniques of tokenization, stop-words and lemmitization for our Naive Bayes model
# Evaluation Metric
![SS-1](https://user-images.githubusercontent.com/62702112/126283455-99a3466f-1b8f-4b9e-b424-f84f07b19cbd.JPG)
# Results
![SS-2](https://user-images.githubusercontent.com/62702112/126283532-c30dacef-5725-4d3f-a11f-81fc28eff5a0.JPG)
# Detailed Report for Multinomial NB
![SS-3](https://user-images.githubusercontent.com/62702112/126283551-3cfe1c56-9103-4d3f-b10e-19d9bb9c64eb.JPG)

## How to use:
1. first install latest version of python
2. open the cmd in the folder containing repo and run "pip install -r requirements.txt"
3. add your linkedin login details in log.py
4. run the test.py file.

## Tech-Stacks
* Selenium
* Python
