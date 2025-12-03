
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum notes (MIDI numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on beats 1 and 3
kick_beat_1 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start, end=bar_1_start + 0.375)
kick_beat_3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start + 1.125, end=bar_1_start + 1.5)

# Snare on beats 2 and 4
snare_beat_2 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_1_start + 0.75, end=bar_1_start + 0.75 + 0.375)
snare_beat_4 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_1_start + 1.5 - 0.375, end=bar_1_start + 1.5)

# Hihat on every eighth note
hihat_notes = []
for i in range(8):
    hihat_start = bar_1_start + i * 0.375
    hihat_end = hihat_start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_start, end=hihat_end))

# Add drum notes to the drum instrument
drums.notes.extend([kick_beat_1, kick_beat_3, snare_beat_2, snare_beat_4] + hihat_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start with piano and bass
bar_2_start = 1.5
bar_2_end = 3.0
bar_3_start = 3.0
bar_3_end = 4.5
bar_4_start = 4.5
bar_4_end = 6.0

# ---------------------------
# BASS: Marcus
# Walking bass line in F: F - G - A - Bb (MIDI 53 - 55 - 57 - 58)
# Roots and fifths with chromatic approaches
# Bar 2: F - G - A - Bb  
# Bar 3: Bb - C - D - Eb
# Bar 4: Eb - F - G - A

bass_notes = []

# Bar 2
bass_notes.append(pretty_midi.Note(velocity=70, pitch=53, start=bar_2_start, end=bar_2_start + 0.375))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=55, start=bar_2_start + 0.75, end=bar_2_start + 1.125))  # chromatic
bass_notes.append(pretty_midi.Note(velocity=70, pitch=57, start=bar_2_start + 1.125, end=bar_2_start + 1.5))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=58, start=bar_2_start + 1.5, end=bar_2_start + 1.875))

# Bar 3
bass_notes.append(pretty_midi.Note(velocity=70, pitch=58, start=bar_3_start, end=bar_3_start + 0.375))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=60, start=bar_3_start + 0.75, end=bar_3_start + 1.125))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=62, start=bar_3_start + 1.125, end=bar_3_start + 1.5))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=64, start=bar_3_start + 1.5, end=bar_3_start + 1.875))

# Bar 4
bass_notes.append(pretty_midi.Note(velocity=70, pitch=64, start=bar_4_start, end=bar_4_start + 0.375))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=65, start=bar_4_start + 0.75, end=bar_4_start + 1.125))  # chromatic
bass_notes.append(pretty_midi.Note(velocity=70, pitch=67, start=bar_4_start + 1.125, end=bar_4_start + 1.5))
bass_notes.append(pretty_midi.Note(velocity=70, pitch=69, start=bar_4_start + 1.5, end=bar_4_start + 1.875))

bass.notes.extend(bass_notes)

# ---------------------------
# PIANO: Diane
# Open voicings, different chords each bar, resolutions on the last beat
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
# Bar 4: Em7 (E, G, B, D)

piano_notes = []

# Bar 2: Fmaj7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=bar_2_start, end=bar_2_start + 0.375))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar_2_start, end=bar_2_start + 0.375))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start, end=bar_2_start + 0.375))  # E
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start + 0.75, end=bar_2_start + 0.75 + 0.375))  # A

# Bar 3: Bbmaj7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=58, start=bar_3_start, end=bar_3_start + 0.375))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_3_start, end=bar_3_start + 0.375))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_3_start, end=bar_3_start + 0.375))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_3_start + 0.75, end=bar_3_start + 0.75 + 0.375))  # Ab

# Bar 4: Em7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar_4_start, end=bar_4_start + 0.375))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_4_start, end=bar_4_start + 0.375))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_4_start, end=bar_4_start + 0.375))  # B
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_4_start + 0.75, end=bar_4_start + 0.75 + 0.375))  # D

piano.notes.extend(piano_notes)

# ---------------------------
# DRUMS: Continue the pattern from Bar 1
# Bars 2-4: Same pattern with kicks on 1 & 3, snares on 2 & 4, hihat on every eighth

# Bar 2
for i in range(8):
    hihat_start = bar_2_start + i * 0.375
    hihat_end = hihat_start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_start, end=hihat_end))

kick_beat_1_bar2 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_2_start, end=bar_2_start + 0.375)
kick_beat_3_bar2 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_2_start + 1.125, end=bar_2_start + 1.5)
snare_beat_2_bar2 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_2_start + 0.75, end=bar_2_start + 0.75 + 0.375)
snare_beat_4_bar2 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_2_start + 1.5 - 0.375, end=bar_2_start + 1.5)

# Bar 3
for i in range(8):
    hihat_start = bar_3_start + i * 0.375
    hihat_end = hihat_start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_start, end=hihat_end))

kick_beat_1_bar3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_3_start, end=bar_3_start + 0.375)
kick_beat_3_bar3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_3_start + 1.125, end=bar_3_start + 1.5)
snare_beat_2_bar3 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_3_start + 0.75, end=bar_3_start + 0.75 + 0.375)
snare_beat_4_bar3 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_3_start + 1.5 - 0.375, end=bar_3_start + 1.5)

# Bar 4
for i in range(8):
    hihat_start = bar_4_start + i * 0.375
    hihat_end = hihat_start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_start, end=hihat_end))

kick_beat_1_bar4 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_4_start, end=bar_4_start + 0.375)
kick_beat_3_bar4 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_4_start + 1.125, end=bar_4_start + 1.5)
snare_beat_2_bar4 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_4_start + 0.75, end=bar_4_start + 0.75 + 0.375)
snare_beat_4_bar4 = pretty_midi.Note(velocity=110, pitch=SNARE, start=bar_4_start + 1.5 - 0.375, end=bar_4_start + 1.5)

# Add these to the drums instrument
drums.notes.extend([kick_beat_1_bar2, kick_beat_3_bar2, snare_beat_2_bar2, snare_beat_4_bar2] + hihat_notes)
drums.notes.extend([kick_beat_1_bar3, kick_beat_3_bar3, snare_beat_2_bar3, snare_beat_4_bar3])
drums.notes.extend([kick_beat_1_bar4, kick_beat_3_bar4, snare_beat_2_bar4, snare_beat_4_bar4])

# ---------------------------
# SAX: Dante's motif
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - A - C - D - F (MIDI 53 - 58 - 60 - 62 - 53)
# Play it on beat 1 of bar 2, then again on beat 3 of bar 2, then end with an F on beat 3 of bar 4

sax_notes = []

# Bar 2: Play the motif
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=bar_2_start, end=bar_2_start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=58, start=bar_2_start + 0.75, end=bar_2_start + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=bar_2_start + 1.125, end=bar_2_start + 1.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar_2_start + 1.5, end=bar_2_start + 1.875))

# Bar 3: Repeat the motif
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=bar_3_start, end=bar_3_start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=58, start=bar_3_start + 0.75, end=bar_3_start + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=bar_3_start + 1.125, end=bar_3_start + 1.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar_3_start + 1.5, end=bar_3_start + 1.875))

# Bar 4: End with an F on beat 3
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=bar_4_start + 1.125, end=bar_4_start + 1.5))

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
