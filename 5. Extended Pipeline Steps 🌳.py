# core/tree_builder.py
class TreeBuilder:
    SUPPORTED_METHODS = {
        "fasttree": {"type": "fast", "models": ["JTT", "WAG", "LG"]},
        "raxml": {"type": "accurate", "models": ["PROTGAMMAJTT", "PROTGAMMAWAG"]},
        "iqtree": {"type": "accurate", "models": ["JTT", "LG", "WAG"]}
    }
    
    def build_tree(self, alignment_file, method="fasttree", model="JTT", bootstrap=1000):
        """Build phylogenetic tree from alignment"""
        if method == "fasttree":
            return self._build_fasttree(alignment_file, model)
        elif method == "raxml":
            return self._build_raxml(alignment_file, model, bootstrap)
        elif method == "iqtree":
            return self._build_iqtree(alignment_file, model, bootstrap)