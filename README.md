# RoboMusic
VST3 plug-in for musical composition synthesis using NCP and Deep Q-Learning

Inspired by "Polyphonic Music Composition with LSTM Neural Networks and Reinforcement Learning"

TODO:
- Import musical sequences from multiple formats (.mp3, .mp4, .wav, etc.), e.g. AnthemScore
- Transpose musical sequences to same key (http://nickkellyresearch.com/python-script-transpose-midi-files-c-minor/)
- Tempo quantization to ensure that a small, common set of note durations represents note lengths in all these tracks
- Temporal quantization to adjust misaligned notes
- Encode the pitch values as a one-hot encoded vector of length equal to the number of pitches playable on most pianos (88, from A0 to C8)
- Encode the durations as a one-hot vector, with each bit corresponding to a note duration that is frequently observed in the musical corpus
- Multi-Stream Note Representation
- HyperOpt for architecture/past-to-future context ratio optimization
- Q-Learning with cross entropy (Each prediction task is an input sequence of l_c note-sets in the multi-stream representation, where l_c is the context length for predicting the next note-set. Given these, the neural network is expected to predict the pitch and duration values for all n_s streams in the next note-set.)
- Plan (limiting the search space from Rn to {(p1, p2, ...p_n) : p_i ∈ {0, 1}}, i.e. dominance-based)
- Reward/Penalties UI (e.g. Occurrence of seventh chords, triads, etc., high pitch entropy, overuse of very short/long note durations, identical note-sets, ...)
- Support microtones (stream.pitch.ps)

Misc Notes:
Discount factor, learning rate, plan bits? = 0.8, 0.075, 20

Useful Links:
https://towardsdatascience.com/practical-tips-for-training-a-music-model-755c62560ec2
https://www.datacamp.com/community/tutorials/using-tensorflow-to-compose-music
https://web.mit.edu/music21/doc/developerReference/index.html
