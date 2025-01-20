import torch
from transformers import pipeline

import config as config


def load_model():
    """
    Loads a text generation model pipeline.

    This function initializes a text generation model pipeline using the specified
    model name, torch data type, and device map. The pipeline is configured for
    text generation tasks.

    Returns:
        pipe: The initialized text generation model pipeline.
    """
    pipe = pipeline(
        "text-generation",
        model=config.MODEL_NAME,
        torch_dtype=getattr(torch, config.TORCH_DTYPE),
        device_map=config.DEVICE_MAP,
    )
    return pipe


def generate_response(pipe, messages, max_new_tokens=256):
    """
    Generates a response based on the provided messages using the specified pipeline.

    Args:
        pipe: The pipeline object used for generating the response.
        It should have a tokenizer with an `apply_chat_template`
        method and be callable to generate outputs.

        messages (list): A list of messages to be formatted
        and used as input for the pipeline.

        max_new_tokens (int, optional): The maximum number of
        new tokens to generate. Defaults to 256.

    Returns:
        str: The generated response text.
    """

    prompt = pipe.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    outputs = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
    )
    response = outputs[0]["generated_text"].split("<|assistant|>")[-1].strip()
    return response
