def prefilter_items(data):
    # Уберем самые популярные товары (их и так купят)
    popularity = data_train.groupby('item_id')['user_id'].nunique().reset_index() / data_train['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]

    # Уберем товары, которые не продавались за последние 12 месяцев

    # Уберем не интересные для рекоммендаций категории (department)

    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.

    # Уберем слишком дорогие товарыs

    # ...


def postfilter_items(user_id, recommednations):
    pass


def get_recommendations(user, model, sparse_user_item, N=5):
    """Рекомендуем топ-N товаров"""

    res = [id_to_itemid[rec[0]] for rec in
           model.recommend(userid=userid_to_id[user],
                           user_items=sparse_user_item,  # на вход user-item matrix
                           N=N,
                           filter_already_liked_items=False,
                           filter_items=[itemid_to_id[999999]],  # !!!
                           recalculate_user=True)]
    return res


