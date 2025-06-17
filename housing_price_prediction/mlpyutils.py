def plot_scatter(plot_title, actual_values, predicted_values):
    """
    Generates and displays a scatter plot comparing actual vs. predicted values.

    Args:
        plot_title (str): The title for the scatter plot.
        actual_values (pd.Series or np.ndarray): The actual values.
        predicted_values (pd.Series or np.ndarray): The predicted values.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(actual_values, predicted_values, alpha=0.5)
    # Add a line representing perfect prediction
    plt.plot([actual_values.min(), actual_values.max()],
             [actual_values.min(), actual_values.max()], 'k--', lw=2)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(plot_title)
    plt.grid(True)
    plt.show()


def print_data(predicted_values):
    output = pd.DataFrame({'Id': test_id,
                       'SalePrice': predicted_values.squeeze()})
    print(output.head())
