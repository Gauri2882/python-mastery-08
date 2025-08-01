""" Project: Markdown to HTML Converter """

import markdown

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:  # Fix encoding
        return file.read()

def convert_markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def wrap_in_html_template(content):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markdown to HTML</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            h1, h2, h3 {{
                color: #333;
            }}
            a {{
                color: #1a73e8;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html_template

def write_html_file(html_content, output_path):
    with open(output_path, "w", encoding="utf-8") as file:  # Fix encoding
        file.write(html_content)

def main():
    print("Welcome to the Markdown to HTML Converter!")
    markdown_file = input("Enter the path to your Markdown file: ")
    output_file = input("Enter the path to save HTML file (include .html at end): ")

    try:
        markdown_text = read_markdown_file(markdown_file)
        html_content = convert_markdown_to_html(markdown_text)
        html_with_template = wrap_in_html_template(html_content)
        write_html_file(html_with_template, output_file)
        print(f"\n✅ Successfully converted and saved to: {output_file}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()