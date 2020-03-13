// MatchFuncsDll.h
#ifdef COMB2_EXPORTS
#define COMB2_API __declspec(dllexport)
#else
#define COMB2_API __declspec(dllimport)
#endif

namespace Math
{
	class Comb
	{
	public:
		static COMB2_API int Factorial(int n);
		static COMB2_API void GenPerm(int* A,int n);
		static COMB2_API void swap(int* A,int i,int j);
	};
}