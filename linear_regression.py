#some possible inputs
N = 5
M = 5
X = np.matrix(np.random.normal(1,1,N*M)).reshape(N,M)
Y = np.matrix(np.random.normal(1,1,N*1)).reshape(N,1)
x_test_to_predict = np.matrix(np.random.normal(1,1,N*M)).reshape(N,M)
###############
#####This class takes into account possible known heteroscedasticity of errors
###############
class LinearRegression_:
    "multivariate OLS with heteroscedasticity"
    def __init__(self, Y, X):
        self.X = np.c_[np.ones(X.shape[0]), X]
        self.Y = Y
        self.obs = X.shape[1]+1
        self.M = X.shape[0]
        self.beta_hat = ((self.X.T*self.X)**(-1)*self.X.T*Y).reshape(1,self.obs).tolist()[0]
        self.proj = (self.X.T*self.X)**(-1)*self.X.T
        self.beta_hat2 = (self.X.T*self.X)**(-1)*self.X.T*Y
        self.e = Y - self.X*((self.X.T*self.X)**(-1)*self.X.T*Y)
        self.mse = ((Y - self.X*((self.X.T*self.X)**(-1)*self.X.T*Y)).T*(Y - self.X*((self.X.T*self.X)**(-1)*self.X.T*Y))).tolist()[0][0]
    def fit(self):
        "this is beta_hat vector"
        return self.beta_hat
    def intercept(self):
        "this is intercept i.e. beta_hat[0]"
        return self.beta_hat[0]
    def coef(self):
        "these are coefficients i.e. beta_hat[1:K]"
        return self.beta_hat[1:]
    def coef_error(self, omega = None):
        "Var(beta_hat|X), where Omega is Var(e|X), in case of homoscedastic it takes I_nxn matrix by default"
        if omega == None:
            omega = np.diag(np.full(self.M,1))
        return self.proj*omega*self.proj.T
    def errors(self):
        "vector of residuals"
        return self.e
    def mean_square_error(self):
        "MSE"
        return self.mse        
    def predict(self, x):
        "predict y on x"
        return (np.c_[np.ones(self.M), x])*self.beta_hat2
