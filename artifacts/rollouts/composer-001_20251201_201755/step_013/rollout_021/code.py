
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line (F2 - Bb2), roots and fifths with chromatic approaches
bass_notes = [
    # F2 root
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # Bb2 fifth
    pretty_midi.Note(velocity=90, pitch=56, start=1.875, end=2.25),
    # F2 root (chromatic approach from Gb)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),
    # Bb2 fifth
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (chromatic approach to C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - Bb (play F and Bb in bar 2, then C and Bb in bar 4)
sax_notes = [
    # Bar 2: F (Bb)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # Bb
    # Bar 3: silence, hold the tension
    # Bar 4: C (Bb)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4, same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Add the rest of the bar 1 pattern to the second bar
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bar 2-4 drums (same pattern repeated)
for note in drum_notes:
    note.start += 4.5
    note.end += 4.5
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
