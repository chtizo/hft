def file_upload(f):  
    vlink = 'hft_qasum/upload/' + f.name
    with open(vlink, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    return vlink