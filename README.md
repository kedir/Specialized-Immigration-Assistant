<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
--



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> Specialized-Immigration-Assistant-LLM-Chatbot

</h3>

</div>



<!--PROJECT Describtion-->
## Project Description

<p align="justify">
The Specialized Immigration Assistant LLM is an innovative application that leverages the power of LLAMA2, a Large Language Model, to provide specialized legal assistance in the field of immigration law. Our project aims to make legal information more accessible and comprehensible to users seeking guidance in US immigration matters.
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--PROJECT Objective-->
## Key Features:

<p align="justify">

    <strong>Training with Legal Articles:</strong> We utilized a comprehensive collection of legal articles sourced from a prominent Law group to train and fine-tune the LLAMA2 Large Language Model.

    <strong>Customized Immigration Assistant Model:</strong> We tailored LLAMA2's capabilities to create a specialized Immigration Assistant model that understands and generates accurate legal language for immigration-related queries.

    <strong>Improved Accuracy:</strong> By fine-tuning the model on a rich dataset of legal nuances and terminology, we achieved improved accuracy and context-specific responses.

    <strong>Real-time Immigration Information:</strong> We are actively working on enabling users to access reliable and up-to-date legal information through an AI interface, contributing to more informed decision-making in US immigration matters.

</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--Built With-->
## Built With
* Python
* Numpy (Use matrix math operations)
* PyTorch (Build Deep Learning models)
* Datasets (Access datasets from huggingface hub)
* Huggingface_hub (access huggingface data & models)
* Transformers (Access models from HuggingFace hub)
* Trl (Transformer Reinforcement Learning. And fine-tuning.)
* Bitsandbytes (makes models smaller, aka 'quantization')
* Sentencepiece (Byte Pair Encoding scheme aka 'tokenization')
* OpenAI (Create synthetic fine-tuning and reward model data)
* Peft (Parameter Efficient Fine Tuning, use low rank adaption (LoRa) to fine-tune)
* Jupyter Notebook

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--Data Source-->
## Data Sources

<p align="justify">

* The dataset provided by private Legal firm and is not included in the GitHub repository for data privacy reasons.

</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!--Named Entity Recognation-->
## Named Entity Recognition

<p align="justify">

* NER is a widely used NLP technique that recognizes entities contained in a piece of text, commonly things like people organization, locations etc. This project also includes an NER model implemented using [BERT](https://arxiv.org/abs/1810.04805) and huggingface PyTorch library to quickly and efficiently fine-tune the BERT model to do the state of the art performance in Named Entity Recognition. The transformer package provides a BertForTokenClassification class for token-level predictions. BertForTokenClassification is a fine-tuning model that wraps BertModel and adds a token-level classifier on top of the BertModel. The token-level classifier is a linear layer that takes as input the last hidden state of the sequence. 

* Below is an example of an input and output of our named entity model, served with a streamlit app.

![alt text](https://github.com/kedir/GLG--Topic-Modeling-and-Document-Clustering/blob/main/doc/ner_example.png)

</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation
1. Install all dependencies using [pip](https://pip.pypa.io/en/stable/installation/)

  ```sh
   pip install numpy pandas torch datasets huggingface_hub transformers trl bitsandbytes sentencepiece openai peft evaluate rouge_score
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Training
<p align="justify">

To train the Immigration Assistant model, you have the option to execute the llam2_training.ipynb notebook either locally on your machine or remotely through a cloud service such as Google Colab Pro. It's important to note that the training process requires the availability of a GPU for optimal performance.

In case you don't have access to a GPU, a convenient and cost-effective alternative is to utilize Google Colab Pro, which is available at a monthly cost of $10.

For those interested in gaining deeper insights into the training process and the nuances of our specialized Immigration Assistant model, you can explore detailed information within the llam2_training.ipynb notebook. This notebook provides a comprehensive overview of the training methodology and the underlying mechanisms that make the Immigration Assistant so effective in providing accurate legal guidance for immigration-related queries.
</p>
<strong>Cloud Training</strong>

click here: https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot/blob/main/notebooks/llam2_training.ipynb/ 

<strong>Local Training</strong>

  ```sh
    git clone https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot.git
    cd notebooks
    jupyter llam2_training.ipynb
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Support -->
## Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* <strong>Kedir Ahmed</strong> - [@linkedin](https://www.linkedin.com/in/kedir-ahmed/) - [kedirhamid@gmail.com](kedirhamid@gmail.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- References -->
## Acknowledgments
<strong>Meta</strong>
<strong>HuggingFace</strong>
<strong>OpenAI</strong>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/kedir/Specialized-Immigration-Assistant-LLM-Chatbot.svg?style=for-the-badge
[forks-url]: https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot/network/members
[stars-shield]: https://img.shields.io/github/stars/kedir/Specialized-Immigration-Assistant-LLM-Chatbot.svg?style=for-the-badge
[stars-url]: https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot
[issues-shield]: https://img.shields.io/github/issues/kedir/Specialized-Immigration-Assistant-LLM-Chatbot.svg?style=for-the-badge
[issues-url]: https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot/issues
[license-shield]: https://img.shields.io/github/license/kedir/Specialized-Immigration-Assistant-LLM-Chatbot.svg?style=for-the-badge
[license-url]: https://github.com/kedir/Specialized-Immigration-Assistant-LLM-Chatbot/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kedirahmed
