import numpy as np


def hit_rate(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    flags = np.isin(recommended_list, bought_list)

    precision = np.sum(prices_recommended * flags) / np.sum(prices_recommended)

    return precision


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(1, k + 1):

        if flags[i] == True:
            p_k = precision_at_k(recommended_list, bought_list, k=i)
            sum_ += p_k

    result = sum_ / sum(flags)

    return result


def map_k(recommended_lists, bought_lists, k=5):
    result = []

    for rec, purch in zip(recommended_lists, bought_lists):
        result.append(ap_k(rec, purch, k))

    return np.mean(result)


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, bought_prices, k=5):
    bought_list = np.array(bought_list)
    bought_prices = np.array(bought_prices[:k])

    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])

    flags = np.isin(recommended_list, bought_list)

    recall = np.sum(flags * bought_prices) / np.sum(bought_prices)

    return recall


def reciprocal_rank(recommended_list, bought_list):
    for i, value in enumerate(bought_list):
        if np.isin(value, recommended_list):
            return 1/(i + 1)
