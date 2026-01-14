def test_print_output(capsys):
    # Importing the module will execute the print statement
    import main  # noqa: F401

    captured = capsys.readouterr()
    assert captured.out == "This is test file.\n"
