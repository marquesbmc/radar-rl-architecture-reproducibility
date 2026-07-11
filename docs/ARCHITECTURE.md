# Architecture Summary

RADAR (*Reinforced Attention for Dynamic Agent Relations*) is an attentional neural architecture for partially observable multi-agent environments.

## Input representation

Each agent receives a local 7 × 7 field of view encoded in three primary channels. The action space contains nine actions, including remaining stationary.

## C2FN — Cross-Channel Fusion Network

C2FN augments the original input with semantically meaningful pairwise channel compositions. For RGB input, the derived channels are R+G, G+B, and R+B. Original and derived channels are processed independently before feature integration.

## SALM — Spatial Attention via L2 and Mean Pooling

SALM combines mean pooling and the L2 norm to construct a continuous spatial attention mask. The mask amplifies tactically relevant regions while reducing the influence of low-relevance areas.

## Decision layer

The processed feature maps are flattened and passed to an MLP that estimates action values. The article evaluates DQN, Double DQN, and Dueling DQN with both the CNN–MLP baseline and RADAR.
