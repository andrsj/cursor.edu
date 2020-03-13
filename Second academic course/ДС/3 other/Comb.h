
namespace Combinatory {
	class part1
	{
	public:

		static int factorial(int n);
		
		static int A(int n, int k);
		
		static int _A(int n, int k);
		
		static int C(int n, int k);
		
		static int _C(int n, int k);
		
	};

	//PRINT
	class print
	{
	public:
		static void Print(int *a, int n);
	};

	//PART 2
	class part2
	{
	public:
		static bool GenPerm(int *a, int n);
	};

	//PART 3
	class part3
	{
	public:
		static bool GenComb(int *a, int n, int k);
	};

}