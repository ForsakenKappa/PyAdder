import sys
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlLabel
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class DeveloperInfoWindow(BaseWidget):
    def __init__(self):
        super().__init__('О разработчиках')
        
        # Размер окна (немного увеличил для вместимости текста)
        self.size = (700, 550)
        
        # Формируем текст с разработчиками
        developers_text = """
        Карасев Алексей Валерьевич
        Клюева Ксения Викторовна
        Кольцова Екатерина Павловна
        Митрофанов Роман Алексеевич
        Хилько Екатерина Сергеевна
        Шин Марина Сергеевна
        """
        
        # Заголовок
        self.label_title = ControlLabel('<b>О разработчиках</b>')
        self.label_title.label.setAlignment(Qt.AlignCenter)
        self.label_title.label.setStyleSheet("font-size: 26px; color: #333; margin-bottom: 10px;")
        
        # Список разработчиков
        self.label_developers = ControlLabel(developers_text)
        self.label_developers.label.setAlignment(Qt.AlignCenter)
        self.label_developers.label.setStyleSheet("font-size: 16px; line-height: 1.5; color: #555;")
        
        # Версия и год
        self.label_meta = ControlLabel('Версия: 1.0 | 2026 год')
        self.label_meta.label.setAlignment(Qt.AlignCenter)
        self.label_meta.label.setStyleSheet("font-size: 14px; color: #888; font-style: italic;")
        
        # Благодарность
        self.label_thanks = ControlLabel('Спасибо, что воспользовались нашим калькулятором! ♡')
        self.label_thanks.label.setAlignment(Qt.AlignCenter)
        self.label_thanks.label.setStyleSheet("font-size: 18px; margin-top: 20px; color: #2196F3;")
        
        # Таймер
        self.label_timer = ControlLabel('Закрытие через 10 сек')
        self.label_timer.label.setAlignment(Qt.AlignCenter)
        self.label_timer.label.setStyleSheet("font-size: 16px; background-color: #f0f0f0; padding: 5px; border-radius: 5px; margin-top: 10px;")
        
        # Верстка (formset)
        # Используем пустые строки ' ' для создания отступов
        self.formset = [
            'label_title',
            ' ',
            'label_developers',
            ' ',
            'label_meta',
            ' ',
            'label_thanks',
            ' ',
            'label_timer'
        ]
        
        # Настройка таймера
        self.countdown = 10
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # тик каждую секунду
        
    def update_timer(self):
        """Обновление таймера обратного отсчета"""
        self.countdown -= 1
        self.label_timer.value = f'Закрытие через {self.countdown} сек'
        
        if self.countdown <= 0:
            self.timer.stop()
            self.close()  # Закрываем окно приложения

def show_developer_info():
    """Функция запуска окна"""
    # geometry=(x, y, width, height)
    pyforms.start_app(DeveloperInfoWindow, geometry=(400, 200, 700, 550))

if __name__ == '__main__':
    show_developer_info()
