'''
Author:Kavitha Subramaniyan
Module:Fetch.py
Description:Implementing cosine similarity to find how two documents are similar.
'''
def preprocess(dicti):
    words = []
    # Tokenization--Splitting sentences into words
    for key, value in dicti.items():
        words = value.split()

    # stopwords removal
    stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
                 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such',
                 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him',
                 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don',
                 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while',
                 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them',
                 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because',
                 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
                 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being',
                 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than',
                 "you'll", "don't", "we'll"]

    # Convert the list strings to lowercase
    lower = []
    lower = [element.lower() for element in words]

    # Remove stopwords from the lower list
    no_stopwords = []
    for i in lower:
        if i not in stopwords:
            no_stopwords.append(i)

    # Removing Punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''';
    punct = []
    for i in no_stopwords:
        for char in i:
            if char in punctuations:
                i = i.replace(char, "")
        punct.append(i)
    return punct


# Defining the parent compute similarity function to perform preprocess functions in order
def compute_similarity(doc1, doc2):
    doc1_dict = {"doc1": doc1}
    doc1_preprocess = preprocess(doc1_dict)
    doc2_dict = {"doc2": doc2}
    doc2_preprocess = preprocess(doc2_dict)
    # Concatenate first and 2nd document
    merge_list = []
    for i in doc2_preprocess:
        merge_list.append(i)
    for i in doc1_preprocess:
        merge_list.append(i)

    # Remove duplicates in the merged documents(1 and 2)
    full_list_no_dup = list(dict.fromkeys(merge_list))
    doc1_final = compare_func(full_list_no_dup, doc1_preprocess)
    doc2_final = compare_func(full_list_no_dup, doc2_preprocess)
    sim_doc12 = cosine(full_list_no_dup, doc1_final, doc2_final)
    return sim_doc12


# Compare two documents one by one with merged list-->1-word exists,0-word not exists
def compare_func(mylist, a):
    d = []
    for i in mylist:
        if i in a:
            d.append(1)
        else:
            d.append(0)
    return d


# cosine similarity for first and second document
def cosine(full_list_no_dup, doc1_final, doc2_final):
    cosine_doc1_2 = 0
    for i in range(len(full_list_no_dup)):
        cosine_doc1_2 = cosine_doc1_2 + (doc1_final[i] * doc2_final[i])
    # Find sum of first doc list
    doc1_total = 0
    for i in range(len(doc1_final)):
        doc1_total = doc1_total + doc1_final[i]
    # Find sum of second doc list
    doc2_total = 0
    for i in range(len(doc2_final)):
        doc2_total = doc2_total + doc2_final[i]
    similarity_doc1_2 = cosine_doc1_2 / ((doc1_total * doc2_total) ** 0.5)
    return similarity_doc1_2
