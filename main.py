import openai
import gradio
from services.analysys import validateQuestionforWord

openai.api_key_path= "credencialOpenai.txt"

"""in role user, the content is the question, in role system, the content is the answer"""  
"""This function is to answer the question of the user, the question is the parameter of the function."""
def answerQuestion(nameUser, questionUser):
    messages=[
        {"role": "system",
         "content": "marketer encargado de crear contenidos  para linkedin que puntúen alto en los motores de búsqueda sobre cero residuos y medio ambiente"
        }
    ]
    sms = validateQuestionforWord(questionUser)
    if sms == None:
        messages.append({"role": "user","content": questionUser})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
        )
        replay = response["choices"][0]["message"]["content"]
    else:
        replay = sms
    messages.append({"role": "assistant","content": replay})
    welcome = f"Bienvenido(a) {nameUser}, al chat que te ayudará a crear publicaciones para linkedin sobre cero residuos y medio ambiente. ¡Empecemos!"

    return welcome, replay
   

demo = gradio.Interface(
    fn=answerQuestion, 
    inputs= [gradio.inputs.Textbox(lines=1, placeholder="ColoqueSu nombre aquí..."),gradio.Textbox(lines=5, placeholder="Escriba su pregunta aquí...")],
    outputs=["textbox", "textbox"],
    title="Content Creator AI", 
    description="Esta es una aplicación que te ayudará a crear contenido para linkedin."
)
demo.launch(share=True)