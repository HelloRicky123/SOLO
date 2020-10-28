from ..registry import DETECTORS
from .single_stage_ins import SingleStageInsDetector


@DETECTORS.register_module
class SOLO9point(SingleStageInsDetector):

    def __init__(self,
                 backbone,
                 neck,
                 bbox_head,
                 train_cfg=None,
                 test_cfg=None,
                 pretrained=None):
        super(SOLO9point, self).__init__(backbone, neck, bbox_head, None, train_cfg,
                                   test_cfg, pretrained)
