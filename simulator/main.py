from meckerboard import Meckerboard

board = Meckerboard()

board.add_node("The Cloud", 60, 100, 50)
board.add_node("Edge Cluster", 6, 2, 30)
board.add_node("User Device", 3, 1, 0)

board.submit_task(300, 5)
board.submit_task(360, 6)

board.run()



