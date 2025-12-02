
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody starts
# D7 chord: D F# A C#
# Diane plays 7th chords on 2 and 4
# Marcus walks bass line
# Little Ray continues pattern

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.875), # C#
]

for note in piano_notes:
    piano.notes.append(note)

# Bass: walking line with chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # G
]

for note in bass_notes:
    bass.notes.append(note)

# Sax: short motif in D, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5), # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Continue pattern
# Drums
for i in range(3):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125), # Snare on 2
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 1.5),     # Hihat on every 8th
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Piano: 7th chords on 2 and 4
for i in range(3):
    start = 1.5 + i * 1.5
    piano_notes = [
        pretty_midi.Note(velocity=100, pitch=62, start=start + 1.5, end=start + 1.875), # D
        pretty_midi.Note(velocity=100, pitch=67, start=start + 1.5, end=start + 1.875), # F#
        pretty_midi.Note(velocity=100, pitch=71, start=start + 1.5, end=start + 1.875), # A
        pretty_midi.Note(velocity=100, pitch=64, start=start + 1.5, end=start + 1.875), # C#
        pretty_midi.Note(velocity=100, pitch=62, start=start + 2.625, end=start + 2.875), # D
        pretty_midi.Note(velocity=100, pitch=67, start=start + 2.625, end=start + 2.875), # F#
        pretty_midi.Note(velocity=100, pitch=71, start=start + 2.625, end=start + 2.875), # A
        pretty_midi.Note(velocity=100, pitch=64, start=start + 2.625, end=start + 2.875), # C#
    ]
    for note in piano_notes:
        piano.notes.append(note)

# Bass: walking line
for i in range(3):
    start = 1.5 + i * 1.5
    bass_notes = [
        pretty_midi.Note(velocity=100, pitch=62, start=start + 1.5, end=start + 1.875), # D
        pretty_midi.Note(velocity=100, pitch=60, start=start + 1.875, end=start + 2.25), # C
        pretty_midi.Note(velocity=100, pitch=61, start=start + 2.25, end=start + 2.625), # C#
        pretty_midi.Note(velocity=100, pitch=62, start=start + 2.625, end=start + 3.0), # D
        pretty_midi.Note(velocity=100, pitch=64, start=start + 3.0, end=start + 3.375), # D#
        pretty_midi.Note(velocity=100, pitch=65, start=start + 3.375, end=start + 3.75), # E
        pretty_midi.Note(velocity=100, pitch=67, start=start + 3.75, end=start + 4.125), # F#
        pretty_midi.Note(velocity=100, pitch=69, start=start + 4.125, end=start + 4.5), # G
    ]
    for note in bass_notes:
        bass.notes.append(note)

# Sax: continue motif
for i in range(3):
    start = 1.5 + i * 1.5
    sax_notes = [
        pretty_midi.Note(velocity=110, pitch=62, start=start + 1.5, end=start + 1.875), # D
        pretty_midi.Note(velocity=110, pitch=64, start=start + 1.875, end=start + 2.25), # E
        pretty_midi.Note(velocity=110, pitch=67, start=start + 2.25, end=start + 2.625), # F#
        pretty_midi.Note(velocity=110, pitch=62, start=start + 2.625, end=start + 3.0), # D
        pretty_midi.Note(velocity=110, pitch=64, start=start + 3.0, end=start + 3.375), # E
        pretty_midi.Note(velocity=110, pitch=67, start=start + 3.375, end=start + 3.75), # F#
        pretty_midi.Note(velocity=110, pitch=62, start=start + 3.75, end=start + 4.125), # D
        pretty_midi.Note(velocity=110, pitch=64, start=start + 4.125, end=start + 4.5), # E
    ]
    for note in sax_notes:
        sax.notes.append(note)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
