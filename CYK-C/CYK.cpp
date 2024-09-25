// C++ implementation for the
// CYK Algorithm

#include<bits/stdc++.h>
using namespace std;

// Non-terminals symbols
vector<string> terminals,non_terminals;

// Rules of the grammar
unordered_map<string,vector<vector<string>>> R;

// function to perform the CYK Algorithm
void cykParse(vector<string> w)
{
int n = (int)w.size();

// Initialize the table
map<int,map<int,set<string>>> T;

// Filling in the table
for(int j=0;j<n;j++)
{

	// Iterate over the rules
	for(auto x:R)
	{
	string lhs = x.first;
	vector<vector<string>> rule = x.second;
	
	for(auto rhs:rule)
	{

		// If a terminal is found
		if(rhs.size() == 1 && rhs[0] == w[j])
		T[j][j].insert(lhs);
	}

	}
	for(int i=j;i>=0;i--)
	{

	// Iterate over the range from i to j
	for(int k = i;k<=j;k++)
	{

		// Iterate over the rules
		for(auto x:R)
		{
		string lhs = x.first;
		vector<vector<string>> rule = x.second;

		for(auto rhs:rule)
		{
		// If a terminal is found
			if(rhs.size()==2 && T[i][k].find(rhs[0])!=T[i][k].end() && T[k+1][j].find(rhs[1])!=T[k+1][j].end())
			T[i][j].insert(lhs);
		}

		}
	}
	}
}

// If word can be formed by rules
// of given grammar
if(T[0][n-1].size()!=0)
	cout << "True\n";
else
	cout << "False\n";
}

// Driver Code
int main()
{
// terminal symbols
terminals = {"book", "orange", "man", 
			"tall", "heavy", 
			"very", "muscular"};

// non terminal symbols
non_terminals = {"NP", "Nom", "Det", "AP", 
				"Adv", "A"};

// Rules
R["NP"]={{"Det", "Nom"}};
R["Nom"]= {{"AP", "Nom"}, {"book"}, 
			{"orange"}, {"man"}};
R["AP"] = {{"Adv", "A"}, {"heavy"}, 
			{"orange"}, {"tall"}};
R["Det"] = {{"a"}};
R["Adv"] = {{"very"}, {"extremely"}};
R["A"] = {{"heavy"}, {"orange"}, {"tall"}, 
		{"muscular"}};

// Given String
vector<string> w = {"a", "very", "heavy", "orange", "book"};

// Function Call
cykParse(w);

return 0;
}

