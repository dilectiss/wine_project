
.. code:: ipython3

    import numpy as np

.. code:: ipython3

    import pandas as pd

.. code:: ipython3

    # Import WINE data from .csv files
    #
    # Concatenate the smaller tables into one table using pd.concat()
    #
    # Create index as name + vintage
    # the same shall be done for the RATINGS table
    # so that we will have a common index as key
    # This is to be done using set_index() function
    #
    # Remove duplicates using the drop_duplicates() function

.. code:: ipython3

    # Load the raw data files

.. code:: ipython3

    wine_rp = pd.read_csv('./data_raw/wine_rp.csv')
    wine_bc = pd.read_csv('./data_raw/wine_bc.csv')
    wine_bnd = pd.read_csv('./data_raw/wine_bnd.csv')
    wine_jr = pd.read_csv('./data_raw/wine_jr.csv')
    wine_vag = pd.read_csv('./data_raw/wine_vag.csv')

.. code:: ipython3

    frames =  [wine_rp, wine_bc, wine_bnd, wine_jr, wine_vag]

.. code:: ipython3

    # Concatenate the five wine_tables using pd.concat on the dataframes

.. code:: ipython3

    wines = pd.concat(frames)

.. code:: ipython3

    # Create a new 'index' column that is the result of 
    # contatenating the 'name' and the 'vintage' columns

.. code:: ipython3

    wines['index'] = wines[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)

.. code:: ipython3

    # Set the new index of the WINE table to 'index'

.. code:: ipython3

    wines.set_index('index',inplace=True)

.. code:: ipython3

    # Record the number of rows of the original wines

.. code:: ipython3

    size_raw = len(wines)

.. code:: ipython3

    # Remove duplicate rows

.. code:: ipython3

    wines_clean = wines.drop_duplicates()
    wines_clean




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>vintage</th>
          <th>avg_price</th>
          <th>producer</th>
          <th>region/appellation</th>
          <th>country</th>
          <th>blend</th>
          <th>pairing</th>
          <th>style</th>
          <th>alcohol</th>
        </tr>
        <tr>
          <th>index</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Chateau Mouton Rothschild, Pauillac, France1986</th>
          <td>Chateau Mouton Rothschild, Pauillac, France</td>
          <td>1986</td>
          <td>\n€923\n</td>
          <td>Chateau Mouton Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>Chateau d'Yquem, Sauternes, France2015</th>
          <td>Chateau d'Yquem, Sauternes, France</td>
          <td>2015</td>
          <td>\n€327\n</td>
          <td>Chateau d'Yquem</td>
          <td>Sauternes</td>
          <td>\nFrance\n</td>
          <td>Sauvignon Blanc - Semillon</td>
          <td>Blue Cheeses</td>
          <td>Dessert - Lush and Balanced</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Haut-Brion, Pessac-Leognan, France1945</th>
          <td>Chateau Haut-Brion, Pessac-Leognan, France</td>
          <td>1945</td>
          <td>\n€3,565\n</td>
          <td>Chateau Haut-Brion</td>
          <td>Pessac-Leognan</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 15%</td>
        </tr>
        <tr>
          <th>Chateau Haut-Brion, Pessac-Leognan, France1989</th>
          <td>Chateau Haut-Brion, Pessac-Leognan, France</td>
          <td>1989</td>
          <td>\n€2,187\n</td>
          <td>Chateau Haut-Brion</td>
          <td>Pessac-Leognan</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 15%</td>
        </tr>
        <tr>
          <th>Chateau Haut-Brion, Pessac-Leognan, France2005</th>
          <td>Chateau Haut-Brion, Pessac-Leognan, France</td>
          <td>2005</td>
          <td>\n€774\n</td>
          <td>Chateau Haut-Brion</td>
          <td>Pessac-Leognan</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 15%</td>
        </tr>
        <tr>
          <th>Chateau Haut-Brion, Pessac-Leognan, France2010</th>
          <td>Chateau Haut-Brion, Pessac-Leognan, France</td>
          <td>2010</td>
          <td>\n€909\n</td>
          <td>Chateau Haut-Brion</td>
          <td>Pessac-Leognan</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 15%</td>
        </tr>
        <tr>
          <th>Chateau Haut-Brion, Pessac-Leognan, France2015</th>
          <td>Chateau Haut-Brion, Pessac-Leognan, France</td>
          <td>2015</td>
          <td>\n€584\n</td>
          <td>Chateau Haut-Brion</td>
          <td>Pessac-Leognan</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 15%</td>
        </tr>
        <tr>
          <th>Chateau Latour, Pauillac, France1924</th>
          <td>Chateau Latour, Pauillac, France</td>
          <td>1924</td>
          <td>\n€2,004\n</td>
          <td>Chateau Latour</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Cabernet Sauvignon - Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Latour, Pauillac, France1928</th>
          <td>Chateau Latour, Pauillac, France</td>
          <td>1928</td>
          <td>\n€3,123\n</td>
          <td>Chateau Latour</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Cabernet Sauvignon - Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Latour, Pauillac, France1982</th>
          <td>Chateau Latour, Pauillac, France</td>
          <td>1982</td>
          <td>\n€1,992\n</td>
          <td>Chateau Latour</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Cabernet Sauvignon - Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Latour, Pauillac, France2003</th>
          <td>Chateau Latour, Pauillac, France</td>
          <td>2003</td>
          <td>\n€911\n</td>
          <td>Chateau Latour</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Cabernet Sauvignon - Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Margaux, Margaux, France1900</th>
          <td>Chateau Margaux, Margaux, France</td>
          <td>1900</td>
          <td>\n€14,834\n</td>
          <td>Chateau Margaux</td>
          <td>Margaux</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Margaux, Margaux, France1990</th>
          <td>Chateau Margaux, Margaux, France</td>
          <td>1990</td>
          <td>\n€1,204\n</td>
          <td>Chateau Margaux</td>
          <td>Margaux</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Margaux, Margaux, France1996</th>
          <td>Chateau Margaux, Margaux, France</td>
          <td>1996</td>
          <td>\n€804\n</td>
          <td>Chateau Margaux</td>
          <td>Margaux</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Margaux, Margaux, France2015</th>
          <td>Chateau Margaux, Margaux, France</td>
          <td>2015</td>
          <td>\n€1,401\n</td>
          <td>Chateau Margaux</td>
          <td>Margaux</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Petrus, Pomerol, France1921</th>
          <td>Petrus, Pomerol, France</td>
          <td>1921</td>
          <td>\n€27,198\n</td>
          <td>Petrus</td>
          <td>Pomerol</td>
          <td>\nFrance\n</td>
          <td>Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>13 - 15%</td>
        </tr>
        <tr>
          <th>Petrus, Pomerol, France1989</th>
          <td>Petrus, Pomerol, France</td>
          <td>1989</td>
          <td>\n€4,007\n</td>
          <td>Petrus</td>
          <td>Pomerol</td>
          <td>\nFrance\n</td>
          <td>Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>13 - 15%</td>
        </tr>
        <tr>
          <th>Petrus, Pomerol, France1990</th>
          <td>Petrus, Pomerol, France</td>
          <td>1990</td>
          <td>\n€4,148\n</td>
          <td>Petrus</td>
          <td>Pomerol</td>
          <td>\nFrance\n</td>
          <td>Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>13 - 15%</td>
        </tr>
        <tr>
          <th>Petrus, Pomerol, France2015</th>
          <td>Petrus, Pomerol, France</td>
          <td>2015</td>
          <td>\n€3,705\n</td>
          <td>Petrus</td>
          <td>Pomerol</td>
          <td>\nFrance\n</td>
          <td>Merlot</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>13 - 15%</td>
        </tr>
        <tr>
          <th>Tenuta San Guido Sassicaia Bolgheri, Tuscany, Italy1985</th>
          <td>Tenuta San Guido Sassicaia Bolgheri, Tuscany, ...</td>
          <td>1985</td>
          <td>\n€2,129\n</td>
          <td>Tenuta San Guido - Sassicaia</td>
          <td>Bolgheri</td>
          <td>\nItaly\n</td>
          <td>Cabernet Franc - Cabernet Sauvignon</td>
          <td>Beef and Venison</td>
          <td>Red - Bold and Structured</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Lafite Rothschild, Pauillac, France1870</th>
          <td>Chateau Lafite Rothschild, Pauillac, France</td>
          <td>1870</td>
          <td>\n€8,848\n</td>
          <td>Chateau Lafite Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>Chateau Lafite Rothschild, Pauillac, France1953</th>
          <td>Chateau Lafite Rothschild, Pauillac, France</td>
          <td>1953</td>
          <td>\n€1,486\n</td>
          <td>Chateau Lafite Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>Chateau Lafite Rothschild, Pauillac, France2003</th>
          <td>Chateau Lafite Rothschild, Pauillac, France</td>
          <td>2003</td>
          <td>\n€1,090\n</td>
          <td>Chateau Lafite Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>Chateau Mouton Rothschild, Pauillac, France1945</th>
          <td>Chateau Mouton Rothschild, Pauillac, France</td>
          <td>1945</td>
          <td>\n€14,102\n</td>
          <td>Chateau Mouton Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>Chateau Mouton Rothschild, Pauillac, France1959</th>
          <td>Chateau Mouton Rothschild, Pauillac, France</td>
          <td>1959</td>
          <td>\n€2,892\n</td>
          <td>Chateau Mouton Rothschild</td>
          <td>Pauillac</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 13%</td>
        </tr>
        <tr>
          <th>namevintage</th>
          <td>name</td>
          <td>vintage</td>
          <td>avg_price</td>
          <td>producer</td>
          <td>region/appellation</td>
          <td>country</td>
          <td>blend</td>
          <td>pairing</td>
          <td>style</td>
          <td>alcohol</td>
        </tr>
        <tr>
          <th>Chateau Leoville Poyferre, Saint-Julien, France2009</th>
          <td>Chateau Leoville Poyferre, Saint-Julien, France</td>
          <td>2009</td>
          <td>\n€230\n</td>
          <td>Chateau Leoville Poyferre</td>
          <td>Saint-Julien</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 47%</td>
        </tr>
        <tr>
          <th>Domaine Jean-Louis Chave Hermitage, Rhone, France2010</th>
          <td>Domaine Jean-Louis Chave Hermitage, Rhone, France</td>
          <td>2010</td>
          <td>\n$460\n</td>
          <td>Domaine Jean-Louis Chave</td>
          <td>Hermitage</td>
          <td>\nFrance\n</td>
          <td>Syrah</td>
          <td>Lamb</td>
          <td>Red - Bold and Structured</td>
          <td>13 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Ausone, Saint-Emilion Grand Cru, France2003</th>
          <td>Chateau Ausone, Saint-Emilion Grand Cru, France</td>
          <td>2003</td>
          <td>\n€1,001\n</td>
          <td>Chateau Ausone</td>
          <td>Saint-Emilion Grand Cru</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Chateau Ausone, Saint-Emilion Grand Cru, France2005</th>
          <td>Chateau Ausone, Saint-Emilion Grand Cru, France</td>
          <td>2005</td>
          <td>\n€1,453\n</td>
          <td>Chateau Ausone</td>
          <td>Saint-Emilion Grand Cru</td>
          <td>\nFrance\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Savory and Classic</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>Bodegas Cepa 21 Hito Rosado, Ribera del Duero, Spain2015</th>
          <td>Bodegas Cepa 21 Hito Rosado, Ribera del Duero,...</td>
          <td>2015</td>
          <td>\n$9\n</td>
          <td>Ribera del Duero,\nCastilla y Leon, ,\nSpain\n</td>
          <td>Tempranillo</td>
          <td>Tempranillo</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Domaine Servin Cuvee Massale Chablis Vieilles Vignes, Burgundy, France2008</th>
          <td>Domaine Servin Cuvee Massale Chablis Vieilles ...</td>
          <td>2008</td>
          <td>\n$26\n</td>
          <td>Domaine Servin</td>
          <td>Chablis</td>
          <td>\nFrance\n</td>
          <td>Chardonnay</td>
          <td>Shellfish, Crab and Lobster</td>
          <td>White - Green and Flinty</td>
          <td>12%</td>
        </tr>
        <tr>
          <th>Novelty Hill Royal Slope Red, Columbia Valley, USA2009</th>
          <td>Novelty Hill Royal Slope Red, Columbia Valley,...</td>
          <td>2009</td>
          <td>\n$20\n</td>
          <td>Novelty Hill Januik Winery</td>
          <td>Columbia Valley</td>
          <td>\nUSA\n</td>
          <td>Cabernet - Mourvedre - Syrah</td>
          <td>Beef and Venison</td>
          <td>Red - Bold and Structured</td>
          <td>14%</td>
        </tr>
        <tr>
          <th>Wallis Family Estate Little Sister Proprietary Red Blend, Diamond Mountain District, USA2010</th>
          <td>Wallis Family Estate Little Sister Proprietary...</td>
          <td>2010</td>
          <td>\n$50\n</td>
          <td>Wallis Family Estate</td>
          <td>Diamond Mountain District</td>
          <td>\nUSA\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Bold and Structured</td>
          <td>13 - 15%</td>
        </tr>
        <tr>
          <th>Herman Story Tomboy, Santa Barbara County, USA2010</th>
          <td>Herman Story Tomboy, Santa Barbara County, USA</td>
          <td>2010</td>
          <td>\n$48\n</td>
          <td>Herman Story Wines</td>
          <td>Santa Barbara County</td>
          <td>\nUSA\n</td>
          <td>Southern Rhone White Blend</td>
          <td>Root Vegetables and Squashes</td>
          <td>White - Tropical and Balanced</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Famille Brechet Lirac Moulin des Chenes, Rhone, France2010</th>
          <td>Famille Brechet Lirac Moulin des Chenes, Rhone...</td>
          <td>2010</td>
          <td>\n$10\n</td>
          <td>Famille Brechet</td>
          <td>Lirac</td>
          <td>\nFrance\n</td>
          <td>Southern Rhone Red Blend</td>
          <td>Lamb</td>
          <td>Red - Rich and Intense</td>
          <td>14%</td>
        </tr>
        <tr>
          <th>Domaine Hubert Lignier Saint-Romain Sous Le Chateau, Cote de Beaune, Burgundy2010</th>
          <td>Domaine Hubert Lignier Saint-Romain Sous Le Ch...</td>
          <td>2010</td>
          <td>\n$40\n</td>
          <td>Hubert Lignier</td>
          <td>Saint-Romain</td>
          <td>\nFrance\n</td>
          <td>Chardonnay</td>
          <td>Chicken and Turkey</td>
          <td>White - Buttery and Complex</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Marques de Caceres Excellens Rose, Rioja DOCa, Spain2014</th>
          <td>Marques de Caceres Excellens Rose, Rioja DOCa,...</td>
          <td>2014</td>
          <td>\n$6\n</td>
          <td>Marques de Caceres</td>
          <td>Rioja</td>
          <td>\nSpain\n</td>
          <td>Rare Rose Blend</td>
          <td>Tomato-based Dishes</td>
          <td>Rose - Rich and Fruity</td>
          <td>13%</td>
        </tr>
        <tr>
          <th>d'Arenberg The Stump Jump Riesling, McLaren Vale, Australia2015</th>
          <td>d'Arenberg The Stump Jump Riesling, McLaren Va...</td>
          <td>2015</td>
          <td>\n$10\n</td>
          <td>McLaren Vale,\nSouth Australia, ,\nAustralia\n</td>
          <td>Riesling</td>
          <td>Riesling</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Les Cretes Valle d'Aosta Torrette, Aosta Valley, Italy2007</th>
          <td>Les Cretes Valle d'Aosta Torrette, Aosta Valle...</td>
          <td>2007</td>
          <td>\n$14\n</td>
          <td>Les Cretes</td>
          <td>Torrette</td>
          <td>\nItaly\n</td>
          <td>Petit Rouge</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Frederic Magnien Chambolle-Musigny Premier Cru Coeur de Pierres, Cote de Nuits, France2007</th>
          <td>Frederic Magnien Chambolle-Musigny Premier Cru...</td>
          <td>2007</td>
          <td>\n$56\n</td>
          <td>Domaine Michel Magnien - Frederic Magnien</td>
          <td>Chambolle-Musigny Premier Cru</td>
          <td>\nFrance\n</td>
          <td>Pinot Noir</td>
          <td>Duck, Goose and Game Birds</td>
          <td>Red - Savory and Classic</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Au Bon Climat Sanford &amp; Benedict Vineyard Pinot Noir, Santa Ynez Valley, USA2009</th>
          <td>Au Bon Climat Sanford &amp; Benedict Vineyard Pino...</td>
          <td>2009</td>
          <td>91</td>
          <td>Santa Ynez Valley,\nSanta Barbara County, ,\nC...</td>
          <td>Pinot Noir</td>
          <td>Pinot Noir</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Wrath Wines Ex Anima Pinot Noir, Monterey, USA2011</th>
          <td>Wrath Wines Ex Anima Pinot Noir, Monterey, USA</td>
          <td>2011</td>
          <td>\n$19\n</td>
          <td>Wrath Wines</td>
          <td>Monterey</td>
          <td>\nUSA\n</td>
          <td>Pinot Noir</td>
          <td>Chicken and Turkey</td>
          <td>Red - Light and Perfumed</td>
          <td>12 - 14%</td>
        </tr>
        <tr>
          <th>Siduri Rosellas Vineyard Pinot Noir, Santa Lucia Highlands, USA2013</th>
          <td>Siduri Rosellas Vineyard Pinot Noir, Santa Luc...</td>
          <td>2013</td>
          <td>\n$48\n</td>
          <td>Siduri Winery</td>
          <td>Santa Lucia Highlands</td>
          <td>\nUSA\n</td>
          <td>Pinot Noir</td>
          <td>Chicken and Turkey</td>
          <td>Red - Light and Perfumed</td>
          <td>14%</td>
        </tr>
        <tr>
          <th>Silver Heights Family Reserve, Ningxia, China2013</th>
          <td>Silver Heights Family Reserve, Ningxia, China</td>
          <td>2013</td>
          <td>\n$51\n</td>
          <td>Silver Heights</td>
          <td>Ningxia</td>
          <td>\nChina\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Bold and Structured</td>
          <td>13%</td>
        </tr>
        <tr>
          <th>Dominio del Plata BenMarco Cabernet Sauvignon, Mendoza, Argentina2014</th>
          <td>Dominio del Plata BenMarco Cabernet Sauvignon,...</td>
          <td>2014</td>
          <td>\n$26\n</td>
          <td>Mendoza,\nArgentina\n</td>
          <td>Cabernet Sauvignon</td>
          <td>Cabernet Sauvignon</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Domaine Michelot Meursault Les Grands Charrons, Cote de Beaune, France2014</th>
          <td>Domaine Michelot Meursault Les Grands Charrons...</td>
          <td>2014</td>
          <td>\n$39\n</td>
          <td>Meursault,\nCote de Beaune, ,\nBurgundy, ,\nFr...</td>
          <td>Chardonnay</td>
          <td>Chardonnay</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Weingut Josef Ehmoser Von den Terrassen Gruner Veltliner, Wagram, Austria2014</th>
          <td>Weingut Josef Ehmoser Von den Terrassen Gruner...</td>
          <td>2014</td>
          <td>89</td>
          <td>Wagram,\nAustria\n</td>
          <td>Gruner Veltliner</td>
          <td>Gruner Veltliner</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Mission Estate Winery Jewelstone Syrah, Gimblett Gravels, New Zealand2014</th>
          <td>Mission Estate Winery Jewelstone Syrah, Gimble...</td>
          <td>2014</td>
          <td>\n$24\n</td>
          <td>Gimblett Gravels,\nHawkes Bay, ,\nNew Zealand\n</td>
          <td>Syrah</td>
          <td>Syrah</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Bodegas Obalo Joven, Rioja DOCa, Spain2014</th>
          <td>Bodegas Obalo Joven, Rioja DOCa, Spain</td>
          <td>2014</td>
          <td>\n$6\n</td>
          <td>Rioja,\nSpain\n</td>
          <td>Tempranillo</td>
          <td>Tempranillo</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Les Vins de Vienne Viognier, Rhone, Vin de France2014</th>
          <td>Les Vins de Vienne Viognier, Rhone, Vin de France</td>
          <td>2014</td>
          <td>\n$14\n</td>
          <td>Vin de Table - Vin de France,\nFrance\n</td>
          <td>Viognier</td>
          <td>Viognier</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Vins Breban Cotes de Provence Domaine de Paris Rose, France2015</th>
          <td>Vins Breban Cotes de Provence Domaine de Paris...</td>
          <td>2015</td>
          <td>\n$11\n</td>
          <td>Cotes de Provence,\nProvence, ,\nFrance\n</td>
          <td>Southern Rhone Red Blend</td>
          <td>Southern Rhone Red Blend</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Torre dei Beati 'Rosa-ae' Cerasuolo d'Abruzzo, Italy2015</th>
          <td>Torre dei Beati 'Rosa-ae' Cerasuolo d'Abruzzo,...</td>
          <td>2015</td>
          <td>\n$9\n</td>
          <td>Cerasuolo d'Abruzzo,\nAbruzzo, ,\nItaly\n</td>
          <td>Montepulciano</td>
          <td>Montepulciano</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Patrick Javillier Savigny-les-Beaune Les Montchenevoy Blanc, Cote de Beaune, France2008</th>
          <td>Patrick Javillier Savigny-les-Beaune Les Montc...</td>
          <td>2008</td>
          <td>89</td>
          <td>Savigny-les-Beaune,\nCote de Beaune, ,\nBurgun...</td>
          <td>Chardonnay</td>
          <td>Chardonnay</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>De Trafford Merlot, Stellenbosch, South Africa2008</th>
          <td>De Trafford Merlot, Stellenbosch, South Africa</td>
          <td>2008</td>
          <td>\n$28\n</td>
          <td>De Trafford</td>
          <td>Stellenbosch</td>
          <td>\nSouth Africa\n</td>
          <td>Merlot</td>
          <td>Lamb</td>
          <td>Red - Bold and Structured</td>
          <td>15%</td>
        </tr>
        <tr>
          <th>Qupe Bien Nacido Vineyard Syrah, Santa Maria Valley, USA2008</th>
          <td>Qupe Bien Nacido Vineyard Syrah, Santa Maria V...</td>
          <td>2008</td>
          <td>\n$24\n</td>
          <td>Qupe Wine Cellars</td>
          <td>Santa Maria Valley</td>
          <td>\nUSA\n</td>
          <td>Syrah</td>
          <td>Lamb</td>
          <td>Red - Rich and Intense</td>
          <td>13 - 14%</td>
        </tr>
        <tr>
          <th>Les Vins de Vienne Chateauneuf-du-Pape Les Oteliees, Rhone, France2009</th>
          <td>Les Vins de Vienne Chateauneuf-du-Pape Les Ote...</td>
          <td>2009</td>
          <td>\n$59\n</td>
          <td>Sarl Les Vins de Vienne</td>
          <td>Chateauneuf-du-Pape</td>
          <td>\nFrance\n</td>
          <td>Grenache - Mourvedre - Syrah</td>
          <td>Lamb</td>
          <td>Red - Rich and Intense</td>
          <td>14%</td>
        </tr>
        <tr>
          <th>Jean-Luc &amp; Eric Burguet Bourgogne Les Pince Vin, Burgundy, France2009</th>
          <td>Jean-Luc &amp; Eric Burguet Bourgogne Les Pince Vi...</td>
          <td>2009</td>
          <td>\n$43\n</td>
          <td>Jean-Luc &amp; Eric Burguet</td>
          <td>Bourgogne Rouge</td>
          <td>\nFrance\n</td>
          <td>Pinot Noir</td>
          <td>Chicken and Turkey</td>
          <td>Red - Light and Perfumed</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Angelo Innocenti Unisono, La Consulta, Argentina2011</th>
          <td>Angelo Innocenti Unisono, La Consulta, Argentina</td>
          <td>2011</td>
          <td>\n$43\n</td>
          <td>Angulo Innocenti</td>
          <td>La Consulta</td>
          <td>\nArgentina\n</td>
          <td>Bordeaux Blend Red</td>
          <td>Beef and Venison</td>
          <td>Red - Bold and Structured</td>
          <td>15%</td>
        </tr>
        <tr>
          <th>Quivira Vineyards Fig Tree Vineyard Sauvignon Blanc, Dry Creek Valley, USA2012</th>
          <td>Quivira Vineyards Fig Tree Vineyard Sauvignon ...</td>
          <td>2012</td>
          <td>\n$18\n</td>
          <td>Quivira Vineyards</td>
          <td>Dry Creek Valley</td>
          <td>\nUSA\n</td>
          <td>Sauvignon Blanc</td>
          <td>Salads and Green Vegetables</td>
          <td>White - Green and Flinty</td>
          <td>13 - 14%</td>
        </tr>
      </tbody>
    </table>
    <p>64026 rows × 10 columns</p>
    </div>



.. code:: ipython3

    # Record the new number of rows

.. code:: ipython3

    size_clean = len(wines_clean)
    size_clean




.. parsed-literal::

    64026



.. code:: ipython3

    # Compute the number of duplicates

.. code:: ipython3

    duplicates=size_raw - size_clean
    duplicates




.. parsed-literal::

    3398



.. code:: ipython3

    """Duplicates = 3398 as of data from 28.02.2019"""

.. code:: ipython3

    # Export to csv

.. code:: ipython3

    wines_clean.to_csv(r'./wines_clean.csv')
