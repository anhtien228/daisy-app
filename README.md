# Text Summarizer Daisi

## About The Project

The main scope of this project is to build a simple API that summarize the documents input by user. The summarization can be extractive or abstractive, depending on the aim of the application. The development of the web application involve simple one-page design, elements and colors since I love minimalistic.

For the Natural Language Processing (NLP) model, I choose to use the Sequence-2-Sequence model for summarization task. Among the models that I have investigated, BART (Bidirectional Auto-Regressive Transformers) from Facebook has a very good performance in providing abstractive summary (or extractive, if needed). Therefore, I decide to use it for my web application.

## How it works

BART model was introduced at Facebook Research at ACL 2020. It has the ability to generate text based on the information from the encoder, i.e it is specifically used for **sequence-to-sequence** problem compared to BERT (Bidirectional Encoder Representations from Transformers) which only pretrains on encoder, not decoder.

The most used BART model would be base-sized BART provided by Facebook. A distilled version of BART has been implemented by many researchers. One remarkable study was conducted by `Sam Shleifer and Alexander M. Rush`, where three distillation approaches direct knowledge distillation, pseudo-labeling, and shrink and fine-tune (SFT), were compared. In this project, I decided to used the distilled BART model by Sam Shleifer (`distilbart-12-6-cnn`) and fine-tuned it on the datasets `multi_news`. Using the pre-trained model only is actually good enough. But as I have mentioned, I'd like to fine-tune and implement it by myself so I could learn something new during the progress.

The fine-tuned model could be viewed via [datien228/distilbart-cnn-12-6-ftn-multi_news](https://huggingface.co/datien228/distilbart-cnn-12-6-ftn-multi_news)

_For more information about BART model and the dataset, please refer to:_
* [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://scontent.fsgn13-2.fna.fbcdn.net/v/t39.8562-6/106373513_3414102562251474_8005430471454563564_n.pdf?_nc_cat=105&ccb=1-7&_nc_sid=ae5e01&_nc_ohc=7lT9fZ6UN2kAX8hIzMr&_nc_ht=scontent.fsgn13-2.fna&oh=00_AT-pEWAFUAr2sylDWGJwd_LnXEB3q9ajv3p3KmRY_EwA9g&oe=62CEF084)
* [Pre-trained Summarization Distillation](https://arxiv.org/abs/2010.13002)
* [multi_news dataset](https://huggingface.co/datasets/multi_news)


## Usage

The usage is quite simple with one input parameter. API will take in the text from user (it could be either short or long paragraph).
The output will be returned as a summary of the text that has been processed.

## Contact

Linkedin: [atien228](https://www.linkedin.com/in/atien228/)

Email: d.atien228@gmail.com

Project Link: [daisy-app](https://github.com/anhtien228/daisy-app)


## Acknowledgments

Here is the list of resources that I have found during the research and I believe it would be useful for you too.

* [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
* [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://scontent.fsgn13-2.fna.fbcdn.net/v/t39.8562-6/106373513_3414102562251474_8005430471454563564_n.pdf?_nc_cat=105&ccb=1-7&_nc_sid=ae5e01&_nc_ohc=7lT9fZ6UN2kAX8hIzMr&_nc_ht=scontent.fsgn13-2.fna&oh=00_AT-pEWAFUAr2sylDWGJwd_LnXEB3q9ajv3p3KmRY_EwA9g&oe=62CEF084)
* [Transformers](https://towardsdatascience.com/transformers-89034557de14) 
* [Understanding Attention In Deep Learning](https://towardsdatascience.com/attaining-attention-in-deep-learning-a712f93bdb1e)
