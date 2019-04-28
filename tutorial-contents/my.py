#!/usr/bin/python
# -*- coding: UTF-8 -*-

args.model == "gat"
if args.model == "gat":
    n_heads = [int(x) for x in args.heads.strip().split(",")]
    model = BatchGAT(pretrained_emb=influence_dataset.get_embedding(),
            vertex_feature=influence_dataset.get_vertex_features(),
            use_vertex_feature=args.use_vertex_feature,
            n_units=n_units, n_heads=n_heads,
            dropout=args.dropout, instance_normalization=args.instance_normalization)
    print("run gat")