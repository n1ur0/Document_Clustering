#%%
from packages import Parser2txt, Paths, Pre_processing, TextProcessing

class Main():

    def __init__(self):
        # Parser.__init__(self)
        pass

if __name__ == "__main__":
    """
    INFO:
    - detail each function!
    - detail each function!
    - detail each function!
    - detail each function!
    """
    print("Loaded main class\n")
    
    # cv_path = r"/Users/emanuel/Desktop/Document_Clustering"
    cv_path = r"/home/emanuel/Desktop/cvs"
    
    # cv_path = r"C:\Users\sergiojesus\DWesktop\Coisas da Alvita\CV\4-Abril_14"

    parser = Parser2txt(cv_path)
    # lista = parser.docLists()
    
    # gandalf = Paths(cv_path)
    # wizard, bacon = gandalf.getPdfs()

    # parser.outputTxt()

    def test1():
        documents = parser.docLists()
        return documents
        # parser.saveObjs()

    def test2(documents):
        # documents = parser.loadObjs()
        pre = Pre_processing(documents)

        pre.text_process(stem=False, lemma=True)
        pre.saveObjs()

    def test3():
        pre = Pre_processing()
        a, b, c = pre.loadObjs()
        print(c)

    # pre.preparation()
    # print(pre.getTokenized())

    # pre = Pre_processing()
    # a, b, c = pre.loadObjs()

    # docs = test1()
    # test2(docs)
    #test3()

    x = TextProcessing(cv_path)
    #print(x.docs())
    print(x.corpus())