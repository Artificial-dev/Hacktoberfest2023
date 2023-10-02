import pdfkit

def convert_website_to_pdf(url, output_path):
    pdfkit.from_url(url, output_path)

if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with the URL of the website you want to convert
    output_path = "output.pdf"  # The desired output file name

    convert_website_to_pdf(url, output_path)
