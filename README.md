# CS143-SP26-P4
Course: CS143 – Artificial Intelligence (Spring 2026)

Instructor: Md Alimoor Reza, Assistant Professor of Computer Science, Drake University

Due: Tuesday, April 7, 11:59 PM
Total: 10 points

## Adversarial Search for Connect-Four Game

The goal of this assignment is to solve an AI problem using informed search techniques such as A* Search, and Greedy Best-First Search. Similar to your previous project, you will work with an AI agent that interacts with a simulated street network environment built on a real-world street map.

<p align="center">
  <img src="connect_four.png" alt="Connect Four Game" width="200"/>
</p>
You will complete the implementation of two informed search strategies: <b>A* Search</b> and <b>Greedy Best-First Search</b>. Note that incomplete implementations for both algorithms are provided. Your task is to finish these implementations by filling in the missing components and completing all associated tasks.
Your implementation may rely on several useful data structures, such as <i>deque, set</i>, and <i>priority queue</i>. In class, we have already practiced the basic functionalities of these data structures. Here are the links to the scripts we worked on in class, which might be helpful:
<ul>
  <li> <a href="https://github.com/alimoorreza/CS143-sp26-notes/blob/main/deque_python_datastructure.ipynb"> Deque </a>    
  <li> <a href="https://github.com/alimoorreza/CS143-sp26-notes/blob/main/set_python_datastructure.ipynb"> Set </a>    
  <li> <a href="https://github.com/alimoorreza/CS143-sp26-notes/blob/main/priority_queue_python_datastructure_reza_solution.ipynb"> Priority Queue</a>
</ul>

## Tasks
Complete and run both A* Search and Greedy Best-First Search on two copies of the same map, and then display the routes to see the different routes that were found (they may be similar depending on the map and locations). Make sure the displayed maps are visible in the notebook you submit.

> You should complete the exercises and then perform a comparative analysis using the table below. First, use the source location with `location_id` **160854122** and the goal location with `location_id` **160855919**. This table should help you organize and compare your results for the given destination node in the Des Moines map.



| **Informed search method**     | **Number of nodes along the path**| **Number of nodes expanded**  | **Time took** |
|---------------|--------------------|----------------|----------------|
| greedy\_best\_first           |                    |                   |                |
| a_star         |                    |                |                   |


> You should redo a similar comparative analysis using the table below. This time, keep the source location as `location_id` **160854122**, but choose a different goal location (e.g., `location_id` **160834040**). Then, organize and report your results for that goal node in the Des Moines map.


| **Informed search method**     | **Number of nodes along the path**| **Number of nodes expanded**  | **Time took** |
|---------------|--------------------|----------------|----------------|
| greedy\_best\_first           |                    |                   |                |
| a_star         |                    |                |                   |


Also include a text/Markdown cell that addresses the following points:

1. Explain the basis on which the path costs are computed.

2. Specify the heuristic function used.

3. Provide a brief description of the modifications made to the code.

4. Discuss any differences observed—using the comparative table above—in the computed routes, execution time, number of nodes expanded, and related metrics.

5. Conclude by stating which algorithm you recommend, A* Search or Greedy Best-First Search, and justify your choice briefly.

## Grading

The assignment is worth 10 points. Partial credit (4–6 points) will be awarded if any of the required components are incomplete.

* Up to 2 points: You made code changes that demonstrate a reasonable attempt to complete the implementation of the **SSWSearchNode** class—specifically, by implementing the heuristic function `set_h_value(), set_g_value()`, and `set_f_value()`.

* Up to 4 points: You made code changes that demonstrate a reasonable attempt toward implementing A* search.

* Up to 5 points: You attempted an A* implementation that does not fully work, but you clearly describe the issues encountered and provide your best assessment of how they might be resolved.

* Up to 7 points: You implemented a working version of A* search and attempted a Greedy Best-First Search implementation that does not fully work, but you clearly describe the issues encountered and provide your best assessment of how they might be resolved.

* Up to 8 points: You implemented working versions of both A* search and Greedy Best-First Search and successfully display the maps with the computed routes.

* Up to 10 points: You implemented a working version of A* search, compared its results with your Greedy Best-First Search implementation, and addressed all of the required items in a text/Markdown cell.

### Turning it in

Share the notebook in the same way you did for Project 2.

