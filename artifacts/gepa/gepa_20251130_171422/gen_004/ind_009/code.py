
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F7 chord: F A C E (F7 is F A C Eb)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 = F A C Eb
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 = F A C Eb
# Start on F, skip to Eb, then A, then C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=5.75, end=6.0),  # Eb
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
