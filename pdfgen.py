from fpdf import FPDF

# Create an instance of FPDF
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell (rectangular area that can hold content)
pdf.cell(200, 10, txt="Hello, this is a PDF generated using fpdf2!", ln=True, align='C')

# Save the PDF to a file
pdf.output("output.pdf")

print("PDF generated successfully!")
