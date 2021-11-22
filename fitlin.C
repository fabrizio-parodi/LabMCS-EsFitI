namespace data{
  vector<double>  x, y, ex, ey;
}

double fun(const double *x,const double *par){
  return par[0]*(*x)+par[1];
}

void fcn(int &npar, double *gin, double &f, double *par, int iflag){
  //....
}

void fitlin(){
  ifstream file("pendolo.dat");
  double x,y,ex,ey;
  while (file >> x >> y >> ex >> ey){
    data::x.push_back(x); data::y.push_back(y); data::ex.push_back(ex); data::ey.push_back(ey);
  }

  // Define the minimization problem

  // Minimize

  // Get result

}
