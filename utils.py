from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from message_template import system_message, human_message

def generate_word_context(word, api_key):

    model = init_chat_model(model="deepseek-reasoner",
                            model_provider="deepseek",
                            api_key=api_key,
                            base_url="https://api.deepseek.com")

    prompt = ChatPromptTemplate(
        [
            ('system', system_message),
            ('human', human_message)
        ]
    )

    chain = prompt | model
    result = chain.invoke({'word': word}).content
    
    return result