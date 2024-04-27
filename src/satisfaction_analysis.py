import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

def compute_engagement_score(data, engagement_clusters):
    """
    Compute the engagement score for each user.

    Args:
        data (pd.DataFrame): The input data.
        engagement_clusters (pd.DataFrame): The engagement clusters.

    Returns:
        pd.Series: The engagement scores.
    """
    # Compute the Euclidean distance between each user and the least engaged cluster
    least_engaged_cluster = engagement_clusters[engagement_clusters['cluster'] == min(engagement_clusters['cluster'])]
    engagement_scores = pairwise_distances(data, least_engaged_cluster.drop('cluster', axis=1), metric='euclidean').ravel()
    
    return engagement_scores

def compute_experience_score(data, experience_clusters):
    """
    Compute the experience score for each user.

    Args:
        data (pd.DataFrame): The input data.
        experience_clusters (pd.DataFrame): The experience clusters.

    Returns:
        pd.Series: The experience scores.
    """
    # Compute the Euclidean distance between each user and the worst experience cluster
    worst_experience_cluster = experience_clusters[experience_clusters['cluster'] == max(experience_clusters['cluster'])]
    experience_scores = pairwise_distances(data, worst_experience_cluster.drop('cluster', axis=1), metric='euclidean').ravel()
    
    return experience_scores

def compute_satisfaction_score(engagement_scores, experience_scores):
    """
    Compute the satisfaction score for each user.

    Args:
        engagement_scores (pd.Series): The engagement scores.
        experience_scores (pd.Series): The experience scores.

    Returns:
        pd.Series: The satisfaction scores.
    """
    satisfaction_scores = (engagement_scores + experience_scores) / 2
    return satisfaction_scores

def build_regression_model(data):
    """
    Build a linear regression model to predict the satisfaction score.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        sklearn.linear_model.LinearRegression: The trained linear regression model.
    """
    # Preprocess the data and select relevant features
    X = data[['feature1', 'feature2', ...]]
    y = data['satisfaction_score']

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model