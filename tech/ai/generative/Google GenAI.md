# Generative AI

Google says that it started the Generative AI revolution.

Google states that it is a leader in Large Language Models and Enterprise Solutions.

## What is GenAI?

Classical ML uses supervised or unsupervised learning to provide prediction for a given piece of data, based on prior trends.

Deep Learning is slightly more complex, in the sense that there are layers of neural networks, required to "train" a neural "model" for predictive analysis.

Generative AI is a subset of Deep Learning. 

Deep Learning has 2 types of models :

1. Discriminative - classify data points. Ex: Given an image of a dog, it classifies it as a dog.
2. Generative - generate new data points. Ex: Given an image of a dog, it generates another umage of a dog.

For any given function $$ y = f(x) $$

It is a Gen AI when $y$ is :

1. Natural Language
2. Image
3. Audio

It is not Gen AI if $y$ is :

1. Number
2. Discrete
3. Class
4. Probability

Gen AI uses training code, labeled data and unlabeled data.

Generative AI uses "Transformers". A transformer uses an "Encoder" and "Decoder". Encoder encodes the input and sends it to a decoder, which dictates how the data is supposed to be read.

Erroneous data is known as "Hallucinations".

## Difference from Predictive AI

We train a model to recognize an object, that is then used to predict based on the observed patterns, the object that it was trained for. This is the prediction AI model.

Generative AI on the other hand, creates new data from the patterns learned from the training data, which is received as supervised and unsupervised structured or unstructured data.

## Why Google AI?

1. Govern data strictly.
2. Match cost for value.
3. Grounded in factuality(Where the data, or facts come from)
4. Easy to get started
5. Manageable at scale

## Responsible AI

1. Education, research and tools
2. Product and use case reviews
3. Other responsible AI offerings

## Building blocks

1. Conservation AI
2. Enterprise Search
3. Foundation Model


Foundation models are a super set of large models. These form the basis of a lot of GenAI products.  
Vertex AI Conversation to answer complex statements.  
Vertex AI Search for custom search engines for customers and employees.  

## Use Cases

### External Customer Facing sites

1. E-Commerce
2. Media Content
3. Customer Service Support

### Functional Use Case

1. Knowledge Base Query
2. Document Repository
3. Intranet

### Technical Machine and System Logs

1. Infrastructure log query
2. Debugging reports

## Generative AI products in Google Cloud

Segments :

1. Consumer Products
2. Enterprise Products

### Consumer Products

1. Bard
2. Makersuite

The data in bard is owned by Google and is used by Google to train their data.
Makersuite is for fine tuning the experience in Bard.

### Enterprise Products

1. Vertex AI
2. Vertex AI - Search and Conversation

### Vertex AI

Contains : Model Garden and Generative AI Studio
Fine tuning of foundation models

## Model Garden

Contains a language model as well as a vision model.

Language Models include :

1. PaLM for text and chat
2. BERT

Vision Models include :

1. Embeddings extractor
2. Stable Diffusion v1-5
3. BLIP image captioning
4. BLIP VQA
5. CLIP
6. OWL ViT
7. ViT GPT2

### Generative AI decision tree

Is this an AI use case? If yes, is generative AI or existing AI products? If yes, Can this be solved with an out of the box use case? If yes, the Vertex AI Search and Conversation, or else Vertex AI.


## Vertex AI Search vs Cloud Retail Search

Cloud Retail Search is a pre-trained search for ecommerce vertical. It is intended for increasing the performance of revenue per visit. It is search as a service for ecommerce.

Decision for using cloud retail search : 

Are you earning revenue online?  
Are you selling Products?  
Does each product have it's own price?  
Does your data fit the retail product catalog schema?  
Are you interested in optimizing for Profit and Loss?  

If the answer to all of these questions is yes yje use Cloud Retail Search. If not, then Vertex AI Search.

## Vertex AI

Has state of the art models.  
Tuning, Prompting and decoding can be doe on the cloud.  
Model Management is provided along with this.  
Your Data, your terms  
Enterprise ready, out of the box.

Google AI provides tools for experimentation, training and deploying, as well as MLOps via Google's ML platform. With Vertex AI, we obtain Model Garden that provides Open Source, Task-Specific and Foundation models. It alse provides Generative AI studio, that allows for Prompt design and tuning.

### Generative AI Studio

This generates code that can be used to modify or optimize the behaviour.

### Foundation Models

They are classified into :

1. Text
2. Code
3. Image
4. Dialogue
5. Audio and Music
6. Video

They all rely on a fundamental language model called **PaLM**.

PaLM for Text and Chat - PaLM2 for Text, PaLM2 for Chat.

Embedding API for text, allows extracting semantics from unclassified data. Variety of data modality.

Codey API for Text-to-Code. Can be used for contextual code development. Provides Code Completion and Generation, a multi-turn code chatbot, with privacy. PAI is segregated into Code Generation, Code Chat and Code Completion.

Imagen for Text-to-Image. Generate images, Edit Images, Caption and Classify Images.




