import matplotlib.pyplot as plt

log1 = """epoch: 0/199: : 910it [00:06, 139.33it/s, loss=0.070639]                        
eval psnr: 16.88
epoch: 1/199: : 910it [00:06, 135.61it/s, loss=0.018622]                        
eval psnr: 18.60
epoch: 2/199: : 910it [00:06, 136.87it/s, loss=0.013291]                        
eval psnr: 19.32
epoch: 3/199: : 910it [00:06, 137.00it/s, loss=0.011141]                        
epoch: 4/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 21.12
epoch: 4/199: : 910it [00:07, 129.60it/s, loss=0.010075]                        
eval psnr: 22.06
epoch: 5/199: : 910it [00:06, 134.40it/s, loss=0.009463]                        
epoch: 6/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 22.19
epoch: 6/199: : 910it [00:06, 139.38it/s, loss=0.009224]                        
epoch: 7/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 22.01
epoch: 7/199: : 910it [00:06, 130.38it/s, loss=0.008744]                        
epoch: 8/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 21.80
epoch: 8/199: : 910it [00:06, 134.52it/s, loss=0.008571]                        
eval psnr: 22.00
epoch: 9/199: : 910it [00:06, 149.92it/s, loss=0.008503]                        
epoch: 10/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.90
epoch: 10/199: : 910it [00:06, 132.90it/s, loss=0.008405]                       
epoch: 11/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.21
epoch: 11/199: : 910it [00:06, 134.26it/s, loss=0.008202]                       
eval psnr: 22.25
epoch: 12/199: : 910it [00:06, 141.26it/s, loss=0.008150]                       
eval psnr: 22.03
epoch: 13/199: : 910it [00:06, 133.85it/s, loss=0.008136]
epoch: 14/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.15
epoch: 14/199: : 910it [00:06, 138.67it/s, loss=0.008139]                       
eval psnr: 22.59
epoch: 15/199: : 910it [00:07, 127.89it/s, loss=0.007909]                       
epoch: 16/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.89
epoch: 16/199: : 910it [00:07, 123.77it/s, loss=0.007841]
epoch: 17/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.28
epoch: 17/199: : 910it [00:07, 119.96it/s, loss=0.007797]
epoch: 18/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.86
epoch: 18/199: : 910it [00:07, 122.93it/s, loss=0.007939]
epoch: 19/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.88
epoch: 19/199: : 910it [00:07, 119.47it/s, loss=0.007912]
epoch: 20/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.18
epoch: 20/199: : 910it [00:07, 124.85it/s, loss=0.007661]
eval psnr: 22.78
epoch: 21/199: : 910it [00:07, 120.30it/s, loss=0.007536]
eval psnr: 22.84
epoch: 22/199: : 910it [00:07, 124.07it/s, loss=0.007831]
epoch: 23/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.66
epoch: 23/199: : 910it [00:07, 117.57it/s, loss=0.007766]
eval psnr: 22.80
epoch: 24/199: : 910it [00:07, 123.04it/s, loss=0.007624]
epoch: 25/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.75
epoch: 25/199: : 910it [00:07, 122.18it/s, loss=0.007442]
eval psnr: 22.57
epoch: 26/199: : 910it [00:07, 122.18it/s, loss=0.007407]
eval psnr: 22.99
epoch: 27/199: : 910it [00:07, 121.32it/s, loss=0.007470]                       
eval psnr: 22.22
epoch: 28/199: : 910it [00:07, 122.93it/s, loss=0.007205]
epoch: 29/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.57
epoch: 29/199: : 910it [00:07, 124.85it/s, loss=0.007537]
epoch: 30/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.84
epoch: 30/199: : 910it [00:07, 121.56it/s, loss=0.007337]
epoch: 31/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.14
epoch: 31/199: : 910it [00:07, 124.46it/s, loss=0.007282]
eval psnr: 23.20
epoch: 32/199: : 910it [00:07, 120.27it/s, loss=0.007300]
eval psnr: 22.63
epoch: 33/199: : 910it [00:07, 122.31it/s, loss=0.007051]
eval psnr: 22.36
epoch: 34/199: : 910it [00:07, 121.67it/s, loss=0.007238]
eval psnr: 22.50
epoch: 35/199: : 910it [00:07, 120.75it/s, loss=0.007326]
epoch: 36/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.25
epoch: 36/199: : 910it [00:07, 120.15it/s, loss=0.007134]                       
eval psnr: 23.32
epoch: 37/199: : 910it [00:07, 121.36it/s, loss=0.007530]
eval psnr: 22.48
epoch: 38/199: : 910it [00:07, 119.44it/s, loss=0.007124]
eval psnr: 22.96
epoch: 39/199: : 910it [00:07, 124.57it/s, loss=0.007154]
eval psnr: 22.80
epoch: 40/199: : 910it [00:07, 118.45it/s, loss=0.007122]                       
eval psnr: 23.14
epoch: 41/199: : 910it [00:07, 123.25it/s, loss=0.007068]                       
eval psnr: 22.99
epoch: 42/199: : 910it [00:07, 124.21it/s, loss=0.007061]                       
eval psnr: 23.26
epoch: 43/199: : 910it [00:07, 125.64it/s, loss=0.007148]
eval psnr: 22.71
epoch: 44/199: : 910it [00:07, 120.94it/s, loss=0.007131]
epoch: 45/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.78
epoch: 45/199: : 910it [00:07, 124.97it/s, loss=0.007256]
eval psnr: 22.73
epoch: 46/199: : 910it [00:07, 123.11it/s, loss=0.007221]
eval psnr: 22.91
epoch: 47/199: : 910it [00:07, 123.61it/s, loss=0.006991]
eval psnr: 22.99
epoch: 48/199: : 910it [00:07, 123.17it/s, loss=0.006739]                       
eval psnr: 22.85
epoch: 49/199: : 910it [00:07, 123.12it/s, loss=0.007123]                       
epoch: 50/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.86
epoch: 50/199: : 910it [00:07, 121.61it/s, loss=0.006832]
epoch: 51/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.94
epoch: 51/199: : 910it [00:07, 125.88it/s, loss=0.006954]
eval psnr: 22.95
epoch: 52/199: : 910it [00:07, 120.26it/s, loss=0.006888]                       
eval psnr: 23.00
epoch: 53/199: : 910it [00:07, 121.65it/s, loss=0.007244]
epoch: 54/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.26
epoch: 54/199: : 910it [00:07, 120.68it/s, loss=0.006998]
epoch: 55/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.79
epoch: 55/199: : 910it [00:07, 122.34it/s, loss=0.006812]
eval psnr: 23.10
epoch: 56/199: : 910it [00:07, 123.40it/s, loss=0.006670]
epoch: 57/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.97
epoch: 57/199: : 910it [00:07, 123.52it/s, loss=0.006925]                       
epoch: 58/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.78
epoch: 58/199: : 910it [00:07, 121.63it/s, loss=0.006804]
eval psnr: 22.77
epoch: 59/199: : 910it [00:07, 123.76it/s, loss=0.006957]
eval psnr: 23.24
epoch: 60/199: : 910it [00:07, 119.80it/s, loss=0.006786]
epoch: 61/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.93
epoch: 61/199: : 910it [00:07, 126.55it/s, loss=0.006962]
epoch: 62/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.26
epoch: 62/199: : 910it [00:07, 122.90it/s, loss=0.006899]
epoch: 63/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.35
epoch: 63/199: : 910it [00:07, 124.91it/s, loss=0.006832]
epoch: 64/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.37
epoch: 64/199: : 910it [00:07, 121.72it/s, loss=0.006569]
eval psnr: 22.98
epoch: 65/199: : 910it [00:07, 128.13it/s, loss=0.006809]
eval psnr: 22.56
epoch: 66/199: : 910it [00:07, 120.25it/s, loss=0.007327]
epoch: 67/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.70
epoch: 67/199: : 910it [00:07, 122.33it/s, loss=0.006819]
eval psnr: 22.95
epoch: 68/199: : 910it [00:07, 119.48it/s, loss=0.006873]
epoch: 69/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.55
epoch: 69/199: : 910it [00:07, 121.52it/s, loss=0.006605]
epoch: 70/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.29
epoch: 70/199: : 910it [00:06, 130.87it/s, loss=0.006896]
eval psnr: 23.14
epoch: 71/199: : 910it [00:06, 130.59it/s, loss=0.006687]
epoch: 72/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 72/199: : 910it [00:07, 127.14it/s, loss=0.006667]
epoch: 73/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.90
epoch: 73/199: : 910it [00:07, 122.57it/s, loss=0.006885]
eval psnr: 23.17
epoch: 74/199: : 910it [00:07, 120.94it/s, loss=0.006608]
epoch: 75/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.18
epoch: 75/199: : 910it [00:07, 118.77it/s, loss=0.006786]
epoch: 76/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.50
epoch: 76/199: : 910it [00:07, 121.29it/s, loss=0.006716]
eval psnr: 22.86
epoch: 77/199: : 910it [00:07, 121.04it/s, loss=0.006679]
epoch: 78/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.55
epoch: 78/199: : 910it [00:07, 123.47it/s, loss=0.006831]                       
epoch: 79/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.74
epoch: 79/199: : 910it [00:07, 120.71it/s, loss=0.006669]
epoch: 80/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.98
epoch: 80/199: : 910it [00:07, 122.26it/s, loss=0.006809]
epoch: 81/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.88
epoch: 81/199: : 910it [00:07, 118.79it/s, loss=0.006689]                       
epoch: 82/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.05
epoch: 82/199: : 910it [00:07, 121.43it/s, loss=0.006867]
eval psnr: 22.75
epoch: 83/199: : 910it [00:07, 117.05it/s, loss=0.006611]
eval psnr: 22.93
epoch: 84/199: : 910it [00:07, 123.73it/s, loss=0.006705]                       
epoch: 85/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.72
epoch: 85/199: : 910it [00:07, 120.93it/s, loss=0.006635]                       
epoch: 86/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.28
epoch: 86/199: : 910it [00:07, 125.17it/s, loss=0.006642]
eval psnr: 22.91
epoch: 87/199: : 910it [00:07, 119.11it/s, loss=0.006777]
epoch: 88/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.70
epoch: 88/199: : 910it [00:07, 122.09it/s, loss=0.006604]                       
epoch: 89/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.96
epoch: 89/199: : 910it [00:07, 120.35it/s, loss=0.006571]                       
epoch: 90/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.00
epoch: 90/199: : 910it [00:07, 123.22it/s, loss=0.006618]                       
epoch: 91/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.90
epoch: 91/199: : 910it [00:07, 123.00it/s, loss=0.006563]                       
epoch: 92/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.47
epoch: 92/199: : 910it [00:07, 121.37it/s, loss=0.006718]
epoch: 93/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.59
epoch: 93/199: : 910it [00:07, 120.56it/s, loss=0.006598]
epoch: 94/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.73
epoch: 94/199: : 910it [00:07, 120.90it/s, loss=0.006865]                       
epoch: 95/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.24
epoch: 95/199: : 910it [00:07, 124.35it/s, loss=0.006608]
eval psnr: 23.11
epoch: 96/199: : 910it [00:07, 120.27it/s, loss=0.006673]                       
epoch: 97/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.31
epoch: 97/199: : 910it [00:07, 120.53it/s, loss=0.006724]
epoch: 98/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.67
epoch: 98/199: : 910it [00:07, 127.88it/s, loss=0.006753]
epoch: 99/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.15
epoch: 99/199: : 910it [00:07, 119.07it/s, loss=0.006654]
epoch: 100/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 22.85
epoch: 100/199: : 910it [00:07, 119.47it/s, loss=0.006542]
eval psnr: 22.97
epoch: 101/199: : 910it [00:07, 122.46it/s, loss=0.006487]
eval psnr: 23.12
epoch: 102/199: : 910it [00:07, 124.30it/s, loss=0.006647]                      
epoch: 103/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.60
epoch: 103/199: : 910it [00:07, 119.05it/s, loss=0.006479]                      
eval psnr: 23.45
epoch: 104/199: : 910it [00:07, 120.84it/s, loss=0.006726]
epoch: 105/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.01
epoch: 105/199: : 910it [00:07, 124.63it/s, loss=0.006483]                      
eval psnr: 22.76
epoch: 106/199: : 910it [00:07, 121.04it/s, loss=0.006524]
epoch: 107/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.72
epoch: 107/199: : 910it [00:07, 122.62it/s, loss=0.006580]
epoch: 108/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.17
epoch: 108/199: : 910it [00:07, 123.70it/s, loss=0.006432]
eval psnr: 23.43
epoch: 109/199: : 910it [00:07, 120.54it/s, loss=0.006802]
epoch: 110/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 110/199: : 910it [00:07, 120.63it/s, loss=0.006614]                      
eval psnr: 22.89
epoch: 111/199: : 910it [00:07, 122.66it/s, loss=0.006451]
eval psnr: 22.98
epoch: 112/199: : 910it [00:07, 121.05it/s, loss=0.006639]
eval psnr: 23.51
epoch: 113/199: : 910it [00:07, 122.84it/s, loss=0.006493]                      
eval psnr: 23.74
epoch: 114/199: : 910it [00:07, 119.91it/s, loss=0.006496]
epoch: 115/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 115/199: : 910it [00:07, 124.11it/s, loss=0.006592]                      
epoch: 116/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 22.57
epoch: 116/199: : 910it [00:07, 118.07it/s, loss=0.006545]
eval psnr: 23.22
epoch: 117/199: : 910it [00:07, 120.47it/s, loss=0.006763]
epoch: 118/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.44
epoch: 118/199: : 910it [00:07, 119.87it/s, loss=0.006610]
epoch: 119/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 22.99
epoch: 119/199: : 910it [00:07, 123.98it/s, loss=0.006404]                      
eval psnr: 23.08
epoch: 120/199: : 910it [00:07, 121.81it/s, loss=0.006356]
epoch: 121/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.52
epoch: 121/199: : 910it [00:07, 122.31it/s, loss=0.006416]                      
eval psnr: 23.28
epoch: 122/199: : 910it [00:07, 120.83it/s, loss=0.006487]
eval psnr: 23.57
epoch: 123/199: : 910it [00:07, 119.65it/s, loss=0.006626]
epoch: 124/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.45
epoch: 124/199: : 910it [00:07, 124.30it/s, loss=0.006459]
epoch: 125/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 22.84
epoch: 125/199: : 910it [00:07, 123.41it/s, loss=0.006570]
epoch: 126/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 126/199: : 910it [00:07, 121.41it/s, loss=0.006512]
epoch: 127/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.39
epoch: 127/199: : 910it [00:07, 120.83it/s, loss=0.006375]                      
eval psnr: 23.33
epoch: 128/199: : 910it [00:07, 122.26it/s, loss=0.006576]
eval psnr: 23.42
epoch: 129/199: : 910it [00:07, 121.09it/s, loss=0.006188]
epoch: 130/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.32
epoch: 130/199: : 910it [00:07, 119.18it/s, loss=0.006238]
epoch: 131/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.57
epoch: 131/199: : 910it [00:07, 121.71it/s, loss=0.006395]
eval psnr: 23.74
epoch: 132/199: : 910it [00:07, 117.17it/s, loss=0.006515]
epoch: 133/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.07
epoch: 133/199: : 910it [00:07, 121.35it/s, loss=0.006332]
eval psnr: 23.20
epoch: 134/199: : 910it [00:07, 121.18it/s, loss=0.006348]                      
eval psnr: 23.63
epoch: 135/199: : 910it [00:07, 117.67it/s, loss=0.006417]
eval psnr: 23.01
epoch: 136/199: : 910it [00:07, 123.02it/s, loss=0.006275]
eval psnr: 23.20
epoch: 137/199: : 910it [00:07, 118.41it/s, loss=0.006326]
epoch: 138/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.23
epoch: 138/199: : 910it [00:07, 124.12it/s, loss=0.006203]
eval psnr: 23.48
epoch: 139/199: : 910it [00:07, 122.92it/s, loss=0.006308]                      
epoch: 140/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.29
epoch: 140/199: : 910it [00:07, 123.32it/s, loss=0.006214]
eval psnr: 23.27
epoch: 141/199: : 910it [00:07, 122.59it/s, loss=0.006389]
eval psnr: 23.79
epoch: 142/199: : 910it [00:07, 121.80it/s, loss=0.006403]
eval psnr: 24.17
epoch: 143/199: : 910it [00:07, 120.50it/s, loss=0.006263]                      
eval psnr: 23.80
epoch: 144/199: : 910it [00:07, 124.00it/s, loss=0.006403]
epoch: 145/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.38
epoch: 145/199: : 910it [00:07, 119.94it/s, loss=0.006160]
eval psnr: 23.42
epoch: 146/199: : 910it [00:07, 121.87it/s, loss=0.006360]                      
epoch: 147/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.30
epoch: 147/199: : 910it [00:07, 119.86it/s, loss=0.006566]
epoch: 148/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.36
epoch: 148/199: : 910it [00:07, 123.14it/s, loss=0.006292]
eval psnr: 23.73
epoch: 149/199: : 910it [00:07, 120.28it/s, loss=0.006212]
epoch: 150/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.78
epoch: 150/199: : 910it [00:07, 120.64it/s, loss=0.006512]
eval psnr: 23.26
epoch: 151/199: : 910it [00:07, 123.83it/s, loss=0.006200]
eval psnr: 23.75
epoch: 152/199: : 910it [00:07, 123.62it/s, loss=0.006347]
epoch: 153/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.02
epoch: 153/199: : 910it [00:07, 121.56it/s, loss=0.006402]
epoch: 154/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.43
epoch: 154/199: : 910it [00:07, 121.43it/s, loss=0.006203]
eval psnr: 23.33
epoch: 155/199: : 910it [00:07, 123.75it/s, loss=0.006621]                      
eval psnr: 23.62
epoch: 156/199: : 910it [00:07, 122.87it/s, loss=0.006352]
eval psnr: 22.86
epoch: 157/199: : 910it [00:07, 121.16it/s, loss=0.006323]
epoch: 158/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.55
epoch: 158/199: : 910it [00:07, 121.31it/s, loss=0.006256]
epoch: 159/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 159/199: : 910it [00:07, 121.78it/s, loss=0.006291]
epoch: 160/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.68
epoch: 160/199: : 910it [00:07, 121.85it/s, loss=0.006321]
eval psnr: 23.58
epoch: 161/199: : 910it [00:07, 120.81it/s, loss=0.006319]
epoch: 162/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.72
epoch: 162/199: : 910it [00:07, 119.94it/s, loss=0.006248]
epoch: 163/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.34
epoch: 163/199: : 910it [00:07, 117.32it/s, loss=0.006192]
eval psnr: 23.10
epoch: 164/199: : 910it [00:07, 124.53it/s, loss=0.006482]                      
epoch: 165/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.98
epoch: 165/199: : 910it [00:07, 121.37it/s, loss=0.006211]
epoch: 166/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.79
epoch: 166/199: : 910it [00:07, 119.82it/s, loss=0.006090]
epoch: 167/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.18
epoch: 167/199: : 910it [00:07, 120.88it/s, loss=0.006296]
eval psnr: 23.92
epoch: 168/199: : 910it [00:07, 122.39it/s, loss=0.006283]
epoch: 169/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.31
epoch: 169/199: : 910it [00:07, 122.08it/s, loss=0.006182]
eval psnr: 23.89
epoch: 170/199: : 910it [00:07, 121.61it/s, loss=0.006357]                      
eval psnr: 23.32
epoch: 171/199: : 910it [00:07, 121.64it/s, loss=0.006547]
eval psnr: 23.57
epoch: 172/199: : 910it [00:07, 120.42it/s, loss=0.006191]                      
eval psnr: 23.56
epoch: 173/199: : 910it [00:07, 119.16it/s, loss=0.006332]                      
epoch: 174/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.76
epoch: 174/199: : 910it [00:07, 121.19it/s, loss=0.006274]                      
eval psnr: 24.20
epoch: 175/199: : 910it [00:07, 121.87it/s, loss=0.006262]
epoch: 176/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.58
epoch: 176/199: : 910it [00:07, 120.28it/s, loss=0.006235]
epoch: 177/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.17
epoch: 177/199: : 910it [00:07, 122.84it/s, loss=0.006441]
eval psnr: 23.13
epoch: 178/199: : 910it [00:07, 119.16it/s, loss=0.006061]                      
epoch: 179/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.21
epoch: 179/199: : 910it [00:07, 118.90it/s, loss=0.006304]
epoch: 180/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.92
epoch: 180/199: : 910it [00:07, 120.62it/s, loss=0.006225]                      
epoch: 181/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.95
epoch: 181/199: : 910it [00:07, 123.12it/s, loss=0.006118]                      
eval psnr: 23.31
epoch: 182/199: : 910it [00:07, 123.17it/s, loss=0.006201]
eval psnr: 23.60
epoch: 183/199: : 910it [00:07, 122.31it/s, loss=0.006342]
epoch: 184/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.95
epoch: 184/199: : 910it [00:07, 121.29it/s, loss=0.006174]
eval psnr: 23.72
epoch: 185/199: : 910it [00:07, 120.99it/s, loss=0.006227]
eval psnr: 23.71
epoch: 186/199: : 910it [00:07, 122.19it/s, loss=0.006147]
eval psnr: 23.80
epoch: 187/199: : 910it [00:07, 123.43it/s, loss=0.005977]                      
eval psnr: 23.91
epoch: 188/199: : 910it [00:07, 120.88it/s, loss=0.006338]
epoch: 189/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.99
epoch: 189/199: : 910it [00:07, 122.43it/s, loss=0.006216]                      
epoch: 190/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.90
epoch: 190/199: : 910it [00:07, 119.40it/s, loss=0.006202]                      
epoch: 191/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.40
epoch: 191/199: : 910it [00:07, 127.13it/s, loss=0.006263]
eval psnr: 23.35
epoch: 192/199: : 910it [00:07, 119.42it/s, loss=0.006008]                      
epoch: 193/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.92
epoch: 193/199: : 910it [00:07, 123.20it/s, loss=0.006203]
epoch: 194/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 194/199: : 910it [00:07, 125.04it/s, loss=0.006032]
epoch: 195/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.34
epoch: 195/199: : 910it [00:07, 125.13it/s, loss=0.006323]
epoch: 196/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.16
epoch: 196/199: : 910it [00:07, 121.52it/s, loss=0.006166]                      
epoch: 197/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.52
epoch: 197/199: : 910it [00:07, 122.87it/s, loss=0.006205]
epoch: 198/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.74
epoch: 198/199: : 910it [00:07, 121.20it/s, loss=0.006172]
epoch: 199/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.16
epoch: 199/199: : 910it [00:07, 121.45it/s, loss=0.006052]
eval psnr: 23.13
best epoch: 178, psnr: 24.21
"""

log2 = """epoch: 0/199: : 910it [00:25, 35.79it/s, loss=0.051732]
eval psnr: 17.01
epoch: 1/199: : 910it [00:24, 36.62it/s, loss=0.020657]
eval psnr: 18.08
epoch: 2/199: : 910it [00:24, 36.74it/s, loss=0.018104]
eval psnr: 18.66
epoch: 3/199: : 910it [00:24, 36.53it/s, loss=0.016404]
epoch: 4/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 18.62
epoch: 4/199: : 910it [00:25, 35.21it/s, loss=0.015153]
epoch: 5/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 18.63
epoch: 5/199: : 910it [00:27, 33.57it/s, loss=0.013915]
eval psnr: 19.58
epoch: 6/199: : 910it [00:27, 33.46it/s, loss=0.012992]
eval psnr: 19.70
epoch: 7/199: : 910it [00:27, 33.39it/s, loss=0.012292]
eval psnr: 19.83
epoch: 8/199: : 910it [00:27, 33.29it/s, loss=0.012046]
eval psnr: 20.23
epoch: 9/199: : 910it [00:27, 33.34it/s, loss=0.011574]
eval psnr: 20.21
epoch: 10/199: : 910it [00:27, 33.48it/s, loss=0.011201]
eval psnr: 20.33
epoch: 11/199: : 910it [00:27, 33.39it/s, loss=0.010767]
epoch: 12/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 20.06
epoch: 12/199: : 910it [00:27, 33.47it/s, loss=0.010114]
eval psnr: 20.67
epoch: 13/199: : 910it [00:27, 33.55it/s, loss=0.010180]
eval psnr: 21.29
epoch: 14/199: : 910it [00:27, 33.40it/s, loss=0.009922]
epoch: 15/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 20.91
epoch: 15/199: : 910it [00:27, 33.47it/s, loss=0.009663]
eval psnr: 20.89
epoch: 16/199: : 910it [00:27, 33.55it/s, loss=0.009422]
eval psnr: 20.54
epoch: 17/199: : 910it [00:27, 33.29it/s, loss=0.009421]
epoch: 18/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.08
epoch: 18/199: : 910it [00:27, 33.38it/s, loss=0.008977]
eval psnr: 20.96
epoch: 19/199: : 910it [00:27, 33.54it/s, loss=0.008734]
eval psnr: 21.03
epoch: 20/199: : 910it [00:27, 33.27it/s, loss=0.008666]
epoch: 21/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 20.85
epoch: 21/199: : 910it [00:27, 33.63it/s, loss=0.008649]
eval psnr: 20.60
epoch: 22/199: : 910it [00:27, 33.59it/s, loss=0.008315]
eval psnr: 21.05
epoch: 23/199: : 910it [00:27, 33.55it/s, loss=0.008578]
eval psnr: 20.66
epoch: 24/199: : 910it [00:27, 33.54it/s, loss=0.008280]
eval psnr: 21.03
epoch: 25/199: : 910it [00:27, 33.36it/s, loss=0.008025]
eval psnr: 21.29
epoch: 26/199: : 910it [00:27, 33.48it/s, loss=0.007968]
eval psnr: 21.58
epoch: 27/199: : 910it [00:28, 32.24it/s, loss=0.007762]
eval psnr: 21.90
epoch: 28/199: : 910it [00:28, 31.77it/s, loss=0.007906]
eval psnr: 21.41
epoch: 29/199: : 910it [00:28, 31.47it/s, loss=0.007681]
epoch: 30/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.19
epoch: 30/199: : 910it [00:27, 32.82it/s, loss=0.007802]
eval psnr: 21.97
epoch: 31/199: : 910it [00:27, 33.55it/s, loss=0.007511]
eval psnr: 21.98
epoch: 32/199: : 910it [00:27, 33.64it/s, loss=0.007611]
eval psnr: 21.34
epoch: 33/199: : 910it [00:27, 33.46it/s, loss=0.007618]
eval psnr: 21.41
epoch: 34/199: : 910it [00:27, 33.54it/s, loss=0.007478]
eval psnr: 22.26
epoch: 35/199: : 910it [00:27, 33.52it/s, loss=0.007385]
eval psnr: 22.37
epoch: 36/199: : 910it [00:27, 33.39it/s, loss=0.007399]
epoch: 37/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.96
epoch: 37/199: : 910it [00:27, 33.48it/s, loss=0.007210]
eval psnr: 21.85
epoch: 38/199: : 910it [00:27, 33.55it/s, loss=0.007119]
eval psnr: 22.23
epoch: 39/199: : 910it [00:27, 33.54it/s, loss=0.007304]
eval psnr: 22.17
epoch: 40/199: : 910it [00:27, 33.48it/s, loss=0.007076]
eval psnr: 21.98
epoch: 41/199: : 910it [00:27, 33.54it/s, loss=0.007011]
eval psnr: 22.50
epoch: 42/199: : 910it [00:27, 33.32it/s, loss=0.007125]
eval psnr: 22.39
epoch: 43/199: : 910it [00:27, 33.47it/s, loss=0.006828]
eval psnr: 22.53
epoch: 44/199: : 910it [00:27, 33.42it/s, loss=0.006790]
eval psnr: 22.81
epoch: 45/199: : 910it [00:27, 33.54it/s, loss=0.006841]
eval psnr: 21.49
epoch: 46/199: : 910it [00:27, 33.62it/s, loss=0.006920]
eval psnr: 22.82
epoch: 47/199: : 910it [00:27, 33.51it/s, loss=0.006643]
epoch: 48/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.10
epoch: 48/199: : 910it [00:27, 33.49it/s, loss=0.006825]
epoch: 49/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.29
epoch: 49/199: : 910it [00:27, 33.64it/s, loss=0.006613]
eval psnr: 22.08
epoch: 50/199: : 910it [00:27, 33.31it/s, loss=0.006777]
epoch: 51/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.70
epoch: 51/199: : 910it [00:27, 33.57it/s, loss=0.006555]
eval psnr: 22.95
epoch: 52/199: : 910it [00:27, 33.55it/s, loss=0.006521]
epoch: 53/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.84
epoch: 53/199: : 910it [00:27, 33.44it/s, loss=0.006600]
eval psnr: 22.34
epoch: 54/199: : 910it [00:27, 33.44it/s, loss=0.006511]
eval psnr: 22.97
epoch: 55/199: : 910it [00:27, 33.60it/s, loss=0.006431]
eval psnr: 22.48
epoch: 56/199: : 910it [00:27, 33.48it/s, loss=0.006485]
eval psnr: 22.66
epoch: 57/199: : 910it [00:27, 33.51it/s, loss=0.006343]
eval psnr: 22.99
epoch: 58/199: : 910it [00:27, 33.58it/s, loss=0.006344]
eval psnr: 23.12
epoch: 59/199: : 910it [00:27, 33.43it/s, loss=0.006501]
eval psnr: 22.46
epoch: 60/199: : 910it [00:27, 33.62it/s, loss=0.006467]
eval psnr: 22.00
epoch: 61/199: : 910it [00:27, 33.45it/s, loss=0.006305]
eval psnr: 23.44
epoch: 62/199: : 910it [00:27, 33.45it/s, loss=0.006487]
epoch: 63/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.74
epoch: 63/199: : 910it [00:27, 33.35it/s, loss=0.006396]
epoch: 64/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.52
epoch: 64/199: : 910it [00:27, 33.46it/s, loss=0.006273]
eval psnr: 22.58
epoch: 65/199: : 910it [00:27, 33.42it/s, loss=0.006238]
epoch: 66/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.96
epoch: 66/199: : 910it [00:27, 33.48it/s, loss=0.006199]
epoch: 67/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.15
epoch: 67/199: : 910it [00:27, 33.34it/s, loss=0.006323]
eval psnr: 23.13
epoch: 68/199: : 910it [00:27, 33.35it/s, loss=0.006149]
eval psnr: 22.62
epoch: 69/199: : 910it [00:27, 33.48it/s, loss=0.006277]
epoch: 70/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.35
epoch: 70/199: : 910it [00:27, 33.52it/s, loss=0.006062]
eval psnr: 23.72
epoch: 71/199: : 910it [00:27, 32.84it/s, loss=0.006124]
eval psnr: 23.49
epoch: 72/199: : 910it [00:29, 31.14it/s, loss=0.006052]
eval psnr: 23.09
epoch: 73/199: : 910it [00:28, 32.18it/s, loss=0.005974]
eval psnr: 23.45
epoch: 74/199: : 910it [00:27, 33.10it/s, loss=0.006046]
epoch: 75/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.89
epoch: 75/199: : 910it [00:27, 33.41it/s, loss=0.005852]
eval psnr: 23.38
epoch: 76/199: : 910it [00:27, 33.37it/s, loss=0.006002]
epoch: 77/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.44
epoch: 77/199: : 910it [00:27, 33.40it/s, loss=0.005913]
eval psnr: 23.03
epoch: 78/199: : 910it [00:27, 33.26it/s, loss=0.006012]
epoch: 79/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.62
epoch: 79/199: : 910it [00:27, 33.57it/s, loss=0.006027]
epoch: 80/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.22
epoch: 80/199: : 910it [00:27, 33.44it/s, loss=0.005820]
epoch: 81/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.35
epoch: 81/199: : 910it [00:27, 33.38it/s, loss=0.005913]
eval psnr: 23.43
epoch: 82/199: : 910it [00:27, 33.21it/s, loss=0.005833]
eval psnr: 23.54
epoch: 83/199: : 910it [00:27, 33.52it/s, loss=0.005806]
epoch: 84/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.44
epoch: 84/199: : 910it [00:27, 33.54it/s, loss=0.005778]
eval psnr: 24.00
epoch: 85/199: : 910it [00:27, 33.19it/s, loss=0.005849]
epoch: 86/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.66
epoch: 86/199: : 910it [00:27, 33.50it/s, loss=0.005653]
epoch: 87/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.64
epoch: 87/199: : 910it [00:27, 33.32it/s, loss=0.005687]
eval psnr: 24.04
epoch: 88/199: : 910it [00:27, 33.52it/s, loss=0.005828]
eval psnr: 23.63
epoch: 89/199: : 910it [00:27, 33.41it/s, loss=0.005588]
eval psnr: 23.75
epoch: 90/199: : 910it [00:27, 33.39it/s, loss=0.005585]
epoch: 91/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.85
epoch: 91/199: : 910it [00:27, 33.48it/s, loss=0.005666]
eval psnr: 24.18
epoch: 92/199: : 910it [00:27, 33.43it/s, loss=0.005823]
epoch: 93/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.40
epoch: 93/199: : 910it [00:27, 33.37it/s, loss=0.005740]
epoch: 94/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.01
epoch: 94/199: : 910it [00:27, 33.52it/s, loss=0.005699]
eval psnr: 23.74
epoch: 95/199: : 910it [00:27, 33.50it/s, loss=0.005727]
epoch: 96/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.39
epoch: 96/199: : 910it [00:27, 33.57it/s, loss=0.005698]
eval psnr: 23.91
epoch: 97/199: : 910it [00:27, 33.07it/s, loss=0.005737]
epoch: 98/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.21
epoch: 98/199: : 910it [00:27, 33.28it/s, loss=0.005635]
epoch: 99/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 99/199: : 910it [00:27, 33.02it/s, loss=0.005600]
eval psnr: 23.93
epoch: 100/199: : 910it [00:27, 33.47it/s, loss=0.005635]
epoch: 101/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.15
epoch: 101/199: : 910it [00:27, 33.59it/s, loss=0.005742]
eval psnr: 23.80
epoch: 102/199: : 910it [00:27, 33.67it/s, loss=0.005631]
epoch: 103/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.82
epoch: 103/199: : 910it [00:27, 33.50it/s, loss=0.005682]
eval psnr: 24.23
epoch: 104/199: : 910it [00:27, 33.52it/s, loss=0.005519]
epoch: 105/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.87
epoch: 105/199: : 910it [00:27, 33.48it/s, loss=0.005438]
epoch: 106/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.17
epoch: 106/199: : 910it [00:27, 33.48it/s, loss=0.005387]
epoch: 107/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.53
epoch: 107/199: : 910it [00:27, 33.30it/s, loss=0.005457]
eval psnr: 24.61
epoch: 108/199: : 910it [00:27, 33.31it/s, loss=0.005333]
epoch: 109/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.11
epoch: 109/199: : 910it [00:27, 33.41it/s, loss=0.005552]
epoch: 110/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.87
epoch: 110/199: : 910it [00:27, 33.40it/s, loss=0.005525]
epoch: 111/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.92
epoch: 111/199: : 910it [00:27, 33.43it/s, loss=0.005458]
epoch: 112/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 112/199: : 910it [00:27, 33.35it/s, loss=0.005410]
epoch: 113/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.73
epoch: 113/199: : 910it [00:27, 33.39it/s, loss=0.005308]
epoch: 114/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.37
epoch: 114/199: : 910it [00:27, 33.43it/s, loss=0.005599]
epoch: 115/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.11
epoch: 115/199: : 910it [00:27, 33.27it/s, loss=0.005300]
epoch: 116/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.09
epoch: 116/199: : 910it [00:27, 33.44it/s, loss=0.005427]
epoch: 117/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.32
epoch: 117/199: : 910it [00:27, 33.50it/s, loss=0.005374]
epoch: 118/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.58
epoch: 118/199: : 910it [00:27, 33.58it/s, loss=0.005169]
epoch: 119/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.21
epoch: 119/199: : 910it [00:27, 33.38it/s, loss=0.005264]
eval psnr: 23.91
epoch: 120/199: : 910it [00:27, 33.55it/s, loss=0.005324]
eval psnr: 23.31
epoch: 121/199: : 910it [00:27, 33.39it/s, loss=0.005398]
eval psnr: 23.27
epoch: 122/199: : 910it [00:27, 33.50it/s, loss=0.005146]
eval psnr: 24.10
epoch: 123/199: : 910it [00:27, 33.53it/s, loss=0.005235]
epoch: 124/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.13
epoch: 124/199: : 910it [00:27, 33.58it/s, loss=0.005382]
eval psnr: 23.35
epoch: 125/199: : 910it [00:27, 33.41it/s, loss=0.005236]
eval psnr: 23.56
epoch: 126/199: : 910it [00:27, 33.24it/s, loss=0.005142]
epoch: 127/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.61
epoch: 127/199: : 910it [00:27, 33.23it/s, loss=0.005198]
epoch: 128/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.23
epoch: 128/199: : 910it [00:27, 33.33it/s, loss=0.005214]
epoch: 129/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.45
epoch: 129/199: : 910it [00:27, 33.49it/s, loss=0.005233]
eval psnr: 24.19
epoch: 130/199: : 910it [00:27, 33.50it/s, loss=0.005275]
eval psnr: 23.97
epoch: 131/199: : 910it [00:27, 33.53it/s, loss=0.005036]
eval psnr: 24.35
epoch: 132/199: : 910it [00:27, 33.59it/s, loss=0.005183]
eval psnr: 24.26
epoch: 133/199: : 910it [00:27, 33.31it/s, loss=0.005251]
epoch: 134/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.51
epoch: 134/199: : 910it [00:27, 33.51it/s, loss=0.005277]
epoch: 135/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.54
epoch: 135/199: : 910it [00:27, 33.51it/s, loss=0.005185]
epoch: 136/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.64
epoch: 136/199: : 910it [00:27, 33.54it/s, loss=0.005161]
eval psnr: 23.86
epoch: 137/199: : 910it [00:27, 33.48it/s, loss=0.005173]
epoch: 138/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.99
epoch: 138/199: : 910it [00:27, 33.42it/s, loss=0.005093]
epoch: 139/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.86
epoch: 139/199: : 910it [00:27, 33.13it/s, loss=0.005147]
epoch: 140/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.22
epoch: 140/199: : 910it [00:27, 33.24it/s, loss=0.005172]
epoch: 141/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.77
epoch: 141/199: : 910it [00:27, 33.35it/s, loss=0.005191]
epoch: 142/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.93
epoch: 142/199: : 910it [00:27, 33.23it/s, loss=0.005100]
eval psnr: 23.49
epoch: 143/199: : 910it [00:27, 33.12it/s, loss=0.005071]
eval psnr: 24.20
epoch: 144/199: : 910it [00:27, 33.24it/s, loss=0.005022]
epoch: 145/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.68
epoch: 145/199: : 910it [00:27, 33.14it/s, loss=0.005031]
epoch: 146/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.12
epoch: 146/199: : 910it [00:27, 33.23it/s, loss=0.004990]
eval psnr: 23.20
epoch: 147/199: : 910it [00:27, 32.99it/s, loss=0.005113]
epoch: 148/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.05
epoch: 148/199: : 910it [00:27, 33.11it/s, loss=0.005150]
epoch: 149/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.51
epoch: 149/199: : 910it [00:27, 33.24it/s, loss=0.005064]
epoch: 150/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.14
epoch: 150/199: : 910it [00:27, 33.24it/s, loss=0.005150]
eval psnr: 23.86
epoch: 151/199: : 910it [00:27, 33.20it/s, loss=0.004962]
epoch: 152/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.18
epoch: 152/199: : 910it [00:27, 33.32it/s, loss=0.004968]
epoch: 153/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.22
epoch: 153/199: : 910it [00:27, 33.25it/s, loss=0.004976]
epoch: 154/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.49
epoch: 154/199: : 910it [00:27, 33.27it/s, loss=0.005125]
eval psnr: 24.26
epoch: 155/199: : 910it [00:27, 33.36it/s, loss=0.004853]
epoch: 156/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.48
epoch: 156/199: : 910it [00:27, 33.36it/s, loss=0.004912]
eval psnr: 24.09
epoch: 157/199: : 910it [00:27, 33.25it/s, loss=0.005070]
epoch: 158/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.79
epoch: 158/199: : 910it [00:27, 33.29it/s, loss=0.005128]
eval psnr: 23.67
epoch: 159/199: : 910it [00:29, 30.86it/s, loss=0.005002]
eval psnr: 24.71
epoch: 160/199: : 910it [00:28, 31.52it/s, loss=0.004990]
epoch: 161/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.73
epoch: 161/199: : 910it [00:28, 31.79it/s, loss=0.004994]
epoch: 162/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.25
epoch: 162/199: : 910it [00:28, 31.89it/s, loss=0.004972]
epoch: 163/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.65
epoch: 163/199: : 910it [00:28, 31.89it/s, loss=0.004945]
eval psnr: 23.45
epoch: 164/199: : 910it [00:28, 31.78it/s, loss=0.004918]
eval psnr: 23.45
epoch: 165/199: : 910it [00:28, 31.95it/s, loss=0.004879]
epoch: 166/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.98
epoch: 166/199: : 910it [00:28, 32.46it/s, loss=0.004839]
eval psnr: 25.25
epoch: 167/199: : 910it [00:27, 33.05it/s, loss=0.004860]
eval psnr: 24.17
epoch: 168/199: : 910it [00:27, 33.12it/s, loss=0.004862]
eval psnr: 24.44
epoch: 169/199: : 910it [00:27, 33.32it/s, loss=0.004767]
eval psnr: 23.42
epoch: 170/199: : 910it [00:27, 33.22it/s, loss=0.005027]
epoch: 171/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.28
epoch: 171/199: : 910it [00:27, 33.31it/s, loss=0.004804]
eval psnr: 23.95
epoch: 172/199: : 910it [00:27, 33.26it/s, loss=0.004777]
epoch: 173/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.48
epoch: 173/199: : 910it [00:27, 33.25it/s, loss=0.004775]
epoch: 174/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.02
epoch: 174/199: : 910it [00:27, 33.18it/s, loss=0.004759]
epoch: 175/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.12
epoch: 175/199: : 910it [00:27, 33.36it/s, loss=0.004934]
epoch: 176/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.34
epoch: 176/199: : 910it [00:27, 33.25it/s, loss=0.004827]
eval psnr: 24.42
epoch: 177/199: : 910it [00:27, 33.17it/s, loss=0.004911]
epoch: 178/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.86
epoch: 178/199: : 910it [00:27, 33.10it/s, loss=0.004868]
epoch: 179/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.49
epoch: 179/199: : 910it [00:27, 32.98it/s, loss=0.004852]
epoch: 180/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.52
epoch: 180/199: : 910it [00:27, 33.25it/s, loss=0.004807]
epoch: 181/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.99
epoch: 181/199: : 910it [00:27, 33.11it/s, loss=0.004686]
epoch: 182/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.73
epoch: 182/199: : 910it [00:27, 33.19it/s, loss=0.004730]
epoch: 183/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.69
epoch: 183/199: : 910it [00:27, 32.94it/s, loss=0.004891]
epoch: 184/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.91
epoch: 184/199: : 910it [00:27, 33.13it/s, loss=0.004856]
epoch: 185/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.83
epoch: 185/199: : 910it [00:27, 33.17it/s, loss=0.004829]
epoch: 186/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.21
epoch: 186/199: : 910it [00:27, 33.08it/s, loss=0.004700]
epoch: 187/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 25.12
epoch: 187/199: : 910it [00:27, 33.19it/s, loss=0.004648]
epoch: 188/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.84
epoch: 188/199: : 910it [00:27, 33.19it/s, loss=0.004688]
epoch: 189/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.50
epoch: 189/199: : 910it [00:27, 33.06it/s, loss=0.004804]
eval psnr: 24.04
epoch: 190/199: : 910it [00:27, 33.26it/s, loss=0.004661]
epoch: 191/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.77
epoch: 191/199: : 910it [00:27, 33.16it/s, loss=0.004627]
eval psnr: 23.71
epoch: 192/199: : 910it [00:27, 33.12it/s, loss=0.004616]
epoch: 193/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.14
epoch: 193/199: : 910it [00:27, 33.18it/s, loss=0.004643]
epoch: 194/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.50
epoch: 194/199: : 910it [00:27, 33.16it/s, loss=0.004673]
epoch: 195/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.56
epoch: 195/199: : 910it [00:27, 33.21it/s, loss=0.004640]
epoch: 196/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.42
epoch: 196/199: : 910it [00:27, 33.11it/s, loss=0.004665]
epoch: 197/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.49
epoch: 197/199: : 910it [00:27, 32.75it/s, loss=0.004638]
eval psnr: 24.15
epoch: 198/199: : 910it [00:28, 32.39it/s, loss=0.004582]
eval psnr: 24.24
epoch: 199/199: : 910it [00:27, 33.14it/s, loss=0.004646]
eval psnr: 24.41
best epoch: 166, psnr: 25.25
"""

log3 = """epoch: 0/199: : 910it [00:40, 22.41it/s, loss=0.018270]
eval psnr: 19.13
epoch: 1/199: : 910it [00:43, 21.15it/s, loss=0.011835]
eval psnr: 19.96
epoch: 2/199: : 910it [00:45, 19.91it/s, loss=0.010935]
epoch: 3/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 20.72
epoch: 3/199: : 910it [00:46, 19.67it/s, loss=0.009754]
eval psnr: 20.99
epoch: 4/199: : 910it [00:46, 19.68it/s, loss=0.008670]
epoch: 5/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 22.18
epoch: 5/199: : 910it [00:46, 19.68it/s, loss=0.007761]
eval psnr: 22.86
epoch: 6/199: : 910it [00:46, 19.66it/s, loss=0.007777]
epoch: 7/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 22.28
epoch: 7/199: : 910it [00:47, 19.32it/s, loss=0.007503]
eval psnr: 21.89
epoch: 8/199: : 910it [00:46, 19.40it/s, loss=0.007009]
eval psnr: 22.31
epoch: 9/199: : 910it [00:46, 19.58it/s, loss=0.007129]
eval psnr: 22.66
epoch: 10/199: : 910it [00:46, 19.53it/s, loss=0.006986]
eval psnr: 22.94
epoch: 11/199: : 910it [00:46, 19.63it/s, loss=0.006749]
eval psnr: 23.36
epoch: 12/199: : 910it [00:46, 19.56it/s, loss=0.006913]
epoch: 13/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.16
epoch: 13/199: : 910it [00:46, 19.59it/s, loss=0.006708]
eval psnr: 23.48
epoch: 14/199: : 910it [00:46, 19.57it/s, loss=0.006868]
epoch: 15/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 15/199: : 910it [00:47, 19.36it/s, loss=0.006712]
epoch: 16/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 16/199: : 910it [00:47, 19.35it/s, loss=0.006664]
epoch: 17/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.44
epoch: 17/199: : 910it [00:47, 19.30it/s, loss=0.006723]
eval psnr: 23.13
epoch: 18/199: : 910it [00:47, 19.29it/s, loss=0.006470]
eval psnr: 23.28
epoch: 19/199: : 910it [00:47, 19.33it/s, loss=0.006474]
eval psnr: 23.48
epoch: 20/199: : 910it [00:46, 19.74it/s, loss=0.006472]
epoch: 21/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.86
epoch: 21/199: : 910it [00:47, 19.28it/s, loss=0.006532]
epoch: 22/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.93
epoch: 22/199: : 910it [00:48, 18.65it/s, loss=0.006525]
epoch: 23/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.27
epoch: 23/199: : 910it [00:47, 19.07it/s, loss=0.006557]
epoch: 24/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.04
epoch: 24/199: : 910it [00:48, 18.95it/s, loss=0.006374]
eval psnr: 23.65
epoch: 25/199: : 910it [00:47, 18.99it/s, loss=0.006633]
epoch: 26/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 26/199: : 910it [00:49, 18.50it/s, loss=0.006403]
epoch: 27/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.87
epoch: 27/199: : 910it [00:51, 17.53it/s, loss=0.006429]
eval psnr: 24.12
epoch: 28/199: : 910it [00:49, 18.45it/s, loss=0.006116]
epoch: 29/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.68
epoch: 29/199: : 910it [00:49, 18.51it/s, loss=0.006305]
epoch: 30/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.24
epoch: 30/199: : 910it [00:49, 18.43it/s, loss=0.006268]
epoch: 31/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.32
epoch: 31/199: : 910it [00:47, 18.98it/s, loss=0.006423]
epoch: 32/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.34
epoch: 32/199: : 910it [00:49, 18.53it/s, loss=0.006372]
epoch: 33/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.64
epoch: 33/199: : 910it [00:48, 18.71it/s, loss=0.006475]
eval psnr: 23.99
epoch: 34/199: : 910it [00:48, 18.60it/s, loss=0.006241]
epoch: 35/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.57
epoch: 35/199: : 910it [00:48, 18.71it/s, loss=0.006405]
epoch: 36/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.75
epoch: 36/199: : 910it [00:49, 18.44it/s, loss=0.006189]
epoch: 37/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.20
epoch: 37/199: : 910it [00:48, 18.58it/s, loss=0.006454]
eval psnr: 23.44
epoch: 38/199: : 910it [00:47, 19.34it/s, loss=0.006197]
eval psnr: 23.86
epoch: 39/199: : 910it [00:47, 19.15it/s, loss=0.006210]
epoch: 40/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.19
epoch: 40/199: : 910it [00:47, 19.27it/s, loss=0.006274]
epoch: 41/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.74
epoch: 41/199: : 910it [00:46, 19.41it/s, loss=0.006208]
epoch: 42/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.58
epoch: 42/199: : 910it [00:47, 19.26it/s, loss=0.006377]
eval psnr: 23.40
epoch: 43/199: : 910it [00:47, 19.35it/s, loss=0.006332]
epoch: 44/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.96
epoch: 44/199: : 910it [00:47, 19.16it/s, loss=0.006264]
eval psnr: 24.46
epoch: 45/199: : 910it [00:47, 19.05it/s, loss=0.006175]
epoch: 46/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.54
epoch: 46/199: : 910it [00:47, 19.18it/s, loss=0.006132]
epoch: 47/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.02
epoch: 47/199: : 910it [00:46, 19.44it/s, loss=0.006299]
eval psnr: 23.70
epoch: 48/199: : 910it [00:46, 19.43it/s, loss=0.006109]
epoch: 49/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.66
epoch: 49/199: : 910it [00:46, 19.42it/s, loss=0.006292]
eval psnr: 23.89
epoch: 50/199: : 910it [00:47, 19.13it/s, loss=0.006085]
epoch: 51/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.74
epoch: 51/199: : 910it [00:47, 19.09it/s, loss=0.006024]
epoch: 52/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.97
epoch: 52/199: : 910it [00:47, 19.22it/s, loss=0.006091]
epoch: 53/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.79
epoch: 53/199: : 910it [00:47, 19.20it/s, loss=0.006125]
epoch: 54/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.51
epoch: 54/199: : 910it [00:47, 19.25it/s, loss=0.006051]
eval psnr: 23.87
epoch: 55/199: : 910it [00:46, 19.40it/s, loss=0.006126]
epoch: 56/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.62
epoch: 56/199: : 910it [00:47, 19.20it/s, loss=0.005913]
eval psnr: 24.10
epoch: 57/199: : 910it [00:48, 18.70it/s, loss=0.006065]
eval psnr: 23.54
epoch: 58/199: : 910it [00:47, 19.15it/s, loss=0.006144]
eval psnr: 23.14
epoch: 59/199: : 910it [00:48, 18.65it/s, loss=0.005805]
epoch: 60/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.38
epoch: 60/199: : 910it [00:48, 18.69it/s, loss=0.005931]
epoch: 61/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.22
epoch: 61/199: : 910it [00:48, 18.84it/s, loss=0.006096]
epoch: 62/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.02
epoch: 62/199: : 910it [00:48, 18.68it/s, loss=0.005983]
epoch: 63/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.25
epoch: 63/199: : 910it [00:49, 18.43it/s, loss=0.006005]
eval psnr: 23.07
epoch: 64/199: : 910it [00:48, 18.94it/s, loss=0.005866]
epoch: 65/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.88
epoch: 65/199: : 910it [00:48, 18.91it/s, loss=0.005945]
eval psnr: 23.71
epoch: 66/199: : 910it [00:48, 18.84it/s, loss=0.005948]
eval psnr: 23.50
epoch: 67/199: : 910it [00:47, 19.16it/s, loss=0.005832]
eval psnr: 23.65
epoch: 68/199: : 910it [00:48, 18.62it/s, loss=0.005818]
epoch: 69/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.92
epoch: 69/199: : 910it [00:48, 18.90it/s, loss=0.005826]
epoch: 70/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.64
epoch: 70/199: : 910it [00:48, 18.65it/s, loss=0.005975]
epoch: 71/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.21
epoch: 71/199: : 910it [00:49, 18.55it/s, loss=0.005936]
epoch: 72/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.97
epoch: 72/199: : 910it [00:47, 19.03it/s, loss=0.005703]
eval psnr: 24.03
epoch: 73/199: : 910it [00:46, 19.54it/s, loss=0.005993]
eval psnr: 24.14
epoch: 74/199: : 910it [00:48, 18.74it/s, loss=0.005795]
epoch: 75/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.86
epoch: 75/199: : 910it [00:46, 19.73it/s, loss=0.005715]
eval psnr: 23.42
epoch: 76/199: : 910it [00:45, 19.91it/s, loss=0.005879]
epoch: 77/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.95
epoch: 77/199: : 910it [00:45, 20.01it/s, loss=0.005961]
epoch: 78/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.91
epoch: 78/199: : 910it [00:46, 19.68it/s, loss=0.005970]
eval psnr: 23.22
epoch: 79/199: : 910it [00:46, 19.66it/s, loss=0.005908]
eval psnr: 23.64
epoch: 80/199: : 910it [00:46, 19.68it/s, loss=0.005822]
epoch: 81/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.19
epoch: 81/199: : 910it [00:46, 19.70it/s, loss=0.005789]
epoch: 82/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.02
epoch: 82/199: : 910it [00:46, 19.67it/s, loss=0.005904]
epoch: 83/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.68
epoch: 83/199: : 910it [00:46, 19.71it/s, loss=0.005752]
eval psnr: 24.22
epoch: 84/199: : 910it [00:47, 19.14it/s, loss=0.005821]
epoch: 85/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.11
epoch: 85/199: : 910it [00:47, 19.13it/s, loss=0.005904]
eval psnr: 24.02
epoch: 86/199: : 910it [00:47, 19.28it/s, loss=0.005757]
epoch: 87/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.58
epoch: 87/199: : 910it [00:46, 19.47it/s, loss=0.005898]
eval psnr: 23.88
epoch: 88/199: : 910it [00:46, 19.39it/s, loss=0.005820]
epoch: 89/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.94
epoch: 89/199: : 910it [00:47, 19.27it/s, loss=0.005659]
eval psnr: 23.77
epoch: 90/199: : 910it [00:47, 19.28it/s, loss=0.005800]
epoch: 91/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.73
epoch: 91/199: : 910it [00:46, 19.42it/s, loss=0.005683]
eval psnr: 23.83
epoch: 92/199: : 910it [00:47, 19.32it/s, loss=0.005644]
epoch: 93/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 93/199: : 910it [00:47, 19.35it/s, loss=0.005867]
epoch: 94/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.13
epoch: 94/199: : 910it [00:47, 19.31it/s, loss=0.005757]
eval psnr: 24.00
epoch: 95/199: : 910it [00:47, 19.22it/s, loss=0.005652]
eval psnr: 23.37
epoch: 96/199: : 910it [00:46, 19.47it/s, loss=0.005683]
eval psnr: 24.62
epoch: 97/199: : 910it [00:46, 19.51it/s, loss=0.005675]
eval psnr: 23.78
epoch: 98/199: : 910it [00:47, 19.31it/s, loss=0.005842]
epoch: 99/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.02
epoch: 99/199: : 910it [00:47, 19.18it/s, loss=0.005810]
eval psnr: 23.35
epoch: 100/199: : 910it [00:47, 19.23it/s, loss=0.005932]
eval psnr: 24.04
epoch: 101/199: : 910it [00:47, 19.10it/s, loss=0.005625]
eval psnr: 24.07
epoch: 102/199: : 910it [00:47, 19.18it/s, loss=0.005704]
epoch: 103/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.22
epoch: 103/199: : 910it [00:47, 19.16it/s, loss=0.005890]
eval psnr: 23.77
epoch: 104/199: : 910it [00:47, 19.24it/s, loss=0.005643]
epoch: 105/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.28
epoch: 105/199: : 910it [00:47, 19.21it/s, loss=0.005601]
epoch: 106/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.81
epoch: 106/199: : 910it [00:47, 19.34it/s, loss=0.005635]
epoch: 107/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.48
epoch: 107/199: : 910it [00:46, 19.42it/s, loss=0.005839]
eval psnr: 24.03
epoch: 108/199: : 910it [00:47, 19.26it/s, loss=0.005618]
eval psnr: 24.06
epoch: 109/199: : 910it [00:47, 19.26it/s, loss=0.005698]
epoch: 110/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.84
epoch: 110/199: : 910it [00:47, 19.24it/s, loss=0.005598]
epoch: 111/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.81
epoch: 111/199: : 910it [00:47, 19.15it/s, loss=0.005625]
eval psnr: 23.79
epoch: 112/199: : 910it [00:46, 19.45it/s, loss=0.005681]
epoch: 113/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.23
epoch: 113/199: : 910it [00:46, 19.61it/s, loss=0.005565]
epoch: 114/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.72
epoch: 114/199: : 910it [00:46, 19.44it/s, loss=0.005532]
epoch: 115/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.70
epoch: 115/199: : 910it [00:47, 19.00it/s, loss=0.005803]
eval psnr: 24.33
epoch: 116/199: : 910it [00:47, 19.21it/s, loss=0.005552]
epoch: 117/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.34
epoch: 117/199: : 910it [01:01, 14.89it/s, loss=0.005524]
eval psnr: 24.78
epoch: 118/199: : 910it [00:47, 19.05it/s, loss=0.005621]
eval psnr: 23.94
epoch: 119/199: : 910it [00:47, 19.15it/s, loss=0.005618]
epoch: 120/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.14
epoch: 120/199: : 910it [00:47, 19.17it/s, loss=0.005640]
epoch: 121/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.34
epoch: 121/199: : 910it [00:47, 19.34it/s, loss=0.005456]
eval psnr: 24.05
epoch: 122/199: : 910it [00:47, 19.31it/s, loss=0.005517]
epoch: 123/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.31
epoch: 123/199: : 910it [00:48, 18.72it/s, loss=0.005557]
eval psnr: 23.85
epoch: 124/199: : 910it [00:47, 19.25it/s, loss=0.005594]
epoch: 125/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.43
epoch: 125/199: : 910it [00:48, 18.74it/s, loss=0.005486]
epoch: 126/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.55
epoch: 126/199: : 910it [00:48, 18.85it/s, loss=0.005402]
epoch: 127/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.31
epoch: 127/199: : 910it [00:48, 18.67it/s, loss=0.005369]
epoch: 128/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.35
epoch: 128/199: : 910it [00:47, 19.09it/s, loss=0.005271]
eval psnr: 24.86
epoch: 129/199: : 910it [00:47, 19.21it/s, loss=0.005372]
epoch: 130/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.10
epoch: 130/199: : 910it [00:47, 19.18it/s, loss=0.005424]
eval psnr: 24.39
epoch: 131/199: : 910it [00:46, 19.52it/s, loss=0.005443]
epoch: 132/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.87
epoch: 132/199: : 910it [00:46, 19.41it/s, loss=0.005534]
epoch: 133/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.22
epoch: 133/199: : 910it [00:46, 19.44it/s, loss=0.005332]
epoch: 134/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.35
epoch: 134/199: : 910it [00:46, 19.42it/s, loss=0.005334]
eval psnr: 24.55
epoch: 135/199: : 910it [00:47, 19.03it/s, loss=0.005346]
epoch: 136/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.75
epoch: 136/199: : 910it [00:49, 18.51it/s, loss=0.005317]
eval psnr: 23.74
epoch: 137/199: : 910it [00:47, 19.01it/s, loss=0.005314]
epoch: 138/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.78
epoch: 138/199: : 910it [00:46, 19.40it/s, loss=0.005341]
eval psnr: 24.70
epoch: 139/199: : 910it [00:46, 19.53it/s, loss=0.005459]
epoch: 140/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.03
epoch: 140/199: : 910it [00:46, 19.55it/s, loss=0.005338]
epoch: 141/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.98
epoch: 141/199: : 910it [00:46, 19.65it/s, loss=0.005415]
epoch: 142/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.01
epoch: 142/199: : 910it [00:47, 19.22it/s, loss=0.005425]
epoch: 143/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.50
epoch: 143/199: : 910it [00:48, 18.77it/s, loss=0.005452]
eval psnr: 24.07
epoch: 144/199: : 910it [00:49, 18.36it/s, loss=0.005291]
eval psnr: 23.66
epoch: 145/199: : 910it [00:49, 18.37it/s, loss=0.005242]
epoch: 146/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.80
epoch: 146/199: : 910it [00:50, 18.18it/s, loss=0.005398]
eval psnr: 24.25
epoch: 147/199: : 910it [00:49, 18.45it/s, loss=0.005369]
epoch: 148/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.38
epoch: 148/199: : 910it [00:49, 18.43it/s, loss=0.005441]
eval psnr: 24.31
epoch: 149/199: : 910it [00:49, 18.31it/s, loss=0.005407]
eval psnr: 24.46
epoch: 150/199: : 910it [00:48, 18.60it/s, loss=0.005197]
epoch: 151/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.94
epoch: 151/199: : 910it [00:49, 18.44it/s, loss=0.005337]
eval psnr: 24.00
epoch: 152/199: : 910it [00:49, 18.29it/s, loss=0.005144]
eval psnr: 24.27
epoch: 153/199: : 910it [00:49, 18.44it/s, loss=0.005361]
epoch: 154/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.95
epoch: 154/199: : 910it [00:49, 18.40it/s, loss=0.005199]
eval psnr: 24.46
epoch: 155/199: : 910it [00:49, 18.55it/s, loss=0.005182]
epoch: 156/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.54
epoch: 156/199: : 910it [00:48, 18.62it/s, loss=0.005307]
eval psnr: 24.00
epoch: 157/199: : 910it [00:48, 18.65it/s, loss=0.005494]
eval psnr: 24.87
epoch: 158/199: : 910it [00:48, 18.60it/s, loss=0.005226]
epoch: 159/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.57
epoch: 159/199: : 910it [00:49, 18.41it/s, loss=0.005294]
epoch: 160/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.65
epoch: 160/199: : 910it [00:49, 18.50it/s, loss=0.005331]
epoch: 161/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.38
epoch: 161/199: : 910it [00:49, 18.56it/s, loss=0.005077]
epoch: 162/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.53
epoch: 162/199: : 910it [00:49, 18.50it/s, loss=0.005331]
eval psnr: 24.14
epoch: 163/199: : 910it [00:48, 18.66it/s, loss=0.005202]
epoch: 164/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.64
epoch: 164/199: : 910it [00:48, 18.74it/s, loss=0.005333]
epoch: 165/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.19
epoch: 165/199: : 910it [00:49, 18.47it/s, loss=0.005379]
eval psnr: 24.35
epoch: 166/199: : 910it [00:49, 18.56it/s, loss=0.005405]
epoch: 167/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.95
epoch: 167/199: : 910it [00:48, 18.69it/s, loss=0.005185]
epoch: 168/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.44
epoch: 168/199: : 910it [00:49, 18.44it/s, loss=0.005160]
epoch: 169/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.61
epoch: 169/199: : 910it [00:49, 18.52it/s, loss=0.005175]
epoch: 170/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.26
epoch: 170/199: : 910it [00:48, 18.57it/s, loss=0.005142]
epoch: 171/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.38
epoch: 171/199: : 910it [00:48, 18.63it/s, loss=0.005266]
eval psnr: 23.48
epoch: 172/199: : 910it [00:49, 18.52it/s, loss=0.005233]
eval psnr: 24.30
epoch: 173/199: : 910it [00:48, 18.75it/s, loss=0.005107]
eval psnr: 23.96
epoch: 174/199: : 910it [00:46, 19.75it/s, loss=0.005189]
eval psnr: 24.44
epoch: 175/199: : 910it [00:45, 19.83it/s, loss=0.005135]
eval psnr: 24.04
epoch: 176/199: : 910it [00:45, 19.82it/s, loss=0.005163]
eval psnr: 23.68
epoch: 177/199: : 910it [00:45, 19.83it/s, loss=0.005392]
epoch: 178/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.99
epoch: 178/199: : 910it [00:45, 19.83it/s, loss=0.005262]
epoch: 179/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.79
epoch: 179/199: : 910it [00:46, 19.77it/s, loss=0.005240]
epoch: 180/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.11
epoch: 180/199: : 910it [00:45, 19.80it/s, loss=0.005265]
epoch: 181/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.34
epoch: 181/199: : 910it [00:45, 19.84it/s, loss=0.004966]
epoch: 182/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.51
epoch: 182/199: : 910it [00:45, 19.88it/s, loss=0.005093]
epoch: 183/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.79
epoch: 183/199: : 910it [00:45, 19.83it/s, loss=0.005257]
eval psnr: 24.10
epoch: 184/199: : 910it [00:46, 19.70it/s, loss=0.005070]
eval psnr: 23.75
epoch: 185/199: : 910it [00:45, 19.81it/s, loss=0.005137]
epoch: 186/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.69
epoch: 186/199: : 910it [00:46, 19.75it/s, loss=0.005178]
eval psnr: 25.08
epoch: 187/199: : 910it [00:46, 19.76it/s, loss=0.005229]
epoch: 188/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.21
epoch: 188/199: : 910it [00:45, 19.82it/s, loss=0.005136]
eval psnr: 24.25
epoch: 189/199: : 910it [00:46, 19.43it/s, loss=0.005140]
eval psnr: 24.59
epoch: 190/199: : 910it [00:46, 19.44it/s, loss=0.005182]
epoch: 191/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.88
epoch: 191/199: : 910it [00:46, 19.74it/s, loss=0.005135]
epoch: 192/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.41
epoch: 192/199: : 910it [00:45, 19.80it/s, loss=0.005060]
eval psnr: 24.16
epoch: 193/199: : 910it [00:46, 19.77it/s, loss=0.005109]
eval psnr: 24.67
epoch: 194/199: : 910it [00:45, 19.80it/s, loss=0.005143]
epoch: 195/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.91
epoch: 195/199: : 910it [00:45, 19.78it/s, loss=0.005155]
eval psnr: 24.07
epoch: 196/199: : 910it [00:45, 19.85it/s, loss=0.005197]
epoch: 197/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.88
epoch: 197/199: : 910it [00:45, 19.85it/s, loss=0.004989]
epoch: 198/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.20
epoch: 198/199: : 910it [00:45, 19.81it/s, loss=0.005129]
eval psnr: 24.35
epoch: 199/199: : 910it [00:46, 19.76it/s, loss=0.005041]
eval psnr: 24.07
best epoch: 186, psnr: 25.08
"""

log4 = """epoch: 0/199: : 910it [01:15, 11.98it/s, loss=0.042029]
eval psnr: 18.93
epoch: 1/199: : 910it [04:16,  3.55it/s, loss=0.013552]
eval psnr: 19.79
epoch: 2/199: : 910it [02:58,  5.11it/s, loss=0.011570]
eval psnr: 20.15
epoch: 3/199: : 910it [04:12,  3.60it/s, loss=0.011102]
eval psnr: 20.54
epoch: 4/199: : 910it [04:06,  3.70it/s, loss=0.009936]
eval psnr: 21.56
epoch: 5/199: : 910it [01:22, 10.97it/s, loss=0.008486]
eval psnr: 21.96
epoch: 6/199: : 910it [01:56,  7.81it/s, loss=0.007913]
eval psnr: 21.39
epoch: 7/199: : 910it [01:38,  9.23it/s, loss=0.007443]
eval psnr: 22.47
epoch: 8/199: : 910it [01:23, 10.87it/s, loss=0.007666]
eval psnr: 22.22
epoch: 9/199: : 910it [01:24, 10.79it/s, loss=0.007393]
eval psnr: 22.47
epoch: 10/199: : 910it [01:39,  9.14it/s, loss=0.007265]
epoch: 11/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.91
epoch: 11/199: : 910it [01:22, 11.07it/s, loss=0.007299]
eval psnr: 22.21
epoch: 12/199: : 910it [02:40,  5.66it/s, loss=0.006997]
eval psnr: 23.07
epoch: 13/199: : 910it [01:21, 11.20it/s, loss=0.006985]
eval psnr: 23.16
epoch: 14/199: : 910it [01:22, 11.09it/s, loss=0.007302]
eval psnr: 22.97
epoch: 15/199: : 910it [01:21, 11.12it/s, loss=0.007168]
epoch: 16/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.27
epoch: 16/199: : 910it [01:22, 11.05it/s, loss=0.006985]
epoch: 17/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.57
epoch: 17/199: : 910it [01:21, 11.10it/s, loss=0.006877]
epoch: 18/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.12
epoch: 18/199: : 910it [01:21, 11.17it/s, loss=0.007058]
eval psnr: 23.14
epoch: 19/199: : 910it [01:21, 11.22it/s, loss=0.006913]
epoch: 20/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.63
epoch: 20/199: : 910it [01:21, 11.12it/s, loss=0.006772]
epoch: 21/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.57
epoch: 21/199: : 910it [01:22, 11.08it/s, loss=0.006703]
epoch: 22/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.64
epoch: 22/199: : 910it [01:22, 11.08it/s, loss=0.006880]
eval psnr: 23.43
epoch: 23/199: : 910it [01:21, 11.10it/s, loss=0.006930]
epoch: 24/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.97
epoch: 24/199: : 910it [01:22, 11.07it/s, loss=0.006629]
eval psnr: 23.19
epoch: 25/199: : 910it [01:22, 11.08it/s, loss=0.006861]
epoch: 26/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.08
epoch: 26/199: : 910it [01:21, 11.12it/s, loss=0.006696]
epoch: 27/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.06
epoch: 27/199: : 910it [01:22, 11.09it/s, loss=0.006753]
eval psnr: 23.29
epoch: 28/199: : 910it [01:22, 11.03it/s, loss=0.006677]
epoch: 29/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.38
epoch: 29/199: : 910it [01:22, 11.08it/s, loss=0.006849]
epoch: 30/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.27
epoch: 30/199: : 910it [01:22, 11.09it/s, loss=0.006656]
epoch: 31/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 31/199: : 910it [01:22, 11.08it/s, loss=0.006654]
epoch: 32/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.12
epoch: 32/199: : 910it [01:22, 11.10it/s, loss=0.006819]
epoch: 33/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.07
epoch: 33/199: : 910it [01:22, 11.09it/s, loss=0.006489]
eval psnr: 23.13
epoch: 34/199: : 910it [01:22, 11.09it/s, loss=0.006571]
epoch: 35/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.10
epoch: 35/199: : 910it [01:21, 11.14it/s, loss=0.006623]
eval psnr: 23.07
epoch: 36/199: : 910it [01:21, 11.21it/s, loss=0.006426]
epoch: 37/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.83
epoch: 37/199: : 910it [01:21, 11.19it/s, loss=0.006249]
eval psnr: 23.55
epoch: 38/199: : 910it [01:21, 11.21it/s, loss=0.006399]
epoch: 39/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.34
epoch: 39/199: : 910it [01:21, 11.17it/s, loss=0.006605]
epoch: 40/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 40/199: : 910it [01:21, 11.11it/s, loss=0.006322]
epoch: 41/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.69
epoch: 41/199: : 910it [01:21, 11.11it/s, loss=0.006527]
epoch: 42/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.67
epoch: 42/199: : 910it [01:22, 11.09it/s, loss=0.006200]
epoch: 43/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.46
epoch: 43/199: : 910it [01:22, 11.09it/s, loss=0.006363]
eval psnr: 23.43
epoch: 44/199: : 910it [01:21, 11.11it/s, loss=0.006292]
epoch: 45/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.16
epoch: 45/199: : 910it [01:21, 11.13it/s, loss=0.006346]
epoch: 46/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.91
epoch: 46/199: : 910it [01:21, 11.11it/s, loss=0.006356]
epoch: 47/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.66
epoch: 47/199: : 910it [01:21, 11.10it/s, loss=0.006245]
eval psnr: 22.48
epoch: 48/199: : 910it [01:26, 10.47it/s, loss=0.006188]
eval psnr: 23.29
epoch: 49/199: : 910it [01:23, 10.96it/s, loss=0.006272]
epoch: 50/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.41
epoch: 50/199: : 910it [01:31,  9.95it/s, loss=0.006253]
epoch: 51/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.93
epoch: 51/199: : 910it [01:38,  9.25it/s, loss=0.006199]
epoch: 52/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.21
epoch: 52/199: : 910it [01:24, 10.79it/s, loss=0.006000]
epoch: 53/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.80
epoch: 53/199: : 910it [01:22, 11.04it/s, loss=0.006216]
eval psnr: 23.21
epoch: 54/199: : 910it [01:23, 10.92it/s, loss=0.005993]
epoch: 55/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.65
epoch: 55/199: : 910it [01:22, 10.97it/s, loss=0.006248]
epoch: 56/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.05
epoch: 56/199: : 910it [01:21, 11.19it/s, loss=0.006035]
eval psnr: 22.88
epoch: 57/199: : 910it [01:21, 11.21it/s, loss=0.006318]
epoch: 58/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.93
epoch: 58/199: : 910it [01:20, 11.25it/s, loss=0.006076]
eval psnr: 23.31
epoch: 59/199: : 910it [01:21, 11.22it/s, loss=0.006150]
epoch: 60/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.88
epoch: 60/199: : 910it [01:20, 11.24it/s, loss=0.006087]
eval psnr: 23.38
epoch: 61/199: : 910it [01:20, 11.24it/s, loss=0.005978]
eval psnr: 22.43
epoch: 62/199: : 910it [01:20, 11.26it/s, loss=0.005948]
eval psnr: 23.60
epoch: 63/199: : 910it [01:21, 11.19it/s, loss=0.006161]
eval psnr: 23.35
epoch: 64/199: : 910it [01:23, 10.86it/s, loss=0.005882]
eval psnr: 23.45
epoch: 65/199: : 910it [01:22, 11.10it/s, loss=0.005988]
epoch: 66/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.44
epoch: 66/199: : 910it [01:20, 11.24it/s, loss=0.005700]
eval psnr: 23.04
epoch: 67/199: : 910it [01:20, 11.25it/s, loss=0.006092]
epoch: 68/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.64
epoch: 68/199: : 910it [01:20, 11.24it/s, loss=0.005855]
epoch: 69/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.19
epoch: 69/199: : 910it [01:20, 11.26it/s, loss=0.005908]
epoch: 70/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.23
epoch: 70/199: : 910it [01:20, 11.35it/s, loss=0.005999]
epoch: 71/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.50
epoch: 71/199: : 910it [01:20, 11.37it/s, loss=0.005988]
eval psnr: 23.73
epoch: 72/199: : 910it [01:20, 11.36it/s, loss=0.005873]
epoch: 73/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.25
epoch: 73/199: : 910it [01:20, 11.27it/s, loss=0.006056]
eval psnr: 23.31
epoch: 74/199: : 910it [01:20, 11.25it/s, loss=0.005725]
eval psnr: 23.34
epoch: 75/199: : 910it [01:20, 11.25it/s, loss=0.005957]
epoch: 76/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 76/199: : 910it [01:20, 11.30it/s, loss=0.005811]
epoch: 77/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 77/199: : 910it [01:20, 11.36it/s, loss=0.005716]
eval psnr: 23.45
epoch: 78/199: : 910it [01:20, 11.35it/s, loss=0.005865]
eval psnr: 23.38
epoch: 79/199: : 910it [01:19, 11.38it/s, loss=0.005794]
epoch: 80/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.19
epoch: 80/199: : 910it [01:20, 11.37it/s, loss=0.005718]
eval psnr: 23.50
epoch: 81/199: : 910it [01:19, 11.38it/s, loss=0.005775]
epoch: 82/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 82/199: : 910it [01:20, 11.29it/s, loss=0.005779]
epoch: 83/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.59
epoch: 83/199: : 910it [01:20, 11.27it/s, loss=0.005596]
epoch: 84/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.28
epoch: 84/199: : 910it [01:20, 11.27it/s, loss=0.005833]
epoch: 85/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.57
epoch: 85/199: : 910it [01:20, 11.27it/s, loss=0.005655]
eval psnr: 22.99
epoch: 86/199: : 910it [01:20, 11.27it/s, loss=0.005741]
epoch: 87/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.20
epoch: 87/199: : 910it [01:20, 11.29it/s, loss=0.005683]
epoch: 88/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.65
epoch: 88/199: : 910it [01:20, 11.26it/s, loss=0.005851]
eval psnr: 23.19
epoch: 89/199: : 910it [01:20, 11.26it/s, loss=0.005605]
epoch: 90/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.25
epoch: 90/199: : 910it [01:20, 11.31it/s, loss=0.005849]
eval psnr: 22.91
epoch: 91/199: : 910it [01:20, 11.31it/s, loss=0.005670]
eval psnr: 23.33
epoch: 92/199: : 910it [01:20, 11.27it/s, loss=0.005682]
eval psnr: 23.66
epoch: 93/199: : 910it [01:20, 11.25it/s, loss=0.005656]
eval psnr: 23.46
epoch: 94/199: : 910it [01:20, 11.24it/s, loss=0.005851]
epoch: 95/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 23.45
epoch: 95/199: : 910it [01:20, 11.27it/s, loss=0.005618]
eval psnr: 24.78
epoch: 96/199: : 910it [01:20, 11.26it/s, loss=0.005604]
eval psnr: 23.78
epoch: 97/199: : 910it [01:20, 11.27it/s, loss=0.005720]
epoch: 98/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 24.00
epoch: 98/199: : 910it [01:20, 11.26it/s, loss=0.005682]
eval psnr: 23.63
epoch: 99/199: : 910it [01:20, 11.27it/s, loss=0.005467]
epoch: 100/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.17
epoch: 100/199: : 910it [01:20, 11.27it/s, loss=0.005553]
eval psnr: 23.78
epoch: 101/199: : 910it [01:20, 11.27it/s, loss=0.005477]
epoch: 102/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.20
epoch: 102/199: : 910it [01:20, 11.28it/s, loss=0.005577]
eval psnr: 23.93
epoch: 103/199: : 910it [01:21, 11.22it/s, loss=0.005492]
eval psnr: 24.00
epoch: 104/199: : 910it [01:20, 11.35it/s, loss=0.005434]
eval psnr: 24.23
epoch: 105/199: : 910it [01:20, 11.28it/s, loss=0.005910]
epoch: 106/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.13
epoch: 106/199: : 910it [01:20, 11.27it/s, loss=0.005651]
eval psnr: 23.66
epoch: 107/199: : 910it [01:20, 11.26it/s, loss=0.005534]
eval psnr: 23.62
epoch: 108/199: : 910it [01:20, 11.26it/s, loss=0.005350]
eval psnr: 23.37
epoch: 109/199: : 910it [01:20, 11.25it/s, loss=0.005683]
epoch: 110/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.56
epoch: 110/199: : 910it [01:19, 11.44it/s, loss=0.005736]
eval psnr: 23.73
epoch: 111/199: : 910it [01:19, 11.42it/s, loss=0.005452]
eval psnr: 23.58
epoch: 112/199: : 910it [01:20, 11.25it/s, loss=0.005599]
eval psnr: 23.42
epoch: 113/199: : 910it [01:20, 11.32it/s, loss=0.005439]
eval psnr: 24.07
epoch: 114/199: : 910it [01:20, 11.32it/s, loss=0.005488]
eval psnr: 23.46
epoch: 115/199: : 910it [01:20, 11.26it/s, loss=0.005493]
epoch: 116/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.53
epoch: 116/199: : 910it [01:21, 11.21it/s, loss=0.005608]
eval psnr: 23.48
epoch: 117/199: : 910it [01:20, 11.29it/s, loss=0.005457]
eval psnr: 23.85
epoch: 118/199: : 910it [01:20, 11.29it/s, loss=0.005450]
eval psnr: 24.07
epoch: 119/199: : 910it [01:20, 11.28it/s, loss=0.005315]
eval psnr: 24.72
epoch: 120/199: : 910it [01:20, 11.28it/s, loss=0.005345]
epoch: 121/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.26
epoch: 121/199: : 910it [01:20, 11.28it/s, loss=0.005495]
epoch: 122/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.27
epoch: 122/199: : 910it [01:20, 11.25it/s, loss=0.005326]
eval psnr: 23.64
epoch: 123/199: : 910it [01:20, 11.28it/s, loss=0.005369]
epoch: 124/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.08
epoch: 124/199: : 910it [01:20, 11.28it/s, loss=0.005448]
epoch: 125/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.65
epoch: 125/199: : 910it [01:20, 11.26it/s, loss=0.005380]
epoch: 126/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.93
epoch: 126/199: : 910it [01:28, 10.26it/s, loss=0.005404]
epoch: 127/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.97
epoch: 127/199: : 910it [01:24, 10.80it/s, loss=0.005549]
eval psnr: 23.51
epoch: 128/199: : 910it [01:21, 11.23it/s, loss=0.005377]
epoch: 129/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.91
epoch: 129/199: : 910it [01:20, 11.25it/s, loss=0.005426]
eval psnr: 23.65
epoch: 130/199: : 910it [01:21, 11.22it/s, loss=0.005334]
epoch: 131/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.24
epoch: 131/199: : 910it [01:20, 11.25it/s, loss=0.005236]
eval psnr: 23.69
epoch: 132/199: : 910it [01:20, 11.25it/s, loss=0.005357]
eval psnr: 23.70
epoch: 133/199: : 910it [01:20, 11.35it/s, loss=0.005461]
epoch: 134/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.58
epoch: 134/199: : 910it [01:19, 11.40it/s, loss=0.005427]
eval psnr: 23.96
epoch: 135/199: : 910it [01:20, 11.37it/s, loss=0.005390]
epoch: 136/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.26
epoch: 136/199: : 910it [01:20, 11.24it/s, loss=0.005414]
eval psnr: 24.48
epoch: 137/199: : 910it [01:21, 11.14it/s, loss=0.005445]
eval psnr: 23.71
epoch: 138/199: : 910it [01:22, 11.08it/s, loss=0.005418]
eval psnr: 24.34
epoch: 139/199: : 910it [01:20, 11.25it/s, loss=0.005410]
eval psnr: 24.03
epoch: 140/199: : 910it [01:20, 11.25it/s, loss=0.005335]
eval psnr: 23.69
epoch: 141/199: : 910it [01:20, 11.25it/s, loss=0.005288]
eval psnr: 23.48
epoch: 142/199: : 910it [01:20, 11.36it/s, loss=0.005399]
eval psnr: 23.62
epoch: 143/199: : 910it [01:21, 11.22it/s, loss=0.005401]
eval psnr: 23.89
epoch: 144/199: : 910it [01:21, 11.22it/s, loss=0.005443]
epoch: 145/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.76
epoch: 145/199: : 910it [01:21, 11.22it/s, loss=0.005232]
eval psnr: 24.15
epoch: 146/199: : 910it [01:21, 11.23it/s, loss=0.005287]
eval psnr: 23.36
epoch: 147/199: : 910it [01:21, 11.17it/s, loss=0.005259]
eval psnr: 23.87
epoch: 148/199: : 910it [01:21, 11.22it/s, loss=0.005314]
eval psnr: 23.53
epoch: 149/199: : 910it [01:20, 11.24it/s, loss=0.005255]
epoch: 150/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.98
epoch: 150/199: : 910it [01:21, 11.23it/s, loss=0.005114]
eval psnr: 24.14
epoch: 151/199: : 910it [01:21, 11.23it/s, loss=0.005308]
epoch: 152/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.30
epoch: 152/199: : 910it [01:21, 11.23it/s, loss=0.005505]
epoch: 153/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.49
epoch: 153/199: : 910it [01:20, 11.25it/s, loss=0.005277]
eval psnr: 23.57
epoch: 154/199: : 910it [01:21, 11.23it/s, loss=0.005239]
epoch: 155/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.94
epoch: 155/199: : 910it [01:21, 11.22it/s, loss=0.005187]
eval psnr: 24.12
epoch: 156/199: : 910it [01:20, 11.26it/s, loss=0.005146]
epoch: 157/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.83
epoch: 157/199: : 910it [01:20, 11.29it/s, loss=0.005349]
epoch: 158/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.11
epoch: 158/199: : 910it [01:21, 11.23it/s, loss=0.005061]
epoch: 159/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.28
epoch: 159/199: : 910it [01:20, 11.24it/s, loss=0.005207]
eval psnr: 23.70
epoch: 160/199: : 910it [01:20, 11.25it/s, loss=0.005411]
eval psnr: 23.95
epoch: 161/199: : 910it [01:20, 11.25it/s, loss=0.005283]
eval psnr: 24.18
epoch: 162/199: : 910it [01:20, 11.25it/s, loss=0.005116]
eval psnr: 24.10
epoch: 163/199: : 910it [01:20, 11.27it/s, loss=0.005328]
epoch: 164/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.30
epoch: 164/199: : 910it [01:21, 11.23it/s, loss=0.005166]
eval psnr: 23.81
epoch: 165/199: : 910it [01:20, 11.25it/s, loss=0.005132]
epoch: 166/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.57
epoch: 166/199: : 910it [01:21, 11.19it/s, loss=0.005082]
eval psnr: 24.45
epoch: 167/199: : 910it [01:22, 11.08it/s, loss=0.005148]
eval psnr: 23.70
epoch: 168/199: : 910it [01:21, 11.11it/s, loss=0.005200]
epoch: 169/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.98
epoch: 169/199: : 910it [01:21, 11.23it/s, loss=0.005177]
eval psnr: 23.70
epoch: 170/199: : 910it [01:20, 11.26it/s, loss=0.005181]
epoch: 171/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.29
epoch: 171/199: : 910it [01:20, 11.24it/s, loss=0.005333]
eval psnr: 23.61
epoch: 172/199: : 910it [01:20, 11.27it/s, loss=0.005239]
eval psnr: 24.40
epoch: 173/199: : 910it [01:21, 11.19it/s, loss=0.005060]
epoch: 174/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.86
epoch: 174/199: : 910it [01:21, 11.22it/s, loss=0.005065]
eval psnr: 23.69
epoch: 175/199: : 910it [01:21, 11.16it/s, loss=0.005279]
epoch: 176/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.10
epoch: 176/199: : 910it [01:22, 11.00it/s, loss=0.005031]
epoch: 177/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.18
epoch: 177/199: : 910it [01:21, 11.19it/s, loss=0.005053]
eval psnr: 23.91
epoch: 178/199: : 910it [01:20, 11.24it/s, loss=0.005156]
epoch: 179/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.92
epoch: 179/199: : 910it [01:21, 11.23it/s, loss=0.005171]
eval psnr: 23.90
epoch: 180/199: : 910it [01:20, 11.24it/s, loss=0.005223]
eval psnr: 24.47
epoch: 181/199: : 910it [01:20, 11.24it/s, loss=0.004999]
eval psnr: 24.46
epoch: 182/199: : 910it [01:21, 11.21it/s, loss=0.005102]
eval psnr: 24.51
epoch: 183/199: : 910it [01:20, 11.24it/s, loss=0.005088]
epoch: 184/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.29
epoch: 184/199: : 910it [01:20, 11.25it/s, loss=0.004989]
epoch: 185/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.95
epoch: 185/199: : 910it [01:20, 11.24it/s, loss=0.005132]
eval psnr: 24.77
epoch: 186/199: : 910it [01:21, 11.21it/s, loss=0.005137]
eval psnr: 23.46
epoch: 187/199: : 910it [01:20, 11.30it/s, loss=0.005071]
eval psnr: 24.13
epoch: 188/199: : 910it [01:20, 11.32it/s, loss=0.004991]
eval psnr: 23.97
epoch: 189/199: : 910it [01:20, 11.25it/s, loss=0.005261]
eval psnr: 24.08
epoch: 190/199: : 910it [01:20, 11.25it/s, loss=0.005081]
eval psnr: 23.98
epoch: 191/199: : 910it [01:21, 11.15it/s, loss=0.005085]
epoch: 192/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 23.90
epoch: 192/199: : 910it [01:20, 11.26it/s, loss=0.005076]
epoch: 193/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.59
epoch: 193/199: : 910it [01:21, 11.22it/s, loss=0.005067]
epoch: 194/199:   0%|                                   | 0/896 [00:00<?, ?it/s]eval psnr: 24.07
epoch: 194/199: : 910it [01:20, 11.24it/s, loss=0.005001]
eval psnr: 24.03
epoch: 195/199: : 910it [01:21, 11.19it/s, loss=0.005136]
eval psnr: 24.38
epoch: 196/199: : 910it [01:21, 11.23it/s, loss=0.004932]
eval psnr: 23.29
epoch: 197/199: : 910it [01:21, 11.23it/s, loss=0.005274]
eval psnr: 23.60
epoch: 198/199: : 910it [01:21, 11.22it/s, loss=0.004976]
eval psnr: 24.07
epoch: 199/199: : 910it [01:21, 11.22it/s, loss=0.004985]
eval psnr: 24.03
best epoch: 95, psnr: 24.78
"""

log5 = """epoch: 0/199: : 910it [13:56,  1.09it/s, loss=0.017342]
eval psnr: 21.28
epoch: 1/199: : 910it [12:48,  1.18it/s, loss=0.008541]
eval psnr: 21.24
epoch: 2/199: : 910it [10:02,  1.51it/s, loss=0.008055]
eval psnr: 21.49
epoch: 3/199: : 910it [17:15,  1.14s/it, loss=0.007592]
eval psnr: 21.93
epoch: 4/199: : 910it [16:57,  1.12s/it, loss=0.007450]
eval psnr: 21.74
epoch: 5/199: : 910it [17:11,  1.13s/it, loss=0.007475]
eval psnr: 22.02
epoch: 6/199: : 910it [17:20,  1.14s/it, loss=0.007181]
eval psnr: 22.27
epoch: 7/199: : 910it [17:05,  1.13s/it, loss=0.007235]
epoch: 8/199:   0%|                                     | 0/896 [00:00<?, ?it/s]eval psnr: 22.04
epoch: 8/199: : 910it [17:01,  1.12s/it, loss=0.006950]
eval psnr: 21.94
epoch: 9/199: : 910it [16:59,  1.12s/it, loss=0.007009]
epoch: 10/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 21.87
epoch: 10/199: : 910it [17:02,  1.12s/it, loss=0.007057]
eval psnr: 22.16
epoch: 11/199: : 910it [16:55,  1.12s/it, loss=0.007041]
eval psnr: 22.33
epoch: 12/199: : 910it [16:59,  1.12s/it, loss=0.006887]
epoch: 13/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.15
epoch: 13/199: : 910it [17:05,  1.13s/it, loss=0.006756]
eval psnr: 22.88
epoch: 14/199: : 910it [16:59,  1.12s/it, loss=0.006582]
eval psnr: 22.49
epoch: 15/199: : 910it [17:01,  1.12s/it, loss=0.006690]
epoch: 16/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.56
epoch: 16/199: : 910it [16:58,  1.12s/it, loss=0.006580]
eval psnr: 22.50
epoch: 17/199: : 910it [17:07,  1.13s/it, loss=0.006443]
eval psnr: 23.21
epoch: 18/199: : 910it [17:06,  1.13s/it, loss=0.006619]
eval psnr: 22.61
epoch: 19/199: : 910it [17:00,  1.12s/it, loss=0.006458]
eval psnr: 22.81
epoch: 20/199: : 910it [17:04,  1.13s/it, loss=0.006545]
eval psnr: 22.64
epoch: 21/199: : 910it [16:33,  1.09s/it, loss=0.006388]
eval psnr: 22.34
epoch: 22/199: : 910it [16:57,  1.12s/it, loss=0.006544]
epoch: 23/199:   0%|                                    | 0/896 [00:00<?, ?it/s]eval psnr: 22.02
epoch: 23/199: : 910it [17:21,  1.14s/it, loss=0.006259]
eval psnr: 22.63
epoch: 24/199: : 910it [17:08,  1.13s/it, loss=0.006184]
eval psnr: 22.46"""

log6 = """epoch: 0/199: : 910it [00:32, 28.35it/s, loss=0.050327]
eval psnr: 15.82
epoch: 1/199: : 910it [00:17, 52.39it/s, loss=0.025327]
eval psnr: 16.77
epoch: 2/199: : 910it [00:16, 53.95it/s, loss=0.021106]
eval psnr: 17.40
epoch: 3/199: : 910it [00:16, 54.72it/s, loss=0.017692]
eval psnr: 17.96
epoch: 4/199: : 910it [00:16, 55.24it/s, loss=0.016271]
eval psnr: 18.23
epoch: 5/199: : 910it [00:16, 54.93it/s, loss=0.014928]
eval psnr: 18.41
epoch: 6/199: : 910it [00:16, 55.37it/s, loss=0.013835]
eval psnr: 18.47
epoch: 7/199: : 910it [00:16, 55.43it/s, loss=0.013069]
eval psnr: 19.43
epoch: 8/199: : 910it [00:16, 55.03it/s, loss=0.012323]
eval psnr: 19.29
epoch: 9/199: : 910it [00:16, 54.86it/s, loss=0.011394]
eval psnr: 20.04
epoch: 10/199: : 910it [00:16, 54.98it/s, loss=0.011149]
eval psnr: 20.12
epoch: 11/199: : 910it [00:16, 54.98it/s, loss=0.011029]
eval psnr: 20.27
epoch: 12/199: : 910it [00:16, 54.42it/s, loss=0.010473]
eval psnr: 20.25
epoch: 13/199: : 910it [00:16, 55.01it/s, loss=0.010240]
eval psnr: 20.49
epoch: 14/199: : 910it [00:16, 54.82it/s, loss=0.009963]
eval psnr: 19.80
epoch: 15/199: : 910it [00:16, 54.73it/s, loss=0.009916]
eval psnr: 20.48
epoch: 16/199: : 910it [00:16, 54.42it/s, loss=0.009677]
eval psnr: 20.49
epoch: 17/199: : 910it [00:16, 54.56it/s, loss=0.009273]
eval psnr: 20.52
epoch: 18/199: : 910it [00:16, 54.70it/s, loss=0.008939]
eval psnr: 20.62
epoch: 19/199: : 910it [00:16, 54.87it/s, loss=0.008779]
eval psnr: 20.54
epoch: 20/199: : 910it [00:16, 54.83it/s, loss=0.008629]
eval psnr: 20.95
epoch: 21/199: : 910it [00:16, 54.59it/s, loss=0.008710]
eval psnr: 21.12
epoch: 22/199: : 910it [00:17, 52.87it/s, loss=0.008254]
eval psnr: 20.91
epoch: 23/199: : 910it [00:17, 52.26it/s, loss=0.008109]
eval psnr: 21.16
epoch: 24/199: : 910it [00:17, 52.09it/s, loss=0.008280]
eval psnr: 20.87
epoch: 25/199: : 910it [00:16, 54.27it/s, loss=0.007994]
eval psnr: 20.93
epoch: 26/199: : 910it [00:16, 54.59it/s, loss=0.007947]
eval psnr: 21.90
epoch: 27/199: : 910it [00:16, 54.58it/s, loss=0.007776]
eval psnr: 21.33
epoch: 28/199: : 910it [00:17, 50.64it/s, loss=0.007788]
eval psnr: 21.24
epoch: 29/199: : 910it [00:16, 54.36it/s, loss=0.007703]
eval psnr: 21.65
epoch: 30/199: : 910it [00:16, 54.95it/s, loss=0.007510]
eval psnr: 22.06
epoch: 31/199: : 910it [00:16, 55.11it/s, loss=0.007459]
eval psnr: 21.65
epoch: 32/199: : 910it [00:16, 55.10it/s, loss=0.007380]
eval psnr: 21.98
epoch: 33/199: : 910it [00:16, 54.96it/s, loss=0.007300]
eval psnr: 21.33
epoch: 34/199: : 910it [00:17, 53.51it/s, loss=0.007495]
eval psnr: 21.25
epoch: 35/199: : 910it [00:16, 53.83it/s, loss=0.007331]
eval psnr: 22.14
epoch: 36/199: : 910it [00:16, 55.13it/s, loss=0.007226]
eval psnr: 21.91
epoch: 37/199: : 910it [00:16, 55.21it/s, loss=0.007012]
eval psnr: 22.37
epoch: 38/199: : 910it [00:17, 52.19it/s, loss=0.006999]
eval psnr: 21.88
epoch: 39/199: : 910it [00:16, 54.92it/s, loss=0.007119]
eval psnr: 22.39
epoch: 40/199: : 910it [00:16, 55.26it/s, loss=0.006885]
eval psnr: 22.38
epoch: 41/199: : 910it [00:16, 55.43it/s, loss=0.006796]
eval psnr: 22.26
epoch: 42/199: : 910it [00:16, 54.68it/s, loss=0.006931]
eval psnr: 22.64
epoch: 43/199: : 910it [00:16, 54.94it/s, loss=0.006816]
eval psnr: 21.89
epoch: 44/199: : 910it [00:16, 54.89it/s, loss=0.006931]
eval psnr: 22.13
epoch: 45/199: : 910it [00:16, 54.22it/s, loss=0.006773]
eval psnr: 22.40
epoch: 46/199: : 910it [00:17, 52.51it/s, loss=0.006586]
eval psnr: 22.52
epoch: 47/199: : 910it [00:17, 52.83it/s, loss=0.006750]
eval psnr: 22.49
epoch: 48/199: : 910it [00:17, 51.30it/s, loss=0.006721]
eval psnr: 22.65
epoch: 49/199: : 910it [00:16, 55.77it/s, loss=0.006735]
eval psnr: 22.73
epoch: 50/199: : 910it [00:16, 55.89it/s, loss=0.006689]
eval psnr: 22.08
epoch: 51/199: : 910it [00:16, 56.05it/s, loss=0.006766]
eval psnr: 22.13
epoch: 52/199: : 910it [00:16, 55.92it/s, loss=0.006638]
eval psnr: 22.94
epoch: 53/199: : 910it [00:16, 55.92it/s, loss=0.006623]
eval psnr: 21.73
epoch: 54/199: : 910it [00:16, 56.14it/s, loss=0.006451]
eval psnr: 22.48
epoch: 55/199: : 910it [00:16, 55.44it/s, loss=0.006383]
eval psnr: 22.70
epoch: 56/199: : 910it [00:16, 56.18it/s, loss=0.006435]
eval psnr: 22.72
epoch: 57/199: : 910it [00:16, 55.98it/s, loss=0.006534]
eval psnr: 22.79
epoch: 58/199: : 910it [00:16, 56.06it/s, loss=0.006437]
eval psnr: 22.23
epoch: 59/199: : 910it [00:16, 56.02it/s, loss=0.006335]
eval psnr: 22.78
epoch: 60/199: : 910it [00:16, 56.10it/s, loss=0.006506]
eval psnr: 23.41
epoch: 61/199: : 910it [00:16, 56.25it/s, loss=0.006139]
eval psnr: 23.41
epoch: 62/199: : 910it [00:16, 55.88it/s, loss=0.006161]
eval psnr: 22.44
epoch: 63/199: : 910it [00:16, 55.75it/s, loss=0.006364]
eval psnr: 22.66
epoch: 64/199: : 910it [00:16, 55.95it/s, loss=0.006346]
eval psnr: 22.81
epoch: 65/199: : 910it [00:16, 55.34it/s, loss=0.006219]
eval psnr: 22.63
epoch: 66/199: : 910it [00:16, 56.06it/s, loss=0.006158]
eval psnr: 23.09
epoch: 67/199: : 910it [00:16, 55.83it/s, loss=0.006228]
eval psnr: 22.76
epoch: 68/199: : 910it [00:16, 55.93it/s, loss=0.006212]
eval psnr: 22.81
epoch: 69/199: : 910it [00:16, 56.00it/s, loss=0.006246]
eval psnr: 22.38
epoch: 70/199: : 910it [00:16, 54.05it/s, loss=0.006177]
eval psnr: 22.73
epoch: 71/199: : 910it [00:16, 53.69it/s, loss=0.006175]
eval psnr: 22.89
epoch: 72/199: : 910it [00:16, 54.60it/s, loss=0.006247]
eval psnr: 22.71
epoch: 73/199: : 910it [00:16, 55.47it/s, loss=0.006050]
eval psnr: 22.38
epoch: 74/199: : 910it [00:16, 55.53it/s, loss=0.006115]
eval psnr: 23.19
epoch: 75/199: : 910it [00:16, 56.14it/s, loss=0.006202]
eval psnr: 22.67
epoch: 76/199: : 910it [00:16, 56.05it/s, loss=0.005941]
eval psnr: 23.51
epoch: 77/199: : 910it [00:16, 56.12it/s, loss=0.005987]
eval psnr: 23.40
epoch: 78/199: : 910it [00:16, 56.28it/s, loss=0.006150]
eval psnr: 22.98
epoch: 79/199: : 910it [00:16, 56.14it/s, loss=0.005839]
eval psnr: 23.56
epoch: 80/199: : 910it [00:16, 56.09it/s, loss=0.006028]
eval psnr: 22.72
epoch: 81/199: : 910it [00:16, 56.15it/s, loss=0.005858]
eval psnr: 23.69
epoch: 82/199: : 910it [00:16, 56.03it/s, loss=0.005953]
eval psnr: 23.30
epoch: 83/199: : 910it [00:16, 55.73it/s, loss=0.006121]
eval psnr: 23.25
epoch: 84/199: : 910it [00:16, 55.84it/s, loss=0.006171]
eval psnr: 22.87
epoch: 85/199: : 910it [00:16, 56.31it/s, loss=0.006283]
eval psnr: 23.22
epoch: 86/199: : 910it [00:16, 55.86it/s, loss=0.005916]
eval psnr: 22.86
epoch: 87/199: : 910it [00:16, 55.88it/s, loss=0.005964]
eval psnr: 23.12
epoch: 88/199: : 910it [00:16, 56.00it/s, loss=0.005849]
eval psnr: 23.20
epoch: 89/199: : 910it [00:16, 56.01it/s, loss=0.005929]
eval psnr: 23.06
epoch: 90/199: : 910it [00:16, 55.72it/s, loss=0.005918]
eval psnr: 22.60
epoch: 91/199: : 910it [00:16, 56.04it/s, loss=0.005652]
eval psnr: 23.04
epoch: 92/199: : 910it [00:16, 55.84it/s, loss=0.005917]
eval psnr: 22.64
epoch: 93/199: : 910it [00:16, 56.10it/s, loss=0.005914]
eval psnr: 23.41
epoch: 94/199: : 910it [00:16, 54.12it/s, loss=0.005849]
eval psnr: 23.42
epoch: 95/199: : 910it [00:16, 54.01it/s, loss=0.006036]
eval psnr: 22.63
epoch: 96/199: : 910it [00:16, 53.84it/s, loss=0.005920]
eval psnr: 22.39
epoch: 97/199: : 910it [00:16, 55.95it/s, loss=0.005862]
eval psnr: 23.85
epoch: 98/199: : 910it [00:16, 56.06it/s, loss=0.005727]
eval psnr: 23.08
epoch: 99/199: : 910it [00:16, 56.15it/s, loss=0.005641]
eval psnr: 23.46
epoch: 100/199: : 910it [00:16, 56.28it/s, loss=0.005773]
eval psnr: 23.11
epoch: 101/199: : 910it [00:16, 56.01it/s, loss=0.005877]
eval psnr: 23.18
epoch: 102/199: : 910it [00:16, 55.92it/s, loss=0.005708]
eval psnr: 23.07
epoch: 103/199: : 910it [00:16, 56.02it/s, loss=0.005606]
eval psnr: 23.20
epoch: 104/199: : 910it [00:16, 56.12it/s, loss=0.005668]
eval psnr: 23.41
epoch: 105/199: : 910it [00:16, 55.98it/s, loss=0.005767]
eval psnr: 23.18
epoch: 106/199: : 910it [00:16, 56.07it/s, loss=0.005758]
eval psnr: 23.14
epoch: 107/199: : 910it [00:16, 55.86it/s, loss=0.005722]
eval psnr: 23.39
epoch: 108/199: : 910it [00:16, 56.09it/s, loss=0.005667]
eval psnr: 23.30
epoch: 109/199: : 910it [00:16, 56.13it/s, loss=0.005751]
eval psnr: 22.82
epoch: 110/199: : 910it [00:16, 56.09it/s, loss=0.005692]
eval psnr: 23.28
epoch: 111/199: : 910it [00:16, 55.93it/s, loss=0.005558]
eval psnr: 22.67
epoch: 112/199: : 910it [00:16, 56.20it/s, loss=0.005701]
eval psnr: 23.21
epoch: 113/199: : 910it [00:16, 56.16it/s, loss=0.005559]
eval psnr: 23.46
epoch: 114/199: : 910it [00:16, 55.87it/s, loss=0.005734]
eval psnr: 23.20
epoch: 115/199: : 910it [00:16, 56.12it/s, loss=0.005688]
eval psnr: 22.88
epoch: 116/199: : 910it [00:16, 56.03it/s, loss=0.005639]
eval psnr: 23.14
epoch: 117/199: : 910it [00:16, 56.11it/s, loss=0.005474]
eval psnr: 23.33
epoch: 118/199: : 910it [00:16, 54.80it/s, loss=0.005680]
eval psnr: 23.23
epoch: 119/199: : 910it [00:17, 53.34it/s, loss=0.005623]
eval psnr: 23.97
epoch: 120/199: : 910it [00:16, 53.56it/s, loss=0.005676]
eval psnr: 23.56
epoch: 121/199: : 910it [00:16, 55.19it/s, loss=0.005631]
eval psnr: 23.12
epoch: 122/199: : 910it [00:16, 56.14it/s, loss=0.005779]
eval psnr: 23.58
epoch: 123/199: : 910it [00:16, 56.12it/s, loss=0.005527]
eval psnr: 23.36
epoch: 124/199: : 910it [00:16, 56.11it/s, loss=0.005565]
eval psnr: 23.56
epoch: 125/199: : 910it [00:16, 56.18it/s, loss=0.005501]
eval psnr: 23.82
epoch: 126/199: : 910it [00:16, 55.95it/s, loss=0.005491]
eval psnr: 24.03
epoch: 127/199: : 910it [00:16, 56.20it/s, loss=0.005581]
eval psnr: 23.44
epoch: 128/199: : 910it [00:16, 56.22it/s, loss=0.005512]
eval psnr: 23.24
epoch: 129/199: : 910it [00:16, 56.08it/s, loss=0.005627]
eval psnr: 23.28
epoch: 130/199: : 910it [00:16, 56.22it/s, loss=0.005469]
eval psnr: 23.36
epoch: 131/199: : 910it [00:16, 56.19it/s, loss=0.005615]
eval psnr: 23.72
epoch: 132/199: : 910it [00:16, 56.32it/s, loss=0.005418]
eval psnr: 23.10
epoch: 133/199: : 910it [00:16, 56.26it/s, loss=0.005583]
eval psnr: 23.21
epoch: 134/199: : 910it [00:16, 56.08it/s, loss=0.005526]
eval psnr: 23.75
epoch: 135/199: : 910it [00:16, 55.88it/s, loss=0.005503]
eval psnr: 23.99
epoch: 136/199: : 910it [00:16, 56.14it/s, loss=0.005407]
eval psnr: 23.83
epoch: 137/199: : 910it [00:16, 55.80it/s, loss=0.005460]
eval psnr: 24.01
epoch: 138/199: : 910it [00:16, 56.24it/s, loss=0.005665]
eval psnr: 23.48
epoch: 139/199: : 910it [00:16, 55.92it/s, loss=0.005666]
eval psnr: 23.62
epoch: 140/199: : 910it [00:16, 55.88it/s, loss=0.005434]
eval psnr: 23.45
epoch: 141/199: : 910it [00:16, 53.65it/s, loss=0.005480]
eval psnr: 23.45
epoch: 142/199: : 910it [00:16, 53.97it/s, loss=0.005488]
eval psnr: 23.68
epoch: 143/199: : 910it [00:16, 54.30it/s, loss=0.005585]
eval psnr: 23.07
epoch: 144/199: : 910it [00:16, 55.87it/s, loss=0.005368]
eval psnr: 23.13
epoch: 145/199: : 910it [00:16, 55.90it/s, loss=0.005396]
eval psnr: 23.42
epoch: 146/199: : 910it [00:16, 56.22it/s, loss=0.005382]
eval psnr: 23.42
epoch: 147/199: : 910it [00:16, 55.95it/s, loss=0.005461]
eval psnr: 23.50
epoch: 148/199: : 910it [00:16, 55.91it/s, loss=0.005268]
eval psnr: 24.07
epoch: 149/199: : 910it [00:16, 55.69it/s, loss=0.005447]
eval psnr: 23.20
epoch: 150/199: : 910it [00:16, 56.18it/s, loss=0.005339]
eval psnr: 23.68
epoch: 151/199: : 910it [00:16, 55.94it/s, loss=0.005367]
eval psnr: 24.40
epoch: 152/199: : 910it [00:16, 55.85it/s, loss=0.005492]
eval psnr: 23.77
epoch: 153/199: : 910it [00:16, 55.90it/s, loss=0.005541]
eval psnr: 23.10
epoch: 154/199: : 910it [00:16, 55.99it/s, loss=0.005337]
eval psnr: 23.53
epoch: 155/199: : 910it [00:16, 55.58it/s, loss=0.005416]
eval psnr: 23.52
epoch: 156/199: : 910it [00:16, 56.01it/s, loss=0.005369]
eval psnr: 23.76
epoch: 157/199: : 910it [00:16, 55.87it/s, loss=0.005538]
eval psnr: 23.30
epoch: 158/199: : 910it [00:16, 56.05it/s, loss=0.005429]
eval psnr: 23.25
epoch: 159/199: : 910it [00:16, 56.01it/s, loss=0.005249]
eval psnr: 23.87
epoch: 160/199: : 910it [00:16, 55.93it/s, loss=0.005356]
eval psnr: 23.71
epoch: 161/199: : 910it [00:16, 55.95it/s, loss=0.005392]
eval psnr: 23.36
epoch: 162/199: : 910it [00:16, 55.76it/s, loss=0.005265]
eval psnr: 23.35
epoch: 163/199: : 910it [00:16, 56.07it/s, loss=0.005266]
eval psnr: 23.54
epoch: 164/199: : 910it [00:16, 55.75it/s, loss=0.005306]
eval psnr: 24.00
epoch: 165/199: : 910it [00:16, 55.69it/s, loss=0.005183]
eval psnr: 23.88
epoch: 166/199: : 910it [00:16, 53.92it/s, loss=0.005268]
eval psnr: 23.41
epoch: 167/199: : 910it [00:16, 54.47it/s, loss=0.005349]
eval psnr: 23.59
epoch: 168/199: : 910it [00:16, 54.76it/s, loss=0.005226]
eval psnr: 23.64
epoch: 169/199: : 910it [00:16, 56.28it/s, loss=0.005210]
eval psnr: 23.11
epoch: 170/199: : 910it [00:16, 56.15it/s, loss=0.005260]
eval psnr: 23.93
epoch: 171/199: : 910it [00:16, 56.07it/s, loss=0.005290]
eval psnr: 23.77
epoch: 172/199: : 910it [00:16, 56.06it/s, loss=0.005313]
eval psnr: 24.18
epoch: 173/199: : 910it [00:16, 56.05it/s, loss=0.005288]
eval psnr: 23.74
epoch: 174/199: : 910it [00:16, 55.67it/s, loss=0.005140]
eval psnr: 24.25
epoch: 175/199: : 910it [00:16, 55.87it/s, loss=0.005252]
eval psnr: 23.38
epoch: 176/199: : 910it [00:16, 55.96it/s, loss=0.005221]
eval psnr: 24.19
epoch: 177/199: : 910it [00:16, 55.96it/s, loss=0.005282]
eval psnr: 24.03
epoch: 178/199: : 910it [00:16, 56.07it/s, loss=0.005304]
eval psnr: 24.40
epoch: 179/199: : 910it [00:16, 55.95it/s, loss=0.005160]
eval psnr: 23.58
epoch: 180/199: : 910it [00:16, 55.83it/s, loss=0.005105]
eval psnr: 23.80
epoch: 181/199: : 910it [00:16, 55.87it/s, loss=0.005346]
eval psnr: 23.90
epoch: 182/199: : 910it [00:16, 56.12it/s, loss=0.005114]
eval psnr: 23.81
epoch: 183/199: : 910it [00:16, 56.01it/s, loss=0.005311]
eval psnr: 23.72
epoch: 184/199: : 910it [00:16, 55.98it/s, loss=0.005187]
eval psnr: 23.19
epoch: 185/199: : 910it [00:16, 55.83it/s, loss=0.005370]
eval psnr: 24.12
epoch: 186/199: : 910it [00:16, 55.88it/s, loss=0.005193]
eval psnr: 23.50
epoch: 187/199: : 910it [00:16, 56.04it/s, loss=0.005112]
eval psnr: 23.52
epoch: 188/199: : 910it [00:16, 55.98it/s, loss=0.005187]
eval psnr: 23.62
epoch: 189/199: : 910it [00:16, 55.73it/s, loss=0.005135]
eval psnr: 23.05
epoch: 190/199: : 910it [00:16, 56.31it/s, loss=0.005197]
eval psnr: 23.37
epoch: 191/199: : 910it [00:16, 55.44it/s, loss=0.005143]
eval psnr: 23.71
epoch: 192/199: : 910it [00:17, 53.46it/s, loss=0.005258]
eval psnr: 24.09
epoch: 193/199: : 910it [00:16, 53.77it/s, loss=0.005234]
eval psnr: 24.13
epoch: 194/199: : 910it [00:16, 54.86it/s, loss=0.005189]
eval psnr: 23.40
epoch: 195/199: : 910it [00:16, 56.05it/s, loss=0.005069]
eval psnr: 24.06
epoch: 196/199: : 910it [00:16, 56.13it/s, loss=0.005121]
eval psnr: 23.84
epoch: 197/199: : 910it [00:16, 55.94it/s, loss=0.005181]
eval psnr: 24.22
epoch: 198/199: : 910it [00:16, 55.81it/s, loss=0.005195]
eval psnr: 23.33
epoch: 199/199: : 910it [00:16, 55.86it/s, loss=0.005125]
eval psnr: 24.09
best epoch: 151, psnr: 24.40"""

log7 = """
epoch: 0/199: : 910it [00:10, 89.14it/s, loss=0.102449]
eval psnr: 16.17
epoch: 1/199: : 910it [00:03, 231.42it/s, loss=0.027654]
eval psnr: 17.21
epoch: 2/199: : 910it [00:04, 183.95it/s, loss=0.018712]
eval psnr: 18.14
epoch: 3/199: : 910it [00:04, 202.32it/s, loss=0.015310]
eval psnr: 19.01
epoch: 4/199: : 910it [00:04, 214.91it/s, loss=0.013524]
eval psnr: 19.65
epoch: 5/199: : 910it [00:04, 217.48it/s, loss=0.011984]
eval psnr: 20.24
epoch: 6/199: : 910it [00:04, 216.74it/s, loss=0.010703]
eval psnr: 21.41
epoch: 7/199: : 910it [00:04, 223.82it/s, loss=0.010085]
eval psnr: 21.98
epoch: 8/199: : 910it [00:03, 262.92it/s, loss=0.009518]
eval psnr: 21.92
epoch: 9/199: : 910it [00:03, 248.40it/s, loss=0.009516]
eval psnr: 22.08
epoch: 10/199: : 910it [00:03, 234.28it/s, loss=0.009083]
eval psnr: 21.05
epoch: 11/199: : 910it [00:05, 181.90it/s, loss=0.008796]
eval psnr: 22.51
epoch: 12/199: : 910it [00:04, 202.35it/s, loss=0.008768]
eval psnr: 21.97
epoch: 13/199: : 910it [00:04, 208.04it/s, loss=0.008743]
eval psnr: 22.05
epoch: 14/199: : 910it [00:04, 190.58it/s, loss=0.008836]
eval psnr: 22.10
epoch: 15/199: : 910it [00:04, 223.28it/s, loss=0.008851]
eval psnr: 21.86
epoch: 16/199: : 910it [00:04, 202.39it/s, loss=0.008461]
eval psnr: 22.33
epoch: 17/199: : 910it [00:04, 186.11it/s, loss=0.008124]
eval psnr: 22.05
epoch: 18/199: : 910it [00:03, 234.08it/s, loss=0.008420]
eval psnr: 22.32
epoch: 19/199: : 910it [00:05, 178.56it/s, loss=0.008141]
eval psnr: 22.31
epoch: 20/199: : 910it [00:05, 169.63it/s, loss=0.008422]
eval psnr: 21.99
epoch: 21/199: : 910it [00:04, 217.61it/s, loss=0.008196]
eval psnr: 21.94
epoch: 22/199: : 910it [00:03, 230.95it/s, loss=0.008165]
eval psnr: 22.67
epoch: 23/199: : 910it [00:03, 233.78it/s, loss=0.007978]
eval psnr: 22.06
epoch: 24/199: : 910it [00:03, 241.76it/s, loss=0.007833]
eval psnr: 22.09
epoch: 25/199: : 910it [00:03, 248.50it/s, loss=0.007995]
eval psnr: 22.58
epoch: 26/199: : 910it [00:04, 216.23it/s, loss=0.007829]
eval psnr: 22.14
epoch: 27/199: : 910it [00:04, 193.90it/s, loss=0.007876]
eval psnr: 22.40
epoch: 28/199: : 910it [00:07, 122.04it/s, loss=0.007868]
eval psnr: 22.77
epoch: 29/199: : 910it [00:04, 209.75it/s, loss=0.007819]
eval psnr: 23.16
epoch: 30/199: : 910it [00:04, 208.68it/s, loss=0.007531]
eval psnr: 22.82
epoch: 31/199: : 910it [00:04, 204.10it/s, loss=0.007649]
eval psnr: 22.65
epoch: 32/199: : 910it [00:04, 222.22it/s, loss=0.007854]
eval psnr: 23.08
epoch: 33/199: : 910it [00:04, 226.00it/s, loss=0.007597]
eval psnr: 22.31
epoch: 34/199: : 910it [00:04, 225.09it/s, loss=0.007589]
eval psnr: 22.65
epoch: 35/199: : 910it [00:04, 210.86it/s, loss=0.007496]
eval psnr: 22.43
epoch: 36/199: : 910it [00:03, 228.71it/s, loss=0.007422]
eval psnr: 22.84
epoch: 37/199: : 910it [00:04, 208.77it/s, loss=0.007419]
eval psnr: 22.73
epoch: 38/199: : 910it [00:04, 218.80it/s, loss=0.007724]
eval psnr: 22.87
epoch: 39/199: : 910it [00:05, 178.84it/s, loss=0.007331]
eval psnr: 22.93
epoch: 40/199: : 910it [00:05, 155.15it/s, loss=0.007631]
eval psnr: 23.24
epoch: 41/199: : 910it [00:05, 174.95it/s, loss=0.007600]
eval psnr: 22.90
epoch: 42/199: : 910it [00:04, 209.70it/s, loss=0.007577]
eval psnr: 22.69
epoch: 43/199: : 910it [00:04, 195.70it/s, loss=0.007451]
eval psnr: 22.48
epoch: 44/199: : 910it [00:06, 139.10it/s, loss=0.007286]
eval psnr: 22.45
epoch: 45/199: : 910it [00:05, 163.27it/s, loss=0.007319]
eval psnr: 22.74
epoch: 46/199: : 910it [00:04, 214.93it/s, loss=0.007456]
eval psnr: 22.86
epoch: 47/199: : 910it [00:04, 219.85it/s, loss=0.007465]
eval psnr: 22.51
epoch: 48/199: : 910it [00:05, 170.51it/s, loss=0.007376]
eval psnr: 22.53
epoch: 49/199: : 910it [00:03, 249.58it/s, loss=0.007455]
eval psnr: 22.96
epoch: 50/199: : 910it [00:03, 238.24it/s, loss=0.007147]
eval psnr: 22.95
epoch: 51/199: : 910it [00:04, 186.13it/s, loss=0.007021]
eval psnr: 22.57
epoch: 52/199: : 910it [00:06, 135.33it/s, loss=0.007442]
eval psnr: 23.10
epoch: 53/199: : 910it [00:04, 195.66it/s, loss=0.007149]
eval psnr: 23.09
epoch: 54/199: : 910it [00:04, 189.96it/s, loss=0.007164]
eval psnr: 22.72
epoch: 55/199: : 910it [00:05, 177.47it/s, loss=0.007025]
eval psnr: 22.58
epoch: 56/199: : 910it [00:04, 191.11it/s, loss=0.007152]
eval psnr: 23.22
epoch: 57/199: : 910it [00:04, 208.79it/s, loss=0.007156]
eval psnr: 23.11
epoch: 58/199: : 910it [00:05, 175.84it/s, loss=0.007082]
eval psnr: 23.27
epoch: 59/199: : 910it [00:05, 154.20it/s, loss=0.007201]
eval psnr: 22.73
epoch: 60/199: : 910it [00:04, 201.86it/s, loss=0.007330]
eval psnr: 22.66
epoch: 61/199: : 910it [00:04, 185.55it/s, loss=0.007186]
eval psnr: 23.00
epoch: 62/199: : 910it [00:04, 217.20it/s, loss=0.007202]
eval psnr: 22.80
epoch: 63/199: : 910it [00:04, 211.83it/s, loss=0.006909]
eval psnr: 22.98
epoch: 64/199: : 910it [00:04, 192.03it/s, loss=0.007087]
eval psnr: 22.88
epoch: 65/199: : 910it [00:05, 180.10it/s, loss=0.007144]
eval psnr: 23.60
epoch: 66/199: : 910it [00:04, 199.70it/s, loss=0.007265]
eval psnr: 23.00
epoch: 67/199: : 910it [00:04, 188.60it/s, loss=0.007136]
eval psnr: 22.88
epoch: 68/199: : 910it [00:04, 210.06it/s, loss=0.007166]
eval psnr: 22.66
epoch: 69/199: : 910it [00:07, 118.36it/s, loss=0.006962]
eval psnr: 22.91
epoch: 70/199: : 910it [00:06, 150.64it/s, loss=0.007205]
eval psnr: 22.84
epoch: 71/199: : 910it [00:05, 178.54it/s, loss=0.006883]
eval psnr: 22.96
epoch: 72/199: : 910it [00:05, 159.93it/s, loss=0.006874]
eval psnr: 22.78
epoch: 73/199: : 910it [00:04, 195.91it/s, loss=0.007183]
eval psnr: 22.54
epoch: 74/199: : 910it [00:04, 207.47it/s, loss=0.007151]
eval psnr: 22.77
epoch: 75/199: : 910it [00:04, 207.80it/s, loss=0.006881]
eval psnr: 23.13
epoch: 76/199: : 910it [00:05, 177.97it/s, loss=0.006989]
eval psnr: 22.98
epoch: 77/199: : 910it [00:04, 206.05it/s, loss=0.006833]
eval psnr: 22.73
epoch: 78/199: : 910it [00:04, 225.31it/s, loss=0.007156]
eval psnr: 23.44
epoch: 79/199: : 910it [00:03, 261.95it/s, loss=0.006915]
eval psnr: 23.50
epoch: 80/199: : 910it [00:03, 248.13it/s, loss=0.006853]
eval psnr: 23.08
epoch: 81/199: : 910it [00:04, 206.21it/s, loss=0.006973]
eval psnr: 22.84
epoch: 82/199: : 910it [00:04, 205.59it/s, loss=0.007299]
eval psnr: 23.03
epoch: 83/199: : 910it [00:04, 198.39it/s, loss=0.006999]
eval psnr: 22.90
epoch: 84/199: : 910it [00:04, 209.89it/s, loss=0.006778]
eval psnr: 22.76
epoch: 85/199: : 910it [00:03, 266.90it/s, loss=0.007112]
eval psnr: 23.44
epoch: 86/199: : 910it [00:04, 224.59it/s, loss=0.006728]
eval psnr: 23.36
epoch: 87/199: : 910it [00:04, 197.04it/s, loss=0.006915]
eval psnr: 23.15
epoch: 88/199: : 910it [00:05, 163.34it/s, loss=0.006759]
eval psnr: 22.85
epoch: 89/199: : 910it [00:04, 214.08it/s, loss=0.007047]
eval psnr: 23.64
epoch: 90/199: : 910it [00:04, 207.19it/s, loss=0.006962]
eval psnr: 22.93
epoch: 91/199: : 910it [00:04, 224.26it/s, loss=0.006715]
eval psnr: 23.11
epoch: 92/199: : 910it [00:03, 228.71it/s, loss=0.007088]
eval psnr: 22.47
epoch: 93/199: : 910it [00:03, 273.67it/s, loss=0.006905]
eval psnr: 23.07
epoch: 94/199: : 910it [00:03, 250.98it/s, loss=0.006662]
eval psnr: 23.15
epoch: 95/199: : 910it [00:04, 209.39it/s, loss=0.006824]
eval psnr: 23.47
epoch: 96/199: : 910it [00:04, 213.01it/s, loss=0.006797]
eval psnr: 23.01
epoch: 97/199: : 910it [00:03, 259.65it/s, loss=0.006886]
eval psnr: 22.70
epoch: 98/199: : 910it [00:03, 232.39it/s, loss=0.006840]
eval psnr: 23.28
epoch: 99/199: : 910it [00:03, 264.44it/s, loss=0.006826]
eval psnr: 22.77
epoch: 100/199: : 910it [00:03, 261.84it/s, loss=0.006709]
eval psnr: 22.88
epoch: 101/199: : 910it [00:03, 275.11it/s, loss=0.007070]
eval psnr: 23.02
epoch: 102/199: : 910it [00:03, 252.12it/s, loss=0.006799]
eval psnr: 23.06
epoch: 103/199: : 910it [00:04, 211.54it/s, loss=0.006749]
eval psnr: 23.56
epoch: 104/199: : 910it [00:03, 245.34it/s, loss=0.006723]
eval psnr: 23.26
epoch: 105/199: : 910it [00:03, 233.09it/s, loss=0.006682]
eval psnr: 23.02
epoch: 106/199: : 910it [00:04, 205.24it/s, loss=0.006731]
eval psnr: 23.11
epoch: 107/199: : 910it [00:03, 240.36it/s, loss=0.006820]
eval psnr: 23.50
epoch: 108/199: : 910it [00:03, 247.96it/s, loss=0.006878]
eval psnr: 23.46
epoch: 109/199: : 910it [00:03, 247.06it/s, loss=0.006609]
eval psnr: 23.05
epoch: 110/199: : 910it [00:04, 196.10it/s, loss=0.006749]
eval psnr: 22.20
epoch: 111/199: : 910it [00:04, 189.24it/s, loss=0.006532]
eval psnr: 23.01
epoch: 112/199: : 910it [00:06, 145.54it/s, loss=0.006640]
eval psnr: 23.30
epoch: 113/199: : 910it [00:04, 215.41it/s, loss=0.006670]
eval psnr: 23.51
epoch: 114/199: : 910it [00:03, 236.37it/s, loss=0.007069]
eval psnr: 23.16
epoch: 115/199: : 910it [00:05, 155.59it/s, loss=0.006560]
eval psnr: 23.21
epoch: 116/199: : 910it [00:03, 232.09it/s, loss=0.006965]
eval psnr: 23.27
epoch: 117/199: : 910it [00:03, 233.57it/s, loss=0.006649]
eval psnr: 23.00
epoch: 118/199: : 910it [00:03, 248.30it/s, loss=0.006556]
eval psnr: 23.10
epoch: 119/199: : 910it [00:03, 255.10it/s, loss=0.006844]
eval psnr: 23.34
epoch: 120/199: : 910it [00:03, 235.73it/s, loss=0.006843]
eval psnr: 22.83
epoch: 121/199: : 910it [00:03, 252.64it/s, loss=0.006539]
eval psnr: 22.81
epoch: 122/199: : 910it [00:03, 266.63it/s, loss=0.006770]
eval psnr: 22.43
epoch: 123/199: : 910it [00:03, 263.00it/s, loss=0.006475]
eval psnr: 23.14
epoch: 124/199: : 910it [00:03, 240.55it/s, loss=0.006802]
eval psnr: 23.12
epoch: 125/199: : 910it [00:03, 241.18it/s, loss=0.006860]
eval psnr: 23.62
epoch: 126/199: : 910it [00:04, 183.41it/s, loss=0.006816]
eval psnr: 23.08
epoch: 127/199: : 910it [00:03, 243.13it/s, loss=0.006682]
eval psnr: 23.36
epoch: 128/199: : 910it [00:04, 224.43it/s, loss=0.006669]
eval psnr: 23.34
epoch: 129/199: : 910it [00:04, 220.91it/s, loss=0.006730]
eval psnr: 22.95
epoch: 130/199: : 910it [00:03, 229.97it/s, loss=0.006493]
eval psnr: 22.77
epoch: 131/199: : 910it [00:05, 180.31it/s, loss=0.006618]
eval psnr: 23.10
epoch: 132/199: : 910it [00:04, 211.76it/s, loss=0.006496]
eval psnr: 23.40
epoch: 133/199: : 910it [00:04, 200.45it/s, loss=0.006817]
eval psnr: 22.85
epoch: 134/199: : 910it [00:03, 234.88it/s, loss=0.006634]
eval psnr: 23.86
epoch: 135/199: : 910it [00:03, 236.49it/s, loss=0.006696]
eval psnr: 22.70
epoch: 136/199: : 910it [00:04, 216.69it/s, loss=0.006484]
eval psnr: 23.39
epoch: 137/199: : 910it [00:04, 206.86it/s, loss=0.006378]
eval psnr: 22.96
epoch: 138/199: : 910it [00:04, 182.65it/s, loss=0.006978]
eval psnr: 23.14
epoch: 139/199: : 910it [00:05, 152.43it/s, loss=0.006720]
eval psnr: 22.85
epoch: 140/199: : 910it [00:06, 147.93it/s, loss=0.006615]
eval psnr: 23.30
epoch: 141/199: : 910it [00:04, 194.68it/s, loss=0.006367]
eval psnr: 23.52
epoch: 142/199: : 910it [00:04, 197.15it/s, loss=0.006762]
eval psnr: 22.82
epoch: 143/199: : 910it [00:04, 197.62it/s, loss=0.006371]
eval psnr: 23.02
epoch: 144/199: : 910it [00:06, 136.23it/s, loss=0.006433]
eval psnr: 23.30
epoch: 145/199: : 910it [00:05, 152.58it/s, loss=0.006617]
eval psnr: 23.11
epoch: 146/199: : 910it [00:05, 170.89it/s, loss=0.006543]
eval psnr: 22.88
epoch: 147/199: : 910it [00:05, 164.74it/s, loss=0.006746]
eval psnr: 23.14
epoch: 148/199: : 910it [00:04, 198.19it/s, loss=0.006460]
eval psnr: 23.41
epoch: 149/199: : 910it [00:06, 138.89it/s, loss=0.006458]
eval psnr: 23.27
epoch: 150/199: : 910it [00:05, 177.52it/s, loss=0.006508]
eval psnr: 23.34
epoch: 151/199: : 910it [00:04, 182.48it/s, loss=0.006457]
eval psnr: 23.01
epoch: 152/199: : 910it [00:04, 195.78it/s, loss=0.006596]
eval psnr: 23.59
epoch: 153/199: : 910it [00:04, 209.18it/s, loss=0.006515]
eval psnr: 22.86
epoch: 154/199: : 910it [00:05, 174.40it/s, loss=0.006908]
eval psnr: 23.65
epoch: 155/199: : 910it [00:05, 172.24it/s, loss=0.006516]
eval psnr: 23.04
epoch: 156/199: : 910it [00:05, 181.35it/s, loss=0.006572]
eval psnr: 23.13
epoch: 157/199: : 910it [00:04, 222.63it/s, loss=0.006505]
eval psnr: 23.15
epoch: 158/199: : 910it [00:04, 199.75it/s, loss=0.006445]
eval psnr: 23.29
epoch: 159/199: : 910it [00:04, 221.07it/s, loss=0.006361]
eval psnr: 22.70
epoch: 160/199: : 910it [00:03, 253.27it/s, loss=0.006774]
eval psnr: 23.37
epoch: 161/199: : 910it [00:03, 246.27it/s, loss=0.006612]
eval psnr: 23.50
epoch: 162/199: : 910it [00:03, 267.88it/s, loss=0.006567]
eval psnr: 22.86
epoch: 163/199: : 910it [00:03, 228.36it/s, loss=0.006544]
eval psnr: 23.00
epoch: 164/199: : 910it [00:05, 167.84it/s, loss=0.006423]
eval psnr: 23.22
epoch: 165/199: : 910it [00:04, 192.37it/s, loss=0.006534]
eval psnr: 23.02
epoch: 166/199: : 910it [00:04, 201.08it/s, loss=0.006253]
eval psnr: 23.16
epoch: 167/199: : 910it [00:05, 178.42it/s, loss=0.006477]
eval psnr: 23.25
epoch: 168/199: : 910it [00:05, 154.94it/s, loss=0.006449]
eval psnr: 22.70
epoch: 169/199: : 910it [00:04, 193.41it/s, loss=0.006385]
eval psnr: 23.44
epoch: 170/199: : 910it [00:07, 119.72it/s, loss=0.006392]
eval psnr: 23.08
epoch: 171/199: : 910it [00:08, 109.01it/s, loss=0.006614]
eval psnr: 23.29
epoch: 172/199: : 910it [00:10, 90.45it/s, loss=0.006563]
eval psnr: 23.01
epoch: 173/199: : 910it [00:09, 99.61it/s, loss=0.006607]
eval psnr: 23.51
epoch: 174/199: : 910it [00:06, 146.52it/s, loss=0.006579]
eval psnr: 23.56
epoch: 175/199: : 910it [00:06, 130.71it/s, loss=0.006376]
eval psnr: 23.15
epoch: 176/199: : 910it [00:04, 201.55it/s, loss=0.006555]
eval psnr: 23.77
epoch: 177/199: : 910it [00:04, 189.10it/s, loss=0.006462]
eval psnr: 23.21
epoch: 178/199: : 910it [00:05, 176.94it/s, loss=0.006201]
eval psnr: 23.15
epoch: 179/199: : 910it [00:07, 127.06it/s, loss=0.006493]
eval psnr: 23.29
epoch: 180/199: : 910it [00:05, 172.97it/s, loss=0.006424]
eval psnr: 22.99
epoch: 181/199: : 910it [00:05, 159.52it/s, loss=0.006211]
eval psnr: 23.09
epoch: 182/199: : 910it [00:12, 73.10it/s, loss=0.006429]
eval psnr: 23.38
epoch: 183/199: : 910it [00:06, 147.45it/s, loss=0.006225]
eval psnr: 22.94
epoch: 184/199: : 910it [00:05, 156.40it/s, loss=0.006492]
eval psnr: 23.37
epoch: 185/199: : 910it [00:05, 174.10it/s, loss=0.006439]
eval psnr: 23.51
epoch: 186/199: : 910it [00:05, 172.97it/s, loss=0.006361]
eval psnr: 23.66
epoch: 187/199: : 910it [00:05, 173.94it/s, loss=0.006299]
eval psnr: 23.06
epoch: 188/199: : 910it [00:05, 176.94it/s, loss=0.006396]
eval psnr: 22.81
epoch: 189/199: : 910it [00:05, 172.06it/s, loss=0.006418]
eval psnr: 22.89
epoch: 190/199: : 910it [00:05, 160.37it/s, loss=0.006519]
eval psnr: 23.49
epoch: 191/199: : 910it [00:05, 168.81it/s, loss=0.006442]
eval psnr: 23.51
epoch: 192/199: : 910it [00:05, 173.13it/s, loss=0.006463]
eval psnr: 23.38
epoch: 193/199: : 910it [00:05, 177.13it/s, loss=0.006435]
eval psnr: 23.33
epoch: 194/199: : 910it [00:05, 176.23it/s, loss=0.006394]
eval psnr: 23.26
epoch: 195/199: : 910it [00:05, 159.22it/s, loss=0.006526]
eval psnr: 23.32
epoch: 196/199: : 910it [00:05, 179.75it/s, loss=0.006568]
eval psnr: 23.10
epoch: 197/199: : 910it [00:06, 151.56it/s, loss=0.006416]
eval psnr: 23.04
epoch: 198/199: : 910it [00:05, 177.81it/s, loss=0.006428]
eval psnr: 22.92
epoch: 199/199: : 910it [00:08, 111.99it/s, loss=0.006708]
eval psnr: 23.42
best epoch: 134, psnr: 23.86
"""
log8 ="""
epoch: 0/199: : 910it [00:06, 146.60it/s, loss=0.087200]                        
eval psnr: 15.52
epoch: 1/199: : 910it [00:03, 248.97it/s, loss=0.026653]                        
eval psnr: 18.65
epoch: 2/199: : 910it [00:03, 251.61it/s, loss=0.013285]                        
eval psnr: 20.95
epoch: 3/199: : 910it [00:03, 241.01it/s, loss=0.010441]                        
eval psnr: 21.81
epoch: 4/199: : 910it [00:03, 261.38it/s, loss=0.009828]                        
eval psnr: 21.80
epoch: 5/199: : 910it [00:03, 249.42it/s, loss=0.009160]                        
eval psnr: 21.97
epoch: 6/199: : 910it [00:03, 250.39it/s, loss=0.008662]                        
eval psnr: 22.26
epoch: 7/199: : 910it [00:03, 248.57it/s, loss=0.008404]                        
eval psnr: 22.38
epoch: 8/199: : 910it [00:03, 245.94it/s, loss=0.008093]                        
eval psnr: 22.56
epoch: 9/199: : 910it [00:03, 245.50it/s, loss=0.008197]                        
eval psnr: 21.97
epoch: 10/199: : 910it [00:03, 247.33it/s, loss=0.008297]                       
eval psnr: 22.33
epoch: 11/199: : 910it [00:03, 251.86it/s, loss=0.007832]                       
eval psnr: 22.56
epoch: 12/199: : 910it [00:03, 242.75it/s, loss=0.007863]                       
eval psnr: 22.99
epoch: 13/199: : 910it [00:03, 242.54it/s, loss=0.007298]                       
eval psnr: 23.17
epoch: 14/199: : 910it [00:03, 253.10it/s, loss=0.007703]                       
eval psnr: 22.73
epoch: 15/199: : 910it [00:03, 242.58it/s, loss=0.007530]                       
eval psnr: 23.18
epoch: 16/199: : 910it [00:03, 241.60it/s, loss=0.007253]                       
eval psnr: 22.75
epoch: 17/199: : 910it [00:03, 243.08it/s, loss=0.007408]                       
eval psnr: 22.92
epoch: 18/199: : 910it [00:03, 249.13it/s, loss=0.007508]                       
eval psnr: 23.21
epoch: 19/199: : 910it [00:03, 251.99it/s, loss=0.007170]                       
eval psnr: 22.34
epoch: 20/199: : 910it [00:03, 252.90it/s, loss=0.007079]                       
eval psnr: 23.29
epoch: 21/199: : 910it [00:03, 240.66it/s, loss=0.007193]                       
eval psnr: 23.06
epoch: 22/199: : 910it [00:03, 248.97it/s, loss=0.007282]                       
eval psnr: 23.13
epoch: 23/199: : 910it [00:03, 259.01it/s, loss=0.006900]                       
eval psnr: 22.98
epoch: 24/199: : 910it [00:03, 254.75it/s, loss=0.007330]                       
eval psnr: 23.50
epoch: 25/199: : 910it [00:03, 248.52it/s, loss=0.006866]                       
eval psnr: 23.24
epoch: 26/199: : 910it [00:03, 249.31it/s, loss=0.006820]                       
eval psnr: 22.69
epoch: 27/199: : 910it [00:03, 244.16it/s, loss=0.007020]                       
eval psnr: 23.49
epoch: 28/199: : 910it [00:03, 250.52it/s, loss=0.006682]                       
eval psnr: 23.15
epoch: 29/199: : 910it [00:03, 254.44it/s, loss=0.006805]                       
eval psnr: 23.60
epoch: 30/199: : 910it [00:03, 246.25it/s, loss=0.006951]                       
eval psnr: 22.97
epoch: 31/199: : 910it [00:03, 255.60it/s, loss=0.006656]                       
eval psnr: 23.69
epoch: 32/199: : 910it [00:03, 254.46it/s, loss=0.006997]                       
eval psnr: 21.91
epoch: 33/199: : 910it [00:03, 248.52it/s, loss=0.006783]                       
eval psnr: 23.47
epoch: 34/199: : 910it [00:03, 250.72it/s, loss=0.006473]                       
eval psnr: 23.27
epoch: 35/199: : 910it [00:03, 240.28it/s, loss=0.006637]                       
eval psnr: 22.66
epoch: 36/199: : 910it [00:03, 247.16it/s, loss=0.006679]                       
eval psnr: 23.68
epoch: 37/199: : 910it [00:03, 251.67it/s, loss=0.006736]                       
eval psnr: 23.32
epoch: 38/199: : 910it [00:03, 247.62it/s, loss=0.006708]                       
eval psnr: 22.35
epoch: 39/199: : 910it [00:03, 255.27it/s, loss=0.006669]                       
eval psnr: 23.02
epoch: 40/199: : 910it [00:03, 246.81it/s, loss=0.006740]                       
eval psnr: 23.11
epoch: 41/199: : 910it [00:03, 257.14it/s, loss=0.006685]                       
eval psnr: 22.92
epoch: 42/199: : 910it [00:03, 246.34it/s, loss=0.006357]                       
eval psnr: 23.68
epoch: 43/199: : 910it [00:03, 247.48it/s, loss=0.006385]                       
eval psnr: 23.63
epoch: 44/199: : 910it [00:03, 246.04it/s, loss=0.006617]                       
eval psnr: 23.06
epoch: 45/199: : 910it [00:03, 258.57it/s, loss=0.006304]                       
eval psnr: 22.65
epoch: 46/199: : 910it [00:03, 245.03it/s, loss=0.006501]                       
eval psnr: 23.24
epoch: 47/199: : 910it [00:03, 255.34it/s, loss=0.006549]                       
eval psnr: 22.99
epoch: 48/199: : 910it [00:03, 248.49it/s, loss=0.006446]                       
eval psnr: 22.65
epoch: 49/199: : 910it [00:03, 247.01it/s, loss=0.006815]                       
eval psnr: 23.55
epoch: 50/199: : 910it [00:03, 247.18it/s, loss=0.006626]                       
eval psnr: 23.55
epoch: 51/199: : 910it [00:03, 256.38it/s, loss=0.006705]                       
eval psnr: 22.79
epoch: 52/199: : 910it [00:03, 258.64it/s, loss=0.006448]                       
eval psnr: 23.04
epoch: 53/199: : 910it [00:03, 243.92it/s, loss=0.006507]                       
eval psnr: 22.74
epoch: 54/199: : 910it [00:03, 252.24it/s, loss=0.006263]                       
eval psnr: 23.41
epoch: 55/199: : 910it [00:03, 247.08it/s, loss=0.006500]                       
eval psnr: 22.15
epoch: 56/199: : 910it [00:03, 251.06it/s, loss=0.006525]                       
eval psnr: 22.58
epoch: 57/199: : 910it [00:03, 246.97it/s, loss=0.006325]                       
eval psnr: 23.27
epoch: 58/199: : 910it [00:03, 250.17it/s, loss=0.006358]                       
eval psnr: 23.23
epoch: 59/199: : 910it [00:03, 256.91it/s, loss=0.006358]                       
eval psnr: 22.98
epoch: 60/199: : 910it [00:03, 251.15it/s, loss=0.006134]                       
eval psnr: 23.32
epoch: 61/199: : 910it [00:03, 254.56it/s, loss=0.006013]                       
eval psnr: 23.19
epoch: 62/199: : 910it [00:03, 247.21it/s, loss=0.006310]                       
eval psnr: 23.50
epoch: 63/199: : 910it [00:03, 245.00it/s, loss=0.006250]                       
eval psnr: 23.68
epoch: 64/199: : 910it [00:03, 242.12it/s, loss=0.006149]                       
eval psnr: 23.43
epoch: 65/199: : 910it [00:03, 248.37it/s, loss=0.006134]                       
eval psnr: 22.33
epoch: 66/199: : 910it [00:03, 246.47it/s, loss=0.006205]                       
eval psnr: 23.32
epoch: 67/199: : 910it [00:03, 247.72it/s, loss=0.006255]                       
eval psnr: 23.65
epoch: 68/199: : 910it [00:03, 245.59it/s, loss=0.005995]                       
eval psnr: 23.24
epoch: 69/199: : 910it [00:03, 249.42it/s, loss=0.006068]                       
eval psnr: 23.75
epoch: 70/199: : 910it [00:03, 253.84it/s, loss=0.006177]                       
eval psnr: 23.12
epoch: 71/199: : 910it [00:03, 250.73it/s, loss=0.006234]                       
eval psnr: 23.30
epoch: 72/199: : 910it [00:03, 254.66it/s, loss=0.006259]                       
eval psnr: 23.53
epoch: 73/199: : 910it [00:03, 251.47it/s, loss=0.006142]                       
eval psnr: 23.71
epoch: 74/199: : 910it [00:03, 242.38it/s, loss=0.005939]                       
eval psnr: 23.65
epoch: 75/199: : 910it [00:03, 251.06it/s, loss=0.006150]                       
eval psnr: 23.98
epoch: 76/199: : 910it [00:03, 241.18it/s, loss=0.006010]                       
eval psnr: 23.12
epoch: 77/199: : 910it [00:03, 242.65it/s, loss=0.005954]                       
eval psnr: 23.78
epoch: 78/199: : 910it [00:03, 247.67it/s, loss=0.006159]                       
eval psnr: 23.10
epoch: 79/199: : 910it [00:03, 253.59it/s, loss=0.006204]                       
eval psnr: 22.66
epoch: 80/199: : 910it [00:03, 252.56it/s, loss=0.006128]                       
eval psnr: 23.23
epoch: 81/199: : 910it [00:03, 248.23it/s, loss=0.005992]                       
eval psnr: 23.99
epoch: 82/199: : 910it [00:03, 248.94it/s, loss=0.006234]                       
eval psnr: 23.76
epoch: 83/199: : 910it [00:03, 248.36it/s, loss=0.006128]                       
eval psnr: 23.33
epoch: 84/199: : 910it [00:03, 248.72it/s, loss=0.006041]                       
eval psnr: 23.84
epoch: 85/199: : 910it [00:03, 239.10it/s, loss=0.006091]                       
eval psnr: 23.94
epoch: 86/199: : 910it [00:03, 255.17it/s, loss=0.005922]                       
eval psnr: 23.31
epoch: 87/199: : 910it [00:03, 252.42it/s, loss=0.005945]                       
eval psnr: 23.54
epoch: 88/199: : 910it [00:03, 254.46it/s, loss=0.005693]                       
eval psnr: 23.20
epoch: 89/199: : 910it [00:03, 238.81it/s, loss=0.006086]                       
eval psnr: 23.27
epoch: 90/199: : 910it [00:03, 253.63it/s, loss=0.006132]                       
eval psnr: 23.06
epoch: 91/199: : 910it [00:03, 253.94it/s, loss=0.005928]                       
eval psnr: 22.93
epoch: 92/199: : 910it [00:03, 244.82it/s, loss=0.006073]                       
eval psnr: 22.73
epoch: 93/199: : 910it [00:03, 249.34it/s, loss=0.005990]                       
eval psnr: 23.81
epoch: 94/199: : 910it [00:03, 247.14it/s, loss=0.006103]                       
eval psnr: 23.39
epoch: 95/199: : 910it [00:03, 253.83it/s, loss=0.005964]                       
eval psnr: 24.02
epoch: 96/199: : 910it [00:03, 251.93it/s, loss=0.006039]                       
eval psnr: 24.17
epoch: 97/199: : 910it [00:03, 243.45it/s, loss=0.005886]                       
eval psnr: 23.59
epoch: 98/199: : 910it [00:03, 259.28it/s, loss=0.005725]                       
eval psnr: 23.89
epoch: 99/199: : 910it [00:03, 247.22it/s, loss=0.006010]                       
eval psnr: 23.63
epoch: 100/199: : 910it [00:03, 255.10it/s, loss=0.005861]                      
eval psnr: 23.61
epoch: 101/199: : 910it [00:03, 248.13it/s, loss=0.006111]                      
eval psnr: 23.30
epoch: 102/199: : 910it [00:03, 256.22it/s, loss=0.005850]                      
eval psnr: 23.43
epoch: 103/199: : 910it [00:03, 256.42it/s, loss=0.005806]                      
eval psnr: 23.71
epoch: 104/199: : 910it [00:03, 254.52it/s, loss=0.005673]                      
eval psnr: 24.29
epoch: 105/199: : 910it [00:03, 243.25it/s, loss=0.005789]                      
eval psnr: 23.63
epoch: 106/199: : 910it [00:03, 248.85it/s, loss=0.005893]                      
eval psnr: 23.70
epoch: 107/199: : 910it [00:03, 245.41it/s, loss=0.006136]                      
eval psnr: 23.26
epoch: 108/199: : 910it [00:03, 258.63it/s, loss=0.005957]                      
eval psnr: 23.48
epoch: 109/199: : 910it [00:03, 257.64it/s, loss=0.005794]                      
eval psnr: 22.95
epoch: 110/199: : 910it [00:03, 235.07it/s, loss=0.005737]                      
eval psnr: 23.23
epoch: 111/199: : 910it [00:03, 245.06it/s, loss=0.005773]                      
eval psnr: 24.04
epoch: 112/199: : 910it [00:03, 239.52it/s, loss=0.005882]                      
eval psnr: 23.83
epoch: 113/199: : 910it [00:03, 240.31it/s, loss=0.006012]                      
eval psnr: 23.49
epoch: 114/199: : 910it [00:03, 251.01it/s, loss=0.005871]                      
eval psnr: 23.11
epoch: 115/199: : 910it [00:03, 241.55it/s, loss=0.005806]                      
eval psnr: 22.67
epoch: 116/199: : 910it [00:03, 239.12it/s, loss=0.005646]                      
eval psnr: 23.84
epoch: 117/199: : 910it [00:03, 245.13it/s, loss=0.005664]                      
eval psnr: 23.34
epoch: 118/199: : 910it [00:03, 248.70it/s, loss=0.005582]                      
eval psnr: 23.24
epoch: 119/199: : 910it [00:03, 248.00it/s, loss=0.005929]                      
eval psnr: 23.64
epoch: 120/199: : 910it [00:03, 236.88it/s, loss=0.005775]                      
eval psnr: 23.77
epoch: 121/199: : 910it [00:03, 243.11it/s, loss=0.005811]                      
eval psnr: 23.17
epoch: 122/199: : 910it [00:03, 253.40it/s, loss=0.005867]                      
eval psnr: 23.42
epoch: 123/199: : 910it [00:03, 240.33it/s, loss=0.005660]                      
eval psnr: 23.33
epoch: 124/199: : 910it [00:03, 241.56it/s, loss=0.005717]                      
eval psnr: 23.55
epoch: 125/199: : 910it [00:03, 236.86it/s, loss=0.005555]                      
eval psnr: 23.58
epoch: 126/199: : 910it [00:03, 245.55it/s, loss=0.005786]                      
eval psnr: 23.96
epoch: 127/199: : 910it [00:03, 250.31it/s, loss=0.005915]                      
eval psnr: 23.21
epoch: 128/199: : 910it [00:03, 241.66it/s, loss=0.005723]                      
eval psnr: 23.89
epoch: 129/199: : 910it [00:03, 252.13it/s, loss=0.005571]                      
eval psnr: 23.46
epoch: 130/199: : 910it [00:03, 238.86it/s, loss=0.005687]                      
eval psnr: 23.57
epoch: 131/199: : 910it [00:03, 244.21it/s, loss=0.005588]                      
eval psnr: 23.55
epoch: 132/199: : 910it [00:03, 241.57it/s, loss=0.005753]                      
eval psnr: 23.15
epoch: 133/199: : 910it [00:03, 239.54it/s, loss=0.005705]                      
eval psnr: 23.08
epoch: 134/199: : 910it [00:03, 237.46it/s, loss=0.005872]                      
eval psnr: 23.15
epoch: 135/199: : 910it [00:03, 234.31it/s, loss=0.005647]                      
eval psnr: 24.33
epoch: 136/199: : 910it [00:03, 247.73it/s, loss=0.005704]                      
eval psnr: 23.68
epoch: 137/199: : 910it [00:03, 244.46it/s, loss=0.005683]                      
eval psnr: 23.82
epoch: 138/199: : 910it [00:03, 252.88it/s, loss=0.005757]                      
eval psnr: 23.20
epoch: 139/199: : 910it [00:03, 251.42it/s, loss=0.005648]                      
eval psnr: 23.69
epoch: 140/199: : 910it [00:03, 246.17it/s, loss=0.005752]                      
eval psnr: 23.25
epoch: 141/199: : 910it [00:03, 272.88it/s, loss=0.005673]                      
eval psnr: 23.50
epoch: 142/199: : 910it [00:03, 257.27it/s, loss=0.005463]                      
eval psnr: 23.28
epoch: 143/199: : 910it [00:03, 244.49it/s, loss=0.005607]                      
eval psnr: 23.10
epoch: 144/199: : 910it [00:03, 250.38it/s, loss=0.005686]                      
eval psnr: 23.92
epoch: 145/199: : 910it [00:03, 245.16it/s, loss=0.005632]                      
eval psnr: 23.16
epoch: 146/199: : 910it [00:03, 249.70it/s, loss=0.005699]                      
eval psnr: 23.86
epoch: 147/199: : 910it [00:03, 255.04it/s, loss=0.005451]                      
eval psnr: 24.12
epoch: 148/199: : 910it [00:03, 254.23it/s, loss=0.005511]                      
eval psnr: 23.67
epoch: 149/199: : 910it [00:03, 248.84it/s, loss=0.005724]                      
eval psnr: 23.80
epoch: 150/199: : 910it [00:03, 253.94it/s, loss=0.005484]                      
eval psnr: 23.07
epoch: 151/199: : 910it [00:03, 245.17it/s, loss=0.005763]                      
eval psnr: 24.00
epoch: 152/199: : 910it [00:03, 242.57it/s, loss=0.005491]                      
eval psnr: 24.40
epoch: 153/199: : 910it [00:03, 251.55it/s, loss=0.005726]                      
eval psnr: 23.48
epoch: 154/199: : 910it [00:03, 247.17it/s, loss=0.005477]                      
eval psnr: 24.16
epoch: 155/199: : 910it [00:03, 252.45it/s, loss=0.005518]                      
eval psnr: 23.65
epoch: 156/199: : 910it [00:03, 246.08it/s, loss=0.005479]                      
eval psnr: 23.38
epoch: 157/199: : 910it [00:03, 248.81it/s, loss=0.005426]                      
eval psnr: 23.80
epoch: 158/199: : 910it [00:03, 257.44it/s, loss=0.005456]                      
eval psnr: 24.09
epoch: 159/199: : 910it [00:03, 261.94it/s, loss=0.005739]                      
eval psnr: 24.10
epoch: 160/199: : 910it [00:03, 251.59it/s, loss=0.005578]                      
eval psnr: 24.04
epoch: 161/199: : 910it [00:03, 250.70it/s, loss=0.005539]                      
eval psnr: 23.83
epoch: 162/199: : 910it [00:03, 251.76it/s, loss=0.005602]                      
eval psnr: 24.01
epoch: 163/199: : 910it [00:03, 250.63it/s, loss=0.005702]                      
eval psnr: 23.85
epoch: 164/199: : 910it [00:03, 253.27it/s, loss=0.005844]                      
eval psnr: 23.56
epoch: 165/199: : 910it [00:03, 252.02it/s, loss=0.005442]                      
eval psnr: 23.78
epoch: 166/199: : 910it [00:03, 256.79it/s, loss=0.005542]                      
eval psnr: 23.60
epoch: 167/199: : 910it [00:03, 256.10it/s, loss=0.005469]                      
eval psnr: 23.63
epoch: 168/199: : 910it [00:03, 266.42it/s, loss=0.005569]                      
eval psnr: 23.22
epoch: 169/199: : 910it [00:03, 244.18it/s, loss=0.005362]                      
eval psnr: 23.99
epoch: 170/199: : 910it [00:03, 249.64it/s, loss=0.005386]                      
eval psnr: 23.53
epoch: 171/199: : 910it [00:03, 256.66it/s, loss=0.005419]                      
eval psnr: 23.78
epoch: 172/199: : 910it [00:03, 254.75it/s, loss=0.005396]                      
eval psnr: 23.92
epoch: 173/199: : 910it [00:03, 253.11it/s, loss=0.005481]                      
eval psnr: 24.65
epoch: 174/199: : 910it [00:03, 250.15it/s, loss=0.005738]                      
eval psnr: 23.34
epoch: 175/199: : 910it [00:03, 242.70it/s, loss=0.005648]                      
eval psnr: 23.88
epoch: 176/199: : 910it [00:03, 249.84it/s, loss=0.005571]                      
eval psnr: 23.61
epoch: 177/199: : 910it [00:03, 251.93it/s, loss=0.005720]                      
eval psnr: 23.93
epoch: 178/199: : 910it [00:03, 250.04it/s, loss=0.005353]                      
eval psnr: 23.73
epoch: 179/199: : 910it [00:03, 248.64it/s, loss=0.005403]                      
eval psnr: 24.01
epoch: 180/199: : 910it [00:03, 250.05it/s, loss=0.005488]                      
eval psnr: 23.57
epoch: 181/199: : 910it [00:03, 243.72it/s, loss=0.005422]                      
eval psnr: 23.51
epoch: 182/199: : 910it [00:03, 243.88it/s, loss=0.005522]                      
eval psnr: 23.77
epoch: 183/199: : 910it [00:03, 252.54it/s, loss=0.005617]                      
eval psnr: 23.81
epoch: 184/199: : 910it [00:03, 252.66it/s, loss=0.005399]                      
eval psnr: 24.01
epoch: 185/199: : 910it [00:06, 136.60it/s, loss=0.005361]                      
eval psnr: 22.95
epoch: 186/199: : 910it [00:03, 241.03it/s, loss=0.005466]                      
eval psnr: 23.91
epoch: 187/199: : 910it [00:03, 243.00it/s, loss=0.005287]                      
eval psnr: 23.21
epoch: 188/199: : 910it [00:03, 245.19it/s, loss=0.005630]                      
eval psnr: 23.73
epoch: 189/199: : 910it [00:03, 255.96it/s, loss=0.005482]                      
eval psnr: 23.84
epoch: 190/199: : 910it [00:03, 240.80it/s, loss=0.005369]                      
eval psnr: 23.84
epoch: 191/199: : 910it [00:03, 244.92it/s, loss=0.005620]                      
eval psnr: 24.47
epoch: 192/199: : 910it [00:03, 243.00it/s, loss=0.005303]                      
eval psnr: 23.99
epoch: 193/199: : 910it [00:03, 232.41it/s, loss=0.005334]                      
eval psnr: 24.16
epoch: 194/199: : 910it [00:03, 246.41it/s, loss=0.005479]                      
eval psnr: 23.42
epoch: 195/199: : 910it [00:03, 232.47it/s, loss=0.005428]                      
eval psnr: 24.16
epoch: 196/199: : 910it [00:03, 240.41it/s, loss=0.005439]                      
eval psnr: 24.17
epoch: 197/199: : 910it [00:03, 237.18it/s, loss=0.005338]                      
eval psnr: 23.47
epoch: 198/199: : 910it [00:03, 243.08it/s, loss=0.005315]                      
eval psnr: 23.83
epoch: 199/199: : 910it [00:03, 243.36it/s, loss=0.005379]                      
eval psnr: 23.49
best epoch: 173, psnr: 24.65
"""
log9 = """
epoch: 0/199: : 910it [00:06, 143.29it/s, loss=0.069116]                        
eval psnr: 15.45
epoch: 1/199: : 910it [00:05, 158.09it/s, loss=0.021133]                        
eval psnr: 17.06
epoch: 2/199: : 910it [00:05, 173.91it/s, loss=0.017540]                        
eval psnr: 18.35
epoch: 3/199: : 910it [00:05, 159.37it/s, loss=0.015707]                        
eval psnr: 19.44
epoch: 4/199: : 910it [00:05, 166.49it/s, loss=0.014279]                        
eval psnr: 19.57
epoch: 5/199: : 910it [00:05, 180.52it/s, loss=0.013748]                        
eval psnr: 19.43
epoch: 6/199: : 910it [00:05, 177.84it/s, loss=0.013517]                        
eval psnr: 19.29
epoch: 7/199: : 910it [00:05, 166.51it/s, loss=0.013302]                        
eval psnr: 19.90
epoch: 8/199: : 910it [00:04, 190.16it/s, loss=0.012168]                        
eval psnr: 19.80
epoch: 9/199: : 910it [00:04, 191.16it/s, loss=0.011831]                        
eval psnr: 19.82
epoch: 10/199: : 910it [00:05, 166.64it/s, loss=0.011642]                       
eval psnr: 20.68
epoch: 11/199: : 910it [00:04, 189.85it/s, loss=0.011012]                       
eval psnr: 20.34
epoch: 12/199: : 910it [00:05, 165.32it/s, loss=0.010681]                       
eval psnr: 20.03
epoch: 13/199: : 910it [00:05, 160.68it/s, loss=0.010607]                       
eval psnr: 20.36
epoch: 14/199: : 910it [00:05, 165.76it/s, loss=0.009932]                       
eval psnr: 20.43
epoch: 15/199: : 910it [00:05, 178.54it/s, loss=0.010116]                       
eval psnr: 21.05
epoch: 16/199: : 910it [00:05, 178.33it/s, loss=0.009700]                       
eval psnr: 20.96
epoch: 17/199: : 910it [00:04, 182.75it/s, loss=0.009665]                       
eval psnr: 21.31
epoch: 18/199: : 910it [00:05, 175.56it/s, loss=0.009383]                       
eval psnr: 20.92
epoch: 19/199: : 910it [00:04, 183.20it/s, loss=0.008970]                       
eval psnr: 21.24
epoch: 20/199: : 910it [00:05, 170.38it/s, loss=0.009196]                       
eval psnr: 21.10
epoch: 21/199: : 910it [00:05, 163.57it/s, loss=0.009016]                       
eval psnr: 21.37
epoch: 22/199: : 910it [00:05, 158.15it/s, loss=0.008636]                       
eval psnr: 21.51
epoch: 23/199: : 910it [00:04, 189.81it/s, loss=0.008858]                       
eval psnr: 21.44
epoch: 24/199: : 910it [00:04, 188.71it/s, loss=0.008779]                       
eval psnr: 21.04
epoch: 25/199: : 910it [00:05, 168.34it/s, loss=0.008546]                       
eval psnr: 20.94
epoch: 26/199: : 910it [00:05, 179.40it/s, loss=0.008446]                       
eval psnr: 21.15
epoch: 27/199: : 910it [00:04, 184.95it/s, loss=0.008250]                       
eval psnr: 21.57
epoch: 28/199: : 910it [00:04, 182.07it/s, loss=0.008186]                       
eval psnr: 21.76
epoch: 29/199: : 910it [00:04, 187.07it/s, loss=0.008051]                       
eval psnr: 21.53
epoch: 30/199: : 910it [00:05, 173.80it/s, loss=0.007999]                       
eval psnr: 21.42
epoch: 31/199: : 910it [00:05, 166.64it/s, loss=0.007870]                       
eval psnr: 21.29
epoch: 32/199: : 910it [00:04, 190.72it/s, loss=0.007697]                       
eval psnr: 21.23
epoch: 33/199: : 910it [00:04, 184.17it/s, loss=0.007613]                       
eval psnr: 21.79
epoch: 34/199: : 910it [00:04, 183.67it/s, loss=0.007672]                       
eval psnr: 21.48
epoch: 35/199: : 910it [00:04, 189.67it/s, loss=0.007643]                       
eval psnr: 22.01
epoch: 36/199: : 910it [00:05, 174.84it/s, loss=0.007650]                       
eval psnr: 21.46
epoch: 37/199: : 910it [00:04, 193.44it/s, loss=0.007656]                       
eval psnr: 21.04
epoch: 38/199: : 910it [00:05, 167.25it/s, loss=0.007444]                       
eval psnr: 21.82
epoch: 39/199: : 910it [00:05, 177.14it/s, loss=0.007317]                       
eval psnr: 21.92
epoch: 40/199: : 910it [00:05, 166.49it/s, loss=0.007235]                       
eval psnr: 21.58
epoch: 41/199: : 910it [00:05, 168.15it/s, loss=0.007063]                       
eval psnr: 21.87
epoch: 42/199: : 910it [00:05, 160.35it/s, loss=0.007013]                       
eval psnr: 21.88
epoch: 43/199: : 910it [00:05, 163.74it/s, loss=0.006994]                       
eval psnr: 22.09
epoch: 44/199: : 910it [00:04, 183.88it/s, loss=0.007104]                       
eval psnr: 22.31
epoch: 45/199: : 910it [00:05, 158.92it/s, loss=0.006975]                       
eval psnr: 22.27
epoch: 46/199: : 910it [00:05, 159.02it/s, loss=0.006914]                       
eval psnr: 22.13
epoch: 47/199: : 910it [00:04, 183.54it/s, loss=0.007072]                       
eval psnr: 22.01
epoch: 48/199: : 910it [00:05, 180.91it/s, loss=0.007030]                       
eval psnr: 22.80
epoch: 49/199: : 910it [00:05, 162.21it/s, loss=0.006766]                       
eval psnr: 22.04
epoch: 50/199: : 910it [00:05, 172.40it/s, loss=0.006736]                       
eval psnr: 22.04
epoch: 51/199: : 910it [00:05, 167.12it/s, loss=0.006797]                       
eval psnr: 22.64
epoch: 52/199: : 910it [00:04, 189.49it/s, loss=0.006893]                       
eval psnr: 22.31
epoch: 53/199: : 910it [00:05, 176.72it/s, loss=0.006662]                       
eval psnr: 22.27
epoch: 54/199: : 910it [00:04, 184.97it/s, loss=0.006610]                       
eval psnr: 22.19
epoch: 55/199: : 910it [00:04, 192.53it/s, loss=0.006695]                       
eval psnr: 21.99
epoch: 56/199: : 910it [00:04, 193.61it/s, loss=0.006535]                       
eval psnr: 22.53
epoch: 57/199: : 910it [00:05, 177.28it/s, loss=0.006527]                       
eval psnr: 22.08
epoch: 58/199: : 910it [00:04, 193.79it/s, loss=0.006460]                       
eval psnr: 22.62
epoch: 59/199: : 910it [00:05, 152.46it/s, loss=0.006578]                       
eval psnr: 22.46
epoch: 60/199: : 910it [00:05, 165.97it/s, loss=0.006530]                       
eval psnr: 22.82
epoch: 61/199: : 910it [00:04, 183.02it/s, loss=0.006431]                       
eval psnr: 23.14
epoch: 62/199: : 910it [00:05, 170.46it/s, loss=0.006421]                       
eval psnr: 23.05
epoch: 63/199: : 910it [00:04, 186.32it/s, loss=0.006336]                       
eval psnr: 22.84
epoch: 64/199: : 910it [00:05, 166.96it/s, loss=0.006240]                       
eval psnr: 23.09
epoch: 65/199: : 910it [00:04, 193.88it/s, loss=0.006332]                       
eval psnr: 22.62
epoch: 66/199: : 910it [00:05, 165.41it/s, loss=0.006207]                       
eval psnr: 23.00
epoch: 67/199: : 910it [00:05, 176.83it/s, loss=0.006169]                       
eval psnr: 23.37
epoch: 68/199: : 910it [00:04, 191.41it/s, loss=0.006197]                       
eval psnr: 22.99
epoch: 69/199: : 910it [00:04, 192.46it/s, loss=0.006245]                       
eval psnr: 22.69
epoch: 70/199: : 910it [00:05, 174.37it/s, loss=0.006142]                       
eval psnr: 22.29
epoch: 71/199: : 910it [00:04, 193.17it/s, loss=0.006157]                       
eval psnr: 22.93
epoch: 72/199: : 910it [00:05, 171.01it/s, loss=0.006110]                       
eval psnr: 22.99
epoch: 73/199: : 910it [00:04, 183.35it/s, loss=0.006061]                       
eval psnr: 22.66
epoch: 74/199: : 910it [00:05, 155.48it/s, loss=0.005975]                       
eval psnr: 22.66
epoch: 75/199: : 910it [00:05, 158.80it/s, loss=0.006045]                       
eval psnr: 23.11
epoch: 76/199: : 910it [00:05, 170.72it/s, loss=0.006169]                       
eval psnr: 22.55
epoch: 77/199: : 910it [00:05, 172.91it/s, loss=0.005989]                       
eval psnr: 22.11
epoch: 78/199: : 910it [00:05, 170.04it/s, loss=0.005916]                       
eval psnr: 22.94
epoch: 79/199: : 910it [00:04, 189.44it/s, loss=0.005992]                       
eval psnr: 23.19
epoch: 80/199: : 910it [00:05, 172.15it/s, loss=0.005925]                       
eval psnr: 22.86
epoch: 81/199: : 910it [00:04, 195.89it/s, loss=0.006114]                       
eval psnr: 22.75
epoch: 82/199: : 910it [00:04, 183.38it/s, loss=0.006126]                       
eval psnr: 22.64
epoch: 83/199: : 910it [00:05, 167.53it/s, loss=0.005988]                       
eval psnr: 23.02
epoch: 84/199: : 910it [00:05, 164.49it/s, loss=0.005788]                       
eval psnr: 22.67
epoch: 85/199: : 910it [00:04, 192.42it/s, loss=0.005852]                       
eval psnr: 22.74
epoch: 86/199: : 910it [00:04, 198.76it/s, loss=0.005907]                       
eval psnr: 23.55
epoch: 87/199: : 910it [00:04, 185.26it/s, loss=0.005769]                       
eval psnr: 23.21
epoch: 88/199: : 910it [00:04, 194.16it/s, loss=0.006020]                       
eval psnr: 22.72
epoch: 89/199: : 910it [00:04, 195.01it/s, loss=0.005858]                       
eval psnr: 23.11
epoch: 90/199: : 910it [00:04, 195.52it/s, loss=0.005715]                       
eval psnr: 22.39
epoch: 91/199: : 910it [00:05, 181.34it/s, loss=0.005877]                       
eval psnr: 23.52
epoch: 92/199: : 910it [00:04, 189.23it/s, loss=0.005841]                       
eval psnr: 23.40
epoch: 93/199: : 910it [00:05, 169.11it/s, loss=0.005852]                       
eval psnr: 22.99
epoch: 94/199: : 910it [00:04, 186.62it/s, loss=0.005673]                       
eval psnr: 23.40
epoch: 95/199: : 910it [00:04, 184.32it/s, loss=0.005694]                       
eval psnr: 22.95
epoch: 96/199: : 910it [00:04, 191.51it/s, loss=0.005699]                       
eval psnr: 23.46
epoch: 97/199: : 910it [00:04, 195.11it/s, loss=0.005661]                       
eval psnr: 23.42
epoch: 98/199: : 910it [00:04, 195.52it/s, loss=0.005668]                       
eval psnr: 23.46
epoch: 99/199: : 910it [00:04, 193.05it/s, loss=0.005628]                       
eval psnr: 23.47
epoch: 100/199: : 910it [00:05, 167.50it/s, loss=0.005801]                      
eval psnr: 23.40
epoch: 101/199: : 910it [00:04, 186.12it/s, loss=0.005646]                      
eval psnr: 22.85
epoch: 102/199: : 910it [00:04, 195.77it/s, loss=0.005577]                      
eval psnr: 22.99
epoch: 103/199: : 910it [00:04, 195.20it/s, loss=0.005520]                      
eval psnr: 23.31
epoch: 104/199: : 910it [00:05, 158.23it/s, loss=0.005590]                      
eval psnr: 23.51
epoch: 105/199: : 910it [00:05, 163.08it/s, loss=0.005667]                      
eval psnr: 24.16
epoch: 106/199: : 910it [00:05, 165.10it/s, loss=0.005515]                      
eval psnr: 22.77
epoch: 107/199: : 910it [00:05, 162.80it/s, loss=0.005625]                      
eval psnr: 22.90
epoch: 108/199: : 910it [00:05, 180.80it/s, loss=0.005564]                      
eval psnr: 23.24
epoch: 109/199: : 910it [00:05, 159.31it/s, loss=0.005652]                      
eval psnr: 23.40
epoch: 110/199: : 910it [00:05, 181.15it/s, loss=0.005609]                      
eval psnr: 23.38
epoch: 111/199: : 910it [00:05, 157.85it/s, loss=0.005383]                      
eval psnr: 23.59
epoch: 112/199: : 910it [00:05, 180.88it/s, loss=0.005588]                      
eval psnr: 23.44
epoch: 113/199: : 910it [00:04, 190.98it/s, loss=0.005428]                      
eval psnr: 22.82
epoch: 114/199: : 910it [00:05, 169.58it/s, loss=0.005537]                      
eval psnr: 23.36
epoch: 115/199: : 910it [00:04, 183.04it/s, loss=0.005391]                      
eval psnr: 23.34
epoch: 116/199: : 910it [00:05, 156.36it/s, loss=0.005448]                      
eval psnr: 23.39
epoch: 117/199: : 910it [00:05, 161.85it/s, loss=0.005500]                      
eval psnr: 23.47
epoch: 118/199: : 910it [00:04, 184.48it/s, loss=0.005366]                      
eval psnr: 23.35
epoch: 119/199: : 910it [00:05, 169.89it/s, loss=0.005418]                      
eval psnr: 23.37
epoch: 120/199: : 910it [00:05, 170.99it/s, loss=0.005482]                      
eval psnr: 23.27
epoch: 121/199: : 910it [00:04, 195.18it/s, loss=0.005299]                      
eval psnr: 23.61
epoch: 122/199: : 910it [00:04, 197.81it/s, loss=0.005472]                      
eval psnr: 23.45
epoch: 123/199: : 910it [00:04, 192.75it/s, loss=0.005378]                      
eval psnr: 23.32
epoch: 124/199: : 910it [00:05, 165.92it/s, loss=0.005297]                      
eval psnr: 23.60
epoch: 125/199: : 910it [00:05, 158.14it/s, loss=0.005403]                      
eval psnr: 23.80
epoch: 126/199: : 910it [00:05, 180.02it/s, loss=0.005454]                      
eval psnr: 23.22
epoch: 127/199: : 910it [00:05, 152.37it/s, loss=0.005258]                      
eval psnr: 23.87
epoch: 128/199: : 910it [00:05, 165.41it/s, loss=0.005355]                      
eval psnr: 24.38
epoch: 129/199: : 910it [00:05, 171.25it/s, loss=0.005254]                      
eval psnr: 23.94
epoch: 130/199: : 910it [00:04, 182.16it/s, loss=0.005197]                      
eval psnr: 23.71
epoch: 131/199: : 910it [00:05, 157.50it/s, loss=0.005348]                      
eval psnr: 23.62
epoch: 132/199: : 910it [00:05, 159.40it/s, loss=0.005377]                      
eval psnr: 23.74
epoch: 133/199: : 910it [00:05, 164.54it/s, loss=0.005363]                      
eval psnr: 23.49
epoch: 134/199: : 910it [00:04, 191.66it/s, loss=0.005251]                      
eval psnr: 23.70
epoch: 135/199: : 910it [00:05, 156.67it/s, loss=0.005232]                      
eval psnr: 23.65
epoch: 136/199: : 910it [00:04, 184.31it/s, loss=0.005246]                      
eval psnr: 22.88
epoch: 137/199: : 910it [00:05, 162.57it/s, loss=0.005193]                      
eval psnr: 23.87
epoch: 138/199: : 910it [00:04, 183.59it/s, loss=0.005123]                      
eval psnr: 23.65
epoch: 139/199: : 910it [00:05, 159.08it/s, loss=0.005144]                      
eval psnr: 24.15
epoch: 140/199: : 910it [00:04, 191.31it/s, loss=0.005102]                      
eval psnr: 23.83
epoch: 141/199: : 910it [00:04, 182.40it/s, loss=0.005209]                      
eval psnr: 23.68
epoch: 142/199: : 910it [00:04, 184.56it/s, loss=0.005312]                      
eval psnr: 23.88
epoch: 143/199: : 910it [00:04, 183.23it/s, loss=0.005199]                      
eval psnr: 24.23
epoch: 144/199: : 910it [00:05, 160.13it/s, loss=0.005186]                      
eval psnr: 23.72
epoch: 145/199: : 910it [00:05, 158.27it/s, loss=0.005134]                      
eval psnr: 23.54
epoch: 146/199: : 910it [00:05, 180.95it/s, loss=0.005257]                      
eval psnr: 23.92
epoch: 147/199: : 910it [00:05, 159.12it/s, loss=0.005214]                      
eval psnr: 23.34
epoch: 148/199: : 910it [00:05, 163.04it/s, loss=0.005253]                      
eval psnr: 23.94
epoch: 149/199: : 910it [00:05, 171.42it/s, loss=0.004994]                      
eval psnr: 23.88
epoch: 150/199: : 910it [00:05, 159.94it/s, loss=0.005083]                      
eval psnr: 23.52
epoch: 151/199: : 910it [00:05, 169.56it/s, loss=0.005089]                      
eval psnr: 23.27
epoch: 152/199: : 910it [00:06, 149.85it/s, loss=0.005182]                      
eval psnr: 23.65
epoch: 153/199: : 910it [00:05, 162.83it/s, loss=0.005235]                      
eval psnr: 23.92
epoch: 154/199: : 910it [00:05, 164.40it/s, loss=0.005135]                      
eval psnr: 23.50
epoch: 155/199: : 910it [00:04, 183.70it/s, loss=0.004979]                      
eval psnr: 24.15
epoch: 156/199: : 910it [00:06, 149.40it/s, loss=0.005088]                      
eval psnr: 23.83
epoch: 157/199: : 910it [00:05, 166.58it/s, loss=0.005014]                      
eval psnr: 24.32
epoch: 158/199: : 910it [00:05, 167.50it/s, loss=0.005022]                      
eval psnr: 24.14
epoch: 159/199: : 910it [00:04, 190.47it/s, loss=0.004933]                      
eval psnr: 24.17
epoch: 160/199: : 910it [00:04, 194.00it/s, loss=0.004969]                      
eval psnr: 23.92
epoch: 161/199: : 910it [00:05, 175.13it/s, loss=0.005053]                      
eval psnr: 23.85
epoch: 162/199: : 910it [00:04, 185.21it/s, loss=0.005010]                      
eval psnr: 23.45
epoch: 163/199: : 910it [00:04, 187.22it/s, loss=0.005094]                      
eval psnr: 23.16
epoch: 164/199: : 910it [00:05, 153.67it/s, loss=0.005122]                      
eval psnr: 23.79
epoch: 165/199: : 910it [00:04, 199.32it/s, loss=0.005102]                      
eval psnr: 23.84
epoch: 166/199: : 910it [00:05, 164.38it/s, loss=0.005006]                      
eval psnr: 23.92
epoch: 167/199: : 910it [00:05, 169.67it/s, loss=0.004957]                      
eval psnr: 23.89
epoch: 168/199: : 910it [00:05, 180.00it/s, loss=0.004869]                      
eval psnr: 23.87
epoch: 169/199: : 910it [00:05, 174.15it/s, loss=0.005035]                      
eval psnr: 23.82
epoch: 170/199: : 910it [00:05, 176.46it/s, loss=0.004921]                      
eval psnr: 23.02
epoch: 171/199: : 910it [00:04, 183.21it/s, loss=0.005163]                      
eval psnr: 23.38
epoch: 172/199: : 910it [00:05, 159.26it/s, loss=0.005163]                      
eval psnr: 23.30
epoch: 173/199: : 910it [00:05, 162.56it/s, loss=0.005197]                      
eval psnr: 23.74
epoch: 174/199: : 910it [00:05, 159.83it/s, loss=0.004913]                      
eval psnr: 23.22
epoch: 175/199: : 910it [00:04, 183.89it/s, loss=0.005025]                      
eval psnr: 24.08
epoch: 176/199: : 910it [00:05, 167.88it/s, loss=0.004848]                      
eval psnr: 23.53
epoch: 177/199: : 910it [00:04, 185.40it/s, loss=0.004903]                      
eval psnr: 23.51
epoch: 178/199: : 910it [00:05, 181.43it/s, loss=0.004913]                      
eval psnr: 24.09
epoch: 179/199: : 910it [00:04, 185.60it/s, loss=0.004883]                      
eval psnr: 23.49
epoch: 180/199: : 910it [00:04, 187.63it/s, loss=0.005003]                      
eval psnr: 24.55
epoch: 181/199: : 910it [00:05, 178.11it/s, loss=0.005027]                      
eval psnr: 24.02
epoch: 182/199: : 910it [00:05, 153.44it/s, loss=0.004896]                      
eval psnr: 23.66
epoch: 183/199: : 910it [00:05, 177.71it/s, loss=0.004808]                      
eval psnr: 23.89
epoch: 184/199: : 910it [00:05, 156.40it/s, loss=0.004843]                      
eval psnr: 24.29
epoch: 185/199: : 910it [00:04, 185.68it/s, loss=0.004894]                      
eval psnr: 23.20
epoch: 186/199: : 910it [00:05, 170.15it/s, loss=0.004736]                      
eval psnr: 23.97
epoch: 187/199: : 910it [00:05, 167.02it/s, loss=0.004734]                      
eval psnr: 23.25
epoch: 188/199: : 910it [00:04, 193.42it/s, loss=0.004825]                      
eval psnr: 23.67
epoch: 189/199: : 910it [00:04, 187.21it/s, loss=0.004793]                      
eval psnr: 23.97
epoch: 190/199: : 910it [00:04, 198.47it/s, loss=0.004826]                      
eval psnr: 23.69
epoch: 191/199: : 910it [00:04, 200.53it/s, loss=0.004672]                      
eval psnr: 23.15
epoch: 192/199: : 910it [00:05, 166.36it/s, loss=0.004850]                      
eval psnr: 23.88
epoch: 193/199: : 910it [00:04, 198.22it/s, loss=0.004823]                      
eval psnr: 23.26
epoch: 194/199: : 910it [00:04, 185.08it/s, loss=0.004872]                      
eval psnr: 24.37
epoch: 195/199: : 910it [00:05, 152.60it/s, loss=0.004922]                      
eval psnr: 23.56
epoch: 196/199: : 910it [00:04, 182.77it/s, loss=0.004827]                      
eval psnr: 24.03
epoch: 197/199: : 910it [00:05, 161.87it/s, loss=0.004788]                      
eval psnr: 23.98
epoch: 198/199: : 910it [00:04, 195.68it/s, loss=0.004863]                      
eval psnr: 23.81
epoch: 199/199: : 910it [00:05, 170.50it/s, loss=0.004758]                      
eval psnr: 24.46
best epoch: 180, psnr: 24.55
"""
log10 = """
epoch: 0/199: : 910it [00:07, 125.01it/s, loss=0.059963]                        
eval psnr: 15.53
epoch: 1/199: : 910it [00:06, 145.13it/s, loss=0.020382]                        
eval psnr: 17.94
epoch: 2/199: : 910it [00:07, 124.10it/s, loss=0.017755]                        
eval psnr: 18.64
epoch: 3/199: : 910it [00:06, 140.09it/s, loss=0.016235]                        
eval psnr: 19.00
epoch: 4/199: : 910it [00:06, 149.74it/s, loss=0.014703]                        
eval psnr: 19.39
epoch: 5/199: : 910it [00:06, 139.87it/s, loss=0.014018]                        
eval psnr: 19.72
epoch: 6/199: : 910it [00:06, 130.22it/s, loss=0.013291]                        
eval psnr: 19.73
epoch: 7/199: : 910it [00:06, 131.24it/s, loss=0.012743]                        
eval psnr: 19.34
epoch: 8/199: : 910it [00:05, 154.88it/s, loss=0.012081]                        
eval psnr: 19.71
epoch: 9/199: : 910it [00:06, 130.68it/s, loss=0.011898]                        
eval psnr: 20.39
epoch: 10/199: : 910it [00:06, 134.13it/s, loss=0.011312]                       
eval psnr: 20.07
epoch: 11/199: : 910it [00:06, 144.72it/s, loss=0.011054]                       
eval psnr: 20.41
epoch: 12/199: : 910it [00:06, 150.45it/s, loss=0.010592]                       
eval psnr: 20.55
epoch: 13/199: : 910it [00:06, 136.71it/s, loss=0.010096]                       
eval psnr: 20.60
epoch: 14/199: : 910it [00:06, 149.06it/s, loss=0.010128]                       
eval psnr: 20.55
epoch: 15/199: : 910it [00:06, 145.33it/s, loss=0.009538]                       
eval psnr: 21.06
epoch: 16/199: : 910it [00:07, 127.81it/s, loss=0.009338]                       
eval psnr: 20.77
epoch: 17/199: : 910it [00:07, 128.55it/s, loss=0.009782]                       
eval psnr: 20.99
epoch: 18/199: : 910it [00:06, 137.80it/s, loss=0.009113]                       
eval psnr: 20.89
epoch: 19/199: : 910it [00:05, 155.33it/s, loss=0.008781]                       
eval psnr: 21.43
epoch: 20/199: : 910it [00:05, 151.67it/s, loss=0.008767]                       
eval psnr: 21.63
epoch: 21/199: : 910it [00:05, 151.76it/s, loss=0.008713]                       
eval psnr: 21.49
epoch: 22/199: : 910it [00:07, 124.93it/s, loss=0.008808]                       
eval psnr: 21.94
epoch: 23/199: : 910it [00:06, 138.81it/s, loss=0.008402]                       
eval psnr: 20.99
epoch: 24/199: : 910it [00:06, 136.50it/s, loss=0.008308]                       
eval psnr: 21.36
epoch: 25/199: : 910it [00:05, 152.93it/s, loss=0.008191]                       
eval psnr: 21.41
epoch: 26/199: : 910it [00:06, 135.44it/s, loss=0.008191]                       
eval psnr: 22.14
epoch: 27/199: : 910it [00:05, 153.98it/s, loss=0.008015]                       
eval psnr: 21.55
epoch: 28/199: : 910it [00:06, 136.82it/s, loss=0.007911]                       
eval psnr: 21.84
epoch: 29/199: : 910it [00:06, 137.53it/s, loss=0.007866]                       
eval psnr: 22.00
epoch: 30/199: : 910it [00:06, 148.76it/s, loss=0.007627]                       
eval psnr: 21.59
epoch: 31/199: : 910it [00:06, 133.73it/s, loss=0.007447]                       
eval psnr: 21.56
epoch: 32/199: : 910it [00:07, 129.47it/s, loss=0.007694]                       
eval psnr: 21.24
epoch: 33/199: : 910it [00:07, 126.79it/s, loss=0.007482]                       
eval psnr: 22.28
epoch: 34/199: : 910it [00:06, 143.20it/s, loss=0.007438]                       
eval psnr: 22.38
epoch: 35/199: : 910it [00:06, 145.37it/s, loss=0.007488]                       
eval psnr: 22.02
epoch: 36/199: : 910it [00:06, 135.72it/s, loss=0.007477]                       
eval psnr: 21.61
epoch: 37/199: : 910it [00:06, 141.08it/s, loss=0.007296]                       
eval psnr: 21.93
epoch: 38/199: : 910it [00:07, 125.52it/s, loss=0.007035]                       
eval psnr: 22.32
epoch: 39/199: : 910it [00:07, 124.34it/s, loss=0.007088]                       
eval psnr: 22.35
epoch: 40/199: : 910it [00:06, 131.00it/s, loss=0.007093]                       
eval psnr: 22.32
epoch: 41/199: : 910it [00:06, 150.91it/s, loss=0.006913]                       
eval psnr: 22.25
epoch: 42/199: : 910it [00:06, 135.01it/s, loss=0.007059]                       
eval psnr: 22.16
epoch: 43/199: : 910it [00:07, 128.57it/s, loss=0.007357]                       
eval psnr: 21.97
epoch: 44/199: : 910it [00:07, 129.48it/s, loss=0.006958]                       
eval psnr: 22.78
epoch: 45/199: : 910it [00:06, 140.36it/s, loss=0.006927]                       
eval psnr: 22.66
epoch: 46/199: : 910it [00:06, 150.02it/s, loss=0.006793]                       
eval psnr: 22.86
epoch: 47/199: : 910it [00:07, 124.69it/s, loss=0.006901]                       
eval psnr: 22.23
epoch: 48/199: : 910it [00:06, 130.33it/s, loss=0.007182]                       
eval psnr: 22.45
epoch: 49/199: : 910it [00:06, 137.05it/s, loss=0.007008]                       
eval psnr: 22.54
epoch: 50/199: : 910it [00:07, 126.90it/s, loss=0.006746]                       
eval psnr: 22.89
epoch: 51/199: : 910it [00:06, 134.26it/s, loss=0.006540]                       
eval psnr: 22.01
epoch: 52/199: : 910it [00:06, 142.59it/s, loss=0.006754]                       
eval psnr: 22.39
epoch: 53/199: : 910it [00:06, 141.19it/s, loss=0.006586]                       
eval psnr: 22.01
epoch: 54/199: : 910it [00:07, 128.73it/s, loss=0.006485]                       
eval psnr: 22.33
epoch: 55/199: : 910it [00:06, 146.79it/s, loss=0.006691]                       
eval psnr: 22.01
epoch: 56/199: : 910it [00:06, 141.23it/s, loss=0.006442]                       
eval psnr: 22.86
epoch: 57/199: : 910it [00:06, 140.85it/s, loss=0.006403]                       
eval psnr: 23.26
epoch: 58/199: : 910it [00:05, 152.29it/s, loss=0.006657]                       
eval psnr: 22.79
epoch: 59/199: : 910it [00:06, 135.30it/s, loss=0.006275]                       
eval psnr: 22.84
epoch: 60/199: : 910it [00:07, 120.62it/s, loss=0.006383]                       
eval psnr: 22.67
epoch: 61/199: : 910it [00:06, 135.54it/s, loss=0.006449]                       
eval psnr: 22.81
epoch: 62/199: : 910it [00:07, 125.70it/s, loss=0.006315]                       
eval psnr: 22.72
epoch: 63/199: : 910it [00:06, 136.61it/s, loss=0.006231]                       
eval psnr: 22.92
epoch: 64/199: : 910it [00:06, 146.36it/s, loss=0.006222]                       
eval psnr: 22.37
epoch: 65/199: : 910it [00:07, 121.53it/s, loss=0.006313]                       
eval psnr: 23.08
epoch: 66/199: : 910it [00:06, 143.45it/s, loss=0.006109]                       
eval psnr: 22.86
epoch: 67/199: : 910it [00:06, 138.30it/s, loss=0.006129]                       
eval psnr: 22.91
epoch: 68/199: : 910it [00:05, 151.79it/s, loss=0.006310]                       
eval psnr: 22.57
epoch: 69/199: : 910it [00:06, 131.11it/s, loss=0.006152]                       
eval psnr: 23.22
epoch: 70/199: : 910it [00:07, 127.09it/s, loss=0.006237]                       
eval psnr: 22.38
epoch: 71/199: : 910it [00:06, 140.37it/s, loss=0.006400]                       
eval psnr: 22.67
epoch: 72/199: : 910it [00:07, 125.09it/s, loss=0.006145]                       
eval psnr: 22.47
epoch: 73/199: : 910it [00:06, 134.82it/s, loss=0.006070]                       
eval psnr: 22.87
epoch: 74/199: : 910it [00:06, 136.31it/s, loss=0.006139]                       
eval psnr: 23.01
epoch: 75/199: : 910it [00:06, 143.78it/s, loss=0.006022]                       
eval psnr: 23.13
epoch: 76/199: : 910it [00:07, 122.94it/s, loss=0.006064]                       
eval psnr: 23.27
epoch: 77/199: : 910it [00:07, 118.66it/s, loss=0.005823]                       
eval psnr: 23.21
epoch: 78/199: : 910it [00:06, 133.78it/s, loss=0.005812]                       
eval psnr: 23.77
epoch: 79/199: : 910it [00:06, 136.80it/s, loss=0.005874]                       
eval psnr: 23.66
epoch: 80/199: : 910it [00:07, 126.41it/s, loss=0.005974]                       
eval psnr: 23.03
epoch: 81/199: : 910it [00:06, 135.71it/s, loss=0.005864]                       
eval psnr: 23.03
epoch: 82/199: : 910it [00:06, 149.62it/s, loss=0.005980]                       
eval psnr: 23.12
epoch: 83/199: : 910it [00:07, 129.56it/s, loss=0.005969]                       
eval psnr: 22.70
epoch: 84/199: : 910it [00:06, 146.98it/s, loss=0.005794]                       
eval psnr: 23.51
epoch: 85/199: : 910it [00:06, 133.00it/s, loss=0.005828]                       
eval psnr: 23.00
epoch: 86/199: : 910it [00:06, 135.16it/s, loss=0.005649]                       
eval psnr: 23.46
epoch: 87/199: : 910it [00:06, 138.13it/s, loss=0.005862]                       
eval psnr: 23.04
epoch: 88/199: : 910it [00:07, 125.61it/s, loss=0.005794]                       
eval psnr: 23.14
epoch: 89/199: : 910it [00:06, 142.53it/s, loss=0.005586]                       
eval psnr: 23.68
epoch: 90/199: : 910it [00:06, 142.17it/s, loss=0.005787]                       
eval psnr: 23.58
epoch: 91/199: : 910it [00:06, 148.77it/s, loss=0.005627]                       
eval psnr: 23.37
epoch: 92/199: : 910it [00:07, 126.75it/s, loss=0.005760]                       
eval psnr: 23.30
epoch: 93/199: : 910it [00:06, 136.83it/s, loss=0.005791]                       
eval psnr: 23.98
epoch: 94/199: : 910it [00:05, 152.23it/s, loss=0.005831]                       
eval psnr: 23.11
epoch: 95/199: : 910it [00:06, 146.05it/s, loss=0.005647]                       
eval psnr: 23.45
epoch: 96/199: : 910it [00:06, 149.36it/s, loss=0.005585]                       
eval psnr: 23.34
epoch: 97/199: : 910it [00:07, 126.31it/s, loss=0.005813]                       
eval psnr: 23.29
epoch: 98/199: : 910it [00:07, 126.27it/s, loss=0.005645]                       
eval psnr: 23.37
epoch: 99/199: : 910it [00:07, 124.98it/s, loss=0.005552]                       
eval psnr: 23.93
epoch: 100/199: : 910it [00:06, 142.93it/s, loss=0.005620]                      
eval psnr: 23.44
epoch: 101/199: : 910it [00:06, 138.59it/s, loss=0.005408]                      
eval psnr: 23.09
epoch: 102/199: : 910it [00:06, 142.31it/s, loss=0.005565]                      
eval psnr: 23.66
epoch: 103/199: : 910it [00:07, 127.02it/s, loss=0.005536]                      
eval psnr: 23.18
epoch: 104/199: : 910it [00:05, 151.72it/s, loss=0.005465]                      
eval psnr: 23.13
epoch: 105/199: : 910it [00:06, 136.51it/s, loss=0.005557]                      
eval psnr: 23.42
epoch: 106/199: : 910it [00:06, 130.81it/s, loss=0.005348]                      
eval psnr: 23.99
epoch: 107/199: : 910it [00:07, 124.02it/s, loss=0.005367]                      
eval psnr: 22.99
epoch: 108/199: : 910it [00:07, 125.52it/s, loss=0.005423]                      
eval psnr: 23.16
epoch: 109/199: : 910it [00:06, 148.15it/s, loss=0.005503]                      
eval psnr: 23.17
epoch: 110/199: : 910it [00:07, 127.62it/s, loss=0.005442]                      
eval psnr: 23.44
epoch: 111/199: : 910it [00:06, 148.49it/s, loss=0.005445]                      
eval psnr: 23.49
epoch: 112/199: : 910it [00:07, 124.95it/s, loss=0.005354]                      
eval psnr: 23.82
epoch: 113/199: : 910it [00:06, 138.71it/s, loss=0.005232]                      
eval psnr: 23.92
epoch: 114/199: : 910it [00:07, 123.84it/s, loss=0.005271]                      
eval psnr: 23.89
epoch: 115/199: : 910it [00:07, 128.95it/s, loss=0.005271]                      
eval psnr: 23.69
epoch: 116/199: : 910it [00:06, 150.02it/s, loss=0.005455]                      
eval psnr: 23.79
epoch: 117/199: : 910it [00:06, 148.86it/s, loss=0.005376]                      
eval psnr: 23.26
epoch: 118/199: : 910it [00:06, 142.84it/s, loss=0.005371]                      
eval psnr: 23.17
epoch: 119/199: : 910it [00:06, 137.11it/s, loss=0.005432]                      
eval psnr: 23.24
epoch: 120/199: : 910it [00:06, 130.71it/s, loss=0.005334]                      
eval psnr: 23.93
epoch: 121/199: : 910it [00:06, 140.79it/s, loss=0.005355]                      
eval psnr: 23.65
epoch: 122/199: : 910it [00:06, 147.20it/s, loss=0.005287]                      
eval psnr: 23.25
epoch: 123/199: : 910it [00:06, 136.51it/s, loss=0.005260]                      
eval psnr: 23.52
epoch: 124/199: : 910it [00:06, 145.78it/s, loss=0.005391]                      
eval psnr: 23.60
epoch: 125/199: : 910it [00:06, 146.76it/s, loss=0.005328]                      
eval psnr: 23.89
epoch: 126/199: : 910it [00:06, 132.35it/s, loss=0.005155]                      
eval psnr: 24.32
epoch: 127/199: : 910it [00:06, 141.85it/s, loss=0.005297]                      
eval psnr: 23.48
epoch: 128/199: : 910it [00:06, 146.54it/s, loss=0.005409]                      
eval psnr: 23.55
epoch: 129/199: : 910it [00:06, 146.62it/s, loss=0.005182]                      
eval psnr: 24.25
epoch: 130/199: : 910it [00:06, 150.33it/s, loss=0.005154]                      
eval psnr: 23.26
epoch: 131/199: : 910it [00:06, 145.43it/s, loss=0.005249]                      
eval psnr: 24.08
epoch: 132/199: : 910it [00:07, 126.96it/s, loss=0.005228]                      
eval psnr: 23.54
epoch: 133/199: : 910it [00:06, 139.52it/s, loss=0.005308]                      
eval psnr: 23.70
epoch: 134/199: : 910it [00:05, 152.24it/s, loss=0.005157]                      
eval psnr: 23.83
epoch: 135/199: : 910it [00:06, 130.85it/s, loss=0.005335]                      
eval psnr: 23.36
epoch: 136/199: : 910it [00:07, 128.73it/s, loss=0.005290]                      
eval psnr: 23.89
epoch: 137/199: : 910it [00:06, 131.38it/s, loss=0.005233]                      
eval psnr: 23.69
epoch: 138/199: : 910it [00:06, 141.15it/s, loss=0.005040]                      
eval psnr: 24.33
epoch: 139/199: : 910it [00:06, 146.98it/s, loss=0.005328]                      
eval psnr: 23.25
epoch: 140/199: : 910it [00:06, 147.78it/s, loss=0.005419]                      
eval psnr: 23.78
epoch: 141/199: : 910it [00:06, 149.03it/s, loss=0.005362]                      
eval psnr: 23.69
epoch: 142/199: : 910it [00:06, 151.11it/s, loss=0.005281]                      
eval psnr: 23.76
epoch: 143/199: : 910it [00:06, 150.38it/s, loss=0.005166]                      
eval psnr: 23.91
epoch: 144/199: : 910it [00:07, 126.63it/s, loss=0.005219]                      
eval psnr: 23.61
epoch: 145/199: : 910it [00:06, 142.09it/s, loss=0.005071]                      
eval psnr: 24.41
epoch: 146/199: : 910it [00:06, 139.93it/s, loss=0.005201]                      
eval psnr: 23.97
epoch: 147/199: : 910it [00:06, 136.58it/s, loss=0.005143]                      
eval psnr: 23.87
epoch: 148/199: : 910it [00:07, 124.48it/s, loss=0.005308]                      
eval psnr: 23.90
epoch: 149/199: : 910it [00:07, 128.27it/s, loss=0.005303]                      
eval psnr: 23.33
epoch: 150/199: : 910it [00:06, 134.44it/s, loss=0.005078]                      
eval psnr: 24.32
epoch: 151/199: : 910it [00:06, 132.27it/s, loss=0.004995]                      
eval psnr: 24.93
epoch: 152/199: : 910it [00:07, 123.84it/s, loss=0.005037]                      
eval psnr: 24.43
epoch: 153/199: : 910it [00:06, 133.90it/s, loss=0.005081]                      
eval psnr: 23.83
epoch: 154/199: : 910it [00:06, 136.40it/s, loss=0.005048]                      
eval psnr: 23.56
epoch: 155/199: : 910it [00:06, 138.90it/s, loss=0.005319]                      
eval psnr: 24.00
epoch: 156/199: : 910it [00:06, 143.92it/s, loss=0.005099]                      
eval psnr: 24.08
epoch: 157/199: : 910it [00:07, 124.98it/s, loss=0.004988]                      
eval psnr: 23.52
epoch: 158/199: : 910it [00:06, 149.33it/s, loss=0.005033]                      
eval psnr: 24.45
epoch: 159/199: : 910it [00:06, 130.71it/s, loss=0.004865]                      
eval psnr: 24.42
epoch: 160/199: : 910it [00:06, 141.91it/s, loss=0.005080]                      
eval psnr: 23.69
epoch: 161/199: : 910it [00:06, 134.27it/s, loss=0.004936]                      
eval psnr: 23.90
epoch: 162/199: : 910it [00:07, 127.88it/s, loss=0.004910]                      
eval psnr: 24.31
epoch: 163/199: : 910it [00:07, 125.18it/s, loss=0.004881]                      
eval psnr: 23.92
epoch: 164/199: : 910it [00:06, 149.49it/s, loss=0.004877]                      
eval psnr: 24.10
epoch: 165/199: : 910it [00:06, 136.56it/s, loss=0.004897]                      
eval psnr: 24.05
epoch: 166/199: : 910it [00:07, 123.64it/s, loss=0.004925]                      
eval psnr: 23.58
epoch: 167/199: : 910it [00:06, 142.40it/s, loss=0.004805]                      
eval psnr: 24.15
epoch: 168/199: : 910it [00:06, 138.92it/s, loss=0.004865]                      
eval psnr: 23.94
epoch: 169/199: : 910it [00:07, 122.37it/s, loss=0.004831]                      
eval psnr: 23.68
epoch: 170/199: : 910it [00:06, 151.06it/s, loss=0.004832]                      
eval psnr: 23.97
epoch: 171/199: : 910it [00:06, 143.27it/s, loss=0.004711]                      
eval psnr: 24.28
epoch: 172/199: : 910it [00:06, 130.82it/s, loss=0.004839]                      
eval psnr: 23.87
epoch: 173/199: : 910it [00:07, 129.40it/s, loss=0.004787]                      
eval psnr: 23.44
epoch: 174/199: : 910it [00:07, 126.02it/s, loss=0.004774]                      
eval psnr: 23.86
epoch: 175/199: : 910it [00:06, 149.90it/s, loss=0.004761]                      
eval psnr: 23.80
epoch: 176/199: : 910it [00:06, 149.62it/s, loss=0.004729]                      
eval psnr: 24.11
epoch: 177/199: : 910it [00:06, 144.84it/s, loss=0.004860]                      
eval psnr: 23.62
epoch: 178/199: : 910it [00:06, 147.06it/s, loss=0.004730]                      
eval psnr: 24.06
epoch: 179/199: : 910it [00:06, 131.93it/s, loss=0.004799]                      
eval psnr: 24.31
epoch: 180/199: : 910it [00:07, 128.81it/s, loss=0.004785]                      
eval psnr: 24.03
epoch: 181/199: : 910it [00:06, 151.43it/s, loss=0.004701]                      
eval psnr: 23.82
epoch: 182/199: : 910it [00:07, 123.10it/s, loss=0.004629]                      
eval psnr: 23.88
epoch: 183/199: : 910it [00:06, 134.36it/s, loss=0.004655]                      
eval psnr: 24.11
epoch: 184/199: : 910it [00:06, 136.13it/s, loss=0.004570]                      
eval psnr: 23.75
epoch: 185/199: : 910it [00:06, 136.64it/s, loss=0.004656]                      
eval psnr: 23.37
epoch: 186/199: : 910it [00:06, 134.96it/s, loss=0.004658]                      
eval psnr: 24.14
epoch: 187/199: : 910it [00:06, 143.66it/s, loss=0.004568]                      
eval psnr: 24.62
epoch: 188/199: : 910it [00:06, 142.80it/s, loss=0.004466]                      
eval psnr: 24.29
epoch: 189/199: : 910it [00:07, 123.93it/s, loss=0.004755]                      
eval psnr: 24.23
epoch: 190/199: : 910it [00:06, 142.09it/s, loss=0.004633]                      
eval psnr: 24.28
epoch: 191/199: : 910it [00:05, 152.90it/s, loss=0.004561]                      
eval psnr: 24.25
epoch: 192/199: : 910it [00:06, 139.94it/s, loss=0.004612]                      
eval psnr: 24.31
epoch: 193/199: : 910it [00:06, 144.45it/s, loss=0.004607]                      
eval psnr: 23.64
epoch: 194/199: : 910it [00:06, 141.04it/s, loss=0.004592]                      
eval psnr: 24.11
epoch: 195/199: : 910it [00:06, 139.37it/s, loss=0.004526]                      
eval psnr: 23.64
epoch: 196/199: : 910it [00:06, 131.09it/s, loss=0.004514]                      
eval psnr: 24.70
epoch: 197/199: : 910it [00:06, 149.49it/s, loss=0.004513]                      
eval psnr: 24.04
epoch: 198/199: : 910it [00:07, 124.12it/s, loss=0.004615]                      
eval psnr: 24.76
epoch: 199/199: : 910it [00:06, 130.40it/s, loss=0.004524]                      
eval psnr: 24.20
best epoch: 151, psnr: 24.93
"""
def analyze(log):
    evalpsnr = []
    epoch = []
    bestepoch = ''
    for i in log.split('\n'):
        if 'best epoch' in i:
            bestepoch = i
        elif 'eval psnr' in i:
            evalpsnr.append(i)
        elif 'epoch' in i:
            epoch.append(i)
    loss = []
    psnr = []
    for i in epoch:
        _loss = float(i.split('loss=')[1].split(']')[0])
        loss.append(_loss)
    for i in evalpsnr:
        _psnr = float(i.split('eval psnr: ')[1])
        psnr.append(_psnr)
    return psnr, bestepoch, loss

psnr1, bestepoch1, loss1 = analyze(log1)
psnr2, bestepoch2, loss2 = analyze(log2)
psnr3, bestepoch3, loss3 = analyze(log3)
psnr4, bestepoch4, loss4 = analyze(log4)
psnr5, bestepoch5, loss5 = analyze(log5)
psnr6, bestepoch6, loss6 = analyze(log6)
psnr7, bestepoch7, loss7 = analyze(log7)
psnr8, bestepoch8, loss8 = analyze(log8)
psnr9, bestepoch9, loss9 = analyze(log9)
psnr10, bestepoch10, loss10 = analyze(log10)
plt.figure()
# plt.plot(loss1, label='SRCNN Loss')
plt.plot(loss2, label='SRResNet Loss')
#plt.plot(loss3, label='VDSR Loss')
#plt.plot(loss4, label='CARN Loss')
#plt.plot(loss5, label='MemNet Loss')
#plt.plot(loss6, label='SRGAN Loss')
# plt.plot(loss7, label='SRCNNA Loss')
plt.plot(loss8, label='DASRCNN Loss')
plt.plot(loss9, label='SRResSCA Loss')
plt.plot(loss10, label='SRResSCA-64 Loss')
plt.title('Loss')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
# plt.plot(psnr1, label='SRCNN psnr')
plt.plot(psnr2, label='SRResNet psnr')
#plt.plot(psnr3, label='VDSR psnr')
#plt.plot(psnr4, label='CARN psnr')
#plt.plot(psnr5, label='MemNet psnr')
#plt.plot(psnr6, label='SRGAN psnr')
# plt.plot(psnr7, label='SRCNNA psnr')
plt.plot(psnr8, label='DASRCNN psnr')
plt.plot(psnr9, label='SRResSCA psnr')
plt.plot(psnr10, label='SRResSCA-64 psnr')
plt.title('psnr')
plt.legend()
plt.grid(True)
plt.show()



print('dd')

