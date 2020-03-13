// RPG_Game_Classes.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
using std::string;

class Hero {
public:
	string Name; // Name
	bool isAntiHero; // чи є він героєм/антигероєм
	int health; // ХП
	int speed;  // швидкість
	int damage; // дає дамаг/хілл
	int defend; // блокує
	Hero(string Name, bool Hero, int health, int speed, int damage, int defend) {
		setHeroParametrs(Name,Hero,health,speed,damage,defend);
	}
	void setHeroParametrs(string Name,bool Hero, int health, int speed, int damage, int defend) {
		this->Name = Name;
		this->isAntiHero = Hero;
		this->health = health;
		this->speed = speed;
		this->damage = damage;
		this->defend = defend;
	}
	void take(Hero object){
		std::cout << std::endl;
		if (object.isAntiHero != this->isAntiHero) {
			this->health = health - (object.damage - defend);
			std::cout << "Taked damage from \"" << object.Name << "\" like " << object.damage << "\nHealth \"" << Name << "\" now: " << health << std::endl;
		}
		else {
			this->health = health + object.damage;
			std::cout << "Taked healthed from \"" << object.Name << "\" like " << object.damage << "\nHealth \"" << Name << "\" now: " << health << std::endl;
		}
	}
	void give(Hero object) {
		std::cout << std::endl;
		if (object.isAntiHero != this->isAntiHero) {
			object.health = object.health - (this->damage - object.defend);
			std::cout << "Gived damage hero by \"" << this->Name << "\" like " << this->damage << "\nHealth \"" << object.Name << "\" now: " << object.health << std::endl;
		}
		else {
			object.health = object.health + this->damage;
			std::cout << "Gived healthed hero by \"" << this->Name << "\" like " << this->damage << "\nHealth \"" << object.Name << "\" now: " << object.health << std::endl;
		}
	}
	void getHeroParametrs() {
		std::cout << std::endl;
		std::cout << "Hero parametrs: \nName: \"" << Name << "\"" << "\nHero | AntiHero (1|0): " << isAntiHero << 
					 "\nHealth: " << health << "\nSpeed: " << speed << 
					 "\nDamage: " << damage << "\nBlock damage: " << defend << std::endl;
	}
};

int main()
{
	Hero HeroYou("GG",true, 100, 10, 10, 10); // ГГ - головний герой
	Hero HeroEnemy("Enemy",false, 100, 10, 15, 15); // Супротивник
	Hero HeroTeammate("Teammate",true, 100, 10, 5, 5); // Teammate
	HeroYou.getHeroParametrs(); // вивід параметрів героя ГГ
	HeroYou.take(HeroEnemy); // взяти дамаг від супротивника
	HeroYou.take(HeroTeammate); // взяти хілку від тіммейта
	HeroEnemy.give(HeroYou); // дати дамаг ГГ від супротивника
}

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
