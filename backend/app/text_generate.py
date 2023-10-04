import re
import os
import torch
from trl.core import LengthSampler
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class textModel:
    
    def __init__(self, model_id):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        if torch.cuda.is_available():
            self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
        # pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
        self.model.eval()

    def remove_incomplete_last_sentence(self, text):
        # Split the text into sentences using a simple regex pattern
        sentences = re.split(r'(?<=[.!?])\s+', text)

        # Check if the last sentence ends with a period
        if sentences and not sentences[-1].endswith('.'):
            sentences.pop()  # Remove the incomplete last sentence

        return ' '.join(sentences)

    # def generate_text(self, question):
    #     prompt = f"[INST]{question.strip()}[/INST]"
    #     input_ids = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids

    #     output_min_length = len(input_ids[0]) + 50
    #     output_max_length = len(input_ids[0]) + 100
    #     output_length_sampler = LengthSampler(output_min_length, output_max_length)
    #     max_new_tokens = output_length_sampler()
    #     output = self.model.generate(input_ids=input_ids, max_new_tokens=max_new_tokens, top_k=200, top_p=0.6, temperature=1.0)
    #     text_output = self.tokenizer.decode(output[0], skip_special_tokens=True)

    #     text_output = text_output.split('[/INST]')[1]
    #     text_output = self.remove_incomplete_last_sentence(text_output)
    #     response_object = {
    #         "response": text_output
    #         }

    #     return response_object

    def generate_text(self, question):
        prompt = f"[INST]{question.strip()}[/INST]"
        
        # Tokenize on CPU
        if torch.cuda.is_available():
            input_ids = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids.cuda()
        else:
            input_ids = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids.to('cpu')

        output_min_length = len(input_ids[0]) + 50
        output_max_length = len(input_ids[0]) + 100
        output_length_sampler = LengthSampler(output_min_length, output_max_length)
        max_new_tokens = output_length_sampler()
        
        # Generate on CPU
        if torch.cuda.is_available():
            output = self.model.generate(input_ids=input_ids, max_new_tokens=max_new_tokens, top_k=200, top_p=0.6, temperature=1.0)
            text_output = self.tokenizer.decode(output[0], skip_special_tokens=True)
        else:
            output = self.model.generate(input_ids=input_ids.to('cpu'), max_new_tokens=max_new_tokens, top_k=200, top_p=0.6, temperature=1.0)
        # Decode on CPU
            text_output = self.tokenizer.decode(output[0].to('cpu'), skip_special_tokens=True)

        text_output = text_output.split('[/INST]')[1]
        text_output = self.remove_incomplete_last_sentence(text_output)
        response_object = {
            "response": text_output
        }

        return response_object

        