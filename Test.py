import pandas as pd

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = sorted(data['whoAmI'].unique())
category_dict = {category: [1 if category == value else 0 for value in categories] for category in categories}

one_hot_encoded = pd.DataFrame(data['whoAmI'].apply(lambda x: category_dict[x]).tolist(), columns=categories)

data = pd.concat([data, one_hot_encoded], axis=1).drop(columns=['whoAmI'])

data.head()