import os
import shutil

while(True):
    result = input("Você deseja iniciar o processo de organização? [S] [N]: ")
    if result.lower() != "s" and result.lower() != "n":
        print("Opção inválida, tente novamente.\n")
    else:
        break

if result.lower() == "n":
    print("Fechando aplicação...")
    exit()
else:
    print("Iniciando o processo de organização...")

# Caminho onde estão os arquivos a serem organizados
path_folder_src = os.path.join(os.path.expanduser("~"), "Desktop")

# Caminho onde os arquivos ficaram organizados
path_folder_dst = os.path.join(path_folder_src, "Pasta Organizada")

# Verifica se o caminho raiz já existe
if not os.path.exists(path_folder_dst):
    os.mkdir(path_folder_dst)

# Função para criar as pastas e chamar a função que move os arquivos
def organizarArquivos(pathFolderSrc, pathFolderDst):

    foldersCreate = [] # Cria uma lista vazia
    for file_path in os.listdir(pathFolderSrc):
        path_file = os.path.join(pathFolderSrc,file_path)
        if os.path.isfile(path_file):
            _, ext = os.path.splitext(path_file)
            extNew = ext.replace(".","").upper()
            if extNew not in foldersCreate:
                foldersCreate.append(extNew)
    
    if len(foldersCreate) == 0:
        print("Não existe arquivo para ser movido na pasta origem.")
        print("Fechando aplicação...")
        exit()

    for folderCreate in foldersCreate:
        folder_toCreate = os.path.join(pathFolderDst,folderCreate) 
        if not os.path.exists(folder_toCreate):
            os.mkdir(folder_toCreate)
    
    print("As pastas foram criadas na pasta raiz escolhida.")
    
    moverArquivos(pathFolderSrc, pathFolderDst)

def moverArquivos(pathFolderSrc, pathFolderDst):
    file_all = [] # Criação da lista onde ficara os itens, path do arquivo e extensão

    for file_name in os.listdir(pathFolderSrc):
        file_path = os.path.join(pathFolderSrc, file_name)
        if os.path.isfile(file_path):
            file_all.append((os.path.splitext(file_path)[0],os.path.splitext(file_path)[1].replace(".","").upper(),file_name))

    for file in file_all:
        path_old = os.path.join(pathFolderSrc,file[2])
        path_new = os.path.join(os.path.join(pathFolderDst,file[1]),file[2])
        shutil.move(path_old,path_new)
    
    print("Todos os arquivos foram movidos com sucesso!")

organizarArquivos(path_folder_src,path_folder_dst)
