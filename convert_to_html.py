import markdown

# Read the Markdown file
with open("QuantConnect_All_Docs.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Wrap in basic HTML structure
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantConnect Documentation</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; }}
        h1, h2, h3 {{ color: #003366; }}
        a {{ color: #007BFF; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Save to an HTML file
with open("QuantConnect_Docs.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_template)

print("✅ Successfully converted Markdown to HTML: QuantConnect_Docs.html")
