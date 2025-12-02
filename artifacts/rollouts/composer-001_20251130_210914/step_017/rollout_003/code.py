
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Comping on piano (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F7: A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F7: C
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F7: Db
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F7: A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F7: C
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # F7: Db
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.625, end=1.75),  # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=1.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),  # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.625),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.625), # Snare
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.875), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.25),    # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),    # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: Tenor sax motif (start on F, short, sing, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.375, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.375, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.875, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
