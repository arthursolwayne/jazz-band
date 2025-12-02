
import pretty_midi

# Initialize MIDI with the appropriate tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Key: D Major
# Scale: D E F# G A B C# D
# Our motif is based on D, F#, A, C# — an ascending D minor triad with a chromatic approach

# Bar 1: Little Ray (Drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hi-hat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start, end=bar_start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 1.125, end=bar_start + 1.5)
    
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2: Full band enters (1.5 - 3.0s)
# Saxophone (Dante): motif starts here
# D4 (D), F#4 (F#), A4 (A), C#5 (C#)
# Start with D, then F#, leave it hanging on A

# Saxophone motif
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D4
sax_note_2 = pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25) # F#4
sax_note_3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625) # A4
sax_note_4 = pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0)  # C#5
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Bass line: Walking line in D major
# D -> C# -> B -> A -> G -> F# -> E -> D
# Bar 2: D, C#, B, A

bass_note_1 = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875) # D
bass_note_2 = pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25) # C#
bass_note_3 = pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625) # B
bass_note_4 = pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0)  # A
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: 7th chords on 2 and 4
# D7 on 2 (F#), G7 on 4 (B)

# D7 = D, F#, A, C
# G7 = G, B, D, F
piano_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25)  # D (held)
piano_note_2 = pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=2.25)  # F#
piano_note_3 = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25)  # A
piano_note_4 = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25)  # C

# G7 on 2.25 (bar 2, beat 2)
piano_note_5 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0)  # G
piano_note_6 = pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0)  # B
piano_note_7 = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0)  # D
piano_note_8 = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0)  # F

piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4,
                    piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Bar 3: Full band
# Saxophone: repeat the motif starting from F#
# F# -> A -> C# -> D

sax_note_5 = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375)  # F#4
sax_note_6 = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75) # A4
sax_note_7 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125) # C#5
sax_note_8 = pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)  # D4
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Bass: E -> D -> C# -> B

bass_note_5 = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375) # E
bass_note_6 = pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75) # D
bass_note_7 = pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125) # C#
bass_note_8 = pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5)  # B
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: B7 on 2, A7 on 4
# B7 = B, D#, F#, A
# A7 = A, C#, E, G

piano_note_9 = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75)  # B
piano_note_10 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75) # D#
piano_note_11 = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75) # F#
piano_note_12 = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75) # A

piano_note_13 = pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5)  # A
piano_note_14 = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.5)  # C#
piano_note_15 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5)  # E
piano_note_16 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5)  # G

piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12,
                    piano_note_13, piano_note_14, piano_note_15, piano_note_16])

# Bar 4: Full band
# Saxophone: repeat motif again, this time resolving to D

sax_note_9 = pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875)  # F#4
sax_note_10 = pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25) # A4
sax_note_11 = pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625) # C#5
sax_note_12 = pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)  # D4
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12])

# Bass: A -> G -> F# -> E

bass_note_9 = pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875) # A
bass_note_10 = pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25) # G
bass_note_11 = pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625) # F#
bass_note_12 = pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0)  # E
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: E7 on 2, D7 on 4
# E7 = E, G#, B, D
# D7 = D, F#, A, C

piano_note_17 = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25)  # E
piano_note_18 = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25)  # G#
piano_note_19 = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25)  # B
piano_note_20 = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25)  # D

piano_note_21 = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=6.0)  # D
piano_note_22 = pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=6.0)  # F#
piano_note_23 = pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0)  # A
piano_note_24 = pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=6.0)  # C

piano.notes.extend([piano_note_17, piano_note_18, piano_note_19, piano_note_20,
                    piano_note_21, piano_note_22, piano_note_23, piano_note_24])

# Add the drums to the last three bars
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hi-hat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start, end=bar_start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + 1.125, end=bar_start + 1.5)
    
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Add all instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
