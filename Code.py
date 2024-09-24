 from transformers import pipeline 
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
captioner("/content/mada.png")
