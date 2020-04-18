"""
Implements a cell, which represents a single location in a maze.
"""
from dataclasses import dataclass, field

@dataclass
class Location:
  row: int
  column: int


@dataclass
class Cell:
  location: Location
  _links: list = field(default_factory=list, init=False)
  _north: int = field(default=None, init=False)
  _south: int = field(default=None, init=False)
  _west: int = field(default=None, init=False)
  _east: int = field(default=None, init=False)

  def link(self, cell, bidirectional: bool=True):
    if cell not in self._links:
      self._links.append(cell)
    if bidirectional:
      cell.link(self, False)

  def unlink(self, cell, bidirectional: bool=True):
    if cell in self._links:
      self._links.remove(cell)
    if bidirectional:
      cell.unlink(self, False)

  @property
  def links(self):
    return self._links

  def is_linked(self, cell):
    return cell in self._links

  def neighbors(self):
    return [direction for  direction in (self._north, self._south, self._west, self._east) if direction is not None]
