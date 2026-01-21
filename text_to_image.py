from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, dtype=torch.float32) #a maioria dos modelos vai usar float32, usando float16 faremos ele ser mais leve 
pipe = pipe.to("cuda") #modelos do diffusers são dessa forma, no transformers é direto na criação do modelo

prompt = "A photo of a programmer coding in Python"
image = pipe(prompt).images[0]  
    
image.save("programmer_coding.png")