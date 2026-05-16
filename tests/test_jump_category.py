import warnings


def test_jump_category_deprecated_alias_still_works():
    """TODO: Delete this test when JumpCategory deprecation is complete (v1.0.0+)."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        from horsetalk import JumpCategory

        assert JumpCategory(1) == JumpCategory.HURDLE
        assert JumpCategory["HURDLE"] == JumpCategory.HURDLE
        assert JumpCategory["h"] == JumpCategory.HURDLE

    assert len(w) >= 1
    assert issubclass(w[0].category, DeprecationWarning)
    assert "v1.0.0" in str(w[0].message)
