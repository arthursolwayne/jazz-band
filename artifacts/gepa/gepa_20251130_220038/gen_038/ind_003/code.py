
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125), # D#
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=95, pitch=74, start=5.25, end=5.625), # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=63, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=105, pitch=64, start=5.625, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.save("dante_russo_intro.mid")
