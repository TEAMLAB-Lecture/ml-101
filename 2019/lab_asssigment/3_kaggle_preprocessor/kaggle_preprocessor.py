import numpy as np
import pandas as pd

def get_train_test_split_dataset(train_dataset_filename  = None, test_dataset_filename = None):
    '''
    - 함수목적
      - Kaggle의 dataset중 "House Price" 문제의 train dataset과 test dataset의 파일을 입력하면 해당 데이터셋을
        학습가능한 형태로 X_train, y_tain, X_test 로 전처리 하여 반환해준다.
      - 반환된 X_train과 yt_train 데이터셋을 자동채점 시스템이 Linear Regression으로 모델을 만들어
        Root-Mean-Squared-Error (RMSE) value를 측정하여 threshold 이상의 결과를 내야만 test를 합격할 수 있다.
      - https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
    - Args
        - train_dataset_filename: house price 문제의 "train.csv" 파일 이름 (str 타입)
        - test_dataset_filename: house price 문제의 "test.csv" 파일 이름 (str 타입)
    - Returns
        - X_train: "train.csv"파일의 feature들을 전처리한 결과값으로 two-dimensional ndarrray type
        - y_train = "train.csv"파일의 feature들 중 `SalePrice` 값이 one-dimensional ndarrray type
        - X_test: "test.csv"파일의 feature들을 전처리한 결과값으로 two-dimensional ndarrray type
        - test_id_idx: "test.csv"파일의 index 값들을 one-dimensional ndarrray type으로 반환함
    - Constraints for return value
        - X_train 에서 사용되는 feature 개수는 30개 이상이어야 한다.
        - X_train과 y_train의 row의 개수는 같아야 한다.
        - X_train과 X_test의 feature의 개수는 같아야 한다.
        - X_train, y_train을 가지고  Root-Mean-Squared-Error (RMSE) value를 취했을 때, 9이상이어야 한다(CV 5 times)
        - test_id_idx의 값의 개수는 X_test의 row의 개수와 같아야 한다.



    '''

    X_train = None
    y_train = None
    X_test = None
    test_id_idx = None

    return X_train, X_test, y_train, test_id_idx
