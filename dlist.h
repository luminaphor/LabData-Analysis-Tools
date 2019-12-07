
// implementation file for the dlist

#include <iostream>
using namespace std;

struct dlist_node
{
  char contents;    // contents in the node
  dlist_node *back, // pointer to previous node in the list
             *next; // pointer to the next node in the list
};

typedef dlist_node *dptr; //we can use the term dptr instead of saying dlist_node.
//typedef lets us use a nickname for other types (I think???)
//OHHHHHH
//its kinda similar to python when you say "import blahSomeModule as blah"
//so when you call methods you can be like blah.someMethod() instead of blahSomeModule.someMethod()

class dlist
{
    private:
      dptr front,   // pointer to the front of the list
           current; // pointer to current node in the list
    public:
      dlist (void);   // constructor creates an empty list
      void insert (char ch);  // inserts a new node
      void remove ();        // removes a node
      void move_right (int distance); // moves current to right
      void move_left (int distance);  // moves current to left
      void print (void);   // prints the list
};

