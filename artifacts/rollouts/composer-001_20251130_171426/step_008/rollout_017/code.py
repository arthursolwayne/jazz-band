
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, D
bass_notes = [
    # Bar 2: F, Gb, Ab, A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # A

    # Bar 3: Bb, B, C, Db
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # Db

    # Bar 4: D, Eb, F, F#
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=75, start=5.625, end=6.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625), # Ab

    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # Ab

    # Bar 4: F7 on beat 2 and 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625), # Ab

    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm triad with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_intro.mid')
