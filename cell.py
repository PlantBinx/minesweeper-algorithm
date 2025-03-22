from tkinter import Button
import random
import settings

class Cell:
    all = []
    false_counter = 0
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=2,
            height=2,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-2>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        self.show_mine()
        if self.is_mine == False:
            false_counter += 1


    def right_click_actions(self, event):
        self.show_cell()
        if self.is_mine:
            false_counter += 1


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
        # After randomizing mines, update the text of all cells
        for cell in Cell.all:
            cell.update_button_text()

    def update_button_text(self):    
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),

            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y),
            self.get_cell_by_axis(self.x, self.y + 1),

            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]

        cells = [
            cell for cell in cells if cell is not None
        ]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
    def show_cell(self):
        self.cell_btn_object.configure(highlightbackground='red')

    def show_mine(self):
        self.cell_btn_object.configure(highlightbackground='green')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        return None