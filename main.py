from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from translate import Translator as Tr

itachi= """
<MyLabel@Label>:
    size_hint : [None,None]
    size:self.texture_size

<MyTextField@TextInput>:
    size_hint :[0.3 , 0.4]
    font_size :'30sp'

<LangButton@Button>
    background_normal : ''
    background_color : [1,1,1,1]
    color: [0,0,0,1]
    bold: True
    font_size : '14sp'
    size_hint: [None,None]
    height: 50
    width : 100
    
FloatLayout:
    canvas.before:
        Color:
            rgba:[1,0,1,1]
        Rectangle:
            pos:self.pos
            size:self.size
    MyLabel:
        text: "[b][color=#FF0000]Language itachi python [/color][/b] Translator"
        markup:True
        pos_hint: {'center_x':0.5,'top':0.95}
        font_size: '30sp'
        color: [0,0,0,1]
    MyLabel:
        text: "From This"
        pos_hint: {'center_x':0.8,'top':0.7}
        font_size: '20sp'
        color: [0,0,0,1]
        bold: True
    MyLabel:
        text: "To This"
        pos_hint: {'center_x':0.2,'top':0.7}
        font_size: '20sp'
        color: [0,0,0,1]
        bold: True
    MyTextField:
        id :field1
        pos_hint: {'center_x':0.2,'top':0.6}
    Image:
        id: image
        size_hint:[0.2,0.2]
        pos_hint: {'center_x':0.5,'top':0.5}
        source:"flags/uk.png"
    MyTextField:
        id :field2
        pos_hint: {'center_x':0.8,'top':0.6}
    BoxLayout:
        pos_hint: {'center_x':0.5,'bottom':0.25}
        orientation:'horizontal'
        MyLabel:
            text: "Translate to"
            font_size: '20sp'
            bold: True
            color :[0,0,0,1]
            
        LangButton:
            text:'English'
            background_color:[1,0,0,0.6]
            on_release:app.translate_to('en', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
            
        LangButton:
            text:'France'
            background_color:[0,1,0,0.6]
            on_release:app.translate_to('fr', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
            
        LangButton:
            text:'Arabic'
            background_color:[0,0,1,0.6]
            on_release:app.translate_to('ar', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
            
        LangButton:
            text:'German'
            background_color:[0.2,0.5,1,0.6]
            on_release:app.translate_to('de', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
        
        LangButton:
            text:'Greek'
            background_color:[1,1,0,0.6]
            on_release:app.translate_to('el', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
        
        LangButton:
            text:'Indonesia'
            background_color:[0,0,1,0.6]
            on_release:app.translate_to('id', field1.text)
        MyLabel:
            text:'  '
            font_size: '18sp'
        
        
        

"""



class MyApp(App):
    def build(self):
        return Builder.load_string(itachi)

    def translate_to(self, lang, content):
        field = self.root.ids['field2']
        translator = Tr(to_lang = lang)
        translation = translator.translate(content)
        field.text = translation
        self.change_image(lang)

    def change_image(self, lang):
        image = self.root.ids['image']
        images = {'en': 'uk.png', 'fr': 'France.png' , 'ar':'morocco.png',
                  'de' : 'germany.png' , 'id': 'indonesia.png' , 'el': 'greece.png' }
        image.source = 'flags/'+images[lang]



if __name__=='__main__':
   app = MyApp()
   app.run()