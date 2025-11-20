from pathlib import Path
from typing import List

class ImageHandlerMiddleware:
    def __init__(self, handler_folder: str = "src/handler"):
        self.handler_folder = Path(handler_folder)
        self.handler_folder.mkdir(exist_ok=True)
        self.user_images = {}
    
    def save_image(self, user_id: int, file_path: bytes, file_id: str) -> str:
        """Salva a imagem e retorna o caminho"""
        if user_id not in self.user_images:
            self.user_images[user_id] = []
        
        image_path = self.handler_folder / f"image_{user_id}_{file_id}.jpg"
        
        with open(image_path, 'wb') as new_file:
            new_file.write(file_path)
        
        self.user_images[user_id].append(str(image_path))
        return str(image_path)
    
    def get_user_images(self, user_id: int) -> List[str]:
        """Retorna lista de imagens do usuário"""
        return self.user_images.get(user_id, [])
    
    def clear_user_images(self, user_id: int) -> None:
        """Limpa as imagens do usuário"""
        if user_id in self.user_images:
            del self.user_images[user_id]