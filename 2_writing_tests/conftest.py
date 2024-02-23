import pytest


@pytest.fixture(scope='function')
def allure_title(request):
    title = request.node.get_closest_marker('title')
    if title:
        return title.args[0]


@pytest.fixture(scope='function')
def allure_description(request):
    description = request.node.get_closest_marker('description')
    if description:
        return description.args[0]


@pytest.fixture(scope='function')
def allure_feature(request):
    feature = request.node.get_closest_marker('feature')
    if feature:
        return feature.args[0]
