def roc_auc(labels, preds, n_bins=1000):
    pos = sum(labels)
    neg = len(labels) - pos
    total_case = pos * neg
    pos_his = [0 for _ in range(n_bins)]
    neg_his = [0 for _ in range(n_bins)]
    bin_width = 1.0 / float(n_bins)
    for i in range(len(labels)):
        nth_bin = int(preds[i] / bin_width)
        if labels[i] == 1:
            pos_his[nth_bin] += 1
        else:
            neg_his[nth_bin] += 1
    acc_neg = 0
    sat_pair = 0
    for i in range(n_bins):
        sat_pair += (pos_his[i] * acc_neg + pos_his[i] * neg_his[i] * 0.5)
        acc_neg += neg_his[i]
    return round(sat_pair / float(total_case), 2)


N = int(input())
labels, preds = [], []
for i in range(N):
    label, pred = map(float, input().split())
    labels.append(label)
    preds.append(pred)
print(roc_auc(labels, preds))
