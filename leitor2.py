import PyPDF2

arquivo_pdf = open ('teste.pdf', 'rb');

pdf = PyPDF2.PdfFileReader(arquivo_pdf);

numero_pagina = pdf.getNumPages()
numero_pagina
pagina = pdf.getPage(0)
conteudo_pagina = pagina.extractText()
conteudo_pagina