from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def convert_to_pdf(file):
    # Create a PdfFileReader object to read the uploaded file
    try:
        pdf_reader = PdfFileReader(file)
        pdf_writer = PdfFileWriter()

        # Add all pages from the file to the writer
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Define the output file path
        output_pdf_path = f'/tmp/{os.path.splitext(file.name)[0]}.pdf'  # Use file name without extension

        # Write the PDF to the temporary file
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        return output_pdf_path
    except Exception as e:
        # Handle any errors that occur during the PDF processing
        print(f"Error converting file to PDF: {e}")
        return None

def convert_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        file_format = request.POST.get('format', '').lower()  # Ensure format is in lowercase
        
        # Handle file conversion based on selected format
        if file_format == 'pdf':
            output_path = convert_to_pdf(file)
            
            if output_path:
                return JsonResponse({'status': 'success', 'output_path': output_path})
            else:
                return JsonResponse({'status': 'error', 'message': 'File conversion failed'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



# Handle file download
def download_file_view(request, file_name):
    file_path = os.path.join('converted_files', file_name)  # Adjust the path to where your converted files are stored
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")  # Adjust content type as needed
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    else:
        return HttpResponse("File not found.", status=404)