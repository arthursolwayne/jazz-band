
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note mappings
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1: Drums only (0.0 to 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bar 2-4: Full ensemble (1.5 to 6.0s)

# Time per bar is 1.5s, so bars 2-4 are at 1.5 to 6.0s
# We'll write from bar 1 (indexing from 0 in the code, but logically bar 2 is the start of the melody)

# Saxophone melody: D7 -> Bb7 -> C7 -> D7
# Short motif, singable, starts and ends on D
# Each note is 1 beat (0.375s), so we'll play four notes over 1.5s
# Start at time 1.5s
sax_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)),  # D7
    (pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=1.875 + 0.375)),  # Bb7
    (pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.25 + 0.375)),  # C7
    (pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.375)),  # D7
]

sax.notes.extend(sax_notes)

# Bass line: Walking line in D, chromatic approaches
# D -> Eb -> E -> F -> G -> A -> B -> C -> D
# Each note is a 0.375s quarter note
bass_notes = [
    (pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.5 + 0.375)),  # D
    (pretty_midi.Note(velocity=70, pitch=63, start=1.875, end=1.875 + 0.375)),  # Eb
    (pretty_midi.Note(velocity=70, pitch=64, start=2.25, end=2.25 + 0.375)),  # E
    (pretty_midi.Note(velocity=70, pitch=65, start=2.625, end=2.625 + 0.375)),  # F
    (pretty_midi.Note(velocity=70, pitch=67, start=2.625, end=2.625 + 0.375)),  # G (start with G at 2.625, but this is overlapping the 4th sax note)
    (pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.0 + 0.375)),  # A
    (pretty_midi.Note(velocity=70, pitch=71, start=3.375, end=3.375 + 0.375)),  # B
    (pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=3.75 + 0.375)),  # C (chromatic approach)
    (pretty_midi.Note(velocity=70, pitch=62, start=4.125, end=4.125 + 0.375)),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, in D major
# Chords: D7 (bar 1), G7 (bar 2), C7 (bar 3), F7 (bar 4)
# Each chord is played on beats 2 and 4 (0.375s duration at 160 BPM)

# Bar 2 (start at 1.5s)
piano_notes = []

# D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=1.875 + 0.375),
])

# G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.625 + 0.375),
])

# C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.375 + 0.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.375 + 0.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.375 + 0.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.375 + 0.375),
])

# F7 (F A C E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.0 + 0.375),
])

piano.notes.extend(piano_notes)

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):  # bars 2 and 3 (logical bars 2-4)
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
