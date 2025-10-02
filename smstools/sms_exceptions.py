# This is the base exception for all of our errors
class SMSToolError(Exception):
    pass

# This is for when the output DB already has messages
class NonEmptyStartDBError(SMSToolError):
    pass

# This is for bad arguments
class ArgumentError(SMSToolError):
    pass

# class SMSToolError(OSError):
#     '''root error for SMSToolErrors, shouldn't ever be raised directly'''
#     pass

class UnrecognizedDBError(SMSToolError):
    '''Unrecognized sqlite format'''
    pass

class UnfinishedError(SMSToolError):
    '''Not yet implimented'''
    pass
