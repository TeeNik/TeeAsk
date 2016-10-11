// 5.4.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <cstring>

using namespace std;



class TeeStack
{
private:
	int size = 8;
	char* arr = new char[size];
public:
	int count = 0;

	~TeeStack()
	{
		delete[] arr;
	}

	void push(char n)
	{
		if (count == size)
		{
			char* buff = new char[count];
			for (int i = 0; i < count; ++i)
				buff[i] = arr[i];
			size *= 2;
			delete[] arr;
			arr = new char[size];
			for (int i = 0; i < count; ++i)
				arr[i] = buff[i];
			delete[] buff;
		}
		arr[count] = n;
		++count;
	}

	char pop()
	{
		--count;
		return arr[count];
	}

	char top()
	{
		return arr[count - 1];
	}

	bool isEmpty()
	{
		return count == 0 ? true : false;
	}
};

int priority(char c)
{
	if (c == '*' || c == '/') return 2;
	if (c == '+' || c == '-') return 1;
	if (c == '(' || c == ')') return 0;
}

char* ToPostfix(char* str)
{
	char* final = new char[100];
	int f = 0;
	TeeStack stack;

	for (int i = 0; i < strlen(str); ++i)
	{
		if (str[i] == '(') stack.push(str[i]);
		else if ((str[i] == '*') || (str[i] == '/') || (str[i] == '+') || (str[i] == '-'))
		{
			if (f == 0 && str[i] == '-')
			{
				final[f] = '0';
				f++;
				final[f] = ' ';
				f++;
			}
			else if (final[f - 1] >= '0' && final[f - 1] <= '9')
			{
				final[f] = ' ';
				f++;
			}
			while ((!stack.isEmpty()) && (priority(stack.top())>=priority(str[i])))
			{
				final[f] = stack.pop();
				f++;
			}

			stack.push(str[i]);
		}
		else if (str[i] == ')')
		{
			while (!stack.isEmpty() && stack.top() != '(')
			{
				final[f] = stack.pop();
				++f;
			}
			stack.pop(); //(2*(5-2)+4)/5
		}
		else
		{
			final[f] = str[i];
			f++;
		}
	}


	while (!stack.isEmpty())
	{
		final[f] = stack.pop();
		f++;
	}
	final[f] = '\0';
	return final;
}

int Evaluate(char* str)
{
	TeeStack stack;
	int num = 0;
	char buff[5];
	int h = 0;

	for (int i = 0; i < strlen(str); i++)
	{
		if (str[i] >= '0' && str[i] <= '9')
		{
			buff[h] = str[i];
			h++;
		}
		else if (str[i] == ' ')
		{
			num = atoi(buff);
			strcpy_s(buff, 5, "\0");
			h = 0;
			stack.push(num);
		}
		else
		{
			if (buff[0] >= '0' && buff[0] <= '9')
			{
				num = atoi(buff);
				strcpy_s(buff, 5, "\0");
				h = 0;
				stack.push(num);
			}
			int x = stack.pop();
			int y = stack.pop(); 
			if (str[i] == '+')
				stack.push(y + x);
			else if (str[i] == '-')
				stack.push(y - x);
			else if (str[i] == '*')
				stack.push(y * x);
			else if (str[i] == '/')
				stack.push(y / x);
		}
	}
	return stack.pop();

}


int main()
{
	char str[100];
	cin >> str;
	char * res = ToPostfix(str);
	cout << Evaluate(res);
	system("pause");
    return 0;
}