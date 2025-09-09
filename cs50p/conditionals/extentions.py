
def main():
    n = input("File Name: ")
    ext(n)
    
# def ext(x):
#     if "gif" in x: 
#         print("image/gif")

def ext(x):
    x = x.lower()
    match True: 
        case _ if x.endswith(".gif"):
            print("image/gif")
        case _ if x.endswith(".jpg"):
            print("image/jpg")
        case _ if x.endswith(".jpeg"):
            print("image/jpeg")
        case _ if x.endswith("png"):
            print("image/png")
        case _ if x.endswith("pdf"):
            print("image/pdf")
        case _ if x.endswith("txt"):
            print("image/txt")
        case _ if x.endswith(".zip"):
            print("image/zip")
        case _:
            print("application/octet-stream")
            

main()