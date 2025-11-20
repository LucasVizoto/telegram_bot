from PIL import Image
import os

def images_to_pdf(local_das_imagens, pdf):
    '''
    Essa função acessa uma pasta criada no projeto para buscar imagens salvas nele e, com essas imagens monta uma lista que em sequência é 
    salva como um arquivo pdf   
    '''
    image_list = []
    
    # Verifica se o diretório existe
    if not os.path.isdir(local_das_imagens):
        print(f"Erro: O diretório '{local_das_imagens}' não foi encontrado.")
        return

    # Obtém todas as imagens da pasta
    # Adicionando uma verificação para garantir que o arquivo é realmente um arquivo
    banco_de_imagens = [f for f in os.listdir(local_das_imagens) 
                        if os.path.isfile(os.path.join(local_das_imagens, f)) and 
                           f.lower().endswith(('.png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    
    banco_de_imagens.sort()  # Ordena os arquivos por nome para uma ordem lógica no PDF
    
    print(f"Encontradas {len(banco_de_imagens)} imagens no diretório '{local_das_imagens}'.")
    
    for file in banco_de_imagens:
        caminho = os.path.join(local_das_imagens, file)
        try:
            # Converte para RGB caso seja PNG ou GIF para garantir compatibilidade com PDF
            imagem_convertida = Image.open(caminho).convert("RGB")
            image_list.append(imagem_convertida)
        except Exception as e:
            print(f"Erro ao carregar ou converter a imagem '{file}': {e}")
            # Você pode optar por continuar ou parar aqui, dependendo da sua necessidade
            
    print(f"Total de {len(image_list)} imagens carregadas com sucesso para a lista.")

    # Verifica se a lista de imagens não está vazia antes de tentar salvar
    if not image_list:
        print("Nenhuma imagem válida foi encontrada ou carregada para criar o PDF.")
        print(f"O PDF '{pdf}' não será criado.")
        return
    
    # Salva todas as imagens como páginas de um PDF
    try:
        # A primeira imagem da lista (image_list[0]) é salva como a primeira página.
        # As imagens restantes (image_list[1:]) são anexadas.
        image_list[0].save(pdf, save_all=True, append_images=image_list[1:])
        print(f"PDF '{pdf}' criado com sucesso a partir de {len(image_list)} imagens.")
    except Exception as e:
        print(f"Erro ao salvar o PDF '{pdf}': {e}")

# Caminho da pasta com imagens e nome do arquivo de saída
local_das_imagens = 'src\handler' 
pdf = "images.pdf"

images_to_pdf(local_das_imagens, pdf)


