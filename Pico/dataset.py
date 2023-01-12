import opendatasets as od
def download_dataset(download_link):
    od.download(download_link)

if __name__ == '__main__':
    print('You need to Enter the Download Link and Your kaggle key later')
    download_link = input('Enter Download link')
    download_dataset(download_link)