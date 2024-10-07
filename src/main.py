from copy_static_to_public import *
from generate_page import *



def main():



    
    copy_static_to_public()
    
    generate_pages_recursive("content", "template.html", "public")







main()