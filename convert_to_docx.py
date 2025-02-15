import pypandoc

# Input Markdown file
md_file = "QuantConnect_All_Docs.md"
# Output DOCX file
docx_file = "QuantConnect_All_Docs.docx"

# Convert Markdown to DOCX
pypandoc.convert_file(md_file, 'docx', outputfile=docx_file)

print(f"✅ Successfully converted {md_file} to {docx_file}")
