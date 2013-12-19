#
# Copyright (C) 2013  UNIVERSIDAD DE CHILE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Karel Mundnich <kmundnic@ing.uchile.cl>

import data_preprocessing as dpp
import utilities
import numpy as np
import unittest


class TestDataPreprocessing(unittest.TestCase):
  def setUp(self):
    # Data paths
    file_noecho = './test_data/frame_no_echo.npy'
    file_v_zero = './test_data/frame_v_zero.npy'
    file_faulty = './test_data/frame_with_faulty_excitation.npy'
    file_noexci = './test_data/frame_with_no_excitation.npy'

    # Data loading
    self.frame_noecho = np.load(file_noecho)[0]
    self.frame_v_zero = np.load(file_v_zero)[0]
    self.frame_faulty = np.load(file_faulty)[0]
    self.frame_noexci = np.load(file_noexci)[0]

  def test_frame_sanity_check(self):
    self.assertTrue(dpp.frame_sanity_check(self.frame_noecho))
    self.assertTrue(dpp.frame_sanity_check(self.frame_v_zero))
    self.assertFalse(dpp.frame_sanity_check(self.frame_faulty))
    self.assertFalse(dpp.frame_sanity_check(self.frame_noexci))

  def test_edge_detection(self):
    self.assertEqual(dpp.edge_detection(self.frame_noecho), 783)
    self.assertEqual(dpp.edge_detection(self.frame_v_zero), 810)

  def test_split_frame(self):
    echoes_v_zero = dpp.split_frame(self.frame_v_zero)
    self.assertTrue(np.max(echoes_v_zero['NORTH']) in np.arange(400, 600))
    echoes_faulty = dpp.split_frame(self.frame_faulty)
    self.assertEqual(echoes_faulty, None)


if __name__ == '__main__':
  unittest.main()
