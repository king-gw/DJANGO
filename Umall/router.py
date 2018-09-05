class Router():

    def db_for_read(self,models,**hints):
        return 'read'
    def db_for_write(self,models,**hints):
        return 'default'