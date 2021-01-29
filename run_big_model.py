from cn_correct import CompareCorrect as CC
from warnings import filterwarnings
from traceback import format_exc

if __name__=='__main__':
    filterwarnings('ignore')
    model_spec_list=[
        {'lin-reg':{'max_poly_deg':3,'fit_intercept':False}},
        {'lasso':{'max_poly_deg':3,'fit_intercept':False}},
        {'gbr':{
            'kwargs':{},#these pass through to sklearn's gbr
                #'n_estimators':10000,
                #'subsample':1,
                #'max_depth':3
                }},
        
    ]
    for model_spec in model_spec_list:
        try:
            cc=CC()
            cc.modeldict['model_specs']=model_spec
            print('modeldict',cc.modeldict)
            cc.runBigModel()
            print('complete')
        except:
            print(format_exc())
            
    
    

    
