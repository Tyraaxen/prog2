// Date  2023-10-12
// Rewied by: Naser Shabani
// Email: tyra_axen@hotmail.se

#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
		int _fib(int);
	private:
		int age;
		int fib(int n){
			if(n<=2)
			return 1;
		return (fib(n-1)+fib(n-2));
		}
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}


int Person::fib(void){
	return fib(get());
}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	int Person_fib(Person* person) {return person->fib();}
	}