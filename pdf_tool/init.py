# from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger
from PyPDF2 import PdfReader,PdfWriter,PdfMerger
from pathlib import Path

# Ici je capte le nom du fichier pdf a transforme et son chemin pour les futures manipulations
class pdf_tools:
    def __init__(self,filename) -> None:
        try:
            self.input_reader = PdfReader(filename) # fichier a manipuler
            self.file_path = None # chemin
            self.pdf_writer = PdfWriter()
            self.pdf_merger = PdfMerger()
            self.pageCount = None
            self.temp_name = None
            self.pages = None
            if self.input_reader:
                self.pageCount = len(self.input_reader.pages)
              
                self.file_path = Path(filename).parent
                self.temp_name = Path(filename).name
            #Get all single pages
                self.pages = self.input_reader.pages
                print(f'PageNumber: {self.pageCount} and Path: {self.file_path} and Name= {self.temp_name}')
        except FileNotFoundError:
            print('file not found occur')
 # Cette function nous permet de retirer la page nom desirer d'un pdf           
    def removePages(self,pageNumber):
        try:
            
            if pageNumber <= self.pageCount:
                self.temp_name = "removed" + self.temp_name
                for i in range(1,self.pageCount):
                    if i != pageNumber:
                        self.pdf_writer.add_page(self.input_reader.pages[i])
                        # print('Everything seems right a this point')
                with open(self.file_path.joinpath(self.temp_name),"wb") as tmp:
                    self.pdf_writer.write(tmp)   
                    print('success')      
        except FileExistsError as error:
            print('Error')               
# cette nous permet D'ajouter le pdf a une position predefinit    
    def Add_pages_to(self,position,new_file):
        temp = PdfReader(new_file)
        new_pages = []
        self.temp_name = "added" + self.temp_name
        try:  
    # check if in begining
            if position == 1:
                new_pages.extend(temp.pages)
                new_pages.extend(self.input_reader.pages)
    # Add pages to an arbitrary position            
            else:
              new_pages.extend(self.input_reader.pages[:position - 1])
              new_pages.extend(temp.pages)
              new_pages.extend(self.input_reader.pages[position - 1:])    
  # at last write to pdf writer         
            for i in range(len(new_pages)):
                self.pdf_writer.add_page(new_pages[i])      
                      
            with open(self.file_path.joinpath(self.temp_name),'wb') as w:
                self.pdf_writer.write(w)           
                print('success')              
        except FileNotFoundError:
            print('File not found occured')
                       
    def swap_pages(self,old_position,new_position):
        try:
            if old_position == new_position:
                assert(ValueError)
            old = self.pages[old_position-1]
            new = self.pages[new_position-1]
            self.temp_name = "swapped" + self.temp_name
            swap_pages = []
            swap_pages.extend(self.input_reader.pages)
            for i in range(1,self.pageCount):
                if i == old_position:
                    self.pdf_writer.add_page(new)
                elif i == new_position:
                    self.pdf_writer.add_page(old)    
                else:
                    self.pdf_writer.add_page(swap_pages[i])
            
            with open(self.file_path.joinpath(self.temp_name),'wb') as w:
                    self.pdf_writer.write(w)         
        except ValueError:
            print('error occur')  
        except TypeError:
            print('typo somewhere')        
            
test = pdf_tools("/home/bvhbi/Desktop/OCR/script/lab03.pdf")
# test.Add_pages_to(2,"/home/bvhbi/Desktop/OCR/pdf_tool/first_pages.pdf")
test.swap_pages(3,3)
#test.removePages(4)
# test.Add_pages_to()
# new_file = "/home/sheperd/Desktop/pdftools/first_pages.pdf"
# position = 4
# test.Add_pages_to(position-1,new_file)
# # # merger = PdfFileMerger()
# # merger.append(PdfFileReader(open("/home/sheperd/Desktop/pdftools/removed.pdf", 'rb')))
# # merger.write("mergeds.pdf")
# # #let's test merging two pdf
# tmp = "first"
# tmp2 = "Second"
# tmp,tmp2 = tmp2,tmp
# print(tmp,tmp2)
# test.removePages(3)
# file = "DECOUVERT.pdf"
# pdf_path = os.path.abspath(file)

# input_pdf = PdfFileReader("/home/sheperd/Desktop/pdftools/DECOUVERT.PDF")
# output_pdf = PdfFileWriter()

# print(input_pdf)
# output_pdf.addPage(input_pdf.getPage(1))

# with open("first_pages.pdf","wb") as ouput:
#     output_pdf.write(ouput)     
