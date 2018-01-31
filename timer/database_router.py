from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING

#tecnav数据库路由规则
class TecnavRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    app_label_tecnav = 'tecnav'
    db_tecnav = 'tecnav'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == TecnavRouter.app_label_tecnav:
            return TecnavRouter.app_label_tecnav
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == TecnavRouter.app_label_tecnav:
            return TecnavRouter.app_label_tecnav
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == TecnavRouter.app_label_tecnav or \
           obj2._meta.app_label == TecnavRouter.app_label_tecnav:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == TecnavRouter.app_label_tecnav:
            return db == TecnavRouter.db_tecnav
        return None
