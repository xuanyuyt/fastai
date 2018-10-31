import nbclean as nbc

path_original_notebook = 'D:/tyang/fastai/courses/dl1/lesson1-breeds.ipynb'
path_save = 'D:/tyang/fastai/courses/dl1/lesson1-breeds.ipynb'
ntbk = nbc.NotebookCleaner(path_original_notebook)
ntbk.clear('output')
ntbk.save(path_save)