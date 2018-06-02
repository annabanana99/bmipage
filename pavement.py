from paver.tasks import task, BuildFailure
from paver.easy import sh, needs

@task
def acceptance_test():
    sh('behave Behave')

@task
def unit_test():
    sh('nosetests tests/bmi_page')

@task
def unit_test2():
    sh('nosetests Behave try 2/steps')

@needs('acceptance_test', 'unit_test', 'unit_test2')
@task
def default():
    pass