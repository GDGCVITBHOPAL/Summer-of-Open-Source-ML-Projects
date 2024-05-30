import requests
from transformers import pipeline
import nltk
from nltk import sent_tokenize
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import pipeline

# nltk.download('punkt') # Run only once

tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang="en_XX")
#pipe = pipeline("text2text-generation", model="SnypzZz/Llama2-13b-Language-translate", tokenizer=tokenizer)
model = None
model_loaded = False


def load_model():
    global model, model_loaded
    model = MBartForConditionalGeneration.from_pretrained("SnypzZz/Llama2-13b-Language-translate") 
    model_loaded =True
    return model

def translation(text,dest_lang,dest_lang_code, src_lang_code):
  
    if(dest_lang_code == src_lang_code):
        return "Please select different languages to translate between."
    
    # headers = {"Authorization": f"Bearer {secrets_sih.api_token_header}"}
    import secret
    # print(f'Bearer {secret.api_token_header}')
    token = secret.api_token_header
    # headers = {"Authorization": str(f'Bearer {secret.api_token_header}')}
    headers = {"Authorization" : f'Bearer {token}'}
    
    # Bengali Done
    if(dest_lang == "Bengali" and src_lang_code == "en_XX"):
        API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/banglat5_nmt_en_bn"
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({
            "inputs": text,
        })
        print(output)
        return output[0]['translation_text']
    else:
        global model
        if model:
            pass
        else:
            model = load_model()
        loaded_model = model
        tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang=src_lang_code)
        #model_inputs = tokenizer(text, return_tensors="pt")
        loaded_model_inputs = tokenizer(text, return_tensors="pt")

        # translate
        generated_tokens = loaded_model.generate(
            **loaded_model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id[dest_lang_code]
        )
        output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        print(output)
        return output[0]

def main_translation(text,dest_lang_code,src_lang_code):
    
    codes = {"en_XX":"English","bn_IN":"Bengali", "en_GB":"English","gu_IN":"Gujarati","hi_IN":"Hindi","ta_IN":"Tamil","te_IN":"Telugu","mr_IN":"Marathi"}
    dest_lang = codes[dest_lang_code]
    src_lang = codes[src_lang_code]

    sentences = sent_tokenize(text)
    output = ""
    for line in sentences:
        output += translation(line,dest_lang,dest_lang_code, src_lang_code)
    return {"output":output}


print(main_translation("hello world", "hi_IN", "en_XX"))