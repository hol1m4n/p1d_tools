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
#include <TFile.h>
#include <TROOT.h>
#include <TRint.h>
#include <TStyle.h>
#include <TLegend.h>
#include <TProfile.h>
#include <TRandom1.h>
#include <sys/stat.h>


int cf_id[53734]; //Chosen forest ID
int mc_id[168045]; //Main catalog ID


//Functions to read the data

string chosen_forest()
{
	int i=0; //dummy variable
  ifstream inCat ("1tmpDR14specNAME.txt");
  while ( !inCat.eof () ) 
  {    
    inCat >> cf_id[i];
    i++;
	}
	inCat.close();
	return "Data from 1tmpDR14specNAME.txt uploaded";
}


string main_catalog()
{
  int i=0; //dummy variable
  ifstream inRejf ("2tmpDR14specNAME.txt");
  while ( !inRejf.eof () ) 
  {    
    inRejf >> mc_id[i];
    i++;
  }
  inRejf.close();
  return "Data from 2tmpDR14specNAME.txt uploaded";
}



void data_input()
{
	cout<<"Entering data"<<endl;
  cout<<chosen_forest()<<endl;
  cout<<main_catalog()<<endl;

  cout<<"DATA ALREADY IN!"<<endl;
  cout<<"             "<<endl;
  cout<<"|||1tmpDR14specNAME.txt|||"<<endl;
  cout<<"ID"<<endl;
  for(int u=0;u<5;u++)
  {
    cout<<" "<<u<<" -- "<<cf_id[u]<<endl;
  }
  cout<<"             "<<endl;
  cout<<"|||2tmpDR14specNAME.txt|||"<<endl;
  cout<<"THING_ID"<<endl;
  for(int u=0;u<5;u++)
  {
    cout<<" "<<u<<" -- "<<mc_id[u]<<endl;
  }
  cout<<"             "<<endl;
}


void filter()
{
  data_input();
  cout<<"             "<<endl;
  cout<<"             "<<endl;
  cout<<"             "<<endl;
  cout<<"             "<<endl;
  cout<<"             "<<endl;
  cout<<"ALL GOOD WITH THE DATA!"<<endl;
  cout<<"             "<<endl;
  cout<<"CLASIFYNG THE DATA"<<endl;


  ofstream output;  //Output data list
	output.open("3tmpDR14specNAME.txt");
	//output<<"************Quasars without reading errors nor forest flaws*************"<<endl;
	output<<"bool_value"<<endl;
	

	int i=0; //dummy variable


	for(int a=0;a<168045;a++)
	{
		for(int b=0;b<53734;b++)
		{
      if(mc_id[a]==cf_id[b])
      {
      	i=1;
      	break;
      }
		}

  
  if(i==1)
  {
  	output<<"True"<<endl;
  }
  else
  {
    output<<"False"<<endl;
  }


  i=0;
	}

	output.close();


}

