#!/usr/bin/env python
# coding: utf-8

# In[13]:


import fitz
import os
os.chdir(os.getcwd())


# In[16]:


import glob
glob.glob("*.pdf")


# In[17]:


for i in glob.glob("*.pdf"):
    pdfIn = fitz.open(i)
    for page in pdfIn:
        print(page)
        texts = ["guideline",
                 "reporting",
                 "reporting guideline",
                 "machine learning",
                 "artificial intelligence",
                 "guide",
                 "checklist",
                 "DECIDE-AI",
                 "DC-Check",
                 "PALISADE",
                 "RELAINCE",
                 "CAIR",
                 "CONSORT-AI",
                 "SPIRIT-AI",
                 "MI-CLAIM",
                 "CLAIM",
                 "PRIME",
                 "PROBAST",
                 "TRIPOD",
                 "CLEAR",
                 "RQS",
                 "MINIMAR",
                 "FUTURE-AI",
                 "PROBAST-AI",
                 "PROBAST+AI",
                 " AI ",
                 "MAIC-10"
        ]
        text_instances = [page.search_for(text) for text in texts] 

        # coordinates of each word found in PDF-page
        print(text_instances)  

        # iterate through each instance for highlighting
        for inst in text_instances:
            annot = page.add_highlight_annot(inst)
            # annot = page.add_rect_annot(inst)

            ## Adding comment to the highlighted text
            info = annot.info
            #info["title"] = "PDF text finder"
            #info["content"] = "found"
            annot.set_info(info)
            annot.update()


    # Saving the PDF Output
    pdfIn.save(f"h_{i}")


# In[ ]:




