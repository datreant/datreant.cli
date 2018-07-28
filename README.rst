=============================================================
datreant.cli: convenient CLI interface for Treant directories
=============================================================

This `datreant`_ submodule adds a convenience CLI interface for Treant
directories. It provides a easy way to filter directories based on tags and
categories.

For more information on what **datreant** is and what it does, check out the
`official documentation`_.

.. _`official documentation`: http://datreant.readthedocs.org/
.. _`datreant`: http://datreant.org/

Getting datreant.cli
====================

If you want to work on the code, either for yourself or to contribute back to
the project, clone the repository to your local machine with::

    git clone https://github.com/datreant/datreant.cli.git
    cd datreant.cli
    python setup.py install


Using datreant.cli
==================

You should have a new command `dtr` available.

For example to look how many files are in each simulation of 1AKE that are
created with gromacs one could use the following line, assuming 1AKE and gromacs
are tags::

   for f in $(dtr search simulations --tags=1AKE --categories gromacs:2016.4)
   do
       ls $l | wc -l
   done

Contributing
============
This project is still under heavy development, and there are certainly rough
edges and bugs. Issues and pull requests welcome!
