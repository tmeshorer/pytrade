from injector import Injector


from pytrade.config.db import Database

injector = Injector()

database = injector.get(Database)
task_repository = injector.get(TaskRepository)
task_service = injector.get(TaskService)