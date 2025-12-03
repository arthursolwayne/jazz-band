
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# --- Bar 1: Little Ray alone (0.0 - 1.5s) ---
# Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time per beat = 0.375s, time per bar = 1.5s

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every eighth
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start, end=end))

# --- Bars 2-4: Full quartet (1.5 - 6.0s) ---

# Bass line: Walking line in F, roots and fifths with chromatic approaches
# F - G - A - Bb - C - D - E - F
# Use D2-G2 (MIDI 38-43) range
# Roots and fifths, with chromatic approaches

bass_notes = [
    (38, 1.5, 1.875),  # F2 (root)
    (40, 1.875, 2.25), # G2 (fifth of F)
    (39, 2.25, 2.625), # Gb2 (chromatic approach to G)
    (41, 2.625, 3.0),  # A2 (next root)
    (43, 3.0, 3.375),  # Bb2 (fifth of A)
    (42, 3.375, 3.75), # Bb2 (chromatic approach to Bb)
    (44, 3.75, 4.125), # C2 (next root)
    (46, 4.125, 4.5),  # D2 (fifth of C)
    (45, 4.5, 4.875),  # C#2 (chromatic approach to D)
    (47, 4.875, 5.25), # E2 (next root)
    (49, 5.25, 5.625), # F2 (fifth of E)
    (48, 5.625, 6.0)   # F2 (chromatic approach to F)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Em7 (E, G, B, D)
# Bar 4: Am7 (A, C, E, G)
# Comp on 2 and 4

# Bar 2 (1.5 - 3.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0))  # F (MIDI 65)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0))  # E

# Bar 3 (3.0 - 4.5)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5))  # D

# Bar 4 (4.5 - 6.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=6.0))  # G

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F - G - A - F (with a slight chromatic twist on G)

# Bar 2 (1.5 - 3.0)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))   # F (resolve)

# Bar 3 (3.0 - 4.5) - leave it hanging
# Just sustain the last note for 1.5 seconds
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5))  # F

# Bar 4 (4.5 - 6.0) - come back and finish it
# Play the same motif again but shorter
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0))   # F (resolve)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
