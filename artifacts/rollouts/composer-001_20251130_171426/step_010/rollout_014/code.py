
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add the drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # F
]

# Add the bass notes
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
]

# Add the piano notes
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Fm motif: F, Ab, Bb, C, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75),  # F (reprise)
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=5.75),  # F
]

# Add the sax notes
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('waynes_moment.mid')
