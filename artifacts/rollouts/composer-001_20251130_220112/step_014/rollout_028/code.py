
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

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F - Ab - Bb - Gb (ascending), then repeat with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.4375, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5625, end=3.75), # Gb
]
for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line, chromatic approaches, never the same note twice
# Fm: F, Gb, Ab, A, Bb, C, Db
# Walking line: F - Gb - Ab - A - Bb - C - Db - F
# 16th note pulse
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.375),  # Db
    pretty_midi.Note(velocity=80, pitch=53, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=2.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=2.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.875, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.375),  # Db
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.5),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Bar 2: Comp on beat 2 (0.75s mark)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.625),  # C

    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.375),  # C

    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=3.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
