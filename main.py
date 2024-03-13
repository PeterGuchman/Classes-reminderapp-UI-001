from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen




class WindowManager(ScreenManager):
    pass
class LogIn(Screen):
    pass
class SignUp(Screen):
    pass
class HomePage(Screen):
    pass
class TimeTable(Screen):
    pass
class Classes(Screen):
    pass
class Exams(Screen):
    pass
class UserDetails(Screen):
    pass


class GridLayoutExample(GridLayout):
    pass
class MainWidget(Widget):
    pass
class ClassReminderApp(App):
    pass

ClassReminderApp().run()