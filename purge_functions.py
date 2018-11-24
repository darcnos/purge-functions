
#!/usr/bin/env python

import requests, json

jsonheaders = {'content-type': 'application/json'}
site = 'https://' + input('https://')

def login():
    """ Login to the site, return a GUID """
    creds = {
    'username': input('Username: '),
    'password': input('Password: ')
    }

    return requests.post('{}/api/login'.format(site), creds).json()



def get_fileIds(DateCreatedFrom, DateCreatedTo):
    """ Returns a list of fileIds based on the date-range search of their creation date """
    fileIds = []
    response = requests.get('{}/api/files?filter=projectId_1,DateCreatedFrom_{},DateCreatedTo_{}&guid={}'.format(site, DateCreatedFrom, DateCreatedTo, guid)).json()
    print('Found {} Files!'.format(len(response)))
    
    [fileIds.append(file['fileId']) for file in response]

    return fileIds


def get_docIds(fileId):
    """ Returns a list of documentIds that belong to a list input of fileIds' """
    docIds = []
    response = doc_request = requests.get('{}/api/files/{}/documents?guid={}'.format(site, fileId, guid)).json()

    [docIds.append(doc['documentId']) for doc in response]

    return docIds




# Main runtime
if __name__ == '__main__':
    guid = login()

    # Iterate through the fileIds
    for file in get_fileIds('11/01/2018', '11/05/2018'):
        print('found FileID {}'.format(file))

        for doc in get_docIds(file):
            print('  deleting DocID {}'.format(doc))
            # Uncomment this to perform the deletion on the docId
            #requests.delete('{}/api/documents/{}?guid={}'.format(site, doc, guid))