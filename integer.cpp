#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();

	private:
		int val;
		int fib2(int);
	};
 
Integer::Integer(int n){
	val = n;
	}

int Integer::fib(){
	int n = val;
	return fib2(n);
}

int Integer::get(){
	return val;
	}

int Integer::fib2(int n){
	if (n <= 1)
	{
		return 1;
	}
	else
	{
		return fib2(n-1) + fib2(n-2);
	}
}


 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}