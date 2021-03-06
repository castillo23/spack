from spack import *
import os


class Global(Package):
    """ The Gnu Global tagging system """

    homepage = "http://www.gnu.org/software/global"
    url = "http://tamacom.com/global/global-6.5.tar.gz"

    version('6.5', 'dfec818b4f53d91721e247cf7b218078')

    depends_on('exuberant-ctags')
    depends_on('ncurses')

    def install(self, spec, prefix):
        config_args = ['--prefix={0}'.format(prefix)]

        config_args.append('--with-exuberant-ctags={0}'.format(
            os.path.join(spec['exuberant-ctags'].prefix.bin, 'ctags')))

        configure(*config_args)

        make()
        make("install")
