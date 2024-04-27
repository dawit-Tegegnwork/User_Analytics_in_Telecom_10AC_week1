import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def aggregate_experience_metrics(data):
    """
    Aggregate the experience metrics per customer.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: The aggregated experience metrics.
    """
    experience_metrics = data.groupby('msisdn')[['tcp_retransmission', 'rtt', 'throughput', 'handset_type']].agg({
        'tcp_retransmission': 'mean',
        'rtt': 'mean',
        'throughput': 'mean',
        'handset_type': 'last'
    }).reset_index()
    experience_metrics = experience_metrics.rename(columns={
        'tcp_retransmission': 'avg_tcp_retransmission',
        'rtt': 'avg_rtt',
        'throughput': 'avg_throughput'
    })
    return experience_metrics

def compute_top_values(data):
    """
    Compute the top, bottom, and most frequent values for TCP, RTT, and throughput.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        dict: A dictionary containing the top, bottom, and most frequent values.
    """
    top_values = {
        'top_tcp': data['tcp_retransmission'].nlargest(10).tolist(),
        'bottom_tcp': data['tcp_retransmission'].nsmallest(10).tolist(),
        'most_frequent_tcp': data['tcp_retransmission'].mode().tolist(),
        'top_rtt': data['rtt'].nlargest(10).tolist(),
        'bottom_rtt': data['rtt'].nsmallest(10).tolist(),
        'most_frequent_rtt': data['rtt'].mode().tolist(),
        'top_throughput': data['throughput'].nlargest(10).tolist(),
        'bottom_throughput': data['throughput'].nsmallest(10).tolist(),
        'most_frequent_throughput': data['throughput'].mode().tolist()
    }
    return top_values

def analyze_experience_metrics(data):
    """
    Analyze the experience metrics based on handset type.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        None
    """
    # Analyze the throughput distribution per handset type
    throughput_by_handset = data.groupby('handset_type')['avg_throughput'].describe()
    print("Throughput Distribution by Handset Type:")
    print(throughput_by_handset)

    # Analyze the TCP retransmission per handset type
    tcp_by_handset = data.groupby('handset_type')['avg_tcp_retransmission'].describe()
    print("\nTCP Retransmission by Handset Type:")
    print(tcp_by_handset)

def cluster_users_by_experience(data, n_clusters=3):
    """
    Cluster users based on experience metrics using k-means clustering.

    Args:
        data (pd.DataFrame): The input data.
        n_clusters (int): The number of clusters.

    Returns:
        pd.DataFrame: The input data with cluster labels.
    """
    # Preprocess the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['avg_tcp_retransmission', 'avg_rtt', 'avg_throughput']])

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(scaled_data)

    # Add cluster labels to the data
    data['experience_cluster'] = clusters

    return data