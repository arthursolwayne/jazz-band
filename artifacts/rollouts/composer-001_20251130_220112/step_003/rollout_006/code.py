
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Diane - piano (7th chords comping on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G7 (D7)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # F#
]
piano.notes.extend(piano_notes)

# Little Ray - drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),    # Hihat
]
drums.notes.extend(drum_notes)

# Dante - saxophone (short motif, make it sing)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),   # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.125),# D
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
