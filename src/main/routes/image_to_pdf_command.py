from src.integrations.telegram_comunicator import bot
from src.controllers.convert_image_to_pdf import images_to_pdf
from src.main.middlewares.image_handler import ImageHandlerMiddleware
from os import remove
from pathlib import Path

# Inicializa o middleware
image_middleware = ImageHandlerMiddleware("src/handler")

@bot.message_handler(commands=['pdf', 'converter'], content_types=['photo'])
def handle_pdf_with_photos(message) -> None:
    user_id = message.chat.id
    
    bot.reply_to(message, "❌ Nenhuma imagem foi anexada ao comando /pdf.\n\nUse: /pdf + anexe as imagens")
    # Verifica se há fotos anexadas
    if not message.photo:
        bot.reply_to(message, "❌ Nenhuma imagem foi anexada ao comando /pdf.\n\nUse: /pdf + anexe as imagens")
        return
    
    try:
        # Processa todas as fotos da mensagem
        for photo in message.photo:
            file_info = bot.get_file(photo.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            image_middleware.save_image(user_id, downloaded_file, photo.file_id)
        
        image_list = image_middleware.get_user_images(user_id)
        
        bot.reply_to(message, f"⏳ Convertendo {len(image_list)} imagem(ns) para PDF...")
        
        # Converte para PDF
        pdf_file = images_to_pdf(image_list, f"src/handler/output_{user_id}.pdf")
        
        # Envia o PDF
        with open(pdf_file, 'rb') as pdf:
            bot.send_document(user_id, pdf, caption="✅ Seu PDF está pronto!")
        
        # Limpa as imagens
        for image_path in image_list:
            remove(image_path)
        remove(pdf_file)
        
        image_middleware.clear_user_images(user_id)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Erro ao gerar PDF: {str(e)}")