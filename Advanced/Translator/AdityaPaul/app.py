#User Interface 

import gradio as gr
import main

def test(text, src, dest):
  ans = main.main_translation(text,dest,src)
  return ans['output']
demo = gr.Interface(
    test,
    ["textbox",
     gr.Dropdown(
            [("English", "en_XX"), ("Hindi","hi_IN"), ("Bengali","bn_IN"), ("Gujarati","gu_IN"), ("Tamil","ta_IN"), ("Telugu","te_IN"), ("Marathi","mr_IN")], label="Source", info="Select the Source Language!"
        ), 
     gr.Dropdown(
            [("English", "en_XX"), ("Hindi","hi_IN"), ("Bengali","bn_IN"), ("Gujarati","gu_IN"), ("Tamil","ta_IN"), ("Telugu","te_IN"), ("Marathi","mr_IN")], label="Destination", info="Select the Destination Language!"
        ), 
     ],
    outputs=["textbox"],
)

demo.launch(share=True)