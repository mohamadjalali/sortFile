#!/usr/bin/python3

import os
import sys


class FileSort(object):
    

    def __init__(self):
        self.list_dir = os.listdir()


    def createIfNotExist(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)


    def move(self, folderName, files=None):
        if folderName not in 'Others':
            for file in files:
                os.replace(file, f"{folderName}/{file}")
        else:
                files = self.other()
                for file in files:
                    os.replace(file, f"{folderName}/{file}")


    def other(self):
        others = []
        for file in self.list_dir:
            ext = os.path.splitext(file)[1].lower()
            if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts)\
              and os.path.isfile(file):
                others.append(file)
        return others

    
    def createPrefixFile(self, args):
        exts   = list(args)
        prefix = [file for file in self.list_dir if os.path.splitext(file)[1].lower() in exts]
        return prefix


if __name__ == '__main__':
        
        path = input('Please enter the path where you want the files to be sorted: ')
        c = os.chdir(path)
        f = FileSort()
        
        
        imgExts   = input('Please Enter your prefeix images: ').split()
        docExts   = input('Please Enter your prefeix docs: ').split()
        mediaExts = input('Please Enter your prefeix medias: ').split()
        
        # Create Folder for transfer file
        f.createIfNotExist('Images')
        f.createIfNotExist('Docs')
        f.createIfNotExist('Media')
        f.createIfNotExist('Others')
        
        ####################################
        # listi az fileha az pasvand haye vared shodeh.
        
        images = f.createPrefixFile(imgExts)
        medias = f.createPrefixFile(mediaExts)
        docs   = f.createPrefixFile(docExts)
        
        # Move file in respective folder
        f.move('Docs',   docs)
        f.move('Media',  medias)
        f.move('Images', images)
        f.move('Others') 
