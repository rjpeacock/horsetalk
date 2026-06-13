from horsetalk import Obstacle


def test_obstacle_can_be_created_from_none():
    assert Obstacle(0) == Obstacle.NONE
    assert Obstacle["NONE"] == Obstacle.NONE


def test_obstacle_can_be_created_from_enum():
    assert Obstacle(1) == Obstacle.HURDLE


def test_obstacle_can_be_created_from_name():
    assert Obstacle["HURDLE"] == Obstacle.HURDLE


def test_obstacle_can_be_created_from_lowercase_name():
    assert Obstacle["hurdle"] == Obstacle.HURDLE


def test_obstacle_can_be_created_from_hyphenated_name():
    assert Obstacle["CROSS-COUNTRY"] == Obstacle.CROSS_COUNTRY


def test_obstacle_can_be_created_from_unhyphenated_name():
    assert Obstacle["CROSS COUNTRY"] == Obstacle.CROSS_COUNTRY


def test_obstacle_can_be_created_from_abbreviation():
    assert Obstacle["h"] == Obstacle.HURDLE
