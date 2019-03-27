class MutationRoot:
    def __init__(self, client):
        self.client = client

    def verifyPassword(self, email, password):
        email_arg = 'email:"%s",' % email
        password_arg = 'password:"%s",' % password
        
        return self.client.mutation('mutation{verifyPassword(%s%s)}' % (email_arg,password_arg))["verifyPassword"]
    
    def verifyWebAuthn(self, challengeResponse, jwtChallenge):
        challengeResponse_arg = 'challengeResponse:"%s",' % challengeResponse
        jwtChallenge_arg = 'jwtChallenge:"%s",' % jwtChallenge
        
        return self.client.mutation('mutation{verifyWebAuthn(%s%s)}' % (challengeResponse_arg,jwtChallenge_arg))["verifyWebAuthn"]
    
    def verifyTotp(self, email=None, code=None):
        
        email_arg = 'email:"%s",' % email if email is not None else ''
        code_arg = 'code:"%s",' % code if code is not None else ''
        return self.client.mutation('mutation{verifyTotp(%s%s)}' % (email_arg,code_arg))["verifyTotp"]
    
    def verifyEmailToken(self, token):
        token_arg = 'token:"%s",' % token
        
        return self.client.mutation('mutation{verifyEmailToken(%s)}' % (token_arg))["verifyEmailToken"]
    
    def sendConfirmationEmail(self, email, operation):
        email_arg = 'email:"%s",' % email
        operation_arg = 'operation:%s,' % operation
        
        return self.client.mutation('mutation{sendConfirmationEmail(%s%s)}' % (email_arg,operation_arg))["sendConfirmationEmail"]
    
    def logIn(self, passwordCertificate=None, webAuthnCertificate=None, totpCertificate=None, emailCertificate=None):
        
        passwordCertificate_arg = 'passwordCertificate:"%s",' % passwordCertificate if passwordCertificate is not None else ''
        webAuthnCertificate_arg = 'webAuthnCertificate:"%s",' % webAuthnCertificate if webAuthnCertificate is not None else ''
        totpCertificate_arg = 'totpCertificate:"%s",' % totpCertificate if totpCertificate is not None else ''
        emailCertificate_arg = 'emailCertificate:"%s",' % emailCertificate if emailCertificate is not None else ''
        return self.client.mutation('mutation{logIn(%s%s%s%s){id}}' % (passwordCertificate_arg,webAuthnCertificate_arg,totpCertificate_arg,emailCertificate_arg))["logIn"]
    
    def createToken(self, tokenType, passwordCertificate=None, webAuthnCertificate=None, totpCertificate=None, emailCertificate=None):
        tokenType_arg = 'tokenType:%s,' % tokenType
        passwordCertificate_arg = 'passwordCertificate:"%s",' % passwordCertificate if passwordCertificate is not None else ''
        webAuthnCertificate_arg = 'webAuthnCertificate:"%s",' % webAuthnCertificate if webAuthnCertificate is not None else ''
        totpCertificate_arg = 'totpCertificate:"%s",' % totpCertificate if totpCertificate is not None else ''
        emailCertificate_arg = 'emailCertificate:"%s",' % emailCertificate if emailCertificate is not None else ''
        return self.client.mutation('mutation{createToken(%s%s%s%s%s)}' % (passwordCertificate_arg,webAuthnCertificate_arg,totpCertificate_arg,emailCertificate_arg,tokenType_arg))["createToken"]
    
    def createPermanentToken(self, name):
        name_arg = 'name:"%s",' % name
        
        return self.client.mutation('mutation{createPermanentToken(%s){id}}' % (name_arg))["createPermanentToken"]
    
    def regeneratePermanentToken(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{regeneratePermanentToken(%s)}' % (id_arg))["regeneratePermanentToken"]
    
    def deletePermanentToken(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deletePermanentToken(%s)}' % (id_arg))["deletePermanentToken"]
    
    def signUp(self, email, name):
        email_arg = 'email:"%s",' % email
        name_arg = 'name:"%s",' % name
        
        return self.client.mutation('mutation{signUp(%s%s){id}}' % (email_arg,name_arg))["signUp"]
    
    def setPassword(self, password):
        password_arg = 'password:"%s",' % password
        
        return self.client.mutation('mutation{setPassword(%s){id}}' % (password_arg))["setPassword"]
    
    def setTotp(self, code=None, secret=None):
        
        code_arg = 'code:"%s",' % code if code is not None else ''
        secret_arg = 'secret:"%s",' % secret if secret is not None else ''
        return self.client.mutation('mutation{setTotp(%s%s)}' % (code_arg,secret_arg))["setTotp"]
    
    def setWebAuthn(self, challengeResponse=None, jwtChallenge=None):
        
        challengeResponse_arg = 'challengeResponse:"%s",' % challengeResponse if challengeResponse is not None else ''
        jwtChallenge_arg = 'jwtChallenge:"%s",' % jwtChallenge if jwtChallenge is not None else ''
        return self.client.mutation('mutation{setWebAuthn(%s%s){id}}' % (challengeResponse_arg,jwtChallenge_arg))["setWebAuthn"]
    
    def changeAuthenticationSettings(self, primaryAuthenticationMethods, secondaryAuthenticationMethods):
        primaryAuthenticationMethods_arg = 'primaryAuthenticationMethods:%s,' % primaryAuthenticationMethods
        secondaryAuthenticationMethods_arg = 'secondaryAuthenticationMethods:%s,' % secondaryAuthenticationMethods
        
        return self.client.mutation('mutation{changeAuthenticationSettings(%s%s){id}}' % (primaryAuthenticationMethods_arg,secondaryAuthenticationMethods_arg))["changeAuthenticationSettings"]
    
    def resendVerificationEmail(self, email):
        email_arg = 'email:"%s",' % email
        
        return self.client.mutation('mutation{resendVerificationEmail(%s)}' % (email_arg))["resendVerificationEmail"]
    
    def shareEnvironment(self, environmentId, role, email=None, userId=None):
        environmentId_arg = 'environmentId:"%s",' % environmentId
        role_arg = 'role:%s,' % role
        email_arg = 'email:"%s",' % email if email is not None else ''
        userId_arg = 'userId:"%s",' % userId if userId is not None else ''
        return self.client.mutation('mutation{shareEnvironment(%s%s%s%s){id}}' % (environmentId_arg,email_arg,userId_arg,role_arg))["shareEnvironment"]
    
    def pendingEnvironmentShare(self, id, role):
        id_arg = 'id:"%s",' % id
        role_arg = 'role:%s,' % role
        
        return self.client.mutation('mutation{pendingEnvironmentShare(%s%s){id}}' % (id_arg,role_arg))["pendingEnvironmentShare"]
    
    def revokePendingEnvironmentShare(self, pendingEnvironmentShareId):
        pendingEnvironmentShareId_arg = 'pendingEnvironmentShareId:"%s",' % pendingEnvironmentShareId
        
        return self.client.mutation('mutation{revokePendingEnvironmentShare(%s)}' % (pendingEnvironmentShareId_arg))["revokePendingEnvironmentShare"]
    
    def acceptPendingEnvironmentShare(self, pendingEnvironmentShareId):
        pendingEnvironmentShareId_arg = 'pendingEnvironmentShareId:"%s",' % pendingEnvironmentShareId
        
        return self.client.mutation('mutation{acceptPendingEnvironmentShare(%s){id}}' % (pendingEnvironmentShareId_arg))["acceptPendingEnvironmentShare"]
    
    def declinePendingEnvironmentShare(self, pendingEnvironmentShareId):
        pendingEnvironmentShareId_arg = 'pendingEnvironmentShareId:"%s",' % pendingEnvironmentShareId
        
        return self.client.mutation('mutation{declinePendingEnvironmentShare(%s)}' % (pendingEnvironmentShareId_arg))["declinePendingEnvironmentShare"]
    
    def stopSharingEnvironment(self, environmentId, email=None, userId=None):
        environmentId_arg = 'environmentId:"%s",' % environmentId
        email_arg = 'email:"%s",' % email if email is not None else ''
        userId_arg = 'userId:"%s",' % userId if userId is not None else ''
        return self.client.mutation('mutation{stopSharingEnvironment(%s%s%s){id}}' % (environmentId_arg,email_arg,userId_arg))["stopSharingEnvironment"]
    
    def leaveEnvironment(self, environmentId):
        environmentId_arg = 'environmentId:"%s",' % environmentId
        
        return self.client.mutation('mutation{leaveEnvironment(%s)}' % (environmentId_arg))["leaveEnvironment"]
    
    def changeOwner(self, environmentId, email=None, userId=None):
        environmentId_arg = 'environmentId:"%s",' % environmentId
        email_arg = 'email:"%s",' % email if email is not None else ''
        userId_arg = 'userId:"%s",' % userId if userId is not None else ''
        return self.client.mutation('mutation{changeOwner(%s%s%s){id}}' % (environmentId_arg,email_arg,userId_arg))["changeOwner"]
    
    def revokePendingOwnerChange(self, pendingOwnerChangeId):
        pendingOwnerChangeId_arg = 'pendingOwnerChangeId:"%s",' % pendingOwnerChangeId
        
        return self.client.mutation('mutation{revokePendingOwnerChange(%s)}' % (pendingOwnerChangeId_arg))["revokePendingOwnerChange"]
    
    def acceptPendingOwnerChange(self, pendingOwnerChangeId):
        pendingOwnerChangeId_arg = 'pendingOwnerChangeId:"%s",' % pendingOwnerChangeId
        
        return self.client.mutation('mutation{acceptPendingOwnerChange(%s){id}}' % (pendingOwnerChangeId_arg))["acceptPendingOwnerChange"]
    
    def declinePendingOwnerChange(self, pendingOwnerChangeId):
        pendingOwnerChangeId_arg = 'pendingOwnerChangeId:"%s",' % pendingOwnerChangeId
        
        return self.client.mutation('mutation{declinePendingOwnerChange(%s)}' % (pendingOwnerChangeId_arg))["declinePendingOwnerChange"]
    
    def changeRole(self, environmentId, email, newRole):
        environmentId_arg = 'environmentId:"%s",' % environmentId
        email_arg = 'email:"%s",' % email
        newRole_arg = 'newRole:%s,' % newRole
        
        return self.client.mutation('mutation{changeRole(%s%s%s){id}}' % (environmentId_arg,email_arg,newRole_arg))["changeRole"]
    
    def createEnvironment(self, name, picture=None, index=None, muted=None):
        name_arg = 'name:"%s",' % name
        picture_arg = 'picture:%s,' % picture if picture is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        muted_arg = 'muted:%s,' % muted if muted is not None else ''
        return self.client.mutation('mutation{createEnvironment(%s%s%s%s){id}}' % (name_arg,picture_arg,index_arg,muted_arg))["createEnvironment"]
    
    def createDevice(self, deviceType=None, firmware=None):
        
        deviceType_arg = 'deviceType:"%s",' % deviceType if deviceType is not None else ''
        firmware_arg = 'firmware:"%s",' % firmware if firmware is not None else ''
        return self.client.mutation('mutation{createDevice(%s%s){id}}' % (deviceType_arg,firmware_arg))["createDevice"]
    
    def claimDevice(self, deviceId, name, environmentId, index=None, muted=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        name_arg = 'name:"%s",' % name
        environmentId_arg = 'environmentId:"%s",' % environmentId
        index_arg = 'index:%s,' % index if index is not None else ''
        muted_arg = 'muted:%s,' % muted if muted is not None else ''
        return self.client.mutation('mutation{claimDevice(%s%s%s%s%s){id}}' % (deviceId_arg,name_arg,index_arg,environmentId_arg,muted_arg))["claimDevice"]
    
    def createNotification(self, deviceId, content, date=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        content_arg = 'content:"%s",' % content
        date_arg = 'date:%s,' % date if date is not None else ''
        return self.client.mutation('mutation{createNotification(%s%s%s){id}}' % (deviceId_arg,content_arg,date_arg))["createNotification"]
    
    def createFloatValue(self, deviceId, permission, name, visibility=None, unitOfMeasurement=None, value=None, precision=None, min=None, max=None, cardSize=None, index=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        permission_arg = 'permission:%s,' % permission
        name_arg = 'name:"%s",' % name
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        unitOfMeasurement_arg = 'unitOfMeasurement:"%s",' % unitOfMeasurement if unitOfMeasurement is not None else ''
        value_arg = 'value:%s,' % value if value is not None else ''
        precision_arg = 'precision:%s,' % precision if precision is not None else ''
        min_arg = 'min:%s,' % min if min is not None else ''
        max_arg = 'max:%s,' % max if max is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{createFloatValue(%s%s%s%s%s%s%s%s%s%s%s){id}}' % (deviceId_arg,permission_arg,visibility_arg,unitOfMeasurement_arg,value_arg,precision_arg,min_arg,max_arg,name_arg,cardSize_arg,index_arg))["createFloatValue"]
    
    def createStringValue(self, deviceId, permission, name, visibility=None, value=None, maxChars=None, cardSize=None, allowedValues=None, index=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        permission_arg = 'permission:%s,' % permission
        name_arg = 'name:"%s",' % name
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        value_arg = 'value:"%s",' % value if value is not None else ''
        maxChars_arg = 'maxChars:%s,' % maxChars if maxChars is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        allowedValues_arg = 'allowedValues:%s,' % allowedValues if allowedValues is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{createStringValue(%s%s%s%s%s%s%s%s%s){id}}' % (deviceId_arg,permission_arg,visibility_arg,value_arg,maxChars_arg,name_arg,cardSize_arg,allowedValues_arg,index_arg))["createStringValue"]
    
    def createBooleanValue(self, deviceId, permission, name, visibility=None, value=None, cardSize=None, index=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        permission_arg = 'permission:%s,' % permission
        name_arg = 'name:"%s",' % name
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        value_arg = 'value:%s,' % value if value is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{createBooleanValue(%s%s%s%s%s%s%s){id}}' % (deviceId_arg,permission_arg,visibility_arg,value_arg,name_arg,cardSize_arg,index_arg))["createBooleanValue"]
    
    def createPlotValue(self, deviceId, name, visibility=None, unitOfMeasurement=None, precision=None, min=None, max=None, cardSize=None, threshold=None, index=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        name_arg = 'name:"%s",' % name
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        unitOfMeasurement_arg = 'unitOfMeasurement:"%s",' % unitOfMeasurement if unitOfMeasurement is not None else ''
        precision_arg = 'precision:%s,' % precision if precision is not None else ''
        min_arg = 'min:%s,' % min if min is not None else ''
        max_arg = 'max:%s,' % max if max is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        threshold_arg = 'threshold:%s,' % threshold if threshold is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{createPlotValue(%s%s%s%s%s%s%s%s%s%s){id}}' % (deviceId_arg,visibility_arg,unitOfMeasurement_arg,precision_arg,min_arg,max_arg,name_arg,cardSize_arg,threshold_arg,index_arg))["createPlotValue"]
    
    def createPlotNode(self, plotId, value, timestamp=None):
        plotId_arg = 'plotId:"%s",' % plotId
        value_arg = 'value:%s,' % value
        timestamp_arg = 'timestamp:%s,' % timestamp if timestamp is not None else ''
        return self.client.mutation('mutation{createPlotNode(%s%s%s){id}}' % (plotId_arg,timestamp_arg,value_arg))["createPlotNode"]
    
    def createCategoryPlotValue(self, deviceId, name, visibility=None, cardSize=None, allowedValues=None, index=None):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        name_arg = 'name:"%s",' % name
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        allowedValues_arg = 'allowedValues:%s,' % allowedValues if allowedValues is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{createCategoryPlotValue(%s%s%s%s%s%s){id}}' % (deviceId_arg,visibility_arg,name_arg,cardSize_arg,allowedValues_arg,index_arg))["createCategoryPlotValue"]
    
    def createCategoryPlotNode(self, plotId, value, timestamp=None):
        plotId_arg = 'plotId:"%s",' % plotId
        value_arg = 'value:"%s",' % value
        timestamp_arg = 'timestamp:%s,' % timestamp if timestamp is not None else ''
        return self.client.mutation('mutation{createCategoryPlotNode(%s%s%s){id}}' % (plotId_arg,timestamp_arg,value_arg))["createCategoryPlotNode"]
    
    def user(self, quietMode=None, devMode=None, paymentPlan=None, name=None, profileIcon=None):
        
        quietMode_arg = 'quietMode:%s,' % quietMode if quietMode is not None else ''
        devMode_arg = 'devMode:%s,' % devMode if devMode is not None else ''
        paymentPlan_arg = 'paymentPlan:%s,' % paymentPlan if paymentPlan is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        profileIcon_arg = 'profileIcon:"%s",' % profileIcon if profileIcon is not None else ''
        return self.client.mutation('mutation{user(%s%s%s%s%s){id}}' % (quietMode_arg,devMode_arg,paymentPlan_arg,name_arg,profileIcon_arg))["user"]
    
    def changeEmail(self, newEmail):
        newEmail_arg = 'newEmail:"%s",' % newEmail
        
        return self.client.mutation('mutation{changeEmail(%s)}' % (newEmail_arg))["changeEmail"]
    
    def settings(self, language=None, lengthAndMass=None, temperature=None, dateFormat=None, timeFormat=None, passwordChangeEmail=None, pendingOwnerChangeReceivedEmail=None, pendingEnvironmentShareReceivedEmail=None, pendingOwnerChangeAcceptedEmail=None, pendingEnvironmentShareAcceptedEmail=None, permanentTokenCreatedEmail=None):
        
        language_arg = 'language:"%s",' % language if language is not None else ''
        lengthAndMass_arg = 'lengthAndMass:%s,' % lengthAndMass if lengthAndMass is not None else ''
        temperature_arg = 'temperature:%s,' % temperature if temperature is not None else ''
        dateFormat_arg = 'dateFormat:%s,' % dateFormat if dateFormat is not None else ''
        timeFormat_arg = 'timeFormat:%s,' % timeFormat if timeFormat is not None else ''
        passwordChangeEmail_arg = 'passwordChangeEmail:%s,' % passwordChangeEmail if passwordChangeEmail is not None else ''
        pendingOwnerChangeReceivedEmail_arg = 'pendingOwnerChangeReceivedEmail:%s,' % pendingOwnerChangeReceivedEmail if pendingOwnerChangeReceivedEmail is not None else ''
        pendingEnvironmentShareReceivedEmail_arg = 'pendingEnvironmentShareReceivedEmail:%s,' % pendingEnvironmentShareReceivedEmail if pendingEnvironmentShareReceivedEmail is not None else ''
        pendingOwnerChangeAcceptedEmail_arg = 'pendingOwnerChangeAcceptedEmail:%s,' % pendingOwnerChangeAcceptedEmail if pendingOwnerChangeAcceptedEmail is not None else ''
        pendingEnvironmentShareAcceptedEmail_arg = 'pendingEnvironmentShareAcceptedEmail:%s,' % pendingEnvironmentShareAcceptedEmail if pendingEnvironmentShareAcceptedEmail is not None else ''
        permanentTokenCreatedEmail_arg = 'permanentTokenCreatedEmail:%s,' % permanentTokenCreatedEmail if permanentTokenCreatedEmail is not None else ''
        return self.client.mutation('mutation{settings(%s%s%s%s%s%s%s%s%s%s%s){id}}' % (language_arg,lengthAndMass_arg,temperature_arg,dateFormat_arg,timeFormat_arg,passwordChangeEmail_arg,pendingOwnerChangeReceivedEmail_arg,pendingEnvironmentShareReceivedEmail_arg,pendingOwnerChangeAcceptedEmail_arg,pendingEnvironmentShareAcceptedEmail_arg,permanentTokenCreatedEmail_arg))["settings"]
    
    def updatePaymentInfo(self, stripeToken):
        stripeToken_arg = 'stripeToken:"%s",' % stripeToken
        
        return self.client.mutation('mutation{updatePaymentInfo(%s)}' % (stripeToken_arg))["updatePaymentInfo"]
    
    def environment(self, id, name=None, picture=None, index=None, muted=None):
        id_arg = 'id:"%s",' % id
        name_arg = 'name:"%s",' % name if name is not None else ''
        picture_arg = 'picture:%s,' % picture if picture is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        muted_arg = 'muted:%s,' % muted if muted is not None else ''
        return self.client.mutation('mutation{environment(%s%s%s%s%s){id}}' % (id_arg,name_arg,picture_arg,index_arg,muted_arg))["environment"]
    
    def device(self, id, deviceType=None, name=None, index=None, signalStatus=None, batteryStatus=None, batteryCharging=None, firmware=None, muted=None, starred=None):
        id_arg = 'id:"%s",' % id
        deviceType_arg = 'deviceType:"%s",' % deviceType if deviceType is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        signalStatus_arg = 'signalStatus:%s,' % signalStatus if signalStatus is not None else ''
        batteryStatus_arg = 'batteryStatus:%s,' % batteryStatus if batteryStatus is not None else ''
        batteryCharging_arg = 'batteryCharging:%s,' % batteryCharging if batteryCharging is not None else ''
        firmware_arg = 'firmware:"%s",' % firmware if firmware is not None else ''
        muted_arg = 'muted:%s,' % muted if muted is not None else ''
        starred_arg = 'starred:%s,' % starred if starred is not None else ''
        return self.client.mutation('mutation{device(%s%s%s%s%s%s%s%s%s%s){id}}' % (id_arg,deviceType_arg,name_arg,index_arg,signalStatus_arg,batteryStatus_arg,batteryCharging_arg,firmware_arg,muted_arg,starred_arg))["device"]
    
    def value(self, id, visibility=None, cardSize=None, name=None, index=None):
        id_arg = 'id:"%s",' % id
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{value(%s%s%s%s%s){id}}' % (id_arg,visibility_arg,cardSize_arg,name_arg,index_arg))["value"]
    
    def moveDevice(self, deviceId, newEnvironmentId):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        newEnvironmentId_arg = 'newEnvironmentId:"%s",' % newEnvironmentId
        
        return self.client.mutation('mutation{moveDevice(%s%s){id}}' % (deviceId_arg,newEnvironmentId_arg))["moveDevice"]
    
    def resetOnlineState(self, deviceId):
        deviceId_arg = 'deviceId:"%s",' % deviceId
        
        return self.client.mutation('mutation{resetOnlineState(%s){id}}' % (deviceId_arg))["resetOnlineState"]
    
    def floatValue(self, id, permission=None, visibility=None, unitOfMeasurement=None, value=None, precision=None, min=None, max=None, name=None, cardSize=None, index=None):
        id_arg = 'id:"%s",' % id
        permission_arg = 'permission:%s,' % permission if permission is not None else ''
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        unitOfMeasurement_arg = 'unitOfMeasurement:"%s",' % unitOfMeasurement if unitOfMeasurement is not None else ''
        value_arg = 'value:%s,' % value if value is not None else ''
        precision_arg = 'precision:%s,' % precision if precision is not None else ''
        min_arg = 'min:%s,' % min if min is not None else ''
        max_arg = 'max:%s,' % max if max is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{floatValue(%s%s%s%s%s%s%s%s%s%s%s){id}}' % (id_arg,permission_arg,visibility_arg,unitOfMeasurement_arg,value_arg,precision_arg,min_arg,max_arg,name_arg,cardSize_arg,index_arg))["floatValue"]
    
    def atomicUpdateFloat(self, id, incrementBy):
        id_arg = 'id:"%s",' % id
        incrementBy_arg = 'incrementBy:%s,' % incrementBy
        
        return self.client.mutation('mutation{atomicUpdateFloat(%s%s){id}}' % (id_arg,incrementBy_arg))["atomicUpdateFloat"]
    
    def stringValue(self, id, permission=None, visibility=None, value=None, maxChars=None, name=None, cardSize=None, allowedValues=None, index=None):
        id_arg = 'id:"%s",' % id
        permission_arg = 'permission:%s,' % permission if permission is not None else ''
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        value_arg = 'value:"%s",' % value if value is not None else ''
        maxChars_arg = 'maxChars:%s,' % maxChars if maxChars is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        allowedValues_arg = 'allowedValues:%s,' % allowedValues if allowedValues is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{stringValue(%s%s%s%s%s%s%s%s%s){id}}' % (id_arg,permission_arg,visibility_arg,value_arg,maxChars_arg,name_arg,cardSize_arg,allowedValues_arg,index_arg))["stringValue"]
    
    def booleanValue(self, id, permission=None, visibility=None, value=None, name=None, cardSize=None, index=None):
        id_arg = 'id:"%s",' % id
        permission_arg = 'permission:%s,' % permission if permission is not None else ''
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        value_arg = 'value:%s,' % value if value is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{booleanValue(%s%s%s%s%s%s%s){id}}' % (id_arg,permission_arg,visibility_arg,value_arg,name_arg,cardSize_arg,index_arg))["booleanValue"]
    
    def plotValue(self, id, visibility=None, unitOfMeasurement=None, precision=None, min=None, max=None, name=None, cardSize=None, threshold=None, index=None):
        id_arg = 'id:"%s",' % id
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        unitOfMeasurement_arg = 'unitOfMeasurement:"%s",' % unitOfMeasurement if unitOfMeasurement is not None else ''
        precision_arg = 'precision:%s,' % precision if precision is not None else ''
        min_arg = 'min:%s,' % min if min is not None else ''
        max_arg = 'max:%s,' % max if max is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        threshold_arg = 'threshold:%s,' % threshold if threshold is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{plotValue(%s%s%s%s%s%s%s%s%s%s){id}}' % (id_arg,visibility_arg,unitOfMeasurement_arg,precision_arg,min_arg,max_arg,name_arg,cardSize_arg,threshold_arg,index_arg))["plotValue"]
    
    def plotNode(self, id, value=None, timestamp=None):
        id_arg = 'id:"%s",' % id
        value_arg = 'value:%s,' % value if value is not None else ''
        timestamp_arg = 'timestamp:%s,' % timestamp if timestamp is not None else ''
        return self.client.mutation('mutation{plotNode(%s%s%s){id}}' % (id_arg,value_arg,timestamp_arg))["plotNode"]
    
    def categoryPlotValue(self, id, visibility=None, name=None, cardSize=None, allowedValues=None, index=None):
        id_arg = 'id:"%s",' % id
        visibility_arg = 'visibility:%s,' % visibility if visibility is not None else ''
        name_arg = 'name:"%s",' % name if name is not None else ''
        cardSize_arg = 'cardSize:%s,' % cardSize if cardSize is not None else ''
        allowedValues_arg = 'allowedValues:%s,' % allowedValues if allowedValues is not None else ''
        index_arg = 'index:%s,' % index if index is not None else ''
        return self.client.mutation('mutation{categoryPlotValue(%s%s%s%s%s%s){id}}' % (id_arg,visibility_arg,name_arg,cardSize_arg,allowedValues_arg,index_arg))["categoryPlotValue"]
    
    def categoryPlotNode(self, id, value=None, timestamp=None):
        id_arg = 'id:"%s",' % id
        value_arg = 'value:"%s",' % value if value is not None else ''
        timestamp_arg = 'timestamp:%s,' % timestamp if timestamp is not None else ''
        return self.client.mutation('mutation{categoryPlotNode(%s%s%s){id}}' % (id_arg,value_arg,timestamp_arg))["categoryPlotNode"]
    
    def notification(self, id, content=None, read=None):
        id_arg = 'id:"%s",' % id
        content_arg = 'content:"%s",' % content if content is not None else ''
        read_arg = 'read:%s,' % read if read is not None else ''
        return self.client.mutation('mutation{notification(%s%s%s){id}}' % (id_arg,content_arg,read_arg))["notification"]
    
    def deleteNotification(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deleteNotification(%s)}' % (id_arg))["deleteNotification"]
    
    def deleteValue(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deleteValue(%s)}' % (id_arg))["deleteValue"]
    
    def deleteDevice(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deleteDevice(%s)}' % (id_arg))["deleteDevice"]
    
    def unclaimDevice(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{unclaimDevice(%s){id}}' % (id_arg))["unclaimDevice"]
    
    def deleteEnvironment(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deleteEnvironment(%s)}' % (id_arg))["deleteEnvironment"]
    
    def deleteUser(self, ):
        
        
        return self.client.mutation('mutation{deleteUser()}' % ())["deleteUser"]
    
    def deletePlotNode(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deletePlotNode(%s)}' % (id_arg))["deletePlotNode"]
    
    def deleteCategoryPlotNode(self, id):
        id_arg = 'id:"%s",' % id
        
        return self.client.mutation('mutation{deleteCategoryPlotNode(%s)}' % (id_arg))["deleteCategoryPlotNode"]
    