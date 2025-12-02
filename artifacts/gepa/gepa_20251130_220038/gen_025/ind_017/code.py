
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # Eb
    # Bar 3
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Ab
    # Bar 4
    # F7 again
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, make it sing
sax_notes = [
    # Bar 2 - Melody start
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),  # A
    # Bar 3 - continue the motif
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.5),  # A
    # Bar 4 - resolve the motif
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
