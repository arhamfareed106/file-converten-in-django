from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
import PyPDF2
import os


from django.shortcuts import render

def convert_file_view(request):
    return render(request, 'index.html')  # Adjust to your main template name


def convert_to_pdf(file):
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Read the uploaded PDF file
    pdf_reader = PyPDF2.PdfFileReader(file)
    
    # Add all pages from the original PDF to the new PDF writer
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    # Create output path for the converted file
    output_pdf_path = f'media/converted/{file.name}.pdf'  # Ensure this directory exists
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

    # Save the new PDF to the output path
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    return output_pdf_path

def convert_file(request):
    if request.method == 'POST':
        # Ensure the file is uploaded
        if 'file' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file uploaded.'})

        file = request.FILES['file']
        format = request.POST.get('format')

        # Validate format selection
        if format == 'pdf':
            output_path = convert_to_pdf(file)
            return JsonResponse({'status': 'success', 'output_path': output_path})
        else:
            return JsonResponse({'status': 'error', 'message': 'Unsupported format.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
