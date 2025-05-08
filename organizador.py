import os
import shutil
from tkinter import filedialog

# Função para selecionar as pastas de origem e destino
def selecionarPastas():
    while True:
        print('\nSelecione a pasta de origem')
        path_folder_src = filedialog.askdirectory(title='Selecione a pasta de origem')
        print('Selecione a pasta de destino')
        path_folder_dst = filedialog.askdirectory(title='Selecione a pasta de destino')

        if not path_folder_src and not path_folder_dst:
            print('Operação cancelada.')
            return None, None
        
        print('\nAs novas pastas selecionadas são: ')
        print(f'Pasta origem: {path_folder_src}')
        print(f'Pasta destino: {path_folder_dst}')
        
        if solicitarConfirmacao('\nConfirma essa escolha?') == 's':
            return path_folder_src, path_folder_dst

        if solicitarConfirmacao('Deseja escolher novamente? caso não deseje, a aplicação irá fechar') == 'n':
            return None, None
# Função para confimar algumas opções de acordo com as escolhas do usuario
def solicitarConfirmacao(textoMsg):
    while True:
        result = input(f'{textoMsg} [S] [N]: ').strip().lower()
        if result in ('s', 'n'):
            return result
        print('Opção inválida.\n')
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
        print("Fechando aplicação...\n")
        exit()

    for folderCreate in foldersCreate:
        folder_toCreate = os.path.join(pathFolderDst,folderCreate) 
        if not os.path.exists(folder_toCreate):
            os.mkdir(folder_toCreate)
    
    print("As pastas foram criadas na pasta de destino.")
    
    moverArquivos(pathFolderSrc, pathFolderDst)
# Função para mover os arquivos para as pastas
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
# Função principal
def main():
    result = solicitarConfirmacao('Você deseja iniciar o processo de organização?')
    if result == 'n':
        print('Fechando aplicação...\n')
        return
    
    path_folder_src = os.path.join(os.path.expanduser("~"), "Desktop") # Caminho onde estão os arquivos a serem organizados
    path_folder_dst = os.path.join(path_folder_src, "Pasta Organizada") # Caminho onde os arquivos ficaram organizados

    print(f'\nA pasta padrão de origem é: {path_folder_src}')
    print(f'A pasta padrão de destino é: {path_folder_dst}\n')

    result = solicitarConfirmacao('Deseja mudar as pastas?')
    if result == 's':
        path_folder_src, path_folder_dst = selecionarPastas()
        if not path_folder_src and not path_folder_dst:
            print('Fechando aplicação...\n')
            return
    else:
        if not os.path.exists(path_folder_dst):
            os.mkdir(path_folder_dst)
    organizarArquivos(path_folder_src,path_folder_dst)

if __name__ == "__main__":
    main()