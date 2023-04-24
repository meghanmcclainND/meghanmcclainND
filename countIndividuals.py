import aspose.words as aw
import os
from pathlib import Path

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

rootdir = r'C:\Users\megha\OneDrive\Documents\NotreDame\spring2023\Research\Code\bxgrid-2023-04-17-222247jpg' 

indivdir = r'C:\Users\megha\OneDrive\Documents\NotreDame\spring2023\Research\Code\bxgrid-2023-04-17-222247jpg\individuals' 

count = 1

for subdir, dirs, files in os.walk(rootdir):
    for file in range(0, len(files)):
        print("////////////////////////////////////////")
        old_file = file
        #print(type(files)) #list
        #print(f'files[-1]: {files[-1]}')
        #print(f"type(file): {type(file)}") #int
        #print(os.path.join(subdir, file))
        filename = Path(os.path.join(subdir, files[file])) #my_source
        my_source = filename
        print(f'my_source: {my_source}')
        #print(f'file: {file}')
        if file == 0:
            print(f"indivdir + '/' + str(files[file])[:5] : {indivdir + '/' + str(files[file])[:5]}")
            os.mkdir(indivdir + '/' + str(files[file])[:5])
            #break
        else:
            currentIndivID = str(files[file])[:5]
            print(f'currentIndivID: {currentIndivID}')
            print(f'files[file-1][:5]: {files[file-1][:5]}')
            if currentIndivID == str(files[file-1][:5]):
                #continue
                print('on same individual')
                my_dest = Path(os.path.join(indivdir + '/' + currentIndivID, files[file]))
                print(f'my_dest: {my_dest}')
                os.replace(my_source, my_dest)
            else:
                #increase individual count by 1
                print('new individual; increase count by 1 & create folder for this individual')
                os.mkdir(indivdir + '/' + currentIndivID)
                my_dest = Path(os.path.join(indivdir + '/' + currentIndivID, files[file]))
                print(f'my_dest: {my_dest}')
                os.replace(my_source, my_dest)
                count += 1
        #print(f'indivID: {currentIndivID}')
        #print(f'filename: {filename}')
        #print(f'subdir: {subdir}')
        new_filename_wo_ext = filename.with_suffix('') #1847437fh
        """ if file == 1000:
            break
        else:
            continue """
        #print(f'new_filename_wo_ext: {new_filename_wo_ext}')
        #os.replace(my_source, my_dest)
        #shape = builder.insert_image(str(filename))
        #shape.image_data.save(str(filename_replace_ext))
        #print(os.path.splitext(os.path.join(subdir, file)))  # returns ('/home/user/somefile', '.txt')
print(f'Number of Individuals: {count}')

#os.rename(my_source, my_dest)
