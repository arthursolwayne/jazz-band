
import pretty_midi

# Create a MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HI_HAT = 42

# Bar 1: Little Ray (Drums) alone (0.0 - 1.5s)
# Create a rhythmic question: sparse, tense, with hihat breathing
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=HI_HAT, start=0.0, end=1.5),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=KICK, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Time per bar = 1.5s, so bar 2 is 1.5-3.0s, bar 3 is 3.0-4.5s, bar 4 is 4.5-6.0s

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
# Fm7 = F, Ab, Bb, D
# Walking line: F, Gb, Ab, Bb, B, C, Db, D, Eb, E, F, Gb, etc. (chromatic)
# We'll create a simple walking bass line over 3 bars (1.5-6.0s)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F (C4)
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # Gb (Bb3)
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625), # Ab (Ab3)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # Bb (Bb3)
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),  # B (B3)
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # C (C3)
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # Db (Db3)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # Bb (Bb3)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Gb (Bb3)
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # F (C4)
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # F# (C#4)
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # F (C4)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Piano, 7th chords on 2 and 4, comping in Fm
# Fm7 = F, Ab, Bb, D
# Fm7 = [F, Ab, Bb, D]
# We'll play each chord on 2 and 4 (beats 2 and 4 of bars 2, 3, 4)

# Bar 2 (1.5 - 3.0s)
# Beat 2: 2.25s, Beat 4: 3.0s
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.375),  # D

    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.125),  # D

    # Bar 3 (3.0 - 4.5s)
    # Beat 2: 3.75s, Beat 4: 4.5s
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=3.875),  # D

    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.625),  # D

    # Bar 4 (4.5 - 6.0s)
    # Beat 2: 5.25s, Beat 4: 6.0s
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.375),  # D

    pretty_midi.Note(velocity=90, pitch=71, start=6.0, end=6.125),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=6.0, end=6.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=6.0, end=6.125),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor Sax — motif that lingers and hints at a deeper story
# A short, singing motif: F, Gb, Ab, Bb — a quartal idea with a question in it
# Play on beat 1 of bar 2 (1.5s), then leave it hanging, come back to resolve

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # Bb

    # Let it hang — no note until bar 4, beat 3
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # F (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
