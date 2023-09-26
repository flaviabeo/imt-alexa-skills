from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, get_supported_interfaces
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

APL_DOCUMENT_ID = "uno"

APL_DOCUMENT_TOKEN = "documentToken"

DATASOURCE = {
    "simpleTextTemplateData": {
        "type": "object",
        "properties": {
            "backgroundImage": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/background-green.png",
            "foregroundImageLocation": "left",
            "foregroundImageSource": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/asparagus.jpeg",
            "headerTitle": "Asparagus",
            "headerSubtitle": "",
            "hintText": "Try, \"Alexa, next question\"",
            "headerAttributionImage": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/logo-world-of-plants-2.png",
            "primaryText": "Asparagus is a member of the Lily family. Plants in the lily family have evolved a close relationship with pollinators. Therefore, they typically have elaborate blooms. Asparagus is a member of the Lily family. Plants in the lily family have evolved a close relationship with pollinators. Therefore, they typically have elaborate blooms. Asparagus is a member of the Lily family. Plants in the lily family have evolved a close relationship with pollinators. Therefore, they typically have elaborate blooms. Asparagus is a member of the Lily family. Plants in the lily family have evolved a close relationship with pollinators. Therefore, they typically have elaborate blooms. ",
            "textAlignment": "start",
            "titleText": "That's correct!"
        }
    }
}

class SampleAPLRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("INTENT_NAME")(handler_input)

    def supports_apl(self, handler_input):
        # Checks whether APL is supported by the User's device
        supported_interfaces = get_supported_interfaces(
            handler_input)
        return supported_interfaces.alexa_presentation_apl != None

    def launch_screen(self, handler_input):
        # Only add APL directive if User's device supports APL
        if self.supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token=APL_DOCUMENT_TOKEN,
                    document={
                        "type": "Link",
                        "src": f"doc://alexa/apl/documents/{APL_DOCUMENT_ID}"
                    },
                    datasources=DATASOURCE
                )
            )

    def handle(self, handler_input):
        # Add APL Template if device is compatible
        self.launch_screen(handler_input)
        # Generate JSON Response
        return handler_input.response_builder.response

sb = SkillBuilder()
sb.add_request_handler(SampleAPLRequestHandler())
lambda_handler = sb.lambda_handler()