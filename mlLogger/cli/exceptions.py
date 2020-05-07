class Base(Exception):
    '''
    Base class for defining exceptions.
    '''
    pass

class WorkspaceExists(Base):
    '''
    Raises when workspace of name is already present in the database.
    '''
    pass

class WorkspaceDoesNotExists(Base):
    '''
    Raises when workspace which is not present is tried to be deleted.
    '''
    pass

class TimeOut(Base):
    '''
    Raises when Things Time out.
    '''
    pass

