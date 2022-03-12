def ocr_init():
    import easyocr
    return easyocr

def ocr_reader(img, easyocr):

    reader = easyocr.Reader(['en'])

    # results = reader.readtext(img)
    results = reader.readtext(img)

    ocr_text = ''

    for line in results:
        ocr_text += line[1]

    return ocr_text