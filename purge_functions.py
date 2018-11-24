
#!/usr/bin/env python

import requests, json
jsonheaders = {'content-type': 'application/json'}

def login(site):
    """ Login to the site, return a GUID """
    creds = {
    'username': input('Username: '),
    'password': input('Password: ')
    }

    return requests.post('{}/api/login'.format(site), creds).json()


def get_fileIds(projectId, DateCreatedFrom, DateCreatedTo):
    """ Returns a list of fileIds based on the date-range search of their creation """
    fileIds = []
    response = requests.get('{}/api/files?filter=projectId_{},DateCreatedFrom_{},DateCreatedTo_{}&guid={}'.format(site, projectId, DateCreatedFrom, DateCreatedTo, guid)).json()
    print('Found {} Files!'.format(len(response)))
    
    [fileIds.append(fileId['fileId']) for fileId in response]

    return fileIds


def get_docIds(fileId):
    """ Returns a list of documentIds that belong to a list input of fileIds """
    docIds = []
    response = requests.get('{}/api/files/{}/documents?guid={}'.format(site, fileId, guid)).json()

    [docIds.append(docId['documentId']) for docId in response]

    return docIds


# Main runtime
if __name__ == '__main__':
    site = 'https://' + input('https://')
    guid = login(site)

    # Iterate through the fileIds
    for fileId in get_fileIds('1', '11/01/2018', '11/05/2018'):
        print('found FileID {}'.format(fileId))

        # Iterate through docIds
        for docId in get_docIds(file):
            print('  deleting DocID {}'.format(docId))
            # Uncomment this to perform the deletion on the docId
            #requests.delete('{}/api/documents/{}?guid={}'.format(site, doc, guid))
