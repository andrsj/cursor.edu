#pragma once
#include<iostream>
using namespace std;
int j = 1;
int i =0;
template<class T >
class tree 
{
public:

	int sort_massive[7];

	struct Node
	{
		T data;
		int index;
		Node * left, *right;
		Node * parent;
	  };
	Node * getroot() {
		return root;
	}
	Node * root;
public:
	tree() { root = NULL; }
	void add(int index,T data)
	{
		Node * el = new Node;
		el->index = index;
		el->data = data;
		el->left = el->right = el->parent = NULL;
		if (root == NULL)
		{
			root = el;
		}
		else 
		{
			Node * tmp = root;
			Node * p = NULL;
			while(tmp!=NULL)
			{
				if (tmp->index == index) {
					delete el;
					return;
				}
				if (tmp->left==NULL || tmp->right== NULL)
				{
					if(i%2==0)
					{
						p = tmp;
						tmp = tmp->left;
						

						
					}
					else
					{
						p = tmp;
					tmp = tmp->right;
				
					}



				}
				else
				{
					while(tmp!=NULL)
					{


					
						
						
						if(tmp !=root){
						if(tmp!=NULL && tmp->right!= NULL)
						{
							
						tmp=tmp->parent;	
						tmp=tmp->right;

						}
						}



						if(tmp->left==NULL || tmp->right== NULL)
						{
							if(i%2==0)
					{
						p = tmp;
						
						el->parent = p;
				p->left = el;i++;
				
			goto bob;
						
					}
					else
					{
						p = tmp;
					
				el->parent = p;
				p->right = el;i++;
					
					goto bob;
					}
						}


						
					p = tmp;
					tmp = tmp->left;
					
					

					}
				}
				
				


			if (i%2==0)
			{
				el->parent = p;
				p->left = el;i++;
			}
			else
			{
				el->parent = p;
				p->right = el;i++;
			}
		}bob: ;

	}
	}
	void show() {
		if (root != NULL) {
			show(root);
		}
	}
	void show(Node * el) 
	{
		cout << el->index << "(" << el->data << ")" << " ";
		
		if (el->left != NULL) {
			show(el->left);
		}
		//
		if (el->right != NULL) {
			show(el->right);
		}
		
		//
	}
	void piramidasort () {
		if (root != NULL) {
			piramidasort(root);
		}
	}
	void piramidasort(Node * el)
	{

		while(root != NULL)
		{
		Node *tmprr =el;
		Node *tmprl =el;

		while(tmprr->right!=NULL)
		{
			tmprr=tmprr->right;
			
			
			
		
		}

		if(tmprl->right!=NULL)
		{
		tmprl=tmprl->right;
		}
		while(tmprl->left!=NULL)
		{
			

			tmprl=tmprl->left;
			
		}

		if((tmprr->index)>(tmprl->index) )
		{
			if((tmprl->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprl->parent->index;

				tmprl->parent->index = tmprl->index;
				
				tmprl->index =temp;
			}

		}
		else if((tmprr->index)<(tmprl->index))
		{
			if((tmprr->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprr->parent->index;

				tmprr->parent->index = tmprr->index;
				
				tmprr->index =temp;
			}
		}
		
		////////////////////////////////////////////////prava vitka
		

		tmprr =el;
		tmprl =el;


		while(tmprl->left!=NULL)
		{
			

			tmprl=tmprl->left;
			
		}

		if(tmprl->left!=NULL)
		{
		tmprr=tmprr->left;///////???????
		}
		while(tmprr->right!=NULL)
		{
			

			tmprr=tmprr->right;
			
		}

		if((tmprr->index)>(tmprl->index) )
		{
			if((tmprl->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprl->parent->index;

				tmprl->parent->index = tmprl->index;
				
				tmprl->index =temp;
			}

		}
		else if((tmprr->index)<(tmprl->index))
		{
			if((tmprr->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprr->parent->index;

				tmprr->parent->index = tmprr->index;
				
				tmprr->index =temp;
			}
		}

		///////////////////////////////// 2 level
		if(el->right!=NULL)
		{
		tmprr =el->right;
		}
		if(el->left!=NULL)
		{
		tmprl =el->left;
		}
		if((tmprr->index)>(tmprl->index) )
		{
			if((tmprl->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprl->parent->index;

				tmprl->parent->index = tmprl->index;
				
				tmprl->index =temp;
			}

		}
		else if((tmprr->index)<(tmprl->index))
		{
			if((tmprr->index)< (tmprl->parent->index))
			{
				int temp;
				temp = tmprr->parent->index;

				tmprr->parent->index = tmprr->index;
				
				tmprr->index =temp;
			}
		}

		///////// zapus in  massive 
		
		int size = 7;
		sort_massive[size-j]=el->index;
		


		Node *f = find(getroot(), 8-j);////!!!!
		j=j+1;
		if (j==8)
		{

			break;
		}

		int temp1 = el->index;
		el->index=f->index;
		
		Node *ttt = f->parent;
		if(ttt->right==f)
		{
		ttt->right=NULL;

		}
		if(ttt->left==f)
		{
		ttt->left=NULL;

		}




	}

		
	}

	void showmessage()
	{

		for (int i = 0; i < 7; i++)
		{
			cout<<sort_massive[i]<<" -> ";
		}

	}
	

	Node * find(Node * start,int data) 
	{
		bool find =true;
		
		Node * time =start;

		while (find ==true) 
		{

			///////////////////// left vitka
			if(start->data == data)
			{

			return start;
			
			}
			
			start =start->left;
			if(start->data == data)
			{

				return start;
			}


			if(start->right!=NULL )
			{
			if (start->right->data==data)
			{
				start =start->right;

				return start ;
			}
		}

			if(start->left!=NULL)
			{
			 if(start->left->data==data)
			{
				start = start->left;

				return start;
			}
			}
			///////////////////// right vitka
			start = time;

			start=start->right;

			if(start->right!=NULL)
			{
			if (start->right->data==data)
			{
				start =start->right;

				return start ;
			}
		}

			if(start->left!=NULL)
			{
			 if(start->left->data==data)
			{
				start = start->left;

				return start;
			}
			}



	}

return start;
	}

};