import sys
import argparse
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os


# Configure Tesseract path (if not in system PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

def ocr_image(image, lang='chi_sim+eng'):
    """Perform OCR on a PIL image using Tesseract."""
    return pytesseract.image_to_string(image, lang=lang)


def convert_pdf_to_images(pdf_path, dpi=300):
    """Convert PDF pages to PIL images."""
    return convert_from_path(pdf_path, dpi=dpi, poppler_path=r'')  # Add poppler path if needed


def extract_text_with_ocr(pdf_path, lang='chi_sim+eng', dpi=300):
    """Extract text from PDF using OCR."""
    images = convert_pdf_to_images(pdf_path, dpi)
    full_text = []

    for i, image in enumerate(images):
        text = ocr_image(image, lang)
        full_text.append(text)
        print(f"Processed page {i + 1}/{len(images)} with OCR")

    return '\n'.join(full_text)


def extract_text_from_pdf(file_path, output_file=None, use_ocr=False, ocr_lang='chi_sim+eng'):
    """
    Hybrid text extraction: Uses OCR if specified, otherwise tries normal extraction.
    """
    try:
        if use_ocr:
            full_text = extract_text_with_ocr(file_path, ocr_lang)
        else:
            with pdfplumber.open(file_path) as pdf:
                full_text = '\n'.join([page.extract_text() or '' for page in pdf.pages])

        # Save to output file
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_text)
        return full_text
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract Chinese text from PDF')
    parser.add_argument('input_pdf', help='Path to input PDF file')
    parser.add_argument('output_txt', nargs='?', help='Path to output text file (optional)')
    parser.add_argument('--ocr', action='store_true', help='Force OCR processing')
    parser.add_argument('--lang', default='chi_sim+eng',
                        help='OCR language codes (e.g., chi_sim, chi_tra, eng)')
    parser.add_argument('--dpi', type=int, default=300,
                        help='DPI for image conversion (default: 300)')

    args = parser.parse_args()

    # Run text extraction
    extracted_text = extract_text_from_pdf(
        args.input_pdf,
        output_file=args.output_txt,
        use_ocr=args.ocr,
        ocr_lang=args.lang
    )

    print(extracted_text)