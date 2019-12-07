
#include <cstdlib>
#include <iostream>
#include "dlist.h"

using namespace std;

int
main (int argc, char *argv[])
{
  char choice, ch;
  int distance;
/****  Declare a dlist variable      ****/
  dlist myList;
  cout << "Select p (print), i (insert), d (delete), r (right),";
  cout << "\n   l (left) or q (quit): ";
  cin >> choice;

  while (choice != 'q')
    {
      switch (choice)
	{
	case 'p':
	  cout << "\nThe list is:\n";
/****  Call the print member function to print the dlist    ****/
        myList.print();

	  cout << endl;
	  break;
	case 'i':
	  cout << "\nEnter the character to insert: ";
	  cin >> ch;
/****  Call the insert member function to insert ch in the dlist   ****/
        myList.insert(ch);
	  break;
	case 'r':
	  cout << "\nEnter the distance to move right: ";
	  cin >> distance;
/****  Call the move_right member to move current to the right distance spots    ****/
        myList.move_right(distance);
	  break;
	case 'l':
	  cout << "\nEnter the distance to move left: ";
	  cin >> distance;
/****  Call the move_left member to move current to the left distance spots    ****/
      myList.move_left(distance);

	  break;
	case 'd':
/****  Call the remove member function to remove the node pointed to by current      ****/
    myList.remove();

	  cout << endl;
	  break;
	default:
	  cout << "\nMust enter p, i, d, r, l, or q!\n";
	}
      cout << "\nSelect p (print), i (insert), d (delete), r (right),";
      cout << "\n   l (left) or q (quit): ";
      cin >> choice;
    }

  cout << "\n\nEditing Complete\n\n";


  return 0;
}

dlist::dlist (void)
{
  front = NULL;
  current = NULL;
}

void dlist::insert (char ch)
{
  dptr p, q;

  if (front == NULL)		//adds a node to brand new linked list
    {
      p = new dlist_node;

      p->contents = ch;
      p->back = NULL;
      p->next = NULL;

      front = p;
      current = p;
    }

  else				//adds node to the end of a linked list
    {
      if (current->next == NULL && front != NULL)
	{
	  p = new dlist_node;

	  p->contents = ch;
	  p->back = current;
	  p->next = NULL;

	  current->next = p;
	  current = p;
	}

      else			//adds node to somewhere that isnt the end of the linked list
	{
	  p = new dlist_node;
	  //dptr q;
	  q = new dlist_node;

	  p->back = current;
	  p->contents = ch;
	  p->next = current->next;

	  q = current->next;
	  current->next = p;
	  p = q->back;
	  p = current;      //current should be pointing to the other dude
	}
    }
  p = NULL;
  q = NULL;
}

void dlist::print(void)
{
    dptr mover;
    
    for (mover = front; mover != NULL;mover = mover -> next)
    {
        if (mover != current)
            cout<<mover->contents;
        else
            cout<<"{"<<mover->contents<<"}";
    }
}

void dlist:: remove (void)  // removes a node
{
    dptr temp1,temp2;
    
    if (front != NULL) //checks that list is not empty
    {
        if (front ==current && front -> next != NULL) //if deleting first node
        {
            front = front -> next;
            front -> back = NULL;
            delete current;
            current = front;
        }
        
        else
        {
            if (front == current && front -> next == NULL) //deleting first and only node
            {
                front = NULL;
                delete current;
                current = front;
            }
            
            else
            {
                if (current -> next != NULL) //deleting node in middle of list
                {
                    temp1 = current -> next;
                    temp2 = current -> back;
                
                    temp1 -> back = temp2;
                    temp2 -> next = temp1;
                    
                    delete current;
                    current = temp1;
                    
                    temp1 = NULL;
                    temp2 = NULL;
                }
                
                else //deleting last node in the list
                {
                    temp1 = current -> back;
                    delete current;
                    current = temp1;
                    current -> next = NULL;
                    temp1 = NULL;
                }
            }
        }
    }
 }  
 
void dlist::move_right (int distance) // moves current to right
{
    if (front != NULL)
    {
        for (int i = 0; i < distance; i++)
        {
           if (current -> next != NULL)
            current = current -> next;
            
           else
            break;
        }
    }
}

void dlist:: move_left (int distance)  // moves current to left
{
     if (front != NULL)
    {
        for (int i = 0; i < distance; i++)
        {
           if (current -> back != NULL)
            current = current -> back;
            
           else
            break;
        }
    }
}

