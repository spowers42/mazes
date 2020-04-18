import pytest

from maze.cell import Location, Cell

@pytest.fixture
def cell1():
  return Cell(Location(1,2))

@pytest.fixture
def cell2():
  return Cell(Location(2,1))

def test_cell_link_unlink_sym(cell1, cell2):
  assert cell2 not in cell1.links
  cell1.link(cell2)
  assert cell2 in cell1.links
  assert cell1.is_linked(cell2)
  cell1.unlink(cell2)
  assert not cell1.is_linked(cell2)


def test_cell_link_unlink_non_sym(cell1, cell2):
  assert cell2 not in cell1.links
  cell1.link(cell2, False)
  assert cell1.is_linked(cell2)
  assert not cell2.is_linked(cell1)
  cell1.unlink(cell2)
  assert not cell1.is_linked(cell2)
  cell1.link(cell2)  # create a symetric link
  cell2.unlink(cell1, False)
  #check that the non symetric delete doesn't wipe out both
  assert not cell2.is_linked(cell1)
  assert cell1.is_linked(cell2)
