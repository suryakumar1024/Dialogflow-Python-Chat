import dialogflow_v2
import os
from google.api_core.exceptions import InvalidArgument


def detect_intent_with_parameters(project_id, session_id, query_params, language_code, user_input):
    session_client = dialogflow_v2.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text = user_input

    text_input = dialogflow_v2.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow_v2.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        query_params=query_params
    )

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))

    return response

GOOGLE_PROJECT_ID = 'eternal-impulse-275610'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = '/home/user/Documents/My Project-165818a03ab4.json'
session_id = 'Xwreswwqqqd'

current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_APPLICATION_CREDENTIALS)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
context_short_name = "does_not_matter"
context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + context_short_name.lower()
parameters = dialogflow_v2.types.struct_pb2.Struct()

input_text = "Hi! I'm surya, can you help me?"

context_1 = dialogflow_v2.types.context_pb2.Context(name=context_name, lifespan_count=2, parameters=parameters)
query_params_1 = {"contexts": [context_1]}
language_code = 'en'
response = detect_intent_with_parameters(project_id=GOOGLE_PROJECT_ID, session_id=session_id,query_params=query_params_1,language_code=language_code,user_input=input_text)
print(response)

