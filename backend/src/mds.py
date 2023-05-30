import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.manifold import MDS


# https://www.statology.org/multidimensional-scaling-in-python/

def mds_analysis(file, dataset):
    dataFrame = pd.read_csv(file, sep='\t')

    # Perform multi-dimensional scaling.
    # 2 dimensions and random start.
    mds_object = MDS(n_components=2, random_state=0, normalized_stress='auto')
    scaled_df = mds_object.fit_transform(dataFrame)

    # View results of multidimensional scaling.
    # print(scaled_df)

    # Create scatterplot.
    plt.scatter(scaled_df[:, 0], scaled_df[:, 1])

    # Add axis labels.
    plt.xlabel('Coordinate 1')
    plt.ylabel('Coordinate 2')
    plt.title(dataset)

    # scaled_df[:, 0] = the first point of the scaled dataframe.
    # scaled_df[:, 1] = the second point of the scaled dataframe.
    # scaled_df[:, 0][0] = the first coordinate of the first point of the scaled dataframe.
    # scaled_df[:, 0][1] = the second coordinate of the first point of the scaled dataframe.
    # print(math.dist(scaled_df[0], scaled_df[1]))
    # print(math.dist(scaled_df[1], scaled_df[2]))

    # Normalize scaled_df.
    scaled_df_normalized = (scaled_df - scaled_df.min()) / (scaled_df.max() - scaled_df.min())

    heatmap_matrix = []

    # Header
    print('\t', end='')
    for row_label in dataFrame.index:
        print(row_label, end='\t')

    print()
    for row_label in dataFrame.index:
        heatmap_row = []
        print(row_label, end='\t')
        for column_label in dataFrame.index:
            print(round(math.dist(scaled_df_normalized[row_label], scaled_df_normalized[column_label]), 4), end='\t')
            heatmap_row.append(round(math.dist(scaled_df_normalized[row_label], scaled_df_normalized[column_label]), 4))
        print()
        heatmap_matrix.append(heatmap_row)

    # Add labels to each point.
    for i, txt in enumerate(dataFrame.index):
        plt.annotate(txt, (scaled_df[:, 0][i] + .3, scaled_df[:, 1][i]))

    # Save the scatterplot.
    plt.savefig('C:/temp/DigiHub 1.0/frontend/electron-app/src/renderer/src/charts/mds.png')

    # Save the heatmap of distances between points.
    sns.heatmap(heatmap_matrix, cbar=0, linewidths=2, vmax=1, vmin=0, square=True, cmap='Blues')
    plt.savefig('C:/temp/DigiHub 1.0/frontend/electron-app/src/renderer/src/charts/mds heatmap.png')

    # Display the scatterplot.
    # plt.show()

if __name__ == '__main__':
    # mds('./data/flavor scores TheGinIsIn.csv', 'The Gin Is In')
    # mds('./data/38 gins 59 features.csv', '38 gins 59 features')
    # mds('./data/flavor scores Bert 29 gins.csv', 'flavor scores Bert 29 gins')
    # mds('./data/quantities 29 gins.csv', 'quantities 29 gins')

    # mds_analysis('./data/Golden Standard Digihub.csv', 'Golden Standard Digihub')
    pass

'''

    MDS can find projections that are different from those produced by linear techniques, such as principal component 
    analysis (PCA).
    
'''
