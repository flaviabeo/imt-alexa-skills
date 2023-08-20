const Alexa = require('ask-sdk-core');
const helloWorldDocument = require('./helloWorldDocument.json');
const helloWorldDataSource = require('./sampleDatasource.json');

const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        // Verify the request is an intent request and has the intent name you intend to handle
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest' &&
            Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    }, 
    handle(handlerInput) {
        // Intents can have slots that you can access inside your skill
        const slotValue = Alexa.getSlotValue(handlerInput.requestEnvelope, "nameSlot");
        
        // Check for APL support on the user's device
        if (Alexa.getSupportedInterfaces(handlerInput.requestEnvelope)['Alexa.Presentation.APL']) {
            // ResponseBuilder is used to add APL RenderDocument directive to response
            handlerInput.responseBuilder.addDirective({
                type: 'Alexa.Presentation.APL.RenderDocument',
                document: helloWorldDocument,
                datasources: helloWorldDataSource
            });
        }
        
        return handlerInput.responseBuilder
            .speak(`Hello, ${slotValue}`)
            .getResponse();
    }
};