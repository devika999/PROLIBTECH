import PyPDF2,yake
def abcde(path):
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page object
    gg = ""
    for i in range(0, pdfReader.numPages):
        print(i)
        pageObj = pdfReader.getPage(i)
        gg = gg + " " + pageObj.extractText()
        # extracting text from page
        text = pageObj.extractText()
        print(text)
        language = "en"
        max_ngram_size = 3
        deduplication_threshold = 0.9
        numOfKeywords = 10
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, top=numOfKeywords,
                                                    features=None)
        keywords = custom_kw_extractor.extract_keywords(gg)

        pdfFileObj.close()
        a = gg.replace(",", "").replace(".", "").replace("0", "").replace("1", "").replace("2", "").replace("3",
                                                                                                            "").replace(
            "4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("0", "").replace(
            "!",
            "").replace(
            "@", "").replace('-', "")

        kw_extractor = yake.KeywordExtractor()
        language = "en"
        'C:\\Users\\User\\PycharmProjects\\project_management12\\static\\report\\20220509-021543.pdf'
        deduplication_threshold = 0.9
        numOfKeywords = 200
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, top=numOfKeywords,
                                                    features=None)
        keywords = custom_kw_extractor.extract_keywords(a)
        for kw in keywords:
            print(kw[0])
            print(kw[1])

abcde('C:\\Users\\User\\PycharmProjects\\project_management12\\static\\report\\20220509-021543.pdf')
