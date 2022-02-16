from django.urls import path
from . import views

urlpatterns = [
    path('send-command', views.send_command_view, name='api_remote_send_command'),
    path('screen-size', views.screen_size_view, name='api_remote_screen_size'),
    path('hotkey', views.hotkey_view, name='api_remote_hotkey'),
    path('key-press', views.key_press_view, name='api_remote_key_press'),
    path('mouse-move', views.mouse_move_view, name='api_remote_mouse_move'),
    path('mouse-button', views.mouse_button_view, name='api_remote_mouse_button'),
    path('save-screenshot', views.save_screenshot_view, name='api_remote_save_screenshot'),
]
