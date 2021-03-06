#!/usr/bin/env python
'''mmtfStructure.py

Decode msgpack unpacked data to mmtf structure

'''
__author__ = "Mars (Shih-Cheng) Huang"
__maintainer__ = "Mars (Shih-Cheng) Huang"
__email__ = "marshuang80@gmail.com"
__version__ = "0.2.0"
__status__ = "Done"

import numpy as np
from mmtf.utils import decoder_utils
from mmtfPyspark.utils import mmtfDecoder


class MmtfStructure(object):
    model_counter = 0
    chain_counter = 0
    group_counter = 0
    atom_counter = 0
    # TODO


    def __init__(self, input_data):
        """Decodes a msgpack unpacked data to mmtf structure"""
        # TODO temporary
        self.input_data = input_data


        self.mmtf_version = mmtfDecoder.get_value(input_data, 'mmtfVersion', required=True)
        self.mmtf_producer = mmtfDecoder.get_value(input_data, 'mmtfProducer', required=True)
        self.unit_cell = mmtfDecoder.get_value(input_data, 'unitCell')
        self.space_group = mmtfDecoder.get_value(input_data, 'spaceGroup')
        self.structure_id = mmtfDecoder.get_value(input_data, 'structureId')
        self.title = mmtfDecoder.get_value(input_data, 'title')
        self.deposition_date = mmtfDecoder.get_value(input_data, 'depositionDate')
        self.release_date = mmtfDecoder.get_value(input_data, 'releaseDate')
        self.ncs_operator_list = mmtfDecoder.get_value(input_data, 'ncsOperatorList')
        self.bio_assembly = mmtfDecoder.get_value(input_data, 'bioAssemblyList')  # TODO naming inconsistency
        self.entity_list = mmtfDecoder.get_value(input_data, 'entityList')
        self.experimental_methods = mmtfDecoder.get_value(input_data, 'experimentalMethods')
        self.resolution = mmtfDecoder.get_value(input_data, 'resolution')
        self.r_free = mmtfDecoder.get_value(input_data, 'rFree')
        self.r_work = mmtfDecoder.get_value(input_data, 'rWork')
        self.num_bonds = mmtfDecoder.get_value(input_data, 'numBonds', required=True)
        self.num_atoms = mmtfDecoder.get_value(input_data, 'numAtoms', required=True)
        self.num_groups = mmtfDecoder.get_value(input_data, 'numGroups', required=True)
        self.num_chains = mmtfDecoder.get_value(input_data, 'numChains', required=True)
        self.num_models = mmtfDecoder.get_value(input_data, 'numModels', required=True)
        self.group_list = mmtfDecoder.get_value(input_data, 'groupList', required=True)
        self._bond_atom_list = None
        #self.bond_atom_list = mmtfDecoder.decode(input_data, 'bondAtomList')
        self._bond_order_list = None
        #self.bond_order_list = mmtfDecoder.decode(input_data, 'bondOrderList')
        self.bondResonanceList = None  # TODO
        self._x_coord_list = None
        self._y_coord_list = None
        self._z_coord_list = None
        #self.x_coord_list = mmtfDecoder.decode(input_data, 'xCoordList', required=True)
        #self.y_coord_list = mmtfDecoder.decode(input_data, 'yCoordList', required=True)
        #self.z_coord_list = mmtfDecoder.decode(input_data, 'zCoordList', required=True)
        self._b_factor_list = None
        self._atom_id_list = None
        self._alt_loc_list = None
        self._occupancy_list = None
        self._sec_struct_list = None
        #self.b_factor_list = mmtfDecoder.decode(input_data, 'bFactorList')
        #self.atom_id_list = mmtfDecoder.decode(input_data, 'atomIdList')
        #self.alt_loc_list = mmtfDecoder.decode(input_data, 'altLocList')
        #self.occupancy_list = mmtfDecoder.decode(input_data, 'occupancyList')
        self._group_id_list = None
        #self.group_id_list = mmtfDecoder.decode(input_data, 'groupIdList', required=True)
        self._group_type_list = None
        #self.group_type_list = mmtfDecoder.decode(input_data, 'groupTypeList', required=True)
        #self.sec_struct_list = mmtfDecoder.decode(input_data, 'secStructList')
        self._ins_code_list = None
        #self.ins_code_list = mmtfDecoder.decode(input_data, 'insCodeList')
        self._sequence_index_list = None
        #self.sequence_index_list = mmtfDecoder.decode(input_data, 'sequenceIndexList')
        self._chain_id_list = None
        #self.chain_id_list = mmtfDecoder.decode(input_data, 'chainIdList', required=True)
        self._chain_name_list = None
        #self.chain_name_list = mmtfDecoder.decode(input_data, 'chainNameList')
        self.groups_per_chain = mmtfDecoder.get_value(input_data, 'groupsPerChain', required=True)
        self.chains_per_model = mmtfDecoder.get_value(input_data, 'chainsPerModel', required=True)

    @property
    def bond_atom_list(self):
        if self._bond_atom_list is not None:
            return self._bond_atom_list
        elif 'bondAtomList' in self.input_data:
            self._bond_atom_list = mmtfDecoder.decode(self.input_data, 'bondAtomList')
            return self._bond_atom_list
        else:
            return None

    @property
    def bond_order_list(self):
        if self._bond_order_list is not None:
            return self._bond_order_list
        elif 'bondOrderList' in self.input_data:
            self._bond_order_list = mmtfDecoder.decode(self.input_data, 'bondOrderList')
            return self._bond_order_list
        else:
            return None

    @property
    def x_coord_list(self):
        if self._x_coord_list is not None:
            return self._x_coord_list
        elif 'xCoordList' in self.input_data:
            self._x_coord_list = mmtfDecoder.decode(self.input_data, 'xCoordList', required=True)
            return self._x_coord_list
        else:
            return None

    @property
    def y_coord_list(self):
        if self._y_coord_list is not None:
            return self._y_coord_list
        elif 'yCoordList' in self.input_data:
            self._y_coord_list = mmtfDecoder.decode(self.input_data, 'yCoordList', required=True)
            return self._y_coord_list
        else:
            return None

    @property
    def z_coord_list(self):
        if self._z_coord_list is not None:
            return self._z_coord_list
        elif 'zCoordList' in self.input_data:
            self._z_coord_list = mmtfDecoder.decode(self.input_data, 'zCoordList', required=True)
            return self._z_coord_list
        else:
            return None

    @property
    def b_factor_list(self):
        if self._b_factor_list is not None:
            return self._b_factor_list
        elif 'bFactorList' in self.input_data:
            self._b_factor_list = mmtfDecoder.decode(self.input_data, 'bFactorList')
            return self._b_factor_list
        else:
            return None

    @property
    def atom_id_list(self):
        if self._atom_id_list is not None:
            return self._atom_id_list
        elif 'atomIdList' in self.input_data:
            self._atom_id_list = mmtfDecoder.decode(self.input_data, 'atomIdList')
            return self._atom_id_list
        else:
            return None

    @property
    def alt_loc_list(self):
        if self._alt_loc_list is not None:
            return self._alt_loc_list
        elif 'altLocList' in self.input_data:
            self._alt_loc_list = mmtfDecoder.decode(self.input_data, 'altLocList')
            return self._alt_loc_list
        else:
            return None

    @property
    def occupancy_list(self):
        if self._occupancy_list is not None:
            return self._occupancy_list
        elif 'occupancyList' in self.input_data:
            self._occupancy_list = mmtfDecoder.decode(self.input_data, 'occupancyList')
            return self._occupancy_list
        else:
            return None

    @property
    def group_id_list(self):
        if self._group_id_list is not None:
            return self._group_id_list
        elif 'groupIdList' in self.input_data:
            self._group_id_list = mmtfDecoder.decode(self.input_data, 'groupIdList', required=True)
            return self._group_id_list
        else:
            return None

    @property
    def group_type_list(self):
        if self._group_type_list is not None:
            return self._group_type_list
        elif 'groupTypeList' in self.input_data:
            self._group_type_list = mmtfDecoder.decode(self.input_data, 'groupTypeList', required=True)
            return self._group_type_list
        else:
            return None

    @property
    def sec_struct_list(self):
        if self._sec_struct_list is not None:
            return self._sec_struct_list
        elif 'secStructList' in self.input_data:
            self._sec_struct_list = mmtfDecoder.decode(self.input_data, 'secStructList')
            return self._sec_struct_list
        else:
            return None

    @property
    def ins_code_list(self):
        if self._ins_code_list is not None:
            return self._ins_code_list
        elif 'insCodeList' in self.input_data:
            self._ins_code_list = mmtfDecoder.decode(self.input_data, 'insCodeList')
            return self._ins_code_list
        else:
            return None

    @property
    def sequence_index_list(self):
        if self._sequence_index_list is not None:
            return self._sequence_index_list
        elif 'sequenceIndexList' in self.input_data:
            self._sequence_index_list = mmtfDecoder.decode(self.input_data, 'sequenceIndexList')
            return self._sequence_index_list
        else:
            return None

    @property
    def chain_id_list(self):
        if self._chain_id_list is not None:
            return self._chain_id_list
        elif 'chainIdList' in self.input_data:
            self._chain_id_list = mmtfDecoder.decode(self.input_data, 'chainIdList', required=True)
            return self._chain_id_list
        else:
            return None

    @property
    def chain_name_list(self):
        if self._chain_name_list is not None:
            return self._chain_name_list
        elif 'chainNameList' in self.input_data:
            self._chain_name_list = mmtfDecoder.decode(self.input_data, 'chainNameList')
            return self._chain_name_list
        else:
            return None

