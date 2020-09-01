import preprocess
import build_features
import train
import predict
import pandas as pd

def main():
    '''
    Prepares the dataset ready for training by preprocessing the data, building
    and engineering the features from the dataset and creating the .csv file of the
    dataset into the data folder.



    Returns:
        data_name_bf : prepared dataset file located on the data folder
    '''
    data_lst = ["val","train"]

    for i in data_lst:

        #Preprocessing the data
        my_input = "../data/{input}.csv".format(input=i)
        preprocess.execute(input_file=my_input,
        output_file='../data/{input}_bf.csv'.format(input=i))

        #Preparing the data for training
        my_input= "../data/{input}_bf.csv".format(input=i)
        build_features.execute(input_file=my_input,
        output_file='../data/{input}_bf.csv'.format(input=i))
        print("{input}_bf.csv file has been created".format(input=i))

    train_acc = train.execute()
    pred_acc = predict.execute()

    compare_models = pd.DataFrame({
        'Model': ['RandForest','ExtTree', 'GraBoo', 'AdaBoo'],
        'Train Score': train_acc,
        'Prediction Score': pred_acc

    })

    return print(compare_models)

#Run the main() function when executed
if __name__ == "__main__":
    main()
