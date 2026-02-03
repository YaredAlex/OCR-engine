from pdf2image import pdfinfo_from_path

info = pdfinfo_from_path("./commercial_registration.pdf")
print(info["Pages"])