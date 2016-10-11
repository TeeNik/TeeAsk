#include "stdafx.h"
#include <iostream>
#include <cstring>

using namespace std;

struct Meeting
{
	int start, end;
};


int Count(Meeting **m, int i, int *count)
{
	int c = 0;
	bool flag = false;
	while (i < 24)
	{
		int min_end = 24;
		for (int j = 0; j < count[i]; j++)
		{
			if (min_end > m[i][j].end)
				min_end = m[i][j].end;
			flag = true;
		}
		if (flag)
		{
			c++;
			i = min_end;
		}
		else
			i++;
		flag = false;
	}
	return c;
}


int main()
{
	char str[] = "1";
	int num;
	int k = 0, count[24], size = 100;
	for (int i = 0; i < 24; i++)
		count[i] = 0;

	Meeting** m = new Meeting*[24];
	for (int i = 0; i < 24; i++)
		m[i] = new Meeting[size];
	int i = 0;
	int a;
	while (!cin.eof())
	{
		cin >> str;
		num = atoi(str);

		if (++k % 2)
		{
			m[num][count[num]].start = num;
			a = num;
		}
		else
		{
			m[a][count[a]].end = num;
			//m[a][count[a]].dif = num - m[count].start;
			++count[a];
		}

		if (count[a] == size)
		{
			size *= 2;
			Meeting* buff = new Meeting[size];
			for (int i = 0; i < count[a]; ++i)
			{
				buff[i] = m[a][i];
			}
			delete[] m[a];
			m[a] = buff;
		}
	}
	int kol = 24, max = 0;
	i = 0;
	while (i<kol)
	{
		int curmax = Count(m, i, count);
		if (kol > 24 - curmax)
			kol = 24 - max;
		if (curmax > max)
			max = curmax;
		i++;
	}
	cout << max;
	system("pause");
	return 0;
}