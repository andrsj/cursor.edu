#ifdef ConsoleApplication_EXPORTS
#define COMB_API __declspec(dllexport)
#else
#define COMB_API __declspec(dllimport)
#endif

namespace Math {
	class MyComb
	{
	public:
		static COMB_API int Factorial(int n);
		static COMB_API bool GenPerm(int *a, int n);
		static COMB_API void Print(int *a, int n);
		static COMB_API bool GenComb(int *a, int n, int k);
	};
}
