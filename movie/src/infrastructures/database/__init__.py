from ...core.config import settings

IS_RELATIONAL_DB = True
IS_DOCUMENT_DB = False
DATABASE_TYPE = settings.DATABASE_TYPE

if DATABASE_TYPE == 'postgresql':
    from .postgres import AsyncPostgreSQLEngine as AsyncRelationalDBEngine
    from .postgres import AsyncPostgreSQLScopedSession as AsyncScopedSession
    from .postgres import get_async_postgresql_session as get_async_session
    from .postgres import initialize_postgres_db as initialize_db

    IS_RELATIONAL_DB = True

elif DATABASE_TYPE == 'mongodb':
    from .mongodb import initialize_mongo_db as initialize_db

    IS_DOCUMENT_DB = True

else:
    raise RuntimeError(
        f'Invalid database type \'{DATABASE_TYPE}\' provided in DATABASE_URI: {settings.DATABASE_URI}'
    )
