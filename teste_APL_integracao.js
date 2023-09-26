const Alexa = require("ask-sdk-core");

const DOCUMENT_ID = "uno";

const datasource = {
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
};

const createDirectivePayload = (aplDocumentId, dataSources = {}, tokenId = "documentToken") => {
    return {
        type: "Alexa.Presentation.APL.RenderDocument",
        token: tokenId,
        document: {
            type: "Link",
            src: "doc://alexa/apl/documents/" + aplDocumentId
        },
        datasources: dataSources
    }
};

const SampleAPLRequestHandler = {
    canHandle(handlerInput) {
        // handle named intent
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'INTENT_NAME';
    },
    handle(handlerInput) {
        if (Alexa.getSupportedInterfaces(handlerInput.requestEnvelope)['Alexa.Presentation.APL']) {
            // generate the APL RenderDocument directive that will be returned from your skill
            const aplDirective = createDirectivePayload(DOCUMENT_ID, datasource);
            // add the RenderDocument directive to the responseBuilder
            handlerInput.responseBuilder.addDirective(aplDirective);
        }

        // send out skill response
        return handlerInput.responseBuilder.getResponse();
    }
};

exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(SampleAPLRequestHandler)
    .lambda();