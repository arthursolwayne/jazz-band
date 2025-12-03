
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm (F2, C2, Gb2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # C2
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Gb2
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0), # Db2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, each bar a different chord
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0), # Eb5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax motif (start on F4, short motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0), # Ab4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375), # Db2
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Gb2
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5), # F2
]
bass.notes.extend(bass_notes)

# Diane: Next chord (Ab7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5), # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5), # Db4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # Gb4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax motif (reprise and resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5), # Ab4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # Gb2
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0), # Db2
]
bass.notes.extend(bass_notes)

# Diane: Final chord (Eb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0), # Gb4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=6.0), # C5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax motif (finish with resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0), # Ab4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
