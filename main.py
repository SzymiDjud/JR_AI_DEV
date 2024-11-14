from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

client.api_key = os.getenv('OPENAI_API_KEY')

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html(article_content):
    prompt = (
        "As an IT specialist, transform the following article into HTML code, using appropriate HTML tags to structure the content. "
        "Identify places where images should be inserted, using the <img> tag with the src attribute set to 'image_placeholder.jpg'. "
        "Add an alt attribute to each image with a precise prompt that can be used to generate the image. "
        "Include captions under the images using the appropriate HTML tag. "
        "Do not include any CSS styling or JavaScript code. "
        "Do not include <html>, <head>, or <body> tags.\n\n"
        
        f"Article:\n{article_content}"
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an IT specialist."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()

def save_html(file_path, html_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    article_path = 'artykul.txt'
    output_path = 'artykul.html'
    
    article_content = read_article(article_path)
    html_content = generate_html(article_content)
    save_html(output_path, html_content)

if __name__ == "__main__":
    main()