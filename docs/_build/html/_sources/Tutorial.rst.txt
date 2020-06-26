.. Quickstart

Quickstart
==========

Getting the data
++++++++++++++++

``gilaa`` is a package for processing data from the GALAH survey, which means that to begin using it you need an initial dataset.
Go to the `Data Central TAP Service site <https://datacentral.org.au/vo/tap>`_ and query for some data you are interested in.
If you are not familiar with query searching, you can go to this `sample queries stie <https://docs.datacentral.org.au/galah/sample-queries/sample-queries-galah-dr2/>`_ to get started.
Download the data preferably as a .csv file (if you download the file and you can't open it directly, try openning it with a regular text editor and from there save it as a .csv file).

Basic plotting
++++++++++++++

Once you have your data saved in some location, you must import the ``plot``module and then
 initialize a ``plot`` object taking the filename as an argument.
In this example, we are using a .csv file named 'ngc632.csv':

.. code-block:: python

        from gilaa import plot
        data = plot.plot('ngc632.csv')


In this way you can interact with all the functions for handling data.
For example, the function ``plot_abundance()`` allows you to (perhaps unsurprisingly) plot the abundance of certain chemical elements in stars.
The function takes two arguments: ``starnames``, which is a list of up to three star IDs that exist in the catalog (if you only wish to pass one star, you have to do it as a one-element string),
and ``elements``, which is a list of elements whose abundance with reference to iron you want to plot (each element of the list must be a string
of the chemical symbol of the element, i.e. input "C" or "c", not "carbon"). We will take the star IDs from the .csv file:

.. code-block:: python

        starnames=['00490142-7054201', '00582635-7038546']
        elements=['ti', 'li', 'al']
        data.plot_abundance(starnames, elements)

The function will produce a (rather beautiful) plot of the star abundances, and it will return a list of 
dictionaries, containing the elemental abundances (values) for each star (key).

You can also plot the variables with their associated uncertainties (if they exist in the catalog). 
To accomplish this, use the ``errorPlot()`` function, which takes two arguments: ``variables``, which is a list
of all the variables you want to plot from the catalog, and ``star_ids``. For ``variables``, the input format must
be the one used in the table columns, which you can consult `here <https://docs.datacentral.org.au/galah/table-schema/dr2-table-schema/>`_.
The function will plot those variables that have an associated uncertainty in the catalog, and will let you
know of those which don't. For example:

.. code-block:: python

        variables=['ba_fe', 'rv_synt', 'al_fe']
        star_ids=['00490142-7054201', '00582635-7038546']
        data.errorPlot(variables, star_ids)

Again, the function will generate a plot with the associated error bars, and will return a dictionary with
the data corresponding to each star.