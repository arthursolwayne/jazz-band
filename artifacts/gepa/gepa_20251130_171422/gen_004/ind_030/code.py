
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: All instruments in (1.5 - 3.0s)

# Bass: Walking line in Fm (F, Gb, Ab, Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping in Fm
# F7 on 2 (1.875 - 2.25)
piano_notes = [
    # F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    # Bbm7 on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Fm (F, Ab, Bb, Gb), start on 1.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),  # Gb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Ab7 on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    # Dm7 on 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    # Bbm7 on 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.75), # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),  # Gb
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.125),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.375), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.375, end=5.5),  # Gb
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
