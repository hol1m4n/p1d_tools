#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <TH1F.h>
#include <TApplication.h>
#include <sstream>
#include <TFile.h>
#include <TROOT.h>
#include <TRint.h>
#include <TStyle.h>
#include <TRandom1.h>
#include <TMath.h>
#include <TGraph2D.h>
#include <TRandom.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TF2.h>
#include <TH1.h>
//#include <iostream.h>
#include <fstream>
#include <TH1D.h>
#include <TVirtualFFT.h>
#include <TGraphErrors.h>
#include <sstream>
#include <TFile.h>
#include <TROOT.h>
#include <TRint.h>
#include <TStyle.h>
#include <TLegend.h>
#include <TProfile.h>
#include <TRandom1.h>
#include <sys/stat.h>
#include <iostream>
#include <string>

void words()
{
   string s; //Palabra a sacar, maximo 20 letras
   cout<<"ingresar frase en minuscula"<<endl;
   cin>>s;
   //s = "preliminares";

   
   int size= s.size(); //Tamano de la palabra

 


   //Matriz de escritura

   int space[7][5] = {{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}};
   int guion[7][5] = {{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,1,1,1,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}};

   //Conversor de texto
   string text;


   //Letras
   
   int A[7][5] = {{0,0,0,0,0},{0,1,1,1,0},{0,1,0,1,0},{0,1,1,1,0},{0,1,0,1,0},{0,1,0,1,0},{0,0,0,0,0}};

   int B[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,0,1,0,1},{0,0,1,1,1},{0,0,1,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int C[7][5] = {{0,0,0,0,0},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,1,1},{0,0,0,0,0}};

   int D[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,0,1,0,1},{0,0,1,0,1},{0,0,1,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int E[7][5] = {{0,0,0,0,0},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,1,1},{0,0,0,0,0}};

   int F[7][5] = {{0,0,0,0,0},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,0,0},{0,0,0,0,0}};

   int G[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,1,0,0,0},{0,1,0,1,1},{0,1,0,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int H[7][5] = {{0,0,0,0,0},{0,1,0,0,1},{0,1,0,0,1},{0,1,1,1,1},{0,1,0,0,1},{0,1,0,0,1},{0,0,0,0,0}};

   int I[7][5] = {{0,0,0,0,0},{0,1,1,1,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,1,1,1,0},{0,0,0,0,0}};

   int J[7][5] = {{0,0,0,0,0},{0,0,1,1,1},{0,0,0,1,0},{0,0,0,1,0},{0,1,0,1,0},{0,1,1,1,0},{0,0,0,0,0}};

   int K[7][5] = {{0,0,0,0,0},{0,1,0,0,1},{0,1,0,1,0},{0,1,1,0,0},{0,1,0,1,0},{0,1,0,0,1},{0,0,0,0,0}};

   int L[7][5] = {{0,0,0,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,1,1},{0,0,0,0,0}};

   int M[7][5] = {{0,0,0,0,0},{1,0,0,0,1},{1,1,0,1,1},{1,0,1,0,1},{1,0,0,0,1},{1,0,0,0,1},{0,0,0,0,0}};

   int N[7][5] = {{0,0,0,0,0},{1,0,0,0,1},{1,1,0,0,1},{1,0,1,0,1},{1,0,0,1,1},{1,0,0,0,1},{0,0,0,0,0}};

   int O[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,1,0,0,1},{0,1,0,0,1},{0,1,0,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int P[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,0,1,0,1},{0,0,1,1,1},{0,0,1,0,0},{0,0,1,0,0},{0,0,0,0,0}};

   int Q[7][5] = {{0,0,0,0,0},{0,1,1,1,0},{0,1,0,1,0},{0,1,0,1,0},{0,1,0,1,0},{0,1,1,1,1},{0,0,0,0,0}};

   int R[7][5] = {{0,0,0,0,0},{1,1,1,1,1},{0,1,0,0,1},{0,1,1,1,1},{0,1,0,1,0},{0,1,0,0,1},{0,0,0,0,0}};

   int S[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,1,0,0,0},{0,1,1,1,1},{0,0,0,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int T[7][5] = {{0,0,0,0,0},{0,1,1,1,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,0,0,0}};

   int U[7][5] = {{0,0,0,0,0},{0,1,0,0,1},{0,1,0,0,1},{0,1,0,0,1},{0,1,0,0,1},{0,1,1,1,1},{0,0,0,0,0}};

   int V[7][5] = {{0,0,0,0,0},{0,1,0,1,0},{0,1,0,1,0},{0,1,0,1,0},{0,1,0,1,0},{0,0,1,0,0},{0,0,0,0,0}};

   int W[7][5] = {{0,0,0,0,0},{1,0,0,0,1},{1,0,0,0,1},{1,0,1,0,1},{1,1,0,1,1},{1,0,0,0,1},{0,0,0,0,0}};

   int X[7][5] = {{0,0,0,0,0},{0,1,0,1,0},{0,1,0,1,0},{0,0,1,0,0},{0,1,0,1,0},{0,1,0,1,0},{0,0,0,0,0}};

   int Y[7][5] = {{0,0,0,0,0},{0,1,0,1,0},{0,1,0,1,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,1,0,0},{0,0,0,0,0}};

   int Z[7][5] = {{0,0,0,0,0},{0,1,1,1,1},{0,0,0,0,1},{0,0,0,1,0},{0,0,1,0,0},{0,1,1,1,1},{0,0,0,0,0}};


   //Loop para cambiar letra


   int t=5*size;
   
   int iterador[7][t];
   
   int p=0;

  

   for(int a=0;a<size;a++)
   {

      if(s[a] == 'a')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = A[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------

      if(s[a] == 'b')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = B[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------

            if(s[a] == 'c')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = C[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'd')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = D[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'e')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = E[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'f')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = F[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'g')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = G[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'h')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = H[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'i')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = I[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'j')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = J[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'k')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = K[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'l')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = L[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'm')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = M[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'n')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = N[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'o')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = O[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'p')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = P[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'q')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = Q[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'r')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = R[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 's')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = S[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 't')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = T[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'u')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = U[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'v')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = V[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'w')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = W[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'x')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = X[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------
            if(s[a] == 'y')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = Y[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------

        if(s[a] == 'z')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = Z[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //-------------------------------------------

      if(s[a] == ' ')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = space[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //----

           //-------------------------------------------

      if(s[a] == '-')
      {
      //cout<<"ok"<<endl;
         for(int i=0;i<7;i++)
         {
            for(int b=0;b<5;b++)
            {
              
               iterador[i][b+p] = guion[i][b];
               //cout<<iterador[i][b+p]<<endl;

            }
         }
      }
     //----






      //scout<<p<<endl;
      p = p+5;
     
   }










   for(int i=0;i<7;i++)
   {
      for(int a=0;a<t;a++)
      {
         if(a < t-1)
         {
            if(iterador[i][a] == 1)
            {
               text = "█";
               cout<< text;
            }
            else
            {
               text = "%";
               cout<< text;
            }

         }
         else
         {
            if(iterador[i][a] == 1)
            {
               text = "█";
               cout<< text <<endl;
            }
            else
            {
               text = "%";
               cout<< text<<endl;
            }

         }
      }
   }


}







int box(){
   string s="inicio"; //all lowercase
   int size= s.size();
   int count;
   
   for(int i=0; i<size; i++){
      count=0;
      for(int j=0; j<size; j++){
         if(s[i]==s[j]){
            count++;
         }
      }
      cout << s[i] << " appears " << count<< " times\n"; 
   }
return 0;   
}

