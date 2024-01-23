from huggingface_hub import hf_hub_download
import re
from PIL import Image
from transformers import NougatProcessor, VisionEncoderDecoderModel
from datasets import load_dataset
import torch


def process_imagePdf(pdf):
    processor = NougatProcessor.from_pretrained("facebook/nougat-base")
    model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-base")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    #filepath = hf_hub_download(repo_id="hf-internal-testing/fixtures_docvqa",filename="nougat_paper.png", repo_type="dataset")
    image = Image.open(pdf)
    pixel_values = processor(image, return_tensors="pt").pixel_values
    outputs = model.generate(
        pixel_values.to(device),
        min_length=1,
        max_new_tokens=30,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
    )

    sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    sequence = processor.post_process_generation(sequence, fix_markdown=False)

    print(repr(sequence))
    return repr(sequence)
