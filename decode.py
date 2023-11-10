text = (
"тѥѣѡѵѳѥРѴѨѥРѯѮѥѳРѷѨѯРѡѲѥРѣѲѡѺѹРѥѮѯѵѧѨРѴѯРѴѨѩѮѫРѴѨѡѴРѴѨѥѹРѣѡѮРѣѨѡѮѧѥРѴѨѥРѷѯѲѬѤЬРѡѲѥРѴѨѥРѯѮѥѳРѷѨѯРѤѯЮ"
)
print('A message is encoded by ASCII. Can you figure out the correct numerical code to decode it?')
while True:
    try:
        code = int(input("Only the worthy may continue. Enter code (from 1 to 1055): "))
        if (code >= 1056) or (code <= 0):
            print('\nnope.\n')
        else:
            texts = []
            for letter in text:
                texts.append(letter)
            result = []
            for element in texts:
                result.extend(ord(num)-code for num in element)
            can_you_decode_this = []
            for element in result:
                can_you_decode_this.extend(chr(element))
            print('\n'+''.join(can_you_decode_this)+'\n')
            print('Did you do it? If not, try again.')
    except ValueError:
        print("\nyou're not good at following instructions, eh?\n")
