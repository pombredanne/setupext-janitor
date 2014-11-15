from distutils.command.clean import clean as _CleanCommand


version_info = (0, 0, 0)
__version__ = '.'.join(str(v) for v in version_info)


class CleanCommand(_CleanCommand):
    """
    Extend the clean command to do additional house keeping.

    The traditional distutils clean command removes the by-products of
    compiling extension code.  This class extends it to remove the
    similar by-products generated by producing a Python distribution.
    Most notably, it will remove .egg/.egg-info directories, the
    generated distribution, those pesky *__pycache__* directories,
    and even the virtual environment that it is running in.

    The level of cleanliness is controlled by command-line options as
    you might expect.  The targets that are removed are influenced by
    the commands that created them.  For example, if you set a custom
    distribution directory using the ``--dist-dir`` option or the
    matching snippet in *setup.cfg*, then this extension will honor
    that setting.  It even goes as far as to detect the virtual
    environment directory based on environment variables.

    This all sounds a little dangerous... there is little to worry
    about though.  This command only removes what it is configured to
    remove which is nothing by default.  It also honors the
    ``--dry-run`` global option so that there should be no question
    what it is going to remove.

    """

    # See _set_options for `user_options`
    pass


def _set_options():
    """
    Set the options for CleanCommand.

    There are a number of reasons that this has to be done in an
    external function instead of inline in the class.  First of all,
    the setuptools machinery really wants the options to be defined
    in a class attribute - otherwise, the help command doesn't work
    so we need a class attribute.  However, we are extending an
    existing command and do not want to "monkey patch" over it so
    we need to define a *new* class attribute with the same name
    that contains a copy of the base class value.  This could be
    accomplished using some magic in ``__new__`` but I would much
    rather set the class attribute externally... it's just cleaner.

    """
    CleanCommand.user_options = _CleanCommand.user_options[:]
    CleanCommand.user_options.extend([
        ('dist', 'd', 'remove distribution directory'),
    ])

_set_options()
