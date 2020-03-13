#include"Header.h"

int main() {

	tree<int> derevo;
	derevo.add(10, 100);
	derevo.add(8, 20);
	derevo.add(4, 100);
	derevo.add(9, 100);
	derevo.add(20, 100);
	derevo.add(19, 100);
	derevo.add(22, 100);
	derevo.show();


	
	
	tree<int>::Node *f = derevo.find(derevo.getroot(), 100);
	
	/*cout << f->index << " - " << f->data << endl;*/

	system("pause");

}