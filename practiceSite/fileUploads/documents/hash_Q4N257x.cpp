#include "iostream";

class hash
{
public:
	int key,value;
	hash *next;
	hash(int key, int value){
		this->key = key;
		this->value = value;
		this->next = NULL;
	}	
};

class SeperateChaining{

};

int main(int argc, char const *argv[])
{
	cout<<"Use:";
	cout<<"\n1.Seperate Chaining.";
	cout<<"\n2.Linear Probing";
	cout<<"\n3.Quadratic Probing";
	int n;
	cin>>n;
	switch(n){
		case 1:	while(1){
					cout<<"Choose:";
					cout<<"\n1.Insert";
					cout<<"\n2.Delete";
					cout<<"\n3.Search";
					cout<<"\n4.Exit";
					int choice;
					cin>>choice;
					switch(choice){
						case 1:;
						case 2:;
						case 3:;
						case 4:break;
					}
				};
		case 2:	while(1){
					cout<<"Choose:";
					cout<<"\n1.Insert";
					cout<<"\n2.Delete";
					cout<<"\n3.Search";
					cout<<"\n4.Exit";
					int choice;
					cin>>choice;
					switch(choice){
						case 1:;
						case 2:;
						case 3:;
						case 4:break;
					}
				};
		case 3:	while(1){
					cout<<"Choose:";
					cout<<"\n1.Insert";
					cout<<"\n2.Delete";
					cout<<"\n3.Search";
					cout<<"\n4.Exit";
					int choice;
					cin>>choice;
					switch(choice){
						case 1:;
						case 2:;
						case 3:;
						case 4:break;
					}
				};
		default:break;
	}
	return 0;
}