
rating_data_cleaning
====================

# {
  "celltoolbar": "Raw Cell Format",
  "kernelspec": {
    "name": "python3",
    "display_name": "Python 3",
    "language": "python"
  },
  "language_info": {
    "name": "python",
    "version": "3.6.8",
    "mimetype": "text/x-python",
    "codemirror_mode": {
      "name": "ipython",
      "version": 3
    },
    "pygments_lexer": "ipython3",
    "nbconvert_exporter": "python",
    "file_extension": ".py"
  }
}

.. code:: ipython3

    import numpy as np
    import pandas as pd
    import pyreadr as pr

.. code:: ipython3

    # Import RATINGS data from .rds files
    # Create index as name + vintage
    # as has been done in the WINE table
    # so that we will have a common index as key
    # This is to be done using set_index() function

.. code:: ipython3

    # Load the .rds file
    # Data from https://arc-git.mpib-berlin.mpg.de/taste/wine/wine-searcher/tree/master/output

.. code:: ipython3

    ratings = pr.read_r('./data_raw/critics_ratings.rds')

.. code:: ipython3

    # Load the .csv file for critics

.. code:: ipython3

    critics = pd.read_csv('./data_raw/critic_id.csv')

.. code:: ipython3

    # Extract the pandas dataframe

.. code:: ipython3

    ratings = ratings[None]

.. code:: ipython3

    # Rename the columns

.. code:: ipython3

    ratings.columns = ['name', 'vintage','popularity','score','avg_price','critic']

.. code:: ipython3

    # Convert types to strings to prepare for concatenation

.. code:: ipython3

    ratings['vintage'] = ratings['vintage'].astype(str)
    ratings['name'] = ratings['name'].astype(str)

.. code:: ipython3

    # Create a new 'wine_id' column that is the result of 
    # contatenating the 'name' and the 'vintage' columns

.. code:: ipython3

    ratings['wine_id'] = ratings[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)

.. code:: ipython3

    # Drop redundant columns

.. code:: ipython3

    ratings = ratings.drop(columns=['name', 'vintage','avg_price'])

.. code:: ipython3

    # Set the index of the new RATINGS table to 'critic'

.. code:: ipython3

    ratings.set_index('critic',inplace=True)

.. code:: ipython3

    # Set the index of the CRITICS table to 'critic_name'

.. code:: ipython3

    critics.set_index('critic_name',inplace=True)

.. code:: ipython3

    # Merge the tables upon index

.. code:: ipython3

    ratings = ratings.merge(critics, left_index=True, right_index=True)

.. code:: ipython3

    # Set the index of RATINGS to 'wine_id'

.. code:: ipython3

    ratings.set_index('wine_id',inplace=True)

.. code:: ipython3

    # Sort the order of the columns

.. code:: ipython3

    ratings = ratings[['critic_id','score','popularity']]

.. code:: ipython3

    ratings




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
          <th>critic_id</th>
          <th>score</th>
          <th>popularity</th>
        </tr>
        <tr>
          <th>wine_id</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>nannan</th>
          <td>5_star_wines</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>Neudorf Moutere Chardonnay, Nelson, New Zealand2014</th>
          <td>campbell_bob</td>
          <td>100</td>
          <td>8563</td>
        </tr>
        <tr>
          <th>Ata Rangi Pinot Noir, Martinborough, New Zealand2014</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>792</td>
        </tr>
        <tr>
          <th>Penfolds Bin 60A Coonawarra Cabernet Sauvignon - Barossa Shiraz, South Australia1962</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>2759</td>
        </tr>
        <tr>
          <th>Dry River Pinot Noir, Martinborough, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>4089</td>
        </tr>
        <tr>
          <th>Trinity Hill Homage Syrah, Gimblett Gravels, New Zealand2014</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>5198</td>
        </tr>
        <tr>
          <th>Church Road Tom Merlot - Cabernet Sauvignon, Hawke's Bay, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>7476</td>
        </tr>
        <tr>
          <th>Bell Hill Chardonnay, Canterbury, New Zealand2012</th>
          <td>campbell_bob</td>
          <td>99</td>
          <td>11123</td>
        </tr>
        <tr>
          <th>Penfolds Grange Bin 95, Australia2006</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>21</td>
        </tr>
        <tr>
          <th>Penfolds Grange Bin 95, Australia1987</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>21</td>
        </tr>
        <tr>
          <th>Penfolds Grange Bin 95, Australia1986</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>21</td>
        </tr>
        <tr>
          <th>Penfolds Bin 707 Cabernet Sauvignon, South Australia2008</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>171</td>
        </tr>
        <tr>
          <th>Penfolds St. Henri Shiraz, South Australia2012</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>227</td>
        </tr>
        <tr>
          <th>Moss Wood Cabernet Sauvignon, Margaret River, Australia2010</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>871</td>
        </tr>
        <tr>
          <th>Te Mata Estate Coleraine, Hawke's Bay, New Zealand2014</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>1364</td>
        </tr>
        <tr>
          <th>Te Mata Estate Coleraine, Hawke's Bay, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>1364</td>
        </tr>
        <tr>
          <th>Bodegas Toro Albala Don PX Convento Seleccion, Montilla-Moriles, Spain1931</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>1915</td>
        </tr>
        <tr>
          <th>Penfolds Yattarna 'Bin 144' Chardonnay, South Australia2010</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2066</td>
        </tr>
        <tr>
          <th>Craggy Range Sophia Merlot, Gimblett Gravels, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2737</td>
        </tr>
        <tr>
          <th>Craggy Range Le Sol Syrah, Gimblett Gravels, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2755</td>
        </tr>
        <tr>
          <th>Craggy Range Le Sol Syrah, Gimblett Gravels, New Zealand2010</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2755</td>
        </tr>
        <tr>
          <th>Craggy Range Le Sol Syrah, Gimblett Gravels, New Zealand2009</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2755</td>
        </tr>
        <tr>
          <th>Dog Point Pinot Noir, Marlborough, New Zealand2012</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>2829</td>
        </tr>
        <tr>
          <th>Penfolds Bin 169 Cabernet Sauvignon, Coonawarra, Australia2010</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3070</td>
        </tr>
        <tr>
          <th>Bell Hill Pinot Noir, Canterbury, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3371</td>
        </tr>
        <tr>
          <th>Bell Hill Pinot Noir, Canterbury, New Zealand2012</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3371</td>
        </tr>
        <tr>
          <th>Bell Hill Pinot Noir, Canterbury, New Zealand2011</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3371</td>
        </tr>
        <tr>
          <th>Felton Road Block 5 Pinot Noir, Bannockburn, New Zealand2013</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3750</td>
        </tr>
        <tr>
          <th>Felton Road Block 5 Pinot Noir, Bannockburn, New Zealand2007</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>3750</td>
        </tr>
        <tr>
          <th>Dry River Pinot Noir, Martinborough, New Zealand2014</th>
          <td>campbell_bob</td>
          <td>98</td>
          <td>4089</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>Stones No 1, Napa Valley, USA2013</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>7340</td>
        </tr>
        <tr>
          <th>Sine Qua Non Stockholm Syndrome Eleven Confession Vineyard Grenache, Central Coast, USA2010</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>8006</td>
        </tr>
        <tr>
          <th>Sine Qua Non 'The Inaugural' Eleven Confessions Vineyard Syrah, Sta Rita Hills, USA2003</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>8741</td>
        </tr>
        <tr>
          <th>Sine Qua Non The 17th Nail in My Cranium, Sta Rita Hills, USA2005</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>8956</td>
        </tr>
        <tr>
          <th>Alban Vineyards Pandora Red, Edna Valley, USA2012</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>9292</td>
        </tr>
        <tr>
          <th>Greenock Creek Vineyards &amp; Cellars Creek Block Shiraz, Barossa Valley, Australia2003</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>9390</td>
        </tr>
        <tr>
          <th>Sine Qua Non Atlantis Fe203 Syrah 1a, 1b &amp; 1c, Central Coast, USA2005</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>9668</td>
        </tr>
        <tr>
          <th>Bevan Cellars Tin Box Vineyard Red, Oakville, USA2011</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10061</td>
        </tr>
        <tr>
          <th>Greenock Creek Vineyards &amp; Cellars Roennfeldt Road Cabernet Sauvignon, Barossa Valley, Australia2002</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10235</td>
        </tr>
        <tr>
          <th>Greenock Creek Vineyards &amp; Cellars Roennfeldt Road Cabernet Sauvignon, Barossa Valley, Australia1998</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10235</td>
        </tr>
        <tr>
          <th>Macauley Vineyard Beckstoffer To Kalon Vineyard Cabernet Sauvignon, Oakville, USA2014</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10296</td>
        </tr>
        <tr>
          <th>Morlet Family Vineyards Coup de Coeur Chardonnay, Sonoma County, USA2009</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10296</td>
        </tr>
        <tr>
          <th>Myriad Cellars Beckstoffer Dr. Crane Vineyard 'Elysian' Reserve Cabernet Sauvignon, Napa Valley, USA2013</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10409</td>
        </tr>
        <tr>
          <th>Larkmead Vineyards The Lark, Napa Valley, USA2013</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10599</td>
        </tr>
        <tr>
          <th>Carter Cellars Beckstoffer To Kalon Vineyard The G.T.O Cabernet Sauvignon, Napa Valley, USA2012</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10662</td>
        </tr>
        <tr>
          <th>Sine Qua Non A Shot in the Dark Syrah, California, USA2006</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>10927</td>
        </tr>
        <tr>
          <th>Alban Vineyards Seymour's Vineyard Syrah, Edna Valley, USA2007</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>11263</td>
        </tr>
        <tr>
          <th>Alban Vineyards Seymour's Vineyard Syrah, Edna Valley, USA2004</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>11263</td>
        </tr>
        <tr>
          <th>Hundred Acre 'Fortification' Port, Napa Valley, USA2008</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>11619</td>
        </tr>
        <tr>
          <th>Hundred Acre 'Fortification' Port, Napa Valley, USA2007</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>11619</td>
        </tr>
        <tr>
          <th>Hundred Acre 'Fortification' Port, Napa Valley, USA2005</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>11619</td>
        </tr>
        <tr>
          <th>Donelan Richards Family Vineyard Syrah, Sonoma Valley, USA2009</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>12910</td>
        </tr>
        <tr>
          <th>Donelan Richards Family Vineyard Syrah, Sonoma Valley, USA2007</th>
          <td>the_wine_advocate</td>
          <td>100</td>
          <td>12910</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>the_wine_front</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>atkin_tim</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>vinous</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>vinum</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>wine_enthusiast</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>wine_spectator</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>nannan</th>
          <td>wine_and_spirits</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    <p>1528 rows × 3 columns</p>
    </div>



.. code:: ipython3

    # Export to .csv

.. code:: ipython3

    ratings.to_csv(r'./ratings_clean.csv')
