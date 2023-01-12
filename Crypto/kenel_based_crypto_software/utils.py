import os
import seaborn as sns
def size_compaison(arr):
    sizes = []
    for i in arr:
        sizes.append(os.path.getsize(i))
    var = sns.barplot(x=arr, y=sizes)
    fig = var.get_figure()
    fig.savefig('fig.png')