
import pretty_midi

# Initialize the MIDI file with tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# -------------------------------
# Bar 1: Little Ray (Drums) - 0.0 - 1.5s
# Use subtle dynamics, space, and tension.

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Subtle variation in hihat placement for texture

# Time in seconds: bar is 1.5s, 4 beats, beat is 0.375s
bar_length = 1.5
beat_length = 0.375

# Add kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375)
kick3 = pretty_midi.Note(velocity=100, pitch=KICK, start=1.125, end=1.5)
drums.notes.append(kick1)
drums.notes.append(kick3)

# Add snare on 2 and 4
snare2 = pretty_midi.Note(velocity=90, pitch=SNARE, start=0.375, end=0.75)
snare4 = pretty_midi.Note(velocity=90, pitch=SNARE, start=1.5, end=1.875)
drums.notes.append(snare2)
drums.notes.append(snare4)

# Hi-hat on every eighth, but vary velocity slightly
hihat1 = pretty_midi.Note(velocity=80, pitch=HIHAT, start=0.0, end=0.1875)
hihat2 = pretty_midi.Note(velocity=85, pitch=HIHAT, start=0.1875, end=0.375)
hihat3 = pretty_midi.Note(velocity=75, pitch=HIHAT, start=0.375, end=0.5625)
hihat4 = pretty_midi.Note(velocity=80, pitch=HIHAT, start=0.5625, end=0.75)
hihat5 = pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.75, end=0.9375)
hihat6 = pretty_midi.Note(velocity=85, pitch=HIHAT, start=0.9375, end=1.125)
hihat7 = pretty_midi.Note(velocity=80, pitch=HIHAT, start=1.125, end=1.3125)
hihat8 = pretty_midi.Note(velocity=85, pitch=HIHAT, start=1.3125, end=1.5)
drums.notes.extend([hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

# -------------------------------
# Bars 2-4: Full Quartet (1.5 - 6.0s)

# Temporal breakdown:
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Time signature: 4/4, key: Dm (D, F, A)

# -------------------------------
# Saxophone (Dante): Motif in Dm, emotional, concise

# Bar 2: Dm (D, F, A) - sax starts
# D (D4), F (F4), D (D4), Bb (Bb4)
# Each note is 0.375s (1 beat)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Rest for tension, then continuation
# Rest on first two beats (1.5 - 2.25s), then Dm7 chord
note5 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875)
note6 = pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.125)
note7 = pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.375)
note8 = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.625)
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: Return to motif, but with variation
note9 = pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.875)
note10 = pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.25)
note11 = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.625)
note12 = pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=5.0)
sax.notes.extend([note9, note10, note11, note12])

# -------------------------------
# Bass (Marcus): Walking line, chromatic approaches, melodic
# Dm7: D, F, A, C
# Bass line: D -> C -> B -> A -> G -> F -> E -> D

# Bar 2: 1.5 - 3.0s
note1 = pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=70, pitch=60, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=70, pitch=59, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=70, pitch=57, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3: 3.0 - 4.5s
note5 = pretty_midi.Note(velocity=70, pitch=55, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=70, pitch=53, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=70, pitch=52, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=70, pitch=50, start=4.125, end=4.5)
bass.notes.extend([note5, note6, note7, note8])

# Bar 4: 4.5 - 6.0s
note9 = pretty_midi.Note(velocity=70, pitch=50, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=70, pitch=52, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=70, pitch=53, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=70, pitch=55, start=5.625, end=6.0)
bass.notes.extend([note9, note10, note11, note12])

# -------------------------------
# Piano (Diane): 7th chords, comp on 2 and 4, emotional
# Key: Dm7 (D, F, A, C)
# Comp on 2 and 4 (beat 2 and 4 of each bar)

# Bar 2: 1.5 - 3.0s
note1 = pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25)  # D
note2 = pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25)  # F
note3 = pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25)  # A
note4 = pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25)  # C
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: 3.0 - 4.5s
note5 = pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75)  # D
note6 = pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75)  # F
note7 = pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75)  # A
note8 = pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75)  # C
piano.notes.extend([note5, note6, note7, note8])

# Bar 4: 4.5 - 6.0s
note9 = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625)  # D
note10 = pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625) # F
note11 = pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625) # A
note12 = pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625) # C
piano.notes.extend([note9, note10, note11, note12])

# -------------------------------
# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write('dante_russo_intro.mid')

print("MIDI file 'dante_russo_intro.mid' created.")
