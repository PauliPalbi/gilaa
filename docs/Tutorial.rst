.. Quickstart

Quickstart
==========

Getting the data
++++++++++++++++

``gilaa`` is a package for processing data from the GALAH survey, which means that to begin using it you need an initial dataset.
Go to the `Data Central TAP Service site <https://datacentral.org.au/vo/tap>`_ and query for some data you are interested in.
If you are not familiar with query searching, you can go to this `sample queries stie <https://docs.datacentral.org.au/galah/sample-queries/sample-queries-galah-dr2/>`_ to get started.
Download the data preferably as a .csv file (if you download the file and you can't open it directly, try openning it with a regular text editor and from there save it as a .csv file).

Once you have your data saved in some location, you can initialize a ``plot`` object taking the filename as an argument.
In this example, we are using a .csv file named 'ngc632.csv':

.. code-block:: python

        import gilaa as gl
        data = gl.plot('ngc632.csv')


In this way you can interact with all the functions for handling data.
For example, the function ``plot_abundance()`` allows you to (perhaps unsurprisingly) plot the abundance of certain chemical elements in stars.
The function takes two arguments: ``starnames```, which is a list of up to three star IDs that exist in the catalog (if you only wish to pass one star, you have to do it as a one-element string),
and ``elements``, which is a list of elements whose abundance with reference to iron you want to plot (each element of the list must be a string
of the chemical symbol of the element, i.e. input "C" or "c", not "carbon"). We will take some data from the .csv file:

.. code-block:: python

        starnames=['00490142-7054201', '00582635-7038546']
        elements=['ti', 'li', 'al']
        data.plot_abundance(starnames, elements)

The function will produce a (rather beautiful) plot of the star abundances, and it will return a list of 
dictionaries, containing the elemental abundances (values) for each star (key).